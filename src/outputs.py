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
    "lp_initial_capital",
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
    "primary_flag",
    "all_flags",
]

CASHFLOW_COLUMNS = [
    "scenario",
    "year",
    "re_opening_nav",
    "re_noi_yield",
    "re_noi",
    "gross_rent",
    "re_asset_mgmt_fee",
    "net_re_cashflow",
    "re_appreciation_rate",
    "re_closing_nav",
    "hf_opening_nav",
    "hf_return",
    "hf_harvest",
    "hf_closing_nav",
    "refinance_proceeds",
    "refinance_use_of_proceeds",
    "cumulative_refinance_proceeds",
    "reserve_opening_nav",
    "reserve_closing_nav",
    "retained_cash",
    "lp_cash_yield_target",
    "lp_cash_yield_paid",
    "lp_cash_yield_shortfall",
    "cumulative_lp_cash_yield_shortfall",
    "lp_cash_yield_coverage_ratio",
    "lp_distribution",
    "lp_cumulative_distribution",
    "lp_remaining_hurdle",
    "economic_hurdle_passed",
    "liquidity_available",
    "liquidity_hurdle_passed",
    "gp_fees",
    "gp_cumulative_fees",
    "gp_residual_nav",
    "fund_nav",
    "event_flag",
]


def write_outputs(
    *,
    results: list[ScenarioResult],
    config: ModelConfig,
    scenarios: ScenarioSet,
    output_dir: Path,
) -> dict[str, pd.DataFrame]:
    output_dir.mkdir(parents=True, exist_ok=True)
    summaries, cashflows, flags = result_dicts(results)
    summary_df = pd.DataFrame(summaries).reindex(columns=SUMMARY_COLUMNS)
    cashflow_df = pd.DataFrame(cashflows).reindex(columns=CASHFLOW_COLUMNS)
    flags_df = pd.DataFrame(flags).reindex(columns=["scenario", "flag", "severity", "explanation"])

    if config.reporting.output_csv:
        summary_df.to_csv(output_dir / "scenario_summary.csv", index=False)
        cashflow_df.to_csv(output_dir / "scenario_cashflows.csv", index=False)
        flags_df.to_csv(output_dir / "scenario_flags.csv", index=False)

    if config.reporting.output_excel:
        write_excel(output_dir / "scenario_summary.xlsx", summary_df, cashflow_df, flags_df, config, scenarios)

    return {"summary": summary_df, "cashflows": cashflow_df, "flags": flags_df}


def write_excel(
    path: Path,
    summary_df: pd.DataFrame,
    cashflow_df: pd.DataFrame,
    flags_df: pd.DataFrame,
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
        if any(token in header for token in ["nav", "capital", "amount", "distribution", "cashflow", "fee", "rent", "noi", "economics", "liquidity", "hurdle"]):
            if "moic" not in header and "pct" not in header and "yield" not in header and "rate" not in header:
                number_format = '$#,##0'
        if "pct" in header or "yield" in header or "rate" in header or header in {"lp_irr", "lp_cash_irr", "lp_economic_irr", "gp_cash_irr_if_co_investment", "hf_return"}:
            number_format = "0.0%"
        if "moic" in header or "multiple" in header:
            number_format = "0.00x"

        if number_format:
            for cell in column_cells[1:]:
                cell.number_format = number_format
