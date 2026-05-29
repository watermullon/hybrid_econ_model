"""Tax module — post-processing tax analysis for the Hybrid Fund model.

Separate from the engine. Takes ScenarioResult objects + deal data + tax config
and produces per-scenario, per-year tax positions.

Based on Investment Thesis Section 6 (Tax Considerations) + OBBBA 2025.

Key concepts:
  - Real estate depreciation (bonus + straight-line) generates passive losses
  - HF trading gains flow through as short-term capital gains (portfolio income)
  - For "ideal" LP (real estate professional), passive losses offset portfolio income
  - For "typical" LP, passive losses only offset passive income (not yet implemented)
  - Tax benefits do NOT create cash — they reduce taxable income
  - The 2x LP hurdle is cash-based and is NOT affected by tax benefits
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

@dataclass
class TaxConfig:
    marginal_federal_rate: float = 0.37
    lp_type: str = "ideal"
    land_ratio: float = 0.20
    residential_years: float = 27.5
    commercial_years: float = 39.0
    cost_segregation_pct: float = 0.25
    bonus_depreciation_rate: float = 1.00
    depreciation_method: str = "straight_line"
    interest_deductible: bool = True
    output_csv: bool = True
    output_excel_sheet: bool = True

    @classmethod
    def from_yaml(cls, path: Path) -> TaxConfig:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        dep = data.get("depreciation", {})
        interest = data.get("interest", {})
        output = data.get("output", {})
        return cls(
            marginal_federal_rate=data.get("marginal_federal_rate", 0.37),
            lp_type=data.get("lp_type", "ideal"),
            land_ratio=dep.get("land_ratio", 0.20),
            residential_years=dep.get("residential_years", 27.5),
            commercial_years=dep.get("commercial_years", 39.0),
            cost_segregation_pct=dep.get("cost_segregation_pct", 0.25),
            bonus_depreciation_rate=dep.get("bonus_depreciation_rate", 1.00),
            depreciation_method=dep.get("method", "straight_line"),
            interest_deductible=interest.get("deductible", True),
            output_csv=output.get("write_csv", True),
            output_excel_sheet=output.get("write_excel_sheet", True),
        )


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------

@dataclass
class DealTaxProfile:
    """Pre-computed depreciation schedule for a single deal."""
    deal_name: str
    purchase_price: float
    building_basis: float          # purchase_price * (1 - land_ratio)
    cost_seg_basis: float          # building_basis * cost_segregation_pct
    remaining_building_basis: float  # building_basis - cost_seg_basis
    bonus_depreciation_y1: float   # cost_seg_basis * bonus_depreciation_rate
    annual_sl_depreciation: float  # remaining_building_basis / recovery_years
    recovery_years: float          # 27.5 for residential, 39 for commercial
    debt_balance: float            # for interest deduction
    interest_rate: float           # for interest deduction


@dataclass
class YearlyTaxResult:
    scenario: str
    year: int

    # Depreciation
    bonus_depreciation: float = 0.0
    straight_line_depreciation: float = 0.0
    total_depreciation: float = 0.0
    cumulative_depreciation: float = 0.0

    # Interest deduction
    interest_deduction: float = 0.0
    cumulative_interest_deduction: float = 0.0

    # Total deductions
    total_deductions: float = 0.0
    cumulative_deductions: float = 0.0

    # Income
    hf_stcg: float = 0.0                    # HF short-term capital gains (portfolio income)
    re_taxable_income: float = 0.0          # RE taxable income (NOI - interest - depreciation)
    total_taxable_income_no_benefit: float = 0.0  # Without depreciation shield
    total_taxable_income_with_benefit: float = 0.0  # With depreciation shield

    # Tax
    tax_no_benefit: float = 0.0             # Tax without depreciation shield
    tax_with_benefit: float = 0.0           # Tax with depreciation shield
    tax_savings: float = 0.0                # Difference = value of shield
    cumulative_tax_savings: float = 0.0

    # After-tax cash
    lp_cash_distributions: float = 0.0      # From engine (pre-tax cash)
    after_tax_cash_ideal: float = 0.0       # LP cash + tax savings (ideal LP)
    cumulative_after_tax_cash_ideal: float = 0.0
    after_tax_moic_ideal: float = 0.0       # Cumulative after-tax cash / initial capital
    after_tax_irr_ideal: float | None = None  # Computed at end

    # Passive loss tracking
    passive_loss_generated: float = 0.0     # Depreciation + interest - NOI (if negative)
    passive_loss_used: float = 0.0          # Actually used to offset income
    passive_loss_carryforward: float = 0.0  # Suspended losses


@dataclass
class ScenarioTaxResult:
    scenario: str
    description: str
    lp_type: str
    yearly: list[YearlyTaxResult] = field(default_factory=list)

    # Summary
    total_depreciation: float = 0.0
    total_interest_deductions: float = 0.0
    total_tax_savings: float = 0.0
    final_after_tax_moic: float = 0.0
    final_after_tax_irr: float | None = None
    final_cumulative_tax_savings: float = 0.0


# ---------------------------------------------------------------------------
# Depreciation engine
# ---------------------------------------------------------------------------

def build_deal_tax_profile(
    deal_name: str,
    purchase_price: float,
    debt_balance: float,
    interest_rate: float,
    tax_config: TaxConfig,
    is_residential: bool = True,
) -> DealTaxProfile:
    """Build a depreciation schedule for a single deal."""
    building_basis = purchase_price * (1 - tax_config.land_ratio)
    cost_seg_basis = building_basis * tax_config.cost_segregation_pct
    remaining_building_basis = building_basis - cost_seg_basis
    bonus_depreciation_y1 = cost_seg_basis * tax_config.bonus_depreciation_rate
    recovery_years = tax_config.residential_years if is_residential else tax_config.commercial_years
    annual_sl = remaining_building_basis / recovery_years if recovery_years > 0 else 0.0

    return DealTaxProfile(
        deal_name=deal_name,
        purchase_price=purchase_price,
        building_basis=building_basis,
        cost_seg_basis=cost_seg_basis,
        remaining_building_basis=remaining_building_basis,
        bonus_depreciation_y1=bonus_depreciation_y1,
        annual_sl_depreciation=annual_sl,
        recovery_years=recovery_years,
        debt_balance=debt_balance,
        interest_rate=interest_rate,
    )


def compute_annual_depreciation(
    profile: DealTaxProfile,
    year: int,
    tax_config: TaxConfig,
) -> tuple[float, float]:
    """Return (bonus_depreciation, straight_line_depreciation) for a given year."""
    if year == 1:
        bonus = profile.bonus_depreciation_y1
    else:
        bonus = 0.0

    sl = profile.annual_sl_depreciation
    # Straight-line continues for the full recovery period from acquisition
    if year > profile.recovery_years:
        sl = 0.0

    return bonus, sl


# ---------------------------------------------------------------------------
# Main tax computation
# ---------------------------------------------------------------------------

def compute_scenario_tax(
    scenario_name: str,
    description: str,
    yearly_results: list[dict[str, Any]],
    deal_profiles: list[DealTaxProfile],
    tax_config: TaxConfig,
    initial_lp_capital: float,
) -> ScenarioTaxResult:
    """Compute full tax position for a single scenario."""
    result = ScenarioTaxResult(
        scenario=scenario_name,
        description=description,
        lp_type=tax_config.lp_type,
    )

    cumulative_dep = 0.0
    cumulative_interest = 0.0
    cumulative_deductions = 0.0
    cumulative_tax_savings = 0.0
    cumulative_after_tax_cash = 0.0
    passive_loss_carryforward = 0.0

    # For IRR calculation
    after_tax_cash_flows: list[float] = [-initial_lp_capital]

    for yr in yearly_results:
        year = yr["year"]
        yt = YearlyTaxResult(scenario=scenario_name, year=year)

        # --- Depreciation from all deals ---
        total_bonus = 0.0
        total_sl = 0.0
        for profile in deal_profiles:
            bonus, sl = compute_annual_depreciation(profile, year, tax_config)
            total_bonus += bonus
            total_sl += sl

        yt.bonus_depreciation = total_bonus
        yt.straight_line_depreciation = total_sl
        yt.total_depreciation = total_bonus + total_sl
        cumulative_dep += yt.total_depreciation
        yt.cumulative_depreciation = cumulative_dep

        # --- Interest deduction ---
        if tax_config.interest_deductible:
            total_interest = sum(
                p.debt_balance * p.interest_rate for p in deal_profiles
            )
            yt.interest_deduction = total_interest
            cumulative_interest += total_interest
            yt.cumulative_interest_deduction = cumulative_interest

        # --- Total deductions ---
        yt.total_deductions = yt.total_depreciation + yt.interest_deduction
        cumulative_deductions += yt.total_deductions
        yt.cumulative_deductions = cumulative_deductions

        # --- Income ---
        # HF short-term capital gains = HF harvest to LP + HF harvest reinvested
        # (all HF gains are taxable as STCG regardless of reinvestment)
        hf_opening_nav = yr.get("hf_opening_nav", 0.0)
        hf_closing_nav = yr.get("hf_closing_nav", 0.0)
        hf_return_rate = yr.get("hf_return", 0.0)
        # HF gain = opening_nav * return_rate (simplified; actual is closing - opening - contributions)
        hf_gain = yr.get("hf_harvest_generated", 0.0)
        # hf_reinvest_from_hf is already included in hf_gain (hf_harvest_generated),
        # so we only add the RE-sourced HF reinvestment here to avoid double-counting.
        hf_reinvest_from_re = yr.get("hf_reinvestment_source_re", 0.0)
        yt.hf_stcg = hf_gain + hf_reinvest_from_re

        # RE taxable income = NOI - interest - depreciation
        noi = yr.get("re_noi", 0.0)
        interest_exp = yt.interest_deduction
        yt.re_taxable_income = noi - interest_exp - yt.total_depreciation

        # Total taxable income without depreciation shield
        yt.total_taxable_income_no_benefit = yt.hf_stcg + noi - interest_exp

        # Total taxable income with depreciation shield
        yt.total_taxable_income_with_benefit = yt.hf_stcg + yt.re_taxable_income

        # --- Tax calculation ---
        yt.tax_no_benefit = max(yt.total_taxable_income_no_benefit, 0.0) * tax_config.marginal_federal_rate
        yt.tax_with_benefit = max(yt.total_taxable_income_with_benefit, 0.0) * tax_config.marginal_federal_rate
        yt.tax_savings = yt.tax_no_benefit - yt.tax_with_benefit
        cumulative_tax_savings += yt.tax_savings
        yt.cumulative_tax_savings = cumulative_tax_savings

        # --- Passive loss tracking ---
        passive_income = max(yt.re_taxable_income, 0.0)
        passive_loss = max(-yt.re_taxable_income, 0.0)
        yt.passive_loss_generated = passive_loss

        if tax_config.lp_type == "ideal":
            # Real estate professional: passive losses offset all income
            yt.passive_loss_used = min(passive_loss + passive_loss_carryforward, yt.hf_stcg)
            passive_loss_carryforward = max(passive_loss + passive_loss_carryforward - yt.passive_loss_used, 0.0)
        else:
            # Passive investor: passive losses only offset passive income
            yt.passive_loss_used = min(passive_loss + passive_loss_carryforward, passive_income)
            passive_loss_carryforward = max(passive_loss + passive_loss_carryforward - yt.passive_loss_used, 0.0)

        yt.passive_loss_carryforward = passive_loss_carryforward

        # --- After-tax cash ---
        yt.lp_cash_distributions = yr.get("lp_cash_distributions", yr.get("lp_distribution", 0.0))
        yt.after_tax_cash_ideal = yt.lp_cash_distributions + yt.tax_savings
        cumulative_after_tax_cash += yt.after_tax_cash_ideal
        yt.cumulative_after_tax_cash_ideal = cumulative_after_tax_cash
        yt.after_tax_moic_ideal = cumulative_after_tax_cash / initial_lp_capital if initial_lp_capital > 0 else 0.0

        after_tax_cash_flows.append(yt.after_tax_cash_ideal)

        result.yearly.append(yt)

    # --- Summary ---
    result.total_depreciation = cumulative_dep
    result.total_interest_deductions = cumulative_interest
    result.total_tax_savings = cumulative_tax_savings
    result.final_cumulative_tax_savings = cumulative_tax_savings

    if result.yearly:
        result.final_after_tax_moic = result.yearly[-1].after_tax_moic_ideal

    # Compute after-tax IRR
    try:
        result.final_after_tax_irr = _compute_irr(after_tax_cash_flows)
    except Exception:
        result.final_after_tax_irr = None

    return result


def _compute_irr(cash_flows: list[float], max_iter: int = 200, tol: float = 1e-8) -> float | None:
    """Compute IRR using Newton-Raphson method."""
    if not cash_flows or len(cash_flows) < 2:
        return None

    # Check if all flows after initial are positive (no IRR)
    if all(cf >= 0 for cf in cash_flows):
        return None

    rate = 0.10  # initial guess
    for _ in range(max_iter):
        npv = 0.0
        d_npv = 0.0
        for t, cf in enumerate(cash_flows):
            denom = (1 + rate) ** t
            npv += cf / denom
            d_npv -= t * cf / (denom * (1 + rate))

        if abs(d_npv) < 1e-15:
            break

        new_rate = rate - npv / d_npv
        if abs(new_rate - rate) < tol:
            return new_rate
        rate = new_rate

        if rate < -0.99:
            rate = -0.99
        if rate > 10.0:
            rate = 10.0

    # Final check
    npv = sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows))
    if abs(npv) < 0.01:
        return rate
    return None


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def run_tax_analysis(
    results: list[Any],
    deals: dict[str, Any] | None,
    tax_config: TaxConfig,
    initial_lp_capital: float,
) -> list[ScenarioTaxResult]:
    """Run tax analysis on all scenario results."""
    scenario_tax_results = []

    for scenario_result in results:
        scenario_name = scenario_result.scenario
        description = scenario_result.description
        yearly_results = [asdict_item(cf) for cf in scenario_result.cashflows]

        # Build deal profiles from deal_cashflows
        deal_profiles: list[DealTaxProfile] = []
        if deals and hasattr(scenario_result, "deal_cashflows") and scenario_result.deal_cashflows:
            deal_names = set()
            for dcf in scenario_result.deal_cashflows:
                d = asdict_item(dcf)
                dn = d.get("deal_name", "")
                if dn and dn not in deal_names:
                    deal_names.add(dn)
                    # Get purchase price from deals config
                    deal_cfg = deals.get("deals", {}).get(dn, {})
                    purchase_price = deal_cfg.get("acquisition", {}).get("purchase_price", 0.0)
                    debt = deal_cfg.get("capital_stack", {}).get("assumed_debt", 0.0)
                    interest = deal_cfg.get("debt", {}).get("interest_rate", 0.0) or 0.0
                    is_res = True  # multifamily = residential

                    if purchase_price > 0:
                        profile = build_deal_tax_profile(
                            dn, purchase_price, debt, interest, tax_config, is_res
                        )
                        deal_profiles.append(profile)

        # If no deal profiles from deal_cashflows, try to infer from summary
        if not deal_profiles and deals:
            for dn, deal_cfg in deals.get("deals", {}).items():
                purchase_price = deal_cfg.get("acquisition", {}).get("purchase_price", 0.0)
                debt = deal_cfg.get("capital_stack", {}).get("assumed_debt", 0.0)
                interest = deal_cfg.get("debt", {}).get("interest_rate", 0.0) or 0.0
                if purchase_price > 0:
                    profile = build_deal_tax_profile(
                        dn, purchase_price, debt, interest, tax_config, True
                    )
                    deal_profiles.append(profile)

        tax_result = compute_scenario_tax(
            scenario_name, description, yearly_results,
            deal_profiles, tax_config, initial_lp_capital,
        )
        scenario_tax_results.append(tax_result)

    return scenario_tax_results


def asdict_item(obj: Any) -> dict[str, Any]:
    """Convert a dataclass or dict to dict."""
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, "__dataclass_fields__"):
        from dataclasses import asdict
        return asdict(obj)
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    return {}


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

TAX_YEARLY_COLUMNS = [
    "scenario", "year",
    "bonus_depreciation", "straight_line_depreciation", "total_depreciation",
    "cumulative_depreciation",
    "interest_deduction", "cumulative_interest_deduction",
    "total_deductions", "cumulative_deductions",
    "hf_stcg", "re_taxable_income",
    "total_taxable_income_no_benefit", "total_taxable_income_with_benefit",
    "tax_no_benefit", "tax_with_benefit", "tax_savings", "cumulative_tax_savings",
    "lp_cash_distributions", "after_tax_cash_ideal", "cumulative_after_tax_cash_ideal",
    "after_tax_moic_ideal",
    "passive_loss_generated", "passive_loss_used", "passive_loss_carryforward",
]

TAX_SUMMARY_COLUMNS = [
    "scenario", "description", "lp_type",
    "total_depreciation", "total_interest_deductions",
    "total_tax_savings", "final_cumulative_tax_savings",
    "final_after_tax_moic", "final_after_tax_irr",
]


def write_tax_outputs(
    tax_results: list[ScenarioTaxResult],
    output_dir: Path,
    tax_config: TaxConfig,
) -> dict[str, pd.DataFrame]:
    """Write tax CSVs and return DataFrames."""
    output_dir.mkdir(parents=True, exist_ok=True)

    yearly_rows = []
    summary_rows = []
    for tr in tax_results:
        for yr in tr.yearly:
            row = {col: getattr(yr, col, None) for col in TAX_YEARLY_COLUMNS}
            yearly_rows.append(row)

        summary_rows.append({
            "scenario": tr.scenario,
            "description": tr.description,
            "lp_type": tr.lp_type,
            "total_depreciation": tr.total_depreciation,
            "total_interest_deductions": tr.total_interest_deductions,
            "total_tax_savings": tr.total_tax_savings,
            "final_cumulative_tax_savings": tr.final_cumulative_tax_savings,
            "final_after_tax_moic": tr.final_after_tax_moic,
            "final_after_tax_irr": tr.final_after_tax_irr,
        })

    yearly_df = pd.DataFrame(yearly_rows).reindex(columns=TAX_YEARLY_COLUMNS)
    summary_df = pd.DataFrame(summary_rows).reindex(columns=TAX_SUMMARY_COLUMNS)

    if tax_config.output_csv:
        yearly_df.to_csv(output_dir / "tax_yearly.csv", index=False)
        summary_df.to_csv(output_dir / "tax_summary.csv", index=False)

    return {"tax_yearly": yearly_df, "tax_summary": summary_df}
