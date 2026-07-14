from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.model_types import ScenarioResult


SUMMARY_TABLE_COLUMNS = [
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

REPORT_COLUMN_LABELS = {
    "scenario": "Scenario",
    "description": "Description",
    "real_estate_mode": "RE model mode",
    "liquidity_constrained": "Liquidity constrained?",
    "final_fund_nav": "Final fund NAV",
    "final_refinance_liability": "Final refi liability",
    "final_re_gross_asset_value": "Final RE gross asset value",
    "final_re_debt_balance": "Final RE debt balance",
    "final_re_assumed_liabilities": "Final RE assumed liabilities",
    "final_re_net_equity_value": "Final RE net equity value",
    "final_re_dscr": "Final RE DSCR",
    "total_deal_refi_proceeds": "Total deal refi proceeds",
    "total_re_cashflow_shortfall": "Total RE cashflow shortfall",
    "total_acquisition_failed_loss": "Total failed acquisition loss",
    "total_acquisition_unfunded_shortfall": "Total acquisition funding shortfall",
    "years_modelled": "Years modelled",
    "lp_cash_moic": "LP cash multiple",
    "lp_economic_moic": "LP economic multiple",
    "lp_cash_irr": "LP cash IRR",
    "lp_economic_irr": "LP economic IRR",
    "lp_hurdle_achieved": "LP 2x achieved?",
    "year_hurdle_achieved": "Year LP 2x achieved",
    "years_until_lp_2x_cash_return": "Years to LP 2x cash",
    "lp_cashflow_profile_type": "LP cashflow profile",
    "hurdle_trigger_executed": "Trigger executed?",
    "hurdle_trigger_year": "Trigger year",
    "total_trigger_cash_from_hf_liquidation": "HF liquidation used",
    "total_trigger_cash_from_refi": "Refi used",
    "total_distributed_to_lp": "Total paid to LP",
    "total_reinvested_into_hf": "Total reinvested into HF",
    "total_added_to_reserve": "Total added to reserve",
    "backend_liquidity_strategy_enabled": "Backend strategy enabled?",
    "backend_liquidity_target_years": "Backend target years",
    "backend_liquidity_refi_first": "Backend refi-first?",
    "gp_survivability_risk": "GP survivability risk?",
    "gp_residual_nav": "GP residual NAV",
    "gp_total_economics": "GP total economics",
    "primary_flag": "Primary diagnostic flag",
}

MONEY_COLUMNS = {
    "final_fund_nav",
    "final_refinance_liability",
    "gp_residual_nav",
    "gp_total_economics",
    "total_deal_refi_proceeds",
    "total_distributed_to_lp",
    "total_reinvested_into_hf",
    "total_trigger_cash_from_hf_liquidation",
    "total_trigger_cash_from_refi",
    "total_trigger_cash_from_reserve",
    "total_trigger_cash_from_retained_cash",
    "total_trigger_cash_from_re_sale",
}

PERCENT_COLUMNS = {
    "lp_cash_irr",
    "lp_economic_irr",
}

MULTIPLE_COLUMNS = {
    "lp_cash_moic",
    "lp_economic_moic",
}

YEAR_COLUMNS = {
    "years_modelled",
    "year_hurdle_achieved",
    "years_until_lp_2x_cash_return",
    "hurdle_trigger_year",
}

VALUE_LABELS = {
    "BACKEND_HEAVY": "Backend-heavy",
    "MODERATE_YIELD": "Moderate yield",
    "AGGRESSIVE_DISTRIBUTION": "Aggressive distribution",
    "FAST_GP_DYNASTY_OUTCOME": "Fast LP redemption with large GP residual",
    "LP_HURDLE_ACHIEVED": "LP 2x achieved",
    "LP_HURDLE_NOT_ACHIEVED": "LP 2x not achieved",
    "HURDLE_COMPLETION_TRIGGER_EXECUTED": "Hurdle trigger executed",
    "HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT": "Trigger attempted but insufficient",
    "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED": "Value hurdle reached but liquidity constrained",
    "SLOW_TIME_HORIZON_DRIFT": "Slow time horizon drift",
    "GP_SURVIVABILITY_RISK": "GP survivability risk",
    "FUND_NAV_IMPAIRED": "Fund NAV impaired",
    "HF_MAJOR_DRAWDOWN": "HF major drawdown",
    "RE_NAV_IMPAIRMENT": "RE NAV impairment",
    "LP_GOOD_IRR_GP_LARGE_RESIDUAL": "Good LP IRR with large GP residual",
    "LP_CASH_YIELD_SHORTFALL": "LP cash yield shortfall",
    "REFINANCE_EVENT_OCCURRED": "Refinance event occurred",
    "REFI_DEPENDENT_LP_OUTCOME": "Refi-dependent LP outcome",
    "LONG_ZERO_DISTRIBUTION_PERIOD": "Long zero-distribution period",
    "LP_STILL_BELOW_1X_CASH_MOIC_AT_END": "LP still below 1x cash at end",
    "LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV": "Weak LP cash outcome despite positive NAV",
    "LP_REDEEMED_VIA_HF_LIQUIDATION": "LP redeemed via HF liquidation",
    "LP_REDEEMED_VIA_REFI": "LP redeemed via refi",
    "LP_REDEEMED_VIA_PARTIAL_RE_SALE": "LP redeemed via partial RE sale",
}


def write_markdown_report(results: list[ScenarioResult], summary_df: pd.DataFrame, output_path: Path) -> None:
    lines: list[str] = [
        "# Scenario Report",
        "",
        "Deterministic annual model. LP hurdle achievement is based on actual cash distributions received, not NAV appreciation.",
        "",
        "Scenarios are run on a diagnostic horizon set in the YAML inputs, currently 20 years. "
        "The engine stops a scenario early once the LP cash hurdle is achieved, so `years_modelled` "
        "shows the actual time required to reach 2.0x or the full diagnostic horizon if the hurdle is not reached.",
        "",
        "## Summary",
        "",
        markdown_table(summary_df[SUMMARY_TABLE_COLUMNS], REPORT_COLUMN_LABELS),
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
                f"- LP cash multiple: {result.summary['lp_cash_moic']:.2f}x",
                f"- LP economic multiple: {result.summary['lp_economic_moic']:.2f}x",
                f"- LP cash IRR: {format_percent(result.summary['lp_cash_irr'])}",
                f"- LP economic IRR: {format_percent(result.summary['lp_economic_irr'])}",
                f"- Years until LP 2x cash return: {result.summary.get('years_until_lp_2x_cash_return') or 'not reached'}",
                f"- LP cashflow profile: {format_label(result.summary.get('lp_cashflow_profile_type', 'n/a'))}",
                f"- Hurdle completion trigger executed: {result.summary.get('hurdle_trigger_executed', False)}",
                f"- Hurdle trigger year: {result.summary.get('hurdle_trigger_year') or 'not triggered'}",
                f"- Trigger HF liquidation used: ${result.summary.get('total_trigger_cash_from_hf_liquidation', 0):,.0f}",
                f"- Trigger refi used: ${result.summary.get('total_trigger_cash_from_refi', 0):,.0f}",
                f"- Total cash distributed to LP: ${result.summary.get('total_distributed_to_lp', 0):,.0f}",
                f"- Total cash reinvested into HF: ${result.summary.get('total_reinvested_into_hf', 0):,.0f}",
                f"- GP residual NAV: ${result.summary['gp_residual_nav']:,.0f}",
                f"- GP survivability risk: {result.summary['gp_survivability_risk']}",
                f"- Key flags: {format_label(result.summary['all_flags'])}",
                "",
            ]
        )
        if result.summary.get("real_estate_mode") == "bottom_up":
            lines.extend(bottom_up_section(result))
    output_path.write_text("\n".join(lines), encoding="utf-8")


def format_percent(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.1%}"


def markdown_table(df: pd.DataFrame, column_labels: dict[str, str] | None = None) -> str:
    headers = list(df.columns)
    display_headers = [column_labels.get(header, header) if column_labels else header for header in headers]
    lines = [
        "| " + " | ".join(display_headers) + " |",
        "| " + " | ".join("---" for _ in display_headers) + " |",
    ]
    for _, row in df.iterrows():
        values = [format_markdown_value(row[column], column) for column in headers]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def bottom_up_section(result: ScenarioResult) -> list[str]:
    active_rows = [row for row in result.deal_cashflows if row.active]
    first_rows_by_deal = {}
    for row in active_rows:
        first_rows_by_deal.setdefault(row.deal_name, row)

    lines = ["#### Bottom-Up Deal Summary", ""]
    for deal_name, row in first_rows_by_deal.items():
        lines.extend(
            [
                f"- {deal_name}: gross assets ${row.asset_value:,.0f}; assumed debt ${row.debt_balance:,.0f}; "
                f"other liabilities ${row.assumed_liabilities:,.0f}; new equity required ${row.new_equity_required:,.0f}; "
                f"entry equity cushion ${row.entry_equity_cushion:,.0f}; current NOI ${row.noi:,.0f}; "
                f"refi LTV capacity ${row.refi_capacity:,.0f}",
            ]
        )
    if not first_rows_by_deal:
        lines.append("- No active deal rows were produced.")
    lines.append("")

    annual_rows = [
        {
            "Year": row.year,
            "Gross assets": row.re_gross_asset_value,
            "Debt": row.re_debt_balance,
            "Liabilities": row.re_assumed_liabilities,
            "NOI": row.re_noi,
            "DSCR": row.re_dscr,
            "Free cashflow": row.re_free_cashflow_after_debt_and_capex,
            "Refi proceeds": row.re_refi_proceeds_from_deals,
            "Deal NAV": row.re_closing_nav,
        }
        for row in result.cashflows
    ]
    lines.extend(["Annual bottom-up RE portfolio:", "", markdown_table(pd.DataFrame(annual_rows)), ""])
    return lines


def format_markdown_value(value: object, column: str | None = None) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if column in MONEY_COLUMNS:
        return f"${float(value):,.0f}"
    if column in PERCENT_COLUMNS:
        return format_percent(float(value))
    if column in MULTIPLE_COLUMNS:
        return f"{float(value):.2f}x"
    if column in YEAR_COLUMNS:
        return f"Y{int(float(value))}" if value != "" else ""
    if column in {"lp_cashflow_profile_type", "primary_flag", "all_flags"}:
        return format_label(value)
    if isinstance(value, float):
        return f"{value:,.2f}"
    return str(value)


def format_label(value: object) -> str:
    text = str(value or "")
    if not text:
        return ""
    parts = [part.strip() for part in text.replace(";", ",").split(",")]
    labels = [VALUE_LABELS.get(part, part.replace("_", " ").title()) for part in parts if part]
    return ", ".join(labels)
