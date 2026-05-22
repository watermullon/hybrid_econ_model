from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd
import yaml


DEFAULT_OUTPUT_NAME = "chatgpt_model_context.md"

GLOBAL_ASSUMPTION_KEYS = [
    ("model.currency", "Currency"),
    ("model.max_years", "Maximum model years"),
    ("model.initial_lp_capital", "Initial LP capital"),
    ("model.gp_co_investment", "GP co-investment"),
    ("allocation.method", "Allocation method"),
    ("allocation.hedge_fund_allocation_pct", "Initial HF allocation"),
    ("allocation.real_estate_allocation_pct", "Initial real estate allocation"),
    ("allocation.reserve_allocation_pct", "Initial reserve allocation"),
    ("waterfall.lp_hurdle_moic", "LP cash hurdle MOIC"),
    ("waterfall.include_unrealized_nav_in_hurdle_test", "Economic NAV hurdle test enabled"),
    ("waterfall.require_liquidity_for_lp_redemption", "Liquidity required for LP redemption"),
    ("liquidity.hf_liquidation_capacity_pct_per_year", "HF annual liquidity capacity"),
    ("liquidity.reserve_liquidation_capacity_pct_per_year", "Reserve annual liquidity capacity"),
    ("liquidity.max_refinance_or_sale_capacity_pct_of_re_nav", "RE refinance/sale liquidity capacity"),
    ("fees.real_estate_asset_management_fee.rate", "RE asset management fee rate"),
    ("fees.real_estate_asset_management_fee.basis", "RE asset management fee basis"),
    ("distribution_policy.hf_positive_return_harvest_rate", "HF positive return harvest rate"),
    ("cashflow_routing.re_cashflow.lp_distribution_pct", "RE cashflow routed to LP"),
    ("cashflow_routing.re_cashflow.hf_reinvestment_pct", "RE cashflow reinvested into HF"),
    ("cashflow_routing.re_cashflow.reserve_pct", "RE cashflow routed to reserve"),
    ("cashflow_routing.hf_harvest.lp_distribution_pct", "HF harvest routed to LP"),
    ("cashflow_routing.hf_harvest.hf_reinvestment_pct", "HF harvest reinvested into HF"),
    ("cashflow_routing.hf_harvest.reserve_pct", "HF harvest routed to reserve"),
    ("lp_cash_yield_policy.enabled", "LP cash yield policy enabled"),
    ("gp_survivability.minimum_cumulative_fees", "GP survivability minimum cumulative fees"),
    ("hurdle_completion_trigger.enabled", "Active hurdle completion trigger enabled"),
    ("hurdle_completion_trigger.minimum_lp_cash_moic_before_trigger", "Minimum LP cash MOIC before trigger"),
    ("hurdle_completion_trigger.max_hf_liquidation_pct", "Max HF liquidation for trigger"),
    ("hurdle_completion_trigger.max_refi_pct_of_re_nav", "Max RE refi for trigger"),
    ("backend_liquidity_strategy.enabled", "Backend liquidity strategy enabled"),
    ("backend_liquidity_strategy.target_years", "Backend liquidity target years"),
    ("backend_liquidity_strategy.refi_first", "Backend liquidity is refi-led"),
    ("backend_liquidity_strategy.max_refi_pct_of_re_nav", "Backend max RE refi"),
    ("backend_liquidity_strategy.max_hf_liquidation_pct", "Backend max HF liquidation"),
]

SUMMARY_COLUMNS = [
    "scenario",
    "description",
    "years_modelled",
    "lp_cash_moic",
    "lp_economic_moic",
    "lp_cash_irr",
    "lp_economic_irr",
    "lp_hurdle_achieved",
    "year_hurdle_achieved",
    "liquidity_constrained",
    "final_fund_nav",
    "final_refinance_liability",
    "total_distributed_to_lp",
    "total_reinvested_into_hf",
    "total_added_to_reserve",
    "years_until_lp_2x_cash_return",
    "backend_liquidity_strategy_enabled",
    "backend_liquidity_target_years",
    "backend_liquidity_refi_first",
    "hurdle_trigger_executed",
    "hurdle_trigger_year",
    "total_trigger_cash_from_hf_liquidation",
    "total_trigger_cash_from_refi",
    "gp_residual_nav",
    "gp_total_economics",
    "primary_flag",
]

CASHFLOW_COLUMNS = [
    "scenario",
    "year",
    "lp_distribution",
    "lp_cumulative_distribution",
    "lp_remaining_hurdle",
    "re_cashflow_to_lp",
    "re_cashflow_to_hf",
    "re_cashflow_to_reserve",
    "hf_harvest_to_lp",
    "hf_harvest_to_hf",
    "hf_harvest_to_reserve",
    "refinance_proceeds",
    "refinance_liability",
    "re_closing_nav",
    "hf_closing_nav",
    "reserve_closing_nav",
    "retained_cash",
    "fund_nav",
    "liquidity_available",
    "hurdle_trigger_executed",
    "trigger_cash_from_retained_cash",
    "trigger_cash_from_reserve",
    "trigger_cash_from_hf_liquidation",
    "trigger_cash_from_refi",
    "lp_hurdle_shortfall_after_trigger",
    "event_flag",
]

FLAG_COLUMNS = ["scenario", "flag", "severity", "explanation"]


def build_chatgpt_context(root: Path, output_path: Path | None = None) -> Path:
    """Build a compact, upload-friendly Markdown context file from existing inputs and outputs.

    The exporter intentionally reads generated outputs rather than rerunning the model. That
    keeps it useful as both a run_model.py final step and a standalone audit/export command.
    """

    root = root.resolve()
    output_path = output_path or root / "outputs" / DEFAULT_OUTPUT_NAME
    output_path.parent.mkdir(parents=True, exist_ok=True)

    config = _read_yaml(root / "inputs" / "model_config.yaml")
    scenarios = _read_yaml(root / "inputs" / "scenarios.yaml")
    summary = _read_csv(root / "outputs" / "scenario_summary.csv")
    cashflows = _read_csv(root / "outputs" / "scenario_cashflows.csv")
    flags = _read_csv(root / "outputs" / "scenario_flags.csv")

    lines: list[str] = []
    lines.append("# Hybrid Fund Model Context for ChatGPT Analysis")
    lines.append("")
    lines.append(f"Generated: {datetime.now().isoformat(timespec='seconds')}")
    lines.append("")
    lines.append("## How to read this file")
    lines.append("")
    lines.append(
        "This is a compact analysis package generated from the model's YAML inputs and "
        "existing output CSVs. It is intended for ChatGPT review, not as a replacement "
        "for the full workbook or source code."
    )
    lines.append("")
    lines.append("Key interpretation rules:")
    lines.append("- The LP 2.0x hurdle means actual cash distributions received by LPs.")
    lines.append("- NAV growth and economic value are tracked separately from cash received.")
    lines.append("- GP residual asset value is recognized only after LP interests are extinguished through the cash hurdle.")
    lines.append("- Generated RE cashflow and harvested HF gains are routed to LP distributions, HF reinvestment, or reserve according to YAML assumptions.")
    lines.append("- The active hurdle completion trigger is separate from the passive liquidity test; it models the GP choosing to monetize permitted sources to finish the LP cash hurdle.")
    lines.append("")

    _append_global_assumptions(lines, config)
    _append_scenario_inputs(lines, scenarios)
    _append_summary_outputs(lines, summary)
    _append_cashflow_outputs(lines, cashflows, summary)
    _append_flags(lines, flags)
    _append_source_manifest(lines, root)

    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output_path


def _read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Required input file not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"Could not parse YAML file {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML mapping in {path}.")
    return data


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Required output file not found: {path}. Run python run_model.py before building the ChatGPT context file."
        )
    return pd.read_csv(path)


def _append_global_assumptions(lines: list[str], config: dict[str, Any]) -> None:
    rows = []
    for key, label in GLOBAL_ASSUMPTION_KEYS:
        rows.append({"Assumption": label, "YAML path": key, "Value": _format_value(_get_nested(config, key))})

    lines.append("## Selected global assumptions")
    lines.append("")
    lines.append(_markdown_table(rows, ["Assumption", "YAML path", "Value"]))
    lines.append("")


def _append_scenario_inputs(lines: list[str], scenarios_doc: dict[str, Any]) -> None:
    rows = []
    for name, scenario in (scenarios_doc.get("scenarios") or {}).items():
        real_estate = scenario.get("real_estate", {}) or {}
        hedge_fund = scenario.get("hedge_fund", {}) or {}
        rows.append(
            {
                "Scenario": name,
                "Description": scenario.get("description", ""),
                "Years": scenario.get("years", ""),
                "Initial NOI yield": _format_pct(real_estate.get("initial_noi_yield")),
                "NOI growth": _format_pct(real_estate.get("annual_noi_growth")),
                "RE NAV appreciation": _format_value(real_estate.get("annual_nav_appreciation")),
                "Gross rent yield": _format_pct(real_estate.get("gross_rent_yield")),
                "HF returns": _format_pct_list(hedge_fund.get("annual_returns", [])),
                "Overrides": _scenario_overrides(scenario),
            }
        )

    lines.append("## Scenario input assumptions")
    lines.append("")
    lines.append(_markdown_table(rows, list(rows[0].keys()) if rows else []))
    lines.append("")


def _append_summary_outputs(lines: list[str], summary: pd.DataFrame) -> None:
    compact = _select_columns(summary, SUMMARY_COLUMNS)
    compact = compact.copy()
    for column in compact.columns:
        compact[column] = compact[column].map(_format_cell)

    lines.append("## Most important terminal outputs")
    lines.append("")
    lines.append(_markdown_table(compact.to_dict("records"), list(compact.columns)))
    lines.append("")

    if {"lp_cash_moic", "lp_economic_moic", "scenario"}.issubset(summary.columns):
        gap_df = summary.copy()
        gap_df["economic_minus_cash_moic"] = gap_df["lp_economic_moic"] - gap_df["lp_cash_moic"]
        gap_df = gap_df.sort_values("economic_minus_cash_moic", ascending=False).head(5)
        rows = [
            {
                "Scenario": row["scenario"],
                "Cash MOIC": _format_multiple(row["lp_cash_moic"]),
                "Economic MOIC": _format_multiple(row["lp_economic_moic"]),
                "Economic minus cash": _format_multiple(row["economic_minus_cash_moic"]),
            }
            for _, row in gap_df.iterrows()
        ]
        lines.append("### Largest economic-value versus cash gaps")
        lines.append("")
        lines.append(_markdown_table(rows, ["Scenario", "Cash MOIC", "Economic MOIC", "Economic minus cash"]))
        lines.append("")


def _append_cashflow_outputs(lines: list[str], cashflows: pd.DataFrame, summary: pd.DataFrame) -> None:
    compact = _select_columns(cashflows, CASHFLOW_COLUMNS)
    compact = compact.copy()
    for column in compact.columns:
        compact[column] = compact[column].map(_format_cell)

    lines.append("## Compact annual cashflow and NAV trajectory")
    lines.append("")
    lines.append(
        "The table below keeps only the annual columns most useful for tracing LP cash, "
        "cash routing, sleeve NAVs, liquidity, and hurdle events."
    )
    lines.append("")
    lines.append(_markdown_table(compact.to_dict("records"), list(compact.columns)))
    lines.append("")

    rows = []
    for scenario, group in cashflows.groupby("scenario", sort=False):
        summary_row = summary[summary["scenario"] == scenario].iloc[0].to_dict() if "scenario" in summary.columns and not summary[summary["scenario"] == scenario].empty else {}
        rows.append(_scenario_observation(scenario, group, summary_row))

    lines.append("## Auto-generated scenario observations")
    lines.append("")
    for row in rows:
        lines.append(f"### {row['Scenario']}")
        lines.append("")
        lines.append(row["Observation"])
        lines.append("")


def _append_flags(lines: list[str], flags: pd.DataFrame) -> None:
    compact = _select_columns(flags, FLAG_COLUMNS).copy()
    for column in compact.columns:
        compact[column] = compact[column].map(_format_cell)

    lines.append("## Flags and diagnostics")
    lines.append("")
    if compact.empty:
        lines.append("No flags were emitted.")
    else:
        lines.append(_markdown_table(compact.to_dict("records"), list(compact.columns)))
    lines.append("")


def _append_source_manifest(lines: list[str], root: Path) -> None:
    files = [
        "inputs/model_config.yaml",
        "inputs/scenarios.yaml",
        "outputs/scenario_summary.csv",
        "outputs/scenario_cashflows.csv",
        "outputs/scenario_flags.csv",
    ]
    lines.append("## Source files used")
    lines.append("")
    for relative in files:
        path = root / relative
        status = "present" if path.exists() else "missing"
        lines.append(f"- `{relative}`: {status}")
    lines.append("")


def _scenario_observation(scenario: str, group: pd.DataFrame, summary_row: dict[str, Any]) -> dict[str, str]:
    years = int(group["year"].max()) if "year" in group.columns and not group.empty else len(group)
    lp_cash_moic = summary_row.get("lp_cash_moic")
    lp_economic_moic = summary_row.get("lp_economic_moic")
    hurdle = bool(summary_row.get("lp_hurdle_achieved", False))
    total_lp = group["lp_distribution"].sum() if "lp_distribution" in group.columns else summary_row.get("total_distributed_to_lp", 0)
    final_fund_nav = summary_row.get("final_fund_nav", group["fund_nav"].iloc[-1] if "fund_nav" in group.columns and not group.empty else 0)

    sleeve_sentence = _dominant_sleeve_sentence(group)
    hurdle_sentence = (
        "The LP cash hurdle was achieved during the model period."
        if hurdle
        else "The LP cash hurdle was not achieved during the model period."
    )
    event_flags = sorted({str(flag) for flag in group.get("event_flag", pd.Series(dtype=str)).dropna() if str(flag)})
    event_sentence = f"Annual event flags observed: {', '.join(event_flags)}." if event_flags else "No annual event flags were observed."

    observation = (
        f"Over {years} years, LP cash distributions totalled {_format_currency(total_lp)}, "
        f"or {_format_multiple(lp_cash_moic)} cash MOIC. Economic MOIC was {_format_multiple(lp_economic_moic)}, "
        f"with final fund NAV of {_format_currency(final_fund_nav)}. {hurdle_sentence} "
        f"{sleeve_sentence} {event_sentence}"
    )
    return {"Scenario": scenario, "Observation": observation}


def _dominant_sleeve_sentence(group: pd.DataFrame) -> str:
    if group.empty:
        return "There is no annual cashflow data available to identify the dominant value sleeve."
    last = group.iloc[-1]
    values = {
        "real estate": _safe_float(last.get("re_closing_nav")),
        "hedge fund": _safe_float(last.get("hf_closing_nav")),
        "reserve": _safe_float(last.get("reserve_closing_nav")),
        "retained cash": _safe_float(last.get("retained_cash")),
    }
    dominant, amount = max(values.items(), key=lambda item: item[1])
    return f"At the final year, the largest remaining value bucket was {dominant} at {_format_currency(amount)}."


def _scenario_overrides(scenario: dict[str, Any]) -> str:
    override_keys = ["liquidity", "distribution_policy", "cashflow_routing", "lp_cash_yield_policy", "allocation", "reserve", "refinance_events"]
    present = [key for key in override_keys if scenario.get(key)]
    return ", ".join(present) if present else ""


def _select_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    present = [column for column in columns if column in df.columns]
    return df[present]


def _get_nested(data: dict[str, Any], dotted_key: str) -> Any:
    current: Any = data
    for part in dotted_key.split("."):
        if not isinstance(current, dict) or part not in current:
            return ""
        current = current[part]
    return current


def _markdown_table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    if not rows or not columns:
        return "_No data available._"

    def clean(value: Any) -> str:
        text = "" if value is None else str(value)
        return text.replace("|", "\\|").replace("\n", " ")

    output = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows:
        output.append("| " + " | ".join(clean(row.get(column, "")) for column in columns) + " |")
    return "\n".join(output)


def _format_cell(value: Any) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return _format_value(value)
    return str(value)


def _format_value(value: Any) -> str:
    if value is None or value == "":
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list):
        return ", ".join(_format_value(item) for item in value)
    if isinstance(value, float):
        if abs(value) < 1 and value != 0:
            return _format_pct(value)
        return f"{value:,.2f}"
    if isinstance(value, int):
        return f"{value:,}"
    return str(value)


def _format_pct(value: Any) -> str:
    if value is None or value == "":
        return ""
    try:
        return f"{float(value) * 100:.1f}%"
    except (TypeError, ValueError):
        return str(value)


def _format_pct_list(values: Any) -> str:
    if not isinstance(values, list):
        return ""
    return ", ".join(_format_pct(value) for value in values)


def _format_currency(value: Any) -> str:
    number = _safe_float(value)
    if abs(number) >= 1_000_000:
        return f"${number / 1_000_000:,.1f}m"
    if abs(number) >= 1_000:
        return f"${number / 1_000:,.0f}k"
    return f"${number:,.0f}"


def _format_multiple(value: Any) -> str:
    if value is None or value == "":
        return ""
    try:
        if pd.isna(value):
            return ""
        return f"{float(value):.2f}x"
    except (TypeError, ValueError):
        return str(value)


def _safe_float(value: Any) -> float:
    try:
        if pd.isna(value):
            return 0.0
        return float(value)
    except (TypeError, ValueError):
        return 0.0
