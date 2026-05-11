from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.model_types import ScenarioResult


def write_markdown_report(results: list[ScenarioResult], summary_df: pd.DataFrame, output_path: Path) -> None:
    lines: list[str] = [
        "# Scenario Report",
        "",
        "Deterministic annual phase 2 model. Cash MOIC, economic MOIC, cash IRR, and economic IRR are reported separately.",
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
