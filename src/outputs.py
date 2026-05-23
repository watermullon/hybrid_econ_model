from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

from src.engine import result_dicts
from src.model_types import ModelConfig, ScenarioResult, ScenarioSet


SUMMARY_COLUMNS = [
    "scenario",
    "description",
    "real_estate_mode",
    "lp_initial_capital",
    "initial_re_cash_deployed",
    "initial_re_gross_asset_value",
    "initial_re_debt_balance",
    "initial_re_assumed_liabilities",
    "initial_re_net_equity_value",
    "initial_re_entry_equity_cushion",
    "initial_re_value_to_new_equity_multiple",
    "final_re_gross_asset_value",
    "final_re_debt_balance",
    "final_re_assumed_liabilities",
    "final_re_net_equity_value",
    "final_re_dscr",
    "total_re_debt_service",
    "total_re_capex",
    "total_deal_refi_proceeds",
    "total_re_cashflow_shortfall",
    "total_acquisition_equity_required",
    "total_acquisition_funded_from_retained_cash",
    "total_acquisition_funded_from_reserve",
    "total_acquisition_unfunded_shortfall",
    "years_modelled",
    "lp_hurdle_moic",
    "lp_hurdle_amount",
    "lp_cash_distributions",
    "lp_cash_moic",
    "lp_economic_moic",
    "lp_irr",
    "lp_cash_irr",
    "lp_economic_irr",
    "gp_cash_irr_if_co_investment",
    "gp_total_value_multiple_if_co_investment",
    "lp_hurdle_achieved",
    "year_hurdle_achieved",
    "liquidity_constrained",
    "final_fund_nav",
    "final_refinance_liability",
    "gp_cumulative_fees",
    "gp_residual_nav",
    "gp_total_economics",
    "gp_residual_nav_pct_initial_lp_capital",
    "gp_total_economics_pct_initial_lp_capital",
    "gp_cumulative_fees_first_n_years",
    "gp_average_annual_fees_first_n_years",
    "gp_survivability_risk",
    "years_with_zero_lp_distribution",
    "years_with_distribution_below_target_yield",
    "longest_zero_distribution_streak",
    "longest_below_target_yield_streak",
    "years_until_first_distribution",
    "lp_time_under_1x_cash_moic",
    "lp_time_under_1x_economic_moic",
    "lp_final_unrecovered_hurdle",
    "lp_redeemed_by_model_end",
    "total_re_cashflow_generated",
    "total_hf_harvest_generated",
    "total_reinvested_into_hf",
    "total_distributed_to_lp",
    "total_added_to_reserve",
    "pct_total_cash_distributed",
    "pct_total_cash_reinvested",
    "pct_total_cash_reserved",
    "years_until_lp_1x_cash_return",
    "years_until_lp_2x_cash_return",
    "lp_cashflow_profile_type",
    "hurdle_completion_trigger_enabled",
    "backend_liquidity_strategy_enabled",
    "backend_liquidity_target_years",
    "backend_liquidity_refi_first",
    "backend_liquidity_max_refi_pct_of_re_nav",
    "backend_liquidity_max_hf_liquidation_pct",
    "hurdle_trigger_executed",
    "hurdle_trigger_year",
    "total_trigger_cash_from_retained_cash",
    "total_trigger_cash_from_reserve",
    "total_trigger_cash_from_hf_liquidation",
    "total_trigger_cash_from_refi",
    "total_trigger_cash_from_re_sale",
    "lp_hurdle_shortfall_after_final_trigger",
    "primary_flag",
    "all_flags",
]

CASHFLOW_COLUMNS = [
    "scenario",
    "year",
    "real_estate_mode",
    "re_opening_nav",
    "re_gross_asset_value",
    "re_debt_balance",
    "re_assumed_liabilities",
    "re_net_equity_value",
    "re_noi_yield",
    "re_noi",
    "gross_rent",
    "re_debt_service",
    "re_capex",
    "re_dscr",
    "re_prior_refi_liability",
    "re_ending_refi_liability",
    "re_max_debt_supported",
    "re_cash_out_before_refi_costs",
    "re_refi_costs",
    "re_refi_capacity",
    "re_refi_proceeds_from_deals",
    "re_free_cashflow_after_debt_and_capex",
    "re_cashflow_shortfall",
    "active_deal_count",
    "acquisition_starting_retained_cash",
    "acquisition_starting_reserve",
    "acquisition_new_deal_equity_required",
    "acquisition_funded_from_initial_lp_capital",
    "acquisition_funded_from_retained_cash",
    "acquisition_funded_from_reserve",
    "acquisition_unfunded_shortfall",
    "acquisition_ending_retained_cash",
    "acquisition_ending_reserve",
    "acquisition_funding_source",
    "re_asset_mgmt_fee",
    "net_re_cashflow",
    "re_cashflow_generated",
    "re_cashflow_to_lp",
    "re_cashflow_to_hf",
    "re_cashflow_to_reserve",
    "re_appreciation_rate",
    "re_closing_nav",
    "hf_opening_nav",
    "hf_return",
    "hf_harvest",
    "hf_harvest_generated",
    "hf_harvest_to_lp",
    "hf_harvest_to_hf",
    "hf_harvest_to_reserve",
    "hf_closing_nav",
    "refinance_proceeds",
    "refinance_use_of_proceeds",
    "cumulative_refinance_proceeds",
    "refinance_liability",
    "reserve_opening_nav",
    "reserve_closing_nav",
    "retained_cash",
    "lp_cash_yield_target",
    "lp_cash_yield_paid",
    "lp_cash_yield_shortfall",
    "cumulative_lp_cash_yield_shortfall",
    "lp_cash_yield_coverage_ratio",
    "cumulative_reinvested_into_hf",
    "cumulative_cash_distributed_to_lp",
    "cumulative_cash_added_to_reserve",
    "hf_reinvestment_source_re",
    "hf_reinvestment_source_hf",
    "total_cash_reinvested",
    "total_cash_distributed",
    "total_cash_reserved",
    "lp_distribution",
    "lp_cumulative_distribution",
    "lp_remaining_hurdle",
    "economic_hurdle_passed",
    "liquidity_available",
    "liquidity_hurdle_passed",
    "hurdle_trigger_eligible",
    "hurdle_trigger_attempted",
    "hurdle_trigger_executed",
    "hurdle_trigger_required_cash",
    "trigger_cash_from_retained_cash",
    "trigger_cash_from_reserve",
    "trigger_cash_from_hf_liquidation",
    "trigger_cash_from_refi",
    "trigger_cash_from_re_sale",
    "lp_hurdle_shortfall_after_trigger",
    "hf_nav_liquidated_for_hurdle",
    "refi_proceeds_for_hurdle",
    "re_nav_sold_for_hurdle",
    "gp_fees",
    "gp_cumulative_fees",
    "gp_residual_nav",
    "fund_nav",
    "event_flag",
]

DEAL_CASHFLOW_COLUMNS = [
    "scenario",
    "deal_name",
    "year",
    "relative_year",
    "active",
    "asset_value",
    "debt_balance",
    "assumed_liabilities",
    "net_equity_value",
    "noi",
    "gross_rent",
    "debt_service",
    "capex",
    "free_cashflow_after_debt_and_capex",
    "dscr",
    "prior_refi_liability",
    "ending_refi_liability",
    "max_debt_supported",
    "cash_out_before_refi_costs",
    "refi_costs",
    "refi_capacity",
    "refi_proceeds",
    "refi_liability_added",
    "deal_nav_before_refi_liability",
    "deal_nav_after_refi_liability",
    "deal_nav",
    "entry_equity_cushion",
    "value_to_new_equity_multiple",
    "new_equity_required",
    "refinance_proceeds_use",
]


def write_outputs(
    *,
    results: list[ScenarioResult],
    config: ModelConfig,
    scenarios: ScenarioSet,
    output_dir: Path,
) -> dict[str, pd.DataFrame]:
    output_dir.mkdir(parents=True, exist_ok=True)
    summaries, cashflows, flags, deal_cashflows = result_dicts(results)
    summary_df = pd.DataFrame(summaries).reindex(columns=SUMMARY_COLUMNS)
    cashflow_df = pd.DataFrame(cashflows).reindex(columns=CASHFLOW_COLUMNS)
    flags_df = pd.DataFrame(flags).reindex(columns=["scenario", "flag", "severity", "explanation"])
    deal_cashflow_df = pd.DataFrame(deal_cashflows).reindex(columns=DEAL_CASHFLOW_COLUMNS)

    if config.reporting.output_csv:
        summary_df.to_csv(output_dir / "scenario_summary.csv", index=False)
        cashflow_df.to_csv(output_dir / "scenario_cashflows.csv", index=False)
        flags_df.to_csv(output_dir / "scenario_flags.csv", index=False)
        deal_cashflow_df.to_csv(output_dir / "deal_cashflows.csv", index=False)

    if config.reporting.output_excel:
        write_excel(
            output_dir / "scenario_summary.xlsx",
            summary_df,
            cashflow_df,
            flags_df,
            deal_cashflow_df,
            config,
            scenarios,
        )

    return {"summary": summary_df, "cashflows": cashflow_df, "flags": flags_df, "deal_cashflows": deal_cashflow_df}


def write_excel(
    path: Path,
    summary_df: pd.DataFrame,
    cashflow_df: pd.DataFrame,
    flags_df: pd.DataFrame,
    deal_cashflow_df: pd.DataFrame,
    config: ModelConfig,
    scenarios: ScenarioSet,
) -> None:
    assumptions_df = flatten_dict(config.model_dump())
    notes_df = pd.DataFrame(
        [{"scenario": name, "description": scenario.description, "years": scenario.years} for name, scenario in scenarios.scenarios.items()]
    )
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        summary_df.to_excel(writer, sheet_name="Summary", index=False)
        cashflow_df.to_excel(writer, sheet_name="Cashflows", index=False)
        deal_cashflow_df.to_excel(writer, sheet_name="Deal Cashflows", index=False)
        flags_df.to_excel(writer, sheet_name="Flags", index=False)
        assumptions_df.to_excel(writer, sheet_name="Assumptions", index=False)
        notes_df.to_excel(writer, sheet_name="Scenario Notes", index=False)
        for worksheet in writer.book.worksheets:
            format_worksheet(worksheet)


def flatten_dict(data: dict[str, Any], prefix: str = "") -> pd.DataFrame:
    rows: list[dict[str, Any]] = []

    def walk(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                walk(child, f"{path}.{key}" if path else str(key))
        else:
            rows.append({"assumption": path, "value": value})

    walk(data, prefix)
    return pd.DataFrame(rows)


def format_worksheet(worksheet: Any) -> None:
    worksheet.freeze_panes = "A2"
    for cell in worksheet[1]:
        cell.font = Font(bold=True)

    for column_cells in worksheet.columns:
        header = str(column_cells[0].value or "")
        width = min(max(len(header), *(len(str(cell.value)) for cell in column_cells if cell.value is not None)) + 2, 60)
        worksheet.column_dimensions[get_column_letter(column_cells[0].column)].width = width

        number_format = None
        if any(token in header for token in ["nav", "capital", "amount", "distribution", "cashflow", "fee", "rent", "noi", "economics", "liquidity", "hurdle", "liability"]):
            if "moic" not in header and "pct" not in header and "yield" not in header and "rate" not in header:
                number_format = '$#,##0'
        if "pct" in header or "yield" in header or "rate" in header or header in {"lp_irr", "lp_cash_irr", "lp_economic_irr", "gp_cash_irr_if_co_investment", "hf_return"}:
            number_format = "0.0%"
        if "moic" in header or "multiple" in header:
            number_format = "0.00x"

        if number_format:
            for cell in column_cells[1:]:
                cell.number_format = number_format
