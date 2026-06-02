from __future__ import annotations

from dataclasses import dataclass

from src.deal_types import DealConfig, DealYearResult


@dataclass(frozen=True)
class RefiCapacityResult:
    max_debt_supported: float
    cash_out_before_refi_costs: float
    refi_costs: float
    refi_capacity: float


def is_deal_active(deal: DealConfig, model_year: int) -> bool:
    return deal.enabled and model_year >= deal.acquisition_year


def relative_deal_year(deal: DealConfig, model_year: int) -> int:
    return model_year - deal.acquisition_year + 1


def calculate_noi(deal: DealConfig, relative_year: int) -> float:
    current = deal.operations.current_noi
    stabilized = deal.operations.stabilized_noi
    years = deal.operations.years_to_stabilization

    if current is None and stabilized is None:
        raise ValueError("Deal requires at least current_noi or stabilized_noi.")
    if current is None:
        current = stabilized
    if stabilized is None:
        stabilized = current
    assert current is not None
    assert stabilized is not None

    if years <= 1:
        base_noi = stabilized
    elif relative_year <= years:
        progress = (relative_year - 1) / (years - 1)
        base_noi = current + progress * (stabilized - current)
    else:
        base_noi = stabilized * (
            (1 + deal.operations.annual_noi_growth_after_stabilization) ** (relative_year - years)
        )
    return max(0.0, base_noi)


def calculate_gross_rent(deal: DealConfig, relative_year: int) -> float:
    if deal.operations.gross_rent is None:
        return 0.0
    return deal.operations.gross_rent * ((1 + deal.operations.gross_rent_growth) ** (relative_year - 1))


def calculate_debt_service(deal: DealConfig, debt_balance: float) -> float:
    if deal.debt.amortization_type == "interest_only":
        if deal.debt.interest_rate is None:
            raise ValueError("interest_only debt requires interest_rate.")
        return debt_balance * deal.debt.interest_rate
    if deal.debt.amortization_type == "fixed_annual_debt_service":
        if deal.debt.annual_debt_service is None:
            raise ValueError("fixed_annual_debt_service requires annual_debt_service.")
        return deal.debt.annual_debt_service
    raise ValueError(f"Unsupported amortization_type: {deal.debt.amortization_type}")


def calculate_capex(deal: DealConfig, relative_year: int, noi: float) -> float:
    return deal.capex.annual_capex.get(relative_year, 0.0) + deal.capex.recurring_capex_pct_of_noi * noi


def calculate_asset_value(deal: DealConfig, relative_year: int, noi: float) -> float:
    if deal.valuation.method == "growth":
        by_year = deal.valuation.value_growth_by_year
        if by_year:
            # Compound year by year using per-year overrides where specified
            value = deal.acquisition.asset_value
            for yr in range(1, relative_year):
                rate = by_year.get(yr, deal.valuation.annual_value_growth)
                value *= (1 + rate)
            return value
        return deal.acquisition.asset_value * ((1 + deal.valuation.annual_value_growth) ** (relative_year - 1))
    if deal.valuation.method == "cap_rate":
        if deal.valuation.exit_cap_rate is None:
            raise ValueError("cap_rate valuation requires exit_cap_rate.")
        return noi / deal.valuation.exit_cap_rate
    if deal.valuation.method == "fixed_stabilized_value":
        if deal.valuation.stabilized_value is None:
            raise ValueError("fixed_stabilized_value valuation requires stabilized_value.")
        return deal.valuation.stabilized_value
    raise ValueError(f"Unsupported valuation method: {deal.valuation.method}")


def calculate_refi_capacity(
    deal: DealConfig,
    asset_value: float,
    debt_balance: float,
    prior_refi_liability: float,
) -> RefiCapacityResult:
    if not deal.refinance.enabled:
        return RefiCapacityResult(
            max_debt_supported=0.0,
            cash_out_before_refi_costs=0.0,
            refi_costs=0.0,
            refi_capacity=0.0,
        )

    max_debt_supported = asset_value * deal.refinance.refi_ltv
    cash_out_before_costs = max_debt_supported - debt_balance - prior_refi_liability
    refi_costs = max(cash_out_before_costs, 0.0) * deal.refinance.refi_costs_pct
    refi_capacity = max(0.0, cash_out_before_costs - refi_costs)
    if deal.refinance.max_cash_out_pct_of_value is not None:
        refi_capacity = min(refi_capacity, asset_value * deal.refinance.max_cash_out_pct_of_value)

    return RefiCapacityResult(
        max_debt_supported=max_debt_supported,
        cash_out_before_refi_costs=cash_out_before_costs,
        refi_costs=refi_costs,
        refi_capacity=max(0.0, refi_capacity),
    )


def run_deal_year(
    *,
    scenario_name: str,
    deal_name: str,
    deal: DealConfig,
    model_year: int,
    prior_refi_liability: float = 0.0,
    funded: bool = True,
    prior_debt_paydown: float = 0.0,
    available_hf_for_cure: float = 0.0,
) -> DealYearResult:
    entry_equity_cushion = (
        deal.acquisition.asset_value
        - deal.capital_stack.assumed_debt
        - deal.capital_stack.assumed_liabilities
        - deal.capital_stack.seller_note
        - deal.capital_stack.preferred_equity
        - deal.acquisition.new_equity_required
    )

    if not funded or not is_deal_active(deal, model_year):
        return DealYearResult(
            scenario=scenario_name,
            deal_name=deal_name,
            year=model_year,
            relative_year=None,
            active=False,
            asset_value=0.0,
            debt_balance=0.0,
            assumed_liabilities=0.0,
            net_equity_value=0.0,
            noi=0.0,
            gross_rent=0.0,
            debt_service=0.0,
            capex=0.0,
            free_cashflow_after_debt_and_capex=0.0,
            dscr=None,
            prior_refi_liability=prior_refi_liability,
            ending_refi_liability=prior_refi_liability,
            max_debt_supported=0.0,
            cash_out_before_refi_costs=0.0,
            refi_costs=0.0,
            refi_capacity=0.0,
            refi_proceeds=0.0,
            refi_liability_added=0.0,
            deal_nav_before_refi_liability=0.0,
            deal_nav_after_refi_liability=0.0,
            deal_nav=0.0,
            entry_equity_cushion=entry_equity_cushion,
            value_to_new_equity_multiple=None,
            new_equity_required=0.0,
            refinance_proceeds_use=deal.refinance.proceeds_use,
        )

    relative_year = relative_deal_year(deal, model_year)
    debt_balance = deal.capital_stack.assumed_debt - prior_debt_paydown
    assumed_liabilities = deal.capital_stack.assumed_liabilities
    noi = calculate_noi(deal, relative_year)
    gross_rent = calculate_gross_rent(deal, relative_year)
    capex = calculate_capex(deal, relative_year, noi)
    asset_value = calculate_asset_value(deal, relative_year, noi)

    covenant_breach = False
    covenant_ltv: float | None = debt_balance / asset_value if asset_value > 0 else None
    covenant_paydown_required = 0.0
    covenant_paydown_applied = 0.0
    if deal.debt.ltv_covenant is not None and covenant_ltv is not None:
        if covenant_ltv > deal.debt.ltv_covenant:
            covenant_breach = True
            target_debt = asset_value * deal.debt.ltv_covenant
            covenant_paydown_required = debt_balance - target_debt
            covenant_paydown_applied = min(covenant_paydown_required, max(0.0, available_hf_for_cure))
            debt_balance -= covenant_paydown_applied
            covenant_ltv = debt_balance / asset_value if asset_value > 0 else None

    debt_service = calculate_debt_service(deal, debt_balance)
    free_cashflow = noi - debt_service - capex
    net_equity_value = asset_value - debt_balance - assumed_liabilities
    deal_nav_before_refi_liability = (
        net_equity_value - deal.capital_stack.seller_note - deal.capital_stack.preferred_equity
    )
    dscr = noi / debt_service if debt_service > 0 else None
    refi_result = calculate_refi_capacity(deal, asset_value, debt_balance, prior_refi_liability)
    refi_capacity = refi_result.refi_capacity
    refi_proceeds = refi_capacity if deal.refinance.enabled and model_year in deal.refinance.target_years else 0.0
    ending_refi_liability = prior_refi_liability + refi_proceeds
    deal_nav_after_refi_liability = deal_nav_before_refi_liability - ending_refi_liability

    return DealYearResult(
        scenario=scenario_name,
        deal_name=deal_name,
        year=model_year,
        relative_year=relative_year,
        active=True,
        asset_value=asset_value,
        debt_balance=debt_balance,
        assumed_liabilities=assumed_liabilities,
        net_equity_value=net_equity_value,
        noi=noi,
        gross_rent=gross_rent,
        debt_service=debt_service,
        capex=capex,
        free_cashflow_after_debt_and_capex=free_cashflow,
        dscr=dscr,
        prior_refi_liability=prior_refi_liability,
        ending_refi_liability=ending_refi_liability,
        max_debt_supported=refi_result.max_debt_supported,
        cash_out_before_refi_costs=refi_result.cash_out_before_refi_costs,
        refi_costs=refi_result.refi_costs,
        refi_capacity=refi_capacity,
        refi_proceeds=refi_proceeds,
        refi_liability_added=refi_proceeds,
        deal_nav_before_refi_liability=deal_nav_before_refi_liability,
        deal_nav_after_refi_liability=deal_nav_after_refi_liability,
        # Keep deal_nav as the existing pre-refi-liability convention for backward-compatible outputs.
        deal_nav=deal_nav_before_refi_liability,
        entry_equity_cushion=entry_equity_cushion,
        value_to_new_equity_multiple=(
            deal_nav_before_refi_liability / deal.acquisition.new_equity_required
            if deal.acquisition.new_equity_required > 0
            else None
        ),
        new_equity_required=deal.acquisition.new_equity_required,
        refinance_proceeds_use=deal.refinance.proceeds_use,
        covenant_breach=covenant_breach,
        covenant_ltv=covenant_ltv,
        covenant_paydown_required=covenant_paydown_required,
        covenant_paydown_applied=covenant_paydown_applied,
    )
