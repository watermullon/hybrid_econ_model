from __future__ import annotations

from dataclasses import asdict

from src.deal_types import DealSet, RealEstatePortfolioYearResult
from src.metrics import annual_irr, economic_moic, moic
from src.model_types import (
    BackendLiquidityStrategySettings,
    CashflowRoute,
    CashflowRoutingSettings,
    FlagResult,
    HurdleCompletionTriggerSettings,
    LPCashYieldPolicy,
    ModelConfig,
    RefinanceEvent,
    Scenario,
    ScenarioResult,
    YearlyResult,
)
from src.portfolio_aggregator import apply_deal_overrides, build_re_portfolio_year
from src.utils import merge_model, value_for_year
from src.validation import validate_all_scenarios
from src.waterfall import available_liquidity, pay_lp_distribution, redeem_lp


def calculate_initial_allocation(config: ModelConfig, scenario: Scenario) -> tuple[float, float, float]:
    capital = config.model.initial_lp_capital
    allocation = merge_model(config.allocation, scenario.allocation)
    if allocation.method == "fixed":
        hf_nav = capital * allocation.hedge_fund_allocation_pct
        re_nav = capital * allocation.real_estate_allocation_pct
        reserve_nav = capital * allocation.reserve_allocation_pct
    else:
        hf_nav = capital * scenario.real_estate.initial_noi_yield
        reserve_nav = capital * allocation.reserve_allocation_pct
        re_nav = capital - hf_nav - reserve_nav

    if min(hf_nav, re_nav, reserve_nav) < -1e-6:
        raise ValueError("Initial allocation generated a negative sleeve value.")
    if abs((hf_nav + re_nav + reserve_nav) - capital) > 1e-4:
        raise ValueError("Initial allocation does not equal initial LP capital.")
    return re_nav, hf_nav, reserve_nav


def run_all_scenarios(
    config: ModelConfig,
    scenarios: dict[str, Scenario],
    deals: DealSet | None = None,
) -> list[ScenarioResult]:
    validate_all_scenarios(config, scenarios, deals)
    return [run_scenario(name, scenario, config, deals) for name, scenario in scenarios.items()]


def run_scenario(
    name: str,
    scenario: Scenario,
    config: ModelConfig,
    deals: DealSet | None = None,
) -> ScenarioResult:
    liquidity = merge_model(config.liquidity, scenario.liquidity)
    distribution_policy = merge_model(config.distribution_policy, scenario.distribution_policy)
    cashflow_routing = merge_model(config.cashflow_routing, scenario.cashflow_routing)
    lp_cash_yield_policy = merge_model(config.lp_cash_yield_policy, scenario.lp_cash_yield_policy)
    backend_liquidity_strategy = merge_model(
        config.backend_liquidity_strategy, scenario.backend_liquidity_strategy
    )
    if lp_cash_yield_policy.enabled and not lp_cash_yield_policy.reduce_lp_hurdle:
        raise ValueError(
            "LP cash yield policy is invalid: actual LP cash yield payments must reduce the LP cash hurdle."
        )
    reserve_settings = merge_model(config.reserve, scenario.reserve)
    real_estate_settings = merge_model(config.real_estate, scenario.real_estate_model)
    real_estate_mode = real_estate_settings.mode
    refinance_events_by_year = events_by_year(scenario.refinance_events)

    initial_lp_capital = config.model.initial_lp_capital
    lp_hurdle_amount = initial_lp_capital * config.waterfall.lp_hurdle_moic
    portfolio_years: list[RealEstatePortfolioYearResult] = []
    deal_cashflows = []
    effective_deals: DealSet | None = None
    funded_deal_names: set[str] = set()
    cumulative_refi_liability_by_deal: dict[str, float] = {}
    initial_re_cash_deployed = 0.0
    initial_re_gross_asset_value = 0.0
    initial_re_debt_balance = 0.0
    initial_re_assumed_liabilities = 0.0
    initial_re_net_equity_value = 0.0
    initial_re_entry_equity_cushion = 0.0
    initial_re_value_to_new_equity_multiple = None

    if real_estate_mode == "bottom_up":
        if deals is None:
            raise ValueError(f"Scenario '{name}' uses bottom_up real estate mode but no deals were provided.")
        effective_deals = apply_deal_overrides(deals, scenario.deal_overrides)
        funded_deal_names = {
            deal_name
            for deal_name, deal in effective_deals.deals.items()
            if deal.enabled and deal.acquisition_year == 1
        }
        cumulative_refi_liability_by_deal = {deal_name: 0.0 for deal_name in effective_deals.deals}
        initial_portfolio_year, _ = build_re_portfolio_year(
            scenario_name=name,
            deals=effective_deals,
            year=1,
            funded_deal_names=funded_deal_names,
            cumulative_refi_liability_by_deal=cumulative_refi_liability_by_deal.copy(),
        )
        initial_re_cash_deployed = sum(
            deal.acquisition.new_equity_required
            for deal in effective_deals.deals.values()
            if deal.enabled and deal.acquisition_year == 1
        )
        remaining_capital = initial_lp_capital - initial_re_cash_deployed
        if remaining_capital < -1e-6 and not config.bottom_up_allocation.allow_overallocated_deals:
            raise ValueError(
                f"Scenario '{name}' bottom-up deals require ${initial_re_cash_deployed:,.0f} of year-1 equity, "
                f"which exceeds initial LP capital of ${initial_lp_capital:,.0f}."
        )
        allocatable_remaining = max(0.0, remaining_capital)
        hf_nav = allocatable_remaining * config.bottom_up_allocation.remaining_capital_hf_pct
        reserve_nav = allocatable_remaining * config.bottom_up_allocation.remaining_capital_reserve_pct
        re_nav = initial_portfolio_year.deal_nav
        initial_re_gross_asset_value = initial_portfolio_year.gross_asset_value
        initial_re_debt_balance = initial_portfolio_year.debt_balance
        initial_re_assumed_liabilities = initial_portfolio_year.assumed_liabilities
        initial_re_net_equity_value = initial_portfolio_year.net_equity_value
        initial_re_entry_equity_cushion = initial_portfolio_year.entry_equity_cushion
        initial_re_value_to_new_equity_multiple = initial_portfolio_year.value_to_new_equity_multiple
    else:
        re_nav, hf_nav, reserve_nav = calculate_initial_allocation(config, scenario)
        initial_re_cash_deployed = re_nav
        initial_re_gross_asset_value = re_nav
        initial_re_net_equity_value = re_nav
    initial_re_nav = re_nav
    initial_hf_nav = hf_nav

    retained_cash = 0.0
    lp_cumulative_distribution = 0.0
    gp_cumulative_fees = 0.0
    gp_residual_nav = 0.0
    liquidity_constrained = False
    year_hurdle_achieved: int | None = None
    cashflows: list[YearlyResult] = []
    lp_irr_cashflows = [-initial_lp_capital]
    cumulative_lp_cash_yield_shortfall = 0.0
    cumulative_refinance_proceeds = 0.0
    cumulative_refinance_to_lp = 0.0
    refinance_liability = 0.0
    cumulative_reinvested_into_hf = 0.0
    cumulative_cash_added_to_reserve = 0.0
    total_trigger_cash_from_retained_cash = 0.0
    total_trigger_cash_from_reserve = 0.0
    total_trigger_cash_from_hf_liquidation = 0.0
    total_trigger_cash_from_refi = 0.0
    total_trigger_cash_from_re_sale = 0.0
    hurdle_trigger_year: int | None = None
    lp_hurdle_shortfall_after_final_trigger = 0.0

    for year in range(1, scenario.years + 1):
        re_opening_nav = re_nav
        hf_opening_nav = hf_nav
        reserve_opening_nav = reserve_nav

        acquisition_starting_retained_cash = retained_cash
        acquisition_starting_reserve = reserve_nav
        acquisition_new_deal_equity_required = 0.0
        acquisition_funded_from_initial_lp_capital = 0.0
        acquisition_funded_from_retained_cash = 0.0
        acquisition_funded_from_reserve = 0.0
        acquisition_unfunded_shortfall = 0.0
        acquisition_funding_source = ""

        portfolio_year = None
        if real_estate_mode == "bottom_up":
            if effective_deals is None:
                raise ValueError(f"Scenario '{name}' uses bottom_up real estate mode but no deals were provided.")
            acquisition_deals = {
                deal_name: deal
                for deal_name, deal in effective_deals.deals.items()
                if deal.enabled and deal.acquisition_year == year
            }
            acquisition_new_deal_equity_required = sum(
                deal.acquisition.new_equity_required for deal in acquisition_deals.values()
            )
            if year == 1:
                acquisition_funded_from_initial_lp_capital = acquisition_new_deal_equity_required
                acquisition_funding_source = "initial_lp_capital" if acquisition_new_deal_equity_required > 0 else ""
            elif acquisition_new_deal_equity_required > 0:
                funding_need = acquisition_new_deal_equity_required
                acquisition_funded_from_retained_cash = min(retained_cash, funding_need)
                retained_cash -= acquisition_funded_from_retained_cash
                funding_need -= acquisition_funded_from_retained_cash
                acquisition_funded_from_reserve = min(reserve_nav, funding_need)
                reserve_nav -= acquisition_funded_from_reserve
                funding_need -= acquisition_funded_from_reserve
                acquisition_unfunded_shortfall = funding_need
                acquisition_funding_source = "retained_cash;reserve" if acquisition_funded_from_reserve > 0 else "retained_cash"
                if acquisition_unfunded_shortfall <= 1e-9:
                    funded_deal_names.update(acquisition_deals)

            portfolio_year, deal_rows = build_re_portfolio_year(
                scenario_name=name,
                year=year,
                deals=effective_deals,
                funded_deal_names=funded_deal_names,
                cumulative_refi_liability_by_deal=cumulative_refi_liability_by_deal,
            )
            deal_cashflows.extend(deal_rows)

        acquisition_ending_retained_cash = retained_cash
        acquisition_ending_reserve = reserve_nav

        if portfolio_year is None:
            re_noi_yield = scenario.real_estate.initial_noi_yield * (
                (1 + scenario.real_estate.annual_noi_growth) ** (year - 1)
            )
            gross_rent_yield = value_for_year(scenario.real_estate.gross_rent_yield, year)
            re_appreciation_rate = value_for_year(scenario.real_estate.annual_nav_appreciation, year)
            re_noi = re_opening_nav * re_noi_yield
            gross_rent = re_opening_nav * gross_rent_yield
            re_asset_mgmt_fee = calculate_re_fee(config, re_opening_nav, re_noi, gross_rent)
            net_re_cashflow = re_noi - re_asset_mgmt_fee
            re_cashflow_generated = net_re_cashflow
            re_nav = re_opening_nav * (1 + re_appreciation_rate)
            re_gross_asset_value = re_nav
            re_debt_balance = 0.0
            re_assumed_liabilities = 0.0
            re_net_equity_value = re_nav
            re_debt_service = 0.0
            re_capex = 0.0
            re_dscr = None
            re_prior_refi_liability = 0.0
            re_ending_refi_liability = 0.0
            re_max_debt_supported = 0.0
            re_cash_out_before_refi_costs = 0.0
            re_refi_costs = 0.0
            re_refi_capacity = 0.0
            re_refi_proceeds_from_deals = 0.0
            re_free_cashflow_after_debt_and_capex = net_re_cashflow
            active_deal_count = 0
        else:
            re_noi_yield = portfolio_year.noi / re_opening_nav if re_opening_nav > 0 else 0.0
            re_appreciation_rate = (
                portfolio_year.deal_nav / re_opening_nav - 1 if re_opening_nav > 0 else 0.0
            )
            re_noi = portfolio_year.noi
            gross_rent = portfolio_year.gross_rent
            re_asset_mgmt_fee = calculate_re_fee(config, re_opening_nav, re_noi, gross_rent)
            net_re_cashflow = portfolio_year.free_cashflow_after_debt_and_capex - re_asset_mgmt_fee
            re_cashflow_generated = max(0.0, net_re_cashflow)
            re_nav = portfolio_year.deal_nav
            re_gross_asset_value = portfolio_year.gross_asset_value
            re_debt_balance = portfolio_year.debt_balance
            re_assumed_liabilities = portfolio_year.assumed_liabilities
            re_net_equity_value = portfolio_year.net_equity_value
            re_debt_service = portfolio_year.debt_service
            re_capex = portfolio_year.capex
            re_dscr = portfolio_year.dscr
            re_prior_refi_liability = portfolio_year.prior_refi_liability
            re_ending_refi_liability = portfolio_year.ending_refi_liability
            re_max_debt_supported = portfolio_year.max_debt_supported
            re_cash_out_before_refi_costs = portfolio_year.cash_out_before_refi_costs
            re_refi_costs = portfolio_year.refi_costs
            re_refi_capacity = portfolio_year.refi_capacity
            re_refi_proceeds_from_deals = portfolio_year.refi_proceeds
            re_free_cashflow_after_debt_and_capex = portfolio_year.free_cashflow_after_debt_and_capex
            active_deal_count = portfolio_year.active_deal_count

        hf_return = scenario.hedge_fund.annual_returns[year - 1]
        hf_nav_pre_harvest = hf_opening_nav * (1 + hf_return)
        hf_gain = max(0.0, hf_nav_pre_harvest - hf_opening_nav)
        hf_harvest = hf_gain * distribution_policy.hf_positive_return_harvest_rate
        hf_harvest_generated = hf_harvest
        hf_nav = hf_nav_pre_harvest - hf_harvest

        reserve_nav = reserve_opening_nav * (1 + reserve_settings.annual_return)
        reserve_return_cash = reserve_nav - reserve_opening_nav
        re_cashflow_shortfall = 0.0
        if real_estate_mode == "bottom_up" and net_re_cashflow < 0:
            funding_need = -net_re_cashflow
            from_retained_cash = min(retained_cash, funding_need)
            retained_cash -= from_retained_cash
            funding_need -= from_retained_cash
            from_reserve = min(reserve_nav, funding_need)
            reserve_nav -= from_reserve
            funding_need -= from_reserve
            re_cashflow_shortfall = funding_need

        gp_fees = re_asset_mgmt_fee
        gp_cumulative_fees += gp_fees

        re_cashflow_to_lp = 0.0
        re_cashflow_to_hf = 0.0
        re_cashflow_to_reserve = 0.0
        hf_harvest_to_lp = 0.0
        hf_harvest_to_hf = 0.0
        hf_harvest_to_reserve = 0.0
        lp_distribution = 0.0

        net_re_cash_bucket = re_cashflow_generated if real_estate_mode == "bottom_up" else net_re_cashflow
        hf_harvest_cash_bucket = hf_harvest

        if cashflow_routing.enabled:
            lp_remaining_hurdle = max(0.0, lp_hurdle_amount - lp_cumulative_distribution)
            re_route = route_cashflow(re_cashflow_generated, cashflow_routing.re_cashflow)
            re_cashflow_to_lp = min(re_route["lp"], lp_remaining_hurdle)
            lp_distribution += re_cashflow_to_lp
            lp_cumulative_distribution += re_cashflow_to_lp
            retained_cash += re_route["lp"] - re_cashflow_to_lp
            re_cashflow_to_hf = re_route["hf"]
            re_cashflow_to_reserve = re_route["reserve"]

            lp_remaining_hurdle = max(0.0, lp_hurdle_amount - lp_cumulative_distribution)
            hf_route = route_cashflow(hf_harvest_generated, cashflow_routing.hf_harvest)
            hf_harvest_to_lp = min(hf_route["lp"], lp_remaining_hurdle)
            lp_distribution += hf_harvest_to_lp
            lp_cumulative_distribution += hf_harvest_to_lp
            retained_cash += hf_route["lp"] - hf_harvest_to_lp
            hf_harvest_to_hf = hf_route["hf"]
            hf_harvest_to_reserve = hf_route["reserve"]

            hf_nav += re_cashflow_to_hf + hf_harvest_to_hf
            reserve_nav += re_cashflow_to_reserve + hf_harvest_to_reserve
            cumulative_reinvested_into_hf += re_cashflow_to_hf + hf_harvest_to_hf
            cumulative_cash_added_to_reserve += re_cashflow_to_reserve + hf_harvest_to_reserve
            net_re_cash_bucket = 0.0
            hf_harvest_cash_bucket = 0.0

        lp_cash_yield_target = 0.0
        lp_cash_yield_paid = 0.0
        lp_cash_yield_shortfall = 0.0
        if lp_cash_yield_policy.enabled:
            unreturned_lp_capital = max(0.0, initial_lp_capital - lp_cumulative_distribution)
            lp_cash_yield_target = unreturned_lp_capital * lp_cash_yield_policy.target_annual_yield_on_unreturned_capital
            (
                lp_cash_yield_paid,
                lp_cash_yield_shortfall,
                net_re_cash_bucket,
                hf_harvest_cash_bucket,
                retained_cash,
                reserve_nav,
            ) = pay_lp_cash_yield(
                target=lp_cash_yield_target,
                net_re_cashflow=net_re_cash_bucket,
                hf_harvest=hf_harvest_cash_bucket,
                retained_cash=retained_cash,
                reserve_nav=reserve_nav,
                policy=lp_cash_yield_policy,
            )
            cumulative_lp_cash_yield_shortfall += lp_cash_yield_shortfall
            lp_distribution += lp_cash_yield_paid
            if lp_cash_yield_policy.reduce_lp_hurdle:
                lp_cumulative_distribution += lp_cash_yield_paid

        distributable_cash = 0.0
        if not cashflow_routing.enabled:
            if distribution_policy.distribute_re_cashflow_annually:
                distributable_cash += net_re_cash_bucket
            else:
                retained_cash += net_re_cash_bucket
            if distribution_policy.distribute_hf_realized_gains_annually:
                distributable_cash += hf_harvest_cash_bucket
            else:
                retained_cash += hf_harvest_cash_bucket
        retained_cash += reserve_return_cash

        lp_remaining_hurdle = max(0.0, lp_hurdle_amount - lp_cumulative_distribution)
        legacy_lp_distribution, retained_excess = (
            (0.0, distributable_cash)
            if distribution_policy.retain_cash_until_hurdle_redemption
            else pay_lp_distribution(distributable_cash, lp_remaining_hurdle)
        )
        retained_cash += retained_excess
        lp_cumulative_distribution += legacy_lp_distribution
        lp_distribution += legacy_lp_distribution

        refinance_proceeds = 0.0
        refinance_use_of_proceeds = ""
        for refinance_event in refinance_events_by_year.get(year, []):
            event_proceeds = re_nav * refinance_event.pct_of_re_nav
            refinance_proceeds += event_proceeds
            cumulative_refinance_proceeds += event_proceeds
            refinance_liability += event_proceeds
            refinance_use_of_proceeds = append_event_text(refinance_use_of_proceeds, refinance_event.use_of_proceeds)
            if refinance_event.use_of_proceeds == "lp_distribution":
                lp_remaining_hurdle = max(0.0, lp_hurdle_amount - lp_cumulative_distribution)
                refi_lp_distribution = min(event_proceeds, lp_remaining_hurdle)
                lp_distribution += refi_lp_distribution
                lp_cumulative_distribution += refi_lp_distribution
                cumulative_refinance_to_lp += refi_lp_distribution
                retained_cash += event_proceeds - refi_lp_distribution
            elif refinance_event.use_of_proceeds == "retained_cash":
                retained_cash += event_proceeds
            elif refinance_event.use_of_proceeds == "reserve":
                reserve_nav += event_proceeds
            else:
                raise ValueError(f"Unsupported refinance use_of_proceeds: {refinance_event.use_of_proceeds}")

        if real_estate_mode == "bottom_up":
            for deal_row in (row for row in deal_cashflows if row.year == year and row.refi_proceeds > 0):
                event_proceeds = deal_row.refi_proceeds
                refinance_proceeds += event_proceeds
                cumulative_refinance_proceeds += event_proceeds
                refinance_liability += deal_row.refi_liability_added
                refinance_use_of_proceeds = append_event_text(
                    refinance_use_of_proceeds,
                    f"deal:{deal_row.deal_name}:{deal_row.refinance_proceeds_use}",
                )
                if deal_row.refinance_proceeds_use in {"fund_liquidity", "retained_cash"}:
                    retained_cash += event_proceeds
                elif deal_row.refinance_proceeds_use == "reserve":
                    reserve_nav += event_proceeds
                    cumulative_cash_added_to_reserve += event_proceeds
                else:
                    raise ValueError(
                        f"Unsupported deal refinance proceeds_use: {deal_row.refinance_proceeds_use}"
                    )

        lp_remaining_hurdle = max(0.0, lp_hurdle_amount - lp_cumulative_distribution)
        fund_nav_before_redemption = re_nav + hf_nav + reserve_nav + retained_cash - refinance_liability
        economic_hurdle_passed = (
            fund_nav_before_redemption + lp_cumulative_distribution >= lp_hurdle_amount
            if config.waterfall.include_unrealized_nav_in_hurdle_test
            else lp_cumulative_distribution >= lp_hurdle_amount
        )
        liquidity_available = available_liquidity(
            reserve_nav=reserve_nav,
            hf_nav=hf_nav,
            re_nav=re_nav,
            retained_cash=retained_cash,
            liquidity=liquidity,
            refinance_liability=refinance_liability,
        )
        liquidity_hurdle_passed = (
            liquidity_available >= lp_remaining_hurdle
            if config.waterfall.require_liquidity_for_lp_redemption
            else True
        )

        event_flag = ""
        if acquisition_unfunded_shortfall > 0:
            event_flag = append_event_text(event_flag, "ACQUISITION_FUNDING_SHORTFALL")
        if re_cashflow_shortfall > 0:
            event_flag = append_event_text(event_flag, "RE_CASHFLOW_SHORTFALL")
        trigger_result = evaluate_hurdle_completion_trigger(
            trigger=config.hurdle_completion_trigger,
            backend_strategy=backend_liquidity_strategy,
            year=year,
            lp_remaining_hurdle=lp_remaining_hurdle,
            lp_cumulative_distribution=lp_cumulative_distribution,
            initial_lp_capital=initial_lp_capital,
            economic_hurdle_passed=economic_hurdle_passed,
            retained_cash=retained_cash,
            reserve_nav=reserve_nav,
            hf_nav=hf_nav,
            re_nav=re_nav,
            refinance_liability=refinance_liability,
            reserve_liquidation_capacity_pct=liquidity.reserve_liquidation_capacity_pct_per_year,
        )
        if trigger_result["executed"]:
            lp_distribution += trigger_result["lp_distribution"]
            lp_cumulative_distribution += trigger_result["lp_distribution"]
            retained_cash = trigger_result["retained_cash"]
            reserve_nav = trigger_result["reserve_nav"]
            hf_nav = trigger_result["hf_nav"]
            re_nav = trigger_result["re_nav"]
            refinance_liability += trigger_result["from_refi"]
            lp_remaining_hurdle = 0.0
            gp_residual_nav = re_nav + hf_nav + reserve_nav + retained_cash - refinance_liability
            fund_nav = gp_residual_nav
            event_flag = append_event_text(event_flag, "HURDLE_COMPLETION_TRIGGER_EXECUTED")
            year_hurdle_achieved = year
            hurdle_trigger_year = year
            total_trigger_cash_from_retained_cash += trigger_result["from_retained_cash"]
            total_trigger_cash_from_reserve += trigger_result["from_reserve"]
            total_trigger_cash_from_hf_liquidation += trigger_result["from_hf_liquidation"]
            total_trigger_cash_from_refi += trigger_result["from_refi"]
            total_trigger_cash_from_re_sale += trigger_result["from_re_sale"]
            lp_hurdle_shortfall_after_final_trigger = 0.0
        elif trigger_result["attempted"]:
            event_flag = append_event_text(event_flag, "HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT")
            lp_hurdle_shortfall_after_final_trigger = trigger_result["shortfall_after_trigger"]

        if year_hurdle_achieved == year:
            pass
        elif trigger_result["attempted"]:
            liquidity_constrained = liquidity_constrained or economic_hurdle_passed
            fund_nav = fund_nav_before_redemption
        elif not backend_liquidity_strategy.enabled and economic_hurdle_passed and liquidity_hurdle_passed:
            redemption = redeem_lp(
                lp_remaining_hurdle=lp_remaining_hurdle,
                retained_cash=retained_cash,
                reserve_nav=reserve_nav,
                hf_nav=hf_nav,
                re_nav=re_nav,
                liquidity=liquidity,
                refinance_liability=refinance_liability,
            )
            lp_distribution += redemption.lp_distribution
            lp_cumulative_distribution += redemption.lp_distribution
            retained_cash = redemption.retained_cash
            reserve_nav = redemption.reserve_nav
            hf_nav = redemption.hf_nav
            re_nav = redemption.re_nav
            gp_residual_nav = redemption.gp_residual_nav - refinance_liability
            fund_nav = redemption.fund_nav - refinance_liability
            event_flag = redemption.event_flag
            year_hurdle_achieved = year
            lp_remaining_hurdle = 0.0
        elif economic_hurdle_passed:
            liquidity_constrained = True
            fund_nav = fund_nav_before_redemption
            event_flag = "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED"
        else:
            fund_nav = fund_nav_before_redemption

        lp_irr_cashflows.append(lp_distribution)
        cashflows.append(
            YearlyResult(
                scenario=name,
                year=year,
                re_opening_nav=re_opening_nav,
                re_noi_yield=re_noi_yield,
                re_noi=re_noi,
                gross_rent=gross_rent,
                re_asset_mgmt_fee=re_asset_mgmt_fee,
                net_re_cashflow=net_re_cashflow,
                re_cashflow_generated=re_cashflow_generated,
                re_cashflow_to_lp=re_cashflow_to_lp,
                re_cashflow_to_hf=re_cashflow_to_hf,
                re_cashflow_to_reserve=re_cashflow_to_reserve,
                re_appreciation_rate=re_appreciation_rate,
                re_closing_nav=re_nav,
                hf_opening_nav=hf_opening_nav,
                hf_return=hf_return,
                hf_harvest=hf_harvest,
                hf_harvest_generated=hf_harvest_generated,
                hf_harvest_to_lp=hf_harvest_to_lp,
                hf_harvest_to_hf=hf_harvest_to_hf,
                hf_harvest_to_reserve=hf_harvest_to_reserve,
                hf_closing_nav=hf_nav,
                refinance_proceeds=refinance_proceeds,
                refinance_use_of_proceeds=refinance_use_of_proceeds,
                cumulative_refinance_proceeds=cumulative_refinance_proceeds,
                refinance_liability=refinance_liability,
                reserve_opening_nav=reserve_opening_nav,
                reserve_closing_nav=reserve_nav,
                retained_cash=retained_cash,
                lp_cash_yield_target=lp_cash_yield_target,
                lp_cash_yield_paid=lp_cash_yield_paid,
                lp_cash_yield_shortfall=lp_cash_yield_shortfall,
                cumulative_lp_cash_yield_shortfall=cumulative_lp_cash_yield_shortfall,
                lp_cash_yield_coverage_ratio=(
                    lp_cash_yield_paid / lp_cash_yield_target if lp_cash_yield_target > 0 else None
                ),
                cumulative_reinvested_into_hf=cumulative_reinvested_into_hf,
                cumulative_cash_distributed_to_lp=lp_cumulative_distribution,
                cumulative_cash_added_to_reserve=cumulative_cash_added_to_reserve,
                hf_reinvestment_source_re=re_cashflow_to_hf,
                hf_reinvestment_source_hf=hf_harvest_to_hf,
                total_cash_reinvested=re_cashflow_to_hf + hf_harvest_to_hf,
                total_cash_distributed=lp_distribution,
                total_cash_reserved=re_cashflow_to_reserve + hf_harvest_to_reserve,
                lp_distribution=lp_distribution,
                lp_cumulative_distribution=lp_cumulative_distribution,
                lp_remaining_hurdle=lp_remaining_hurdle,
                economic_hurdle_passed=economic_hurdle_passed,
                liquidity_available=liquidity_available,
                liquidity_hurdle_passed=liquidity_hurdle_passed,
                gp_fees=gp_fees,
                gp_cumulative_fees=gp_cumulative_fees,
                gp_residual_nav=gp_residual_nav,
                fund_nav=fund_nav,
                real_estate_mode=real_estate_mode,
                re_gross_asset_value=re_gross_asset_value,
                re_debt_balance=re_debt_balance,
                re_assumed_liabilities=re_assumed_liabilities,
                re_net_equity_value=re_net_equity_value,
                re_debt_service=re_debt_service,
                re_capex=re_capex,
                re_dscr=re_dscr,
                re_prior_refi_liability=re_prior_refi_liability,
                re_ending_refi_liability=re_ending_refi_liability,
                re_max_debt_supported=re_max_debt_supported,
                re_cash_out_before_refi_costs=re_cash_out_before_refi_costs,
                re_refi_costs=re_refi_costs,
                re_refi_capacity=re_refi_capacity,
                re_refi_proceeds_from_deals=re_refi_proceeds_from_deals,
                re_free_cashflow_after_debt_and_capex=re_free_cashflow_after_debt_and_capex,
                re_cashflow_shortfall=re_cashflow_shortfall,
                active_deal_count=active_deal_count,
                acquisition_starting_retained_cash=acquisition_starting_retained_cash,
                acquisition_starting_reserve=acquisition_starting_reserve,
                acquisition_new_deal_equity_required=acquisition_new_deal_equity_required,
                acquisition_funded_from_initial_lp_capital=acquisition_funded_from_initial_lp_capital,
                acquisition_funded_from_retained_cash=acquisition_funded_from_retained_cash,
                acquisition_funded_from_reserve=acquisition_funded_from_reserve,
                acquisition_unfunded_shortfall=acquisition_unfunded_shortfall,
                acquisition_ending_retained_cash=acquisition_ending_retained_cash,
                acquisition_ending_reserve=acquisition_ending_reserve,
                acquisition_funding_source=acquisition_funding_source,
                hurdle_trigger_eligible=trigger_result["eligible"],
                hurdle_trigger_attempted=trigger_result["attempted"],
                hurdle_trigger_executed=trigger_result["executed"],
                hurdle_trigger_required_cash=trigger_result["required_cash"],
                trigger_cash_from_retained_cash=trigger_result["from_retained_cash"],
                trigger_cash_from_reserve=trigger_result["from_reserve"],
                trigger_cash_from_hf_liquidation=trigger_result["from_hf_liquidation"],
                trigger_cash_from_refi=trigger_result["from_refi"],
                trigger_cash_from_re_sale=trigger_result["from_re_sale"],
                lp_hurdle_shortfall_after_trigger=trigger_result["shortfall_after_trigger"],
                hf_nav_liquidated_for_hurdle=trigger_result["from_hf_liquidation"],
                refi_proceeds_for_hurdle=trigger_result["from_refi"],
                re_nav_sold_for_hurdle=trigger_result["from_re_sale"],
                event_flag=event_flag,
            )
        )
        if year_hurdle_achieved is not None:
            break

    final_fund_nav = cashflows[-1].fund_nav if cashflows else 0.0
    lp_cash_moic = moic(lp_cumulative_distribution, initial_lp_capital)
    remaining_claim = 0.0 if year_hurdle_achieved else min(final_fund_nav, max(0.0, lp_hurdle_amount - lp_cumulative_distribution))
    lp_economic_moic = economic_moic(lp_cumulative_distribution, remaining_claim, initial_lp_capital)
    lp_cash_irr = annual_irr(lp_irr_cashflows)
    lp_economic_irr_cashflows = list(lp_irr_cashflows)
    if year_hurdle_achieved is None and lp_economic_irr_cashflows:
        lp_economic_irr_cashflows[-1] += remaining_claim
    lp_economic_irr = annual_irr(lp_economic_irr_cashflows)
    lp_irr = lp_cash_irr
    gp_total_economics = gp_cumulative_fees + gp_residual_nav
    gp_cashflows = [-config.model.gp_co_investment]
    for index, row in enumerate(cashflows):
        gp_cashflow = row.gp_fees
        if index == len(cashflows) - 1:
            gp_cashflow += gp_residual_nav
        gp_cashflows.append(gp_cashflow)
    gp_cash_irr = annual_irr(gp_cashflows) if config.model.gp_co_investment > 0 else None
    gp_total_value_multiple = gp_total_economics / config.model.gp_co_investment if config.model.gp_co_investment > 0 else None
    gp_survivability = calculate_gp_survivability(config, cashflows)
    lp_experience = calculate_lp_experience(config, cashflows, initial_lp_capital, lp_hurdle_amount)
    total_re_cashflow_generated = sum(row.re_cashflow_generated for row in cashflows)
    total_hf_harvest_generated = sum(row.hf_harvest_generated for row in cashflows)
    total_cash_sources = total_re_cashflow_generated + total_hf_harvest_generated
    total_reinvested_into_hf = sum(row.total_cash_reinvested for row in cashflows)
    total_distributed_to_lp = sum(row.total_cash_distributed for row in cashflows)
    total_added_to_reserve = sum(row.total_cash_reserved for row in cashflows)
    final_re_gross_asset_value = cashflows[-1].re_gross_asset_value if cashflows else 0.0
    final_re_debt_balance = cashflows[-1].re_debt_balance if cashflows else 0.0
    final_re_assumed_liabilities = cashflows[-1].re_assumed_liabilities if cashflows else 0.0
    final_re_net_equity_value = cashflows[-1].re_net_equity_value if cashflows else 0.0
    final_re_dscr = cashflows[-1].re_dscr if cashflows else None
    total_re_debt_service = sum(row.re_debt_service for row in cashflows)
    total_re_capex = sum(row.re_capex for row in cashflows)
    total_deal_refi_proceeds = sum(row.re_refi_proceeds_from_deals for row in cashflows)
    total_re_cashflow_shortfall = sum(row.re_cashflow_shortfall for row in cashflows)
    total_acquisition_equity_required = sum(row.acquisition_new_deal_equity_required for row in cashflows)
    total_acquisition_funded_from_retained_cash = sum(row.acquisition_funded_from_retained_cash for row in cashflows)
    total_acquisition_funded_from_reserve = sum(row.acquisition_funded_from_reserve for row in cashflows)
    total_acquisition_unfunded_shortfall = sum(row.acquisition_unfunded_shortfall for row in cashflows)
    flags = build_flags(
        name=name,
        config=config,
        cashflows=cashflows,
        initial_lp_capital=initial_lp_capital,
        initial_hf_nav=initial_hf_nav,
        initial_re_nav=initial_re_nav,
        lp_hurdle_achieved=year_hurdle_achieved is not None,
        year_hurdle_achieved=year_hurdle_achieved,
        liquidity_constrained=liquidity_constrained,
        final_fund_nav=final_fund_nav,
        lp_cumulative_distribution=lp_cumulative_distribution,
        lp_irr=lp_irr,
        gp_residual_nav=gp_residual_nav,
        gp_cumulative_fees=gp_cumulative_fees,
        cumulative_refinance_to_lp=cumulative_refinance_to_lp,
        lp_cash_yield_shortfall=cumulative_lp_cash_yield_shortfall,
        gp_survivability_risk=gp_survivability["gp_survivability_risk"],
        lp_experience=lp_experience,
    )
    primary_flag = choose_primary_flag(flags, lp_hurdle_achieved=year_hurdle_achieved is not None)
    summary = {
        "scenario": name,
        "description": scenario.description,
        "real_estate_mode": real_estate_mode,
        "lp_initial_capital": initial_lp_capital,
        "initial_re_cash_deployed": initial_re_cash_deployed,
        "initial_re_gross_asset_value": initial_re_gross_asset_value,
        "initial_re_debt_balance": initial_re_debt_balance,
        "initial_re_assumed_liabilities": initial_re_assumed_liabilities,
        "initial_re_net_equity_value": initial_re_net_equity_value,
        "initial_re_entry_equity_cushion": initial_re_entry_equity_cushion,
        "initial_re_value_to_new_equity_multiple": initial_re_value_to_new_equity_multiple,
        "final_re_gross_asset_value": final_re_gross_asset_value,
        "final_re_debt_balance": final_re_debt_balance,
        "final_re_assumed_liabilities": final_re_assumed_liabilities,
        "final_re_net_equity_value": final_re_net_equity_value,
        "final_re_dscr": final_re_dscr,
        "total_re_debt_service": total_re_debt_service,
        "total_re_capex": total_re_capex,
        "total_deal_refi_proceeds": total_deal_refi_proceeds,
        "total_re_cashflow_shortfall": total_re_cashflow_shortfall,
        "total_acquisition_equity_required": total_acquisition_equity_required,
        "total_acquisition_funded_from_retained_cash": total_acquisition_funded_from_retained_cash,
        "total_acquisition_funded_from_reserve": total_acquisition_funded_from_reserve,
        "total_acquisition_unfunded_shortfall": total_acquisition_unfunded_shortfall,
        "years_modelled": len(cashflows),
        "lp_hurdle_moic": config.waterfall.lp_hurdle_moic,
        "lp_hurdle_amount": lp_hurdle_amount,
        "lp_cash_distributions": lp_cumulative_distribution,
        "lp_cash_moic": lp_cash_moic,
        "lp_economic_moic": lp_economic_moic,
        "lp_irr": lp_irr,
        "lp_cash_irr": lp_cash_irr,
        "lp_economic_irr": lp_economic_irr,
        "gp_cash_irr_if_co_investment": gp_cash_irr,
        "gp_total_value_multiple_if_co_investment": gp_total_value_multiple,
        "lp_hurdle_achieved": year_hurdle_achieved is not None,
        "year_hurdle_achieved": year_hurdle_achieved,
        "liquidity_constrained": liquidity_constrained,
        "final_fund_nav": final_fund_nav,
        "final_refinance_liability": refinance_liability,
        "gp_cumulative_fees": gp_cumulative_fees,
        "gp_residual_nav": gp_residual_nav,
        "gp_total_economics": gp_total_economics,
        "gp_residual_nav_pct_initial_lp_capital": gp_residual_nav / initial_lp_capital,
        "gp_total_economics_pct_initial_lp_capital": gp_total_economics / initial_lp_capital,
        "gp_cumulative_fees_first_n_years": gp_survivability["gp_cumulative_fees_first_n_years"],
        "gp_average_annual_fees_first_n_years": gp_survivability["gp_average_annual_fees_first_n_years"],
        "gp_survivability_risk": gp_survivability["gp_survivability_risk"],
        "lp_final_unrecovered_hurdle": max(0.0, lp_hurdle_amount - lp_cumulative_distribution),
        "lp_redeemed_by_model_end": year_hurdle_achieved is not None,
        "total_re_cashflow_generated": total_re_cashflow_generated,
        "total_hf_harvest_generated": total_hf_harvest_generated,
        "total_reinvested_into_hf": total_reinvested_into_hf,
        "total_distributed_to_lp": total_distributed_to_lp,
        "total_added_to_reserve": total_added_to_reserve,
        "pct_total_cash_distributed": total_distributed_to_lp / total_cash_sources if total_cash_sources > 0 else None,
        "pct_total_cash_reinvested": total_reinvested_into_hf / total_cash_sources if total_cash_sources > 0 else None,
        "pct_total_cash_reserved": total_added_to_reserve / total_cash_sources if total_cash_sources > 0 else None,
        "years_until_lp_1x_cash_return": year_until_cash_multiple(cashflows, initial_lp_capital, 1.0),
        "years_until_lp_2x_cash_return": year_until_cash_multiple(cashflows, initial_lp_capital, config.waterfall.lp_hurdle_moic),
        "lp_cashflow_profile_type": classify_lp_cashflow_profile(cashflows, initial_lp_capital),
        "hurdle_completion_trigger_enabled": config.hurdle_completion_trigger.enabled,
        "backend_liquidity_strategy_enabled": backend_liquidity_strategy.enabled,
        "backend_liquidity_target_years": ", ".join(str(year) for year in backend_liquidity_strategy.target_years),
        "backend_liquidity_refi_first": backend_liquidity_strategy.refi_first,
        "backend_liquidity_max_refi_pct_of_re_nav": backend_liquidity_strategy.max_refi_pct_of_re_nav,
        "backend_liquidity_max_hf_liquidation_pct": backend_liquidity_strategy.max_hf_liquidation_pct,
        "hurdle_trigger_executed": any(row.hurdle_trigger_executed for row in cashflows),
        "hurdle_trigger_year": hurdle_trigger_year,
        "total_trigger_cash_from_retained_cash": total_trigger_cash_from_retained_cash,
        "total_trigger_cash_from_reserve": total_trigger_cash_from_reserve,
        "total_trigger_cash_from_hf_liquidation": total_trigger_cash_from_hf_liquidation,
        "total_trigger_cash_from_refi": total_trigger_cash_from_refi,
        "total_trigger_cash_from_re_sale": total_trigger_cash_from_re_sale,
        "lp_hurdle_shortfall_after_final_trigger": lp_hurdle_shortfall_after_final_trigger,
        **lp_experience,
        "primary_flag": primary_flag,
        "all_flags": "; ".join(flag.flag for flag in flags),
    }
    return ScenarioResult(name, scenario.description, summary, cashflows, flags, deal_cashflows)


def calculate_re_fee(config: ModelConfig, re_opening_nav: float, re_noi: float, gross_rent: float) -> float:
    fee_config = config.fees.real_estate_asset_management_fee
    if not fee_config.enabled:
        return 0.0
    if fee_config.basis == "gross_rent":
        basis = gross_rent
    elif fee_config.basis == "noi":
        basis = re_noi
    elif fee_config.basis == "re_nav":
        basis = re_opening_nav
    else:
        raise ValueError(f"Unsupported real estate fee basis: {fee_config.basis}")
    return basis * fee_config.rate


def route_cashflow(amount: float, route: CashflowRoute) -> dict[str, float]:
    """Split a generated cashflow into LP, HF reinvestment, and reserve buckets."""
    routed_amount = max(0.0, amount)
    return {
        "lp": routed_amount * route.lp_distribution_pct,
        "hf": routed_amount * route.hf_reinvestment_pct,
        "reserve": routed_amount * route.reserve_pct,
    }


def evaluate_hurdle_completion_trigger(
    *,
    trigger: HurdleCompletionTriggerSettings,
    backend_strategy: BackendLiquidityStrategySettings | None = None,
    year: int | None = None,
    lp_remaining_hurdle: float,
    lp_cumulative_distribution: float,
    initial_lp_capital: float,
    economic_hurdle_passed: bool,
    retained_cash: float,
    reserve_nav: float,
    hf_nav: float,
    re_nav: float,
    refinance_liability: float,
    reserve_liquidation_capacity_pct: float,
) -> dict[str, float | bool]:
    """Test and, if fully fundable, execute the active LP hurdle completion trigger.

    This is separate from the passive liquidity test. It models a GP choosing to
    monetize permitted sources now, but only if the configured sources can fully
    extinguish the remaining LP cash hurdle.
    """
    result: dict[str, float | bool] = {
        "eligible": False,
        "attempted": False,
        "executed": False,
        "required_cash": max(0.0, lp_remaining_hurdle),
        "lp_distribution": 0.0,
        "from_retained_cash": 0.0,
        "from_reserve": 0.0,
        "from_hf_liquidation": 0.0,
        "from_refi": 0.0,
        "from_re_sale": 0.0,
        "shortfall_after_trigger": max(0.0, lp_remaining_hurdle),
        "retained_cash": retained_cash,
        "reserve_nav": reserve_nav,
        "hf_nav": hf_nav,
        "re_nav": re_nav,
    }
    if not trigger.enabled or lp_remaining_hurdle <= 1e-9:
        return result
    if backend_strategy and backend_strategy.enabled:
        if year is None or year not in backend_strategy.target_years:
            return result
    if trigger.trigger_when_economic_hurdle_passed and not economic_hurdle_passed:
        return result

    current_cash_moic = lp_cumulative_distribution / initial_lp_capital
    if current_cash_moic + 1e-9 < trigger.minimum_lp_cash_moic_before_trigger:
        return result

    result["eligible"] = True
    result["attempted"] = True
    if backend_strategy and backend_strategy.enabled:
        capacities = {
            "from_retained_cash": retained_cash if trigger.allow_retained_cash_use and backend_strategy.use_retained_cash else 0.0,
            "from_reserve": (
                reserve_nav * reserve_liquidation_capacity_pct
                if trigger.allow_reserve_use and backend_strategy.use_reserve
                else 0.0
            ),
            "from_hf_liquidation": (
                hf_nav * backend_strategy.max_hf_liquidation_pct if trigger.allow_hf_liquidation else 0.0
            ),
            "from_refi": (
                max(0.0, re_nav * backend_strategy.max_refi_pct_of_re_nav - refinance_liability)
                if trigger.allow_refi
                else 0.0
            ),
            "from_re_sale": re_nav * trigger.max_partial_re_sale_pct_of_re_nav if trigger.allow_partial_re_sale else 0.0,
        }
        funding_order = (
            ["from_retained_cash", "from_refi", "from_reserve", "from_hf_liquidation", "from_re_sale"]
            if backend_strategy.refi_first
            else ["from_retained_cash", "from_reserve", "from_hf_liquidation", "from_refi", "from_re_sale"]
        )
    else:
        capacities = {
            "from_retained_cash": retained_cash if trigger.allow_retained_cash_use else 0.0,
            "from_reserve": reserve_nav * reserve_liquidation_capacity_pct if trigger.allow_reserve_use else 0.0,
            "from_hf_liquidation": hf_nav * trigger.max_hf_liquidation_pct if trigger.allow_hf_liquidation else 0.0,
            "from_refi": max(0.0, re_nav * trigger.max_refi_pct_of_re_nav - refinance_liability) if trigger.allow_refi else 0.0,
            "from_re_sale": re_nav * trigger.max_partial_re_sale_pct_of_re_nav if trigger.allow_partial_re_sale else 0.0,
        }
        funding_order = ["from_retained_cash", "from_reserve", "from_hf_liquidation", "from_refi", "from_re_sale"]
    total_capacity = sum(capacities.values())
    if total_capacity + 1e-6 < lp_remaining_hurdle:
        result["shortfall_after_trigger"] = lp_remaining_hurdle - total_capacity
        return result

    remaining = lp_remaining_hurdle
    for key in funding_order:
        use_amount = min(capacities[key], remaining)
        result[key] = use_amount
        remaining -= use_amount
        if remaining <= 1e-9:
            break

    result["executed"] = True
    result["lp_distribution"] = lp_remaining_hurdle
    result["shortfall_after_trigger"] = 0.0
    result["retained_cash"] = retained_cash - float(result["from_retained_cash"])
    result["reserve_nav"] = reserve_nav - float(result["from_reserve"])
    result["hf_nav"] = hf_nav - float(result["from_hf_liquidation"])
    # Refinance proceeds are new liquidity and do not reduce RE NAV in this version.
    result["re_nav"] = re_nav - float(result["from_re_sale"])
    return result


def year_until_cash_multiple(cashflows: list[YearlyResult], initial_lp_capital: float, multiple: float) -> int | None:
    target = initial_lp_capital * multiple
    for row in cashflows:
        if row.lp_cumulative_distribution >= target:
            return row.year
    return None


def classify_lp_cashflow_profile(cashflows: list[YearlyResult], initial_lp_capital: float) -> str:
    if not cashflows:
        return "MODERATE_YIELD"
    total_distributions = sum(row.lp_distribution for row in cashflows)
    if total_distributions <= 0:
        return "BACKEND_HEAVY"
    final_window_start = max(1, int(len(cashflows) * 0.75) + 1)
    final_window_distributions = sum(row.lp_distribution for row in cashflows if row.year >= final_window_start)
    average_annual_distribution = total_distributions / len(cashflows)
    if final_window_distributions / total_distributions > 0.60:
        return "BACKEND_HEAVY"
    if average_annual_distribution / initial_lp_capital > 0.12:
        return "AGGRESSIVE_DISTRIBUTION"
    return "MODERATE_YIELD"


def pay_lp_cash_yield(
    *,
    target: float,
    net_re_cashflow: float,
    hf_harvest: float,
    retained_cash: float,
    reserve_nav: float,
    policy: LPCashYieldPolicy,
) -> tuple[float, float, float, float, float, float]:
    """Pay target LP cash yield from configured cash sources without selling RE/HF NAV."""
    remaining_target = target
    paid = 0.0
    source_balances = {
        "net_re_cashflow": net_re_cashflow,
        "hf_harvest": hf_harvest,
        "retained_cash": retained_cash,
        "reserve": reserve_nav,
    }
    for source in policy.source_priority:
        available = max(0.0, source_balances[source])
        use_amount = min(available, remaining_target)
        source_balances[source] -= use_amount
        paid += use_amount
        remaining_target -= use_amount
        if remaining_target <= 1e-9:
            break
    return (
        paid,
        max(0.0, target - paid),
        source_balances["net_re_cashflow"],
        source_balances["hf_harvest"],
        source_balances["retained_cash"],
        source_balances["reserve"],
    )


def events_by_year(events: list[RefinanceEvent]) -> dict[int, list[RefinanceEvent]]:
    grouped: dict[int, list[RefinanceEvent]] = {}
    for event in events:
        grouped.setdefault(event.year, []).append(event)
    return grouped


def append_event_text(existing: str, value: str) -> str:
    if not existing:
        return value
    return f"{existing};{value}"


def calculate_gp_survivability(config: ModelConfig, cashflows: list[YearlyResult]) -> dict[str, float | bool]:
    years = config.gp_survivability.first_n_years
    fees = sum(row.gp_fees for row in cashflows[:years])
    denominator = min(years, len(cashflows)) or 1
    average = fees / denominator
    risk = (
        fees < config.gp_survivability.minimum_cumulative_fees
        or average < config.gp_survivability.minimum_average_annual_fees
    )
    return {
        "gp_cumulative_fees_first_n_years": fees,
        "gp_average_annual_fees_first_n_years": average,
        "gp_survivability_risk": risk,
    }


def calculate_lp_experience(
    config: ModelConfig,
    cashflows: list[YearlyResult],
    initial_lp_capital: float,
    lp_hurdle_amount: float,
) -> dict[str, int | None]:
    years_with_zero_distribution = 0
    years_with_distribution_below_target_yield = 0
    longest_zero_distribution_streak = 0
    current_zero_streak = 0
    longest_below_target_yield_streak = 0
    current_below_target_streak = 0
    years_until_first_distribution: int | None = None
    lp_time_under_1x_cash_moic = 0
    lp_time_under_1x_economic_moic = 0

    for row in cashflows:
        if row.lp_distribution == 0:
            years_with_zero_distribution += 1
            current_zero_streak += 1
            longest_zero_distribution_streak = max(longest_zero_distribution_streak, current_zero_streak)
        else:
            if years_until_first_distribution is None:
                years_until_first_distribution = row.year
            current_zero_streak = 0

        if config.lp_cash_yield_policy.enabled and row.lp_distribution < row.lp_cash_yield_target:
            years_with_distribution_below_target_yield += 1
            current_below_target_streak += 1
            longest_below_target_yield_streak = max(longest_below_target_yield_streak, current_below_target_streak)
        else:
            current_below_target_streak = 0

        if row.lp_cumulative_distribution < initial_lp_capital:
            lp_time_under_1x_cash_moic += 1
        remaining_claim = min(row.fund_nav, max(0.0, lp_hurdle_amount - row.lp_cumulative_distribution))
        if row.lp_cumulative_distribution + remaining_claim < initial_lp_capital:
            lp_time_under_1x_economic_moic += 1

    return {
        "years_with_zero_lp_distribution": years_with_zero_distribution,
        "years_with_distribution_below_target_yield": years_with_distribution_below_target_yield,
        "longest_zero_distribution_streak": longest_zero_distribution_streak,
        "longest_below_target_yield_streak": longest_below_target_yield_streak,
        "years_until_first_distribution": years_until_first_distribution,
        "lp_time_under_1x_cash_moic": lp_time_under_1x_cash_moic,
        "lp_time_under_1x_economic_moic": lp_time_under_1x_economic_moic,
    }


def build_flags(
    *,
    name: str,
    config: ModelConfig,
    cashflows: list[YearlyResult],
    initial_lp_capital: float,
    initial_hf_nav: float,
    initial_re_nav: float,
    lp_hurdle_achieved: bool,
    year_hurdle_achieved: int | None,
    liquidity_constrained: bool,
    final_fund_nav: float,
    lp_cumulative_distribution: float,
    lp_irr: float | None,
    gp_residual_nav: float,
    gp_cumulative_fees: float,
    cumulative_refinance_to_lp: float,
    lp_cash_yield_shortfall: float,
    gp_survivability_risk: bool,
    lp_experience: dict[str, int | None],
) -> list[FlagResult]:
    thresholds = config.flag_thresholds
    flags: list[FlagResult] = []

    def add(flag: str, severity: str, explanation: str) -> None:
        flags.append(FlagResult(name, flag, severity, explanation))

    if lp_hurdle_achieved:
        add("LP_HURDLE_ACHIEVED", "info", f"LP reached {config.waterfall.lp_hurdle_moic:.2f}x in year {year_hurdle_achieved}.")
    else:
        add("LP_HURDLE_NOT_ACHIEVED", "high", "LP did not reach the target cash MOIC within the model horizon.")

    if liquidity_constrained:
        add("HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED", "high", "Economic hurdle passed before available liquidity could redeem LPs.")

    if (
        lp_hurdle_achieved
        and year_hurdle_achieved is not None
        and year_hurdle_achieved <= thresholds.fast_gp_dynasty_max_year
        and gp_residual_nav >= thresholds.fast_gp_dynasty_residual_multiple * initial_lp_capital
    ):
        add("FAST_GP_DYNASTY_OUTCOME", "medium", "LP redemption is fast and GP residual NAV is large.")

    if (not lp_hurdle_achieved) or (
        year_hurdle_achieved is not None and year_hurdle_achieved >= thresholds.slow_time_horizon_year
    ):
        add("SLOW_TIME_HORIZON_DRIFT", "medium", "LP outcome takes a long time or does not arrive within the horizon.")

    if gp_survivability_risk:
        add("GP_SURVIVABILITY_RISK", "medium", "GP fee income in the early years is below the configured threshold.")

    if lp_cash_yield_shortfall > 0:
        add("LP_CASH_YIELD_SHORTFALL", "medium", "Available cash was insufficient to meet the configured LP cash yield target.")

    if any(row.hurdle_trigger_executed for row in cashflows):
        add("HURDLE_COMPLETION_TRIGGER_EXECUTED", "info", "Active hurdle completion trigger monetized permitted sources to extinguish LPs.")
    if any(row.hurdle_trigger_attempted and not row.hurdle_trigger_executed for row in cashflows):
        add("HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT", "high", "Active hurdle completion trigger was eligible, but permitted funding sources were insufficient.")
    if any(row.trigger_cash_from_hf_liquidation > 0 for row in cashflows):
        add("LP_REDEEMED_VIA_HF_LIQUIDATION", "medium", "LP hurdle completion used partial hedge fund liquidation.")
    if any(row.trigger_cash_from_refi > 0 for row in cashflows):
        add("LP_REDEEMED_VIA_REFI", "medium", "LP hurdle completion used refinance proceeds.")
    if any(row.trigger_cash_from_re_sale > 0 for row in cashflows):
        add("LP_REDEEMED_VIA_PARTIAL_RE_SALE", "medium", "LP hurdle completion used partial real estate sale proceeds.")

    if any(row.refinance_proceeds > 0 for row in cashflows):
        add("REFINANCE_EVENT_OCCURRED", "info", "One or more configured refinance events generated proceeds.")

    if lp_hurdle_achieved and cumulative_refinance_to_lp > 0 and lp_cumulative_distribution - cumulative_refinance_to_lp < config.model.initial_lp_capital * config.waterfall.lp_hurdle_moic:
        add("REFI_DEPENDENT_LP_OUTCOME", "medium", "LP hurdle achievement depended on refinance proceeds distributed to LPs.")

    if final_fund_nav + lp_cumulative_distribution < initial_lp_capital:
        add("FUND_NAV_IMPAIRED", "high", "Final NAV plus LP distributions is below initial LP capital.")

    min_hf_nav = min((row.hf_closing_nav for row in cashflows), default=initial_hf_nav)
    if initial_hf_nav > 0 and min_hf_nav < initial_hf_nav * (1 - thresholds.hf_major_drawdown_pct):
        add("HF_MAJOR_DRAWDOWN", "medium", "Hedge fund NAV fell by more than the configured drawdown threshold.")

    min_re_nav = min((row.re_closing_nav for row in cashflows), default=initial_re_nav)
    if initial_re_nav > 0 and min_re_nav < initial_re_nav * (1 - thresholds.re_nav_impairment_pct):
        add("RE_NAV_IMPAIRMENT", "medium", "Real estate NAV fell by more than the configured impairment threshold.")

    if (
        lp_irr is not None
        and lp_irr >= thresholds.lp_good_irr_threshold
        and gp_residual_nav >= thresholds.lp_good_irr_gp_residual_multiple * initial_lp_capital
    ):
        add("LP_GOOD_IRR_GP_LARGE_RESIDUAL", "medium", "LP IRR is attractive while GP residual NAV is large.")

    if (lp_experience.get("longest_zero_distribution_streak") or 0) >= thresholds.long_zero_distribution_years:
        add("LONG_ZERO_DISTRIBUTION_PERIOD", "medium", "LP experienced a long streak of zero-distribution years.")

    if cashflows and cashflows[-1].lp_cumulative_distribution < initial_lp_capital:
        add("LP_STILL_BELOW_1X_CASH_MOIC_AT_END", "medium", "LP cash distributions remain below 1.0x at model end.")

    if (
        cashflows
        and cashflows[-1].fund_nav + cashflows[-1].lp_cumulative_distribution >= initial_lp_capital
        and cashflows[-1].lp_cumulative_distribution < initial_lp_capital
    ):
        add("LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV", "medium", "Fund NAV is positive but LP cash recovery remains below 1.0x.")

    return flags


def choose_primary_flag(flags: list[FlagResult], *, lp_hurdle_achieved: bool) -> str:
    if lp_hurdle_achieved:
        priority = {
            "FAST_GP_DYNASTY_OUTCOME": 1,
            "HURDLE_COMPLETION_TRIGGER_EXECUTED": 2,
            "LP_GOOD_IRR_GP_LARGE_RESIDUAL": 3,
            "LP_HURDLE_ACHIEVED": 4,
            "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED": 50,
            "SLOW_TIME_HORIZON_DRIFT": 60,
        }
    else:
        priority = {
            "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED": 1,
            "LP_HURDLE_NOT_ACHIEVED": 2,
            "FUND_NAV_IMPAIRED": 3,
            "SLOW_TIME_HORIZON_DRIFT": 4,
        }
    return sorted((flag.flag for flag in flags), key=lambda flag: priority.get(flag, 50))[0]


def result_dicts(results: list[ScenarioResult]) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    summaries = [result.summary for result in results]
    cashflows = [asdict(row) for result in results for row in result.cashflows]
    flags = [asdict(flag) for result in results for flag in result.flags]
    deal_cashflows = [asdict(row) for result in results for row in result.deal_cashflows]
    return summaries, cashflows, flags, deal_cashflows
