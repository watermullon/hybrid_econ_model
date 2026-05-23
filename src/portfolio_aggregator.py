from __future__ import annotations

from typing import Any

from src.deal_model import run_deal_year
from src.deal_types import DealSet, DealYearResult, RealEstatePortfolioYearResult
from src.utils import deep_merge_dict


def apply_deal_overrides(deals: DealSet, overrides: dict[str, Any] | None) -> DealSet:
    """Apply scenario-level deal overrides and revalidate the complete deal set."""
    if not overrides:
        return deals

    normalized_overrides = overrides.get("deals", overrides)
    if not isinstance(normalized_overrides, dict):
        raise ValueError("deal_overrides must be a mapping of deal names to override mappings.")

    merged = deals.model_dump()
    for deal_name, deal_override in normalized_overrides.items():
        if deal_name not in merged["deals"]:
            raise ValueError(f"Unknown deal override '{deal_name}'.")
        if not isinstance(deal_override, dict):
            raise ValueError(f"Override for deal '{deal_name}' must be a mapping.")
        merged["deals"][deal_name] = deep_merge_dict(merged["deals"][deal_name], deal_override)
    return DealSet.model_validate(merged)


def build_re_portfolio_years(
    *,
    scenario_name: str,
    years: int,
    deals: DealSet,
    deal_overrides: dict[str, Any] | None = None,
) -> tuple[list[RealEstatePortfolioYearResult], list[DealYearResult]]:
    effective_deals = apply_deal_overrides(deals, deal_overrides)
    portfolio_years: list[RealEstatePortfolioYearResult] = []
    deal_rows: list[DealYearResult] = []
    cumulative_refi_liability_by_deal = {deal_name: 0.0 for deal_name in effective_deals.deals}

    for year in range(1, years + 1):
        funded_deal_names = {
            deal_name
            for deal_name, deal in effective_deals.deals.items()
            if deal.enabled and deal.acquisition_year <= year
        }
        portfolio_year, yearly_deals = build_re_portfolio_year(
            scenario_name=scenario_name,
            year=year,
            deals=effective_deals,
            funded_deal_names=funded_deal_names,
            cumulative_refi_liability_by_deal=cumulative_refi_liability_by_deal,
        )
        portfolio_years.append(portfolio_year)
        deal_rows.extend(yearly_deals)

    return portfolio_years, deal_rows


def build_re_portfolio_year(
    *,
    scenario_name: str,
    year: int,
    deals: DealSet,
    funded_deal_names: set[str],
    cumulative_refi_liability_by_deal: dict[str, float],
) -> tuple[RealEstatePortfolioYearResult, list[DealYearResult]]:
    """Build one stateful bottom-up RE portfolio year.

    The fund engine supplies funded_deal_names because deal funding is a
    fund-level cash decision. Unfunded deals still emit zero rows for auditability.
    """
    yearly_deals = []
    for deal_name, deal in deals.deals.items():
        row = run_deal_year(
            scenario_name=scenario_name,
            deal_name=deal_name,
            deal=deal,
            model_year=year,
            prior_refi_liability=cumulative_refi_liability_by_deal.setdefault(deal_name, 0.0),
            funded=deal_name in funded_deal_names,
        )
        cumulative_refi_liability_by_deal[deal_name] = row.ending_refi_liability
        yearly_deals.append(row)

    active_deals = [row for row in yearly_deals if row.active]
    noi = sum(row.noi for row in active_deals)
    debt_service = sum(row.debt_service for row in active_deals)
    entry_equity_cushion = sum(row.entry_equity_cushion for row in active_deals)
    new_equity_required = sum(row.new_equity_required for row in active_deals)
    deal_nav = sum(row.deal_nav for row in active_deals)
    deal_nav_before_refi_liability = sum(row.deal_nav_before_refi_liability for row in active_deals)
    deal_nav_after_refi_liability = sum(row.deal_nav_after_refi_liability for row in active_deals)

    return (
        RealEstatePortfolioYearResult(
            scenario=scenario_name,
            year=year,
            active_deal_count=len(active_deals),
            gross_asset_value=sum(row.asset_value for row in active_deals),
            debt_balance=sum(row.debt_balance for row in active_deals),
            assumed_liabilities=sum(row.assumed_liabilities for row in active_deals),
            net_equity_value=sum(row.net_equity_value for row in active_deals),
            noi=noi,
            gross_rent=sum(row.gross_rent for row in active_deals),
            debt_service=debt_service,
            capex=sum(row.capex for row in active_deals),
            free_cashflow_after_debt_and_capex=sum(row.free_cashflow_after_debt_and_capex for row in active_deals),
            dscr=noi / debt_service if debt_service > 0 else None,
            prior_refi_liability=sum(row.prior_refi_liability for row in active_deals),
            ending_refi_liability=sum(row.ending_refi_liability for row in active_deals),
            max_debt_supported=sum(row.max_debt_supported for row in active_deals),
            cash_out_before_refi_costs=sum(row.cash_out_before_refi_costs for row in active_deals),
            refi_costs=sum(row.refi_costs for row in active_deals),
            refi_capacity=sum(row.refi_capacity for row in active_deals),
            refi_proceeds=sum(row.refi_proceeds for row in active_deals),
            refinance_liability_added=sum(row.refi_liability_added for row in active_deals),
            deal_nav_before_refi_liability=deal_nav_before_refi_liability,
            deal_nav_after_refi_liability=deal_nav_after_refi_liability,
            deal_nav=deal_nav,
            entry_equity_cushion=entry_equity_cushion,
            value_to_new_equity_multiple=deal_nav / new_equity_required if new_equity_required > 0 else None,
        ),
        yearly_deals,
    )
