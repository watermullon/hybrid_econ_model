from __future__ import annotations

from dataclasses import asdict

from src.metrics import annual_irr, economic_moic, moic
from src.model_types import (
    FlagResult,
    LPCashYieldPolicy,
    ModelConfig,
    RefinanceEvent,
    Scenario,
    ScenarioResult,
    YearlyResult,
)
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


def run_all_scenarios(config: ModelConfig, scenarios: dict[str, Scenario]) -> list[ScenarioResult]:
    validate_all_scenarios(config, scenarios)
    return [run_scenario(name, scenario, config) for name, scenario in scenarios.items()]


def run_scenario(name: str, scenario: Scenario, config: ModelConfig) -> ScenarioResult:
    liquidity = merge_model(config.liquidity, scenario.liquidity)
    distribution_policy = merge_model(config.distribution_policy, scenario.distribution_policy)
    lp_cash_yield_policy = merge_model(config.lp_cash_yield_policy, scenario.lp_cash_yield_policy)
    reserve_settings = merge_model(config.reserve, scenario.reserve)
    refinance_events_by_year = events_by_year(scenario.refinance_events)

    initial_lp_capital = config.model.initial_lp_capital
    lp_hurdle_amount = initial_lp_capital * config.waterfall.lp_hurdle_moic
    re_nav, hf_nav, reserve_nav = calculate_initial_allocation(config, scenario)
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

    for year in range(1, scenario.years + 1):
        re_opening_nav = re_nav
        hf_opening_nav = hf_nav
        reserve_opening_nav = reserve_nav

        re_noi_yield = scenario.real_estate.initial_noi_yield * (
            (1 + scenario.real_estate.annual_noi_growth) ** (year - 1)
        )
        gross_rent_yield = value_for_year(scenario.real_estate.gross_rent_yield, year)
        re_appreciation_rate = value_for_year(scenario.real_estate.annual_nav_appreciation, year)
        re_noi = re_opening_nav * re_noi_yield
        gross_rent = re_opening_nav * gross_rent_yield
        re_asset_mgmt_fee = calculate_re_fee(config, re_opening_nav, re_noi, gross_rent)
        net_re_cashflow = re_noi - re_asset_mgmt_fee
        re_nav = re_opening_nav * (1 + re_appreciation_rate)

        hf_return = scenario.hedge_fund.annual_returns[year - 1]
        hf_nav_pre_harvest = hf_opening_nav * (1 + hf_return)
        hf_gain = max(0.0, hf_nav_pre_harvest - hf_opening_nav)
        hf_harvest = hf_gain * distribution_policy.hf_positive_return_harvest_rate
        hf_nav = hf_nav_pre_harvest - hf_harvest

        reserve_nav = reserve_opening_nav * (1 + reserve_settings.annual_return)
        reserve_return_cash = reserve_nav - reserve_opening_nav

        gp_fees = re_asset_mgmt_fee
        gp_cumulative_fees += gp_fees

        net_re_cash_bucket = net_re_cashflow
        hf_harvest_cash_bucket = hf_harvest

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
            if lp_cash_yield_policy.reduce_lp_hurdle:
                lp_cumulative_distribution += lp_cash_yield_paid

        distributable_cash = 0.0
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
        lp_distribution, retained_excess = (
            (0.0, distributable_cash)
            if distribution_policy.retain_cash_until_hurdle_redemption
            else pay_lp_distribution(distributable_cash, lp_remaining_hurdle)
        )
        retained_cash += retained_excess
        lp_cumulative_distribution += lp_distribution
        lp_distribution += lp_cash_yield_paid

        refinance_proceeds = 0.0
        refinance_use_of_proceeds = ""
        for refinance_event in refinance_events_by_year.get(year, []):
            event_proceeds = re_nav * refinance_event.pct_of_re_nav
            refinance_proceeds += event_proceeds
            cumulative_refinance_proceeds += event_proceeds
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

        lp_remaining_hurdle = max(0.0, lp_hurdle_amount - lp_cumulative_distribution)
        fund_nav_before_redemption = re_nav + hf_nav + reserve_nav + retained_cash
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
        )
        liquidity_hurdle_passed = (
            liquidity_available >= lp_remaining_hurdle
            if config.waterfall.require_liquidity_for_lp_redemption
            else True
        )

        event_flag = ""
        if economic_hurdle_passed and liquidity_hurdle_passed:
            redemption = redeem_lp(
                lp_remaining_hurdle=lp_remaining_hurdle,
                retained_cash=retained_cash,
                reserve_nav=reserve_nav,
                hf_nav=hf_nav,
                re_nav=re_nav,
                liquidity=liquidity,
            )
            lp_distribution += redemption.lp_distribution
            lp_cumulative_distribution += redemption.lp_distribution
            retained_cash = redemption.retained_cash
            reserve_nav = redemption.reserve_nav
            hf_nav = redemption.hf_nav
            re_nav = redemption.re_nav
            gp_residual_nav = redemption.gp_residual_nav
            fund_nav = redemption.fund_nav
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
                re_appreciation_rate=re_appreciation_rate,
                re_closing_nav=re_nav,
                hf_opening_nav=hf_opening_nav,
                hf_return=hf_return,
                hf_harvest=hf_harvest,
                hf_closing_nav=hf_nav,
                refinance_proceeds=refinance_proceeds,
                refinance_use_of_proceeds=refinance_use_of_proceeds,
                cumulative_refinance_proceeds=cumulative_refinance_proceeds,
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
        "lp_initial_capital": initial_lp_capital,
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
        **lp_experience,
        "primary_flag": primary_flag,
        "all_flags": "; ".join(flag.flag for flag in flags),
    }
    return ScenarioResult(name, scenario.description, summary, cashflows, flags)


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
            "LP_GOOD_IRR_GP_LARGE_RESIDUAL": 2,
            "LP_HURDLE_ACHIEVED": 3,
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


def result_dicts(results: list[ScenarioResult]) -> tuple[list[dict], list[dict], list[dict]]:
    summaries = [result.summary for result in results]
    cashflows = [asdict(row) for result in results for row in result.cashflows]
    flags = [asdict(flag) for result in results for flag in result.flags]
    return summaries, cashflows, flags
