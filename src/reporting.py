from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.model_types import ScenarioResult


def write_markdown_report(results: list[ScenarioResult], summary_df: pd.DataFrame, output_path: Path) -> None:
    lines: list[str] = [
        "# Scenario Report",
        "",
        "Deterministic annual model. LP hurdle achievement is based on actual cash distributions received, not NAV appreciation.",
        "",
        "## Summary",
        "",
        markdown_table(
            summary_df[
                [
                    "scenario",
                    "years_modelled",
                    "lp_cash_moic",
                    "lp_economic_moic",
                    "lp_cash_irr",
                    "lp_economic_irr",
                    "lp_hurdle_achieved",
                    "years_until_lp_2x_cash_return",
                    "lp_cashflow_profile_type",
                    "hurdle_trigger_executed",
                    "hurdle_trigger_year",
                    "total_trigger_cash_from_hf_liquidation",
                    "total_trigger_cash_from_refi",
                    "total_distributed_to_lp",
                    "total_reinvested_into_hf",
                    "gp_survivability_risk",
                    "gp_residual_nav",
                    "primary_flag",
                ]
            ]
        ),
        "",
        "## Scenario Notes",
        "",
    ]
    for result in results:
        lines.extend(
            [
                f"### {result.scenario}",
                "",
                result.description,
                "",
                f"- LP cash MOIC: {result.summary['lp_cash_moic']:.2f}x",
                f"- LP economic MOIC: {result.summary['lp_economic_moic']:.2f}x",
                f"- LP cash IRR: {format_percent(result.summary['lp_cash_irr'])}",
                f"- LP economic IRR: {format_percent(result.summary['lp_economic_irr'])}",
                f"- Years until LP 2x cash return: {result.summary.get('years_until_lp_2x_cash_return') or 'not reached'}",
                f"- LP cashflow profile type: {result.summary.get('lp_cashflow_profile_type', 'n/a')}",
                f"- Hurdle completion trigger executed: {result.summary.get('hurdle_trigger_executed', False)}",
                f"- Hurdle trigger year: {result.summary.get('hurdle_trigger_year') or 'not triggered'}",
                f"- Trigger HF liquidation used: ${result.summary.get('total_trigger_cash_from_hf_liquidation', 0):,.0f}",
                f"- Trigger refi used: ${result.summary.get('total_trigger_cash_from_refi', 0):,.0f}",
                f"- Total cash distributed to LP: ${result.summary.get('total_distributed_to_lp', 0):,.0f}",
                f"- Total cash reinvested into HF: ${result.summary.get('total_reinvested_into_hf', 0):,.0f}",
                f"- GP residual NAV: ${result.summary['gp_residual_nav']:,.0f}",
                f"- GP survivability risk: {result.summary['gp_survivability_risk']}",
                f"- Key flags: {result.summary['all_flags']}",
                "",
            ]
        )
    output_path.write_text("\n".join(lines), encoding="utf-8")


def format_percent(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.1%}"


def markdown_table(df: pd.DataFrame) -> str:
    headers = list(df.columns)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for _, row in df.iterrows():
        values = [format_markdown_value(row[column]) for column in headers]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def format_markdown_value(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, float):
        return f"{value:,.2f}"
    return str(value)
