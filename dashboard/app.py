from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import yaml


# Streamlit and Plotly are imported lazily in main/chart functions so helper
# functions can be unit-tested without requiring a dashboard runtime import.


APP_VERSION = "Stage 1 dashboard v0.1"
ROOT = Path(__file__).resolve().parents[1]
CASHFLOW_PATH = ROOT / "outputs" / "scenario_cashflows.csv"
SUMMARY_CSV_PATH = ROOT / "outputs" / "scenario_summary.csv"
SUMMARY_XLSX_PATH = ROOT / "outputs" / "scenario_summary.xlsx"
MODEL_CONFIG_PATH = ROOT / "inputs" / "model_config.yaml"
SCENARIOS_PATH = ROOT / "inputs" / "scenarios.yaml"


# Display names describe the scenario input shape rather than the outcome. This
# keeps the presentation neutral for a lawyer reviewing whether outcomes match
# intuition, rather than baking the model result into the label.
SCENARIO_DISPLAY_NAMES = {
    "base_hit_everyone_happy": "Base case (RE moderate, HF moderate)",
    "fast_success_crypto_bull": "Crypto sleeve strong, short horizon",
    "slow_grind": "Slow growth, weak early HF performance",
    "hedge_fund_failure_re_survival": "HF drawdown, RE survives",
    "real_estate_distress_crypto_success": "RE distress, HF strength",
    "exceptional_dynasty_outcome": "Strong RE and strong HF",
    "liquidity_trap": "High NAV growth, low RE liquidity",
    "failure_never_reaches_hurdle": "Weak RE and weak HF",
}


# Every model flag currently emitted by the engine is translated here. The
# severity is used for plain color treatment, not for financial advice.
FLAG_TRANSLATIONS = {
    "LP_HURDLE_ACHIEVED": {
        "tone": "green",
        "text": "The LP received cash distributions equal to or above the 2x hurdle.",
    },
    "LP_HURDLE_NOT_ACHIEVED": {
        "tone": "red",
        "text": "The LP did not receive enough cash to reach the target hurdle by model end.",
    },
    "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED": {
        "tone": "amber",
        "text": "The fund grew in value enough to clear the hurdle on paper, but did not have enough cash on hand to redeem the LP.",
    },
    "FAST_GP_DYNASTY_OUTCOME": {
        "tone": "green",
        "text": "The LP is redeemed quickly and the GP retains a large residual asset base.",
    },
    "SLOW_TIME_HORIZON_DRIFT": {
        "tone": "amber",
        "text": "The LP outcome takes a long time or does not arrive within the model horizon.",
    },
    "GP_SURVIVABILITY_RISK": {
        "tone": "amber",
        "text": "The GP's fee income over this period is low in absolute terms, which may not support running the fund.",
    },
    "FUND_NAV_IMPAIRED": {
        "tone": "red",
        "text": "Final fund value plus LP cash distributions is below the original LP commitment.",
    },
    "HF_MAJOR_DRAWDOWN": {
        "tone": "amber",
        "text": "The hedge fund sleeve suffered a major drawdown from its initial allocation.",
    },
    "RE_NAV_IMPAIRMENT": {
        "tone": "amber",
        "text": "The real estate sleeve lost a meaningful amount of value from its initial allocation.",
    },
    "LP_GOOD_IRR_GP_LARGE_RESIDUAL": {
        "tone": "green",
        "text": "The LP IRR is attractive while the GP also retains a large residual asset base.",
    },
    "LP_CASH_YIELD_SHORTFALL": {
        "tone": "amber",
        "text": "The model could not fully pay the configured interim LP cash yield from available cash.",
    },
    "REFINANCE_EVENT_OCCURRED": {
        "tone": "green",
        "text": "A configured refinance or recapitalisation event generated proceeds.",
    },
    "REFI_DEPENDENT_LP_OUTCOME": {
        "tone": "amber",
        "text": "The LP hurdle was achieved only because refinance proceeds were distributed to the LP.",
    },
    "LONG_ZERO_DISTRIBUTION_PERIOD": {
        "tone": "amber",
        "text": "The LP experienced a long period with no cash distributions.",
    },
    "LP_STILL_BELOW_1X_CASH_MOIC_AT_END": {
        "tone": "red",
        "text": "At model end, the LP has received less in cash than they originally invested.",
    },
    "LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV": {
        "tone": "amber",
        "text": "The fund still has positive value, but the LP's cash recovery remains weak.",
    },
}


TONE_STYLES = {
    "green": ("#e8f5e9", "#1b5e20"),
    "amber": ("#fff7e0", "#7a4b00"),
    "red": ("#fdecea", "#8a1c1c"),
}


def display_name(scenario: str) -> str:
    """Return a presentation label while preserving raw identifiers in hover."""
    return SCENARIO_DISPLAY_NAMES.get(scenario, scenario.replace("_", " ").title())


def to_number(series: pd.Series) -> pd.Series:
    """Convert CSV string values to numeric, preserving blanks as NaN."""
    return pd.to_numeric(series, errors="coerce")


def format_money(value: Any) -> str:
    """Format dollar values as compact $Xm/$Xk labels for non-technical readers."""
    numeric = float(value) if pd.notna(value) else 0.0
    sign = "-" if numeric < 0 else ""
    numeric = abs(numeric)
    if numeric >= 1_000_000:
        return f"{sign}${numeric / 1_000_000:.1f}m"
    if numeric >= 1_000:
        return f"{sign}${numeric / 1_000:.0f}k"
    return f"{sign}${numeric:,.0f}"


def format_multiple(value: Any) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{float(value):.2f}x"


def format_percent(value: Any) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{float(value):.1%}"


def read_dashboard_data() -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    """Read model outputs with defensive fallbacks and return user-visible notes."""
    notes: list[str] = []
    if not CASHFLOW_PATH.exists():
        raise FileNotFoundError(f"Missing required cashflow file: {CASHFLOW_PATH}")
    cashflows = pd.read_csv(CASHFLOW_PATH)

    if SUMMARY_CSV_PATH.exists():
        summary = pd.read_csv(SUMMARY_CSV_PATH)
    elif SUMMARY_XLSX_PATH.exists():
        notes.append("Summary CSV was missing; read the Summary tab from scenario_summary.xlsx instead.")
        summary = pd.read_excel(SUMMARY_XLSX_PATH, sheet_name="Summary")
    else:
        raise FileNotFoundError("Missing summary output: expected scenario_summary.csv or scenario_summary.xlsx.")

    cashflows = normalize_numeric_columns(cashflows)
    summary = normalize_numeric_columns(summary)
    cashflows["scenario_display"] = cashflows["scenario"].map(display_name)
    summary["scenario_display"] = summary["scenario"].map(display_name)
    return cashflows, summary, notes


def read_assumption_yaml() -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    """Read editable YAML assumptions for display in the dashboard.

    The dashboard is intentionally read-only. This function only shows the
    assumptions that generated the pre-baked output files; it does not mutate
    the model or re-run calculations.
    """
    notes: list[str] = []
    model_config: dict[str, Any] = {}
    scenarios: dict[str, Any] = {}

    try:
        with MODEL_CONFIG_PATH.open("r", encoding="utf-8") as file:
            loaded = yaml.safe_load(file) or {}
            if isinstance(loaded, dict):
                model_config = loaded
            else:
                notes.append("model_config.yaml did not contain a mapping and could not be displayed.")
    except FileNotFoundError:
        notes.append("model_config.yaml was not found; global assumptions cannot be displayed.")
    except yaml.YAMLError as exc:
        notes.append(f"model_config.yaml could not be parsed: {exc}")

    try:
        with SCENARIOS_PATH.open("r", encoding="utf-8") as file:
            loaded = yaml.safe_load(file) or {}
            if isinstance(loaded, dict):
                scenarios = loaded.get("scenarios", {})
            else:
                notes.append("scenarios.yaml did not contain a mapping and could not be displayed.")
    except FileNotFoundError:
        notes.append("scenarios.yaml was not found; scenario assumptions cannot be displayed.")
    except yaml.YAMLError as exc:
        notes.append(f"scenarios.yaml could not be parsed: {exc}")

    return model_config, scenarios, notes


def normalize_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize expected numeric output columns after CSV/Excel reads."""
    numeric_columns = [
        "year",
        "lp_cumulative_distribution",
        "lp_distribution",
        "lp_remaining_hurdle",
        "fund_nav",
        "re_closing_nav",
        "hf_closing_nav",
        "reserve_closing_nav",
        "retained_cash",
        "net_re_cashflow",
        "hf_harvest",
        "refinance_proceeds",
        "re_asset_mgmt_fee",
        "reserve_opening_nav",
        "lp_cash_moic",
        "lp_economic_moic",
        "lp_cash_irr",
        "lp_economic_irr",
        "lp_hurdle_amount",
        "lp_initial_capital",
        "gp_total_economics",
        "gp_total_economics_pct_initial_lp_capital",
        "gp_residual_nav",
        "final_fund_nav",
    ]
    for column in numeric_columns:
        if column in df.columns:
            df[column] = to_number(df[column])
    return df


def require_columns(df: pd.DataFrame, required: list[str], context: str, notes: list[str]) -> bool:
    """Record missing columns rather than crashing chart rendering."""
    missing = [column for column in required if column not in df.columns]
    if missing:
        notes.append(f"{context}: missing columns {missing}; this section was skipped or simplified.")
        return False
    return True


def scenario_order(summary: pd.DataFrame) -> list[str]:
    """Worst cash MOIC first, best cash MOIC last."""
    if "lp_cash_moic" not in summary.columns:
        return list(summary["scenario"])
    return list(summary.sort_values("lp_cash_moic", ascending=True)["scenario"])


def generate_scenario_caption(scenario_df: pd.DataFrame, scenario_summary_row: pd.Series) -> str:
    """Generate a plain-English scenario caption directly from output data."""
    scenario = str(scenario_summary_row["scenario"])
    display = display_name(scenario)
    lp_capital = scenario_summary_row.get("lp_initial_capital", 0)
    lp_cash = scenario_summary_row.get("lp_cash_distributions", scenario_df["lp_distribution"].sum())
    years = int(scenario_summary_row.get("years_modelled", scenario_df["year"].max()))
    cash_moic = scenario_summary_row.get("lp_cash_moic", 0)
    economic_moic = scenario_summary_row.get("lp_economic_moic", cash_moic)
    hurdle_achieved = str(scenario_summary_row.get("lp_hurdle_achieved", "False")).lower() == "true"
    year_hurdle = scenario_summary_row.get("year_hurdle_achieved", "")

    if hurdle_achieved:
        hurdle_sentence = f"The LP hurdle was reached in year {int(float(year_hurdle)) if pd.notna(year_hurdle) and year_hurdle != '' else 'n/a'}."
    elif str(scenario_summary_row.get("liquidity_constrained", "False")).lower() == "true":
        hurdle_sentence = "The model shows enough value on paper at some point, but not enough available liquidity to redeem the LP."
    else:
        hurdle_sentence = "The LP hurdle was not reached within the modelled period."

    driver_sentence = infer_driver_sentence(scenario_df, scenario_summary_row)
    return (
        f"{display}: the LP committed {format_money(lp_capital)} and received {format_money(lp_cash)} "
        f"in cash distributions over {years} years. The fund's economic value reached "
        f"{format_multiple(economic_moic)} of the initial commitment, while cash distributions reached "
        f"{format_multiple(cash_moic)}. {hurdle_sentence} {driver_sentence}"
    )


def infer_driver_sentence(scenario_df: pd.DataFrame, summary_row: pd.Series) -> str:
    """Use sleeve NAV trajectories and event flags to describe the likely driver."""
    flags = parse_flags(summary_row.get("all_flags", ""))
    if "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED" in flags:
        return "The key tension is liquidity: asset value exists, but it is not readily available as LP cash."
    if "HF_MAJOR_DRAWDOWN" in flags:
        return "The hedge fund sleeve is a major drag because it suffers a large drawdown."
    if "RE_NAV_IMPAIRMENT" in flags:
        return "The real estate sleeve is a major drag because its NAV declines materially."
    if "LP_HURDLE_ACHIEVED" in flags:
        return "The outcome is driven by enough cash or liquid value becoming available to complete the LP redemption."

    final = scenario_df.sort_values("year").tail(1)
    if final.empty:
        return "The driver is unclear because no annual cashflow rows were available."
    re_nav = float(final.get("re_closing_nav", pd.Series([0])).iloc[0] or 0)
    hf_nav = float(final.get("hf_closing_nav", pd.Series([0])).iloc[0] or 0)
    retained_cash = float(final.get("retained_cash", pd.Series([0])).iloc[0] or 0)
    reserve = float(final.get("reserve_closing_nav", pd.Series([0])).iloc[0] or 0)
    dominant = max(
        [("real estate", re_nav), ("hedge fund", hf_nav), ("retained cash", retained_cash), ("reserve", reserve)],
        key=lambda item: item[1],
    )[0]
    return f"By model end, most remaining value sits in {dominant}, which helps explain the gap between NAV and LP cash."


def parse_flags(value: Any) -> list[str]:
    if pd.isna(value) or not str(value).strip():
        return []
    return [flag.strip() for flag in str(value).split(";") if flag.strip()]


def build_outcome_chart(summary: pd.DataFrame, notes: list[str]):
    """Full-width horizontal scenario outcome chart."""
    import plotly.graph_objects as go

    if not require_columns(
        summary,
        ["scenario", "lp_cash_moic", "lp_economic_moic", "gp_total_economics_pct_initial_lp_capital"],
        "Outcome chart",
        notes,
    ):
        return None

    ordered = summary.sort_values("lp_cash_moic", ascending=True)
    lp_rows = [f"{display_name(s)} - LP" for s in ordered["scenario"]]
    gp_rows = [f"{display_name(s)} - GP" for s in ordered["scenario"]]
    y_values = [value for pair in zip(lp_rows, gp_rows) for value in pair]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=lp_rows,
            x=ordered["lp_economic_moic"],
            orientation="h",
            name="LP economic MOIC",
            marker=dict(color="rgba(0,0,0,0)", line=dict(color="#355c7d", width=2)),
            hovertemplate="%{y}<br>LP economic MOIC: %{x:.2f}x<extra></extra>",
        )
    )
    fig.add_trace(
        go.Bar(
            y=lp_rows,
            x=ordered["lp_cash_moic"],
            orientation="h",
            name="LP cash MOIC",
            marker_color="#2f6f95",
            hovertemplate="%{y}<br>LP cash MOIC: %{x:.2f}x<extra></extra>",
        )
    )
    fig.add_trace(
        go.Bar(
            y=gp_rows,
            x=ordered["gp_total_economics_pct_initial_lp_capital"],
            orientation="h",
            name="GP total economics / initial LP capital",
            marker_color="#9b5de5",
            hovertemplate="%{y}<br>GP total economics: %{x:.2f}x initial LP capital<extra></extra>",
        )
    )
    fig.add_vline(x=1.0, line_width=1, line_dash="dash", line_color="#555", annotation_text="1.0x")
    fig.add_vline(x=2.0, line_width=1, line_dash="dash", line_color="#111", annotation_text="2.0x hurdle")
    fig.update_layout(
        title="LP and GP outcomes across scenarios.",
        barmode="overlay",
        height=620,
        yaxis=dict(categoryorder="array", categoryarray=list(reversed(y_values))),
        xaxis_title="Multiple of initial LP capital",
        legend_orientation="h",
        margin=dict(l=240, r=40, t=105, b=70),
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    return fig


def build_lp_value_chart(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None, notes: list[str]):
    """LP cash distributions versus economic position over time."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    required = ["scenario", "year", "lp_cumulative_distribution", "lp_remaining_hurdle", "fund_nav"]
    if not require_columns(cashflows, required, "LP value chart", notes):
        return None

    scenarios = [selected] if selected else scenario_order(summary)
    rows, cols = panel_shape(scenarios)
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=[display_name(s) for s in scenarios],
        vertical_spacing=0.16 if not selected else 0.10,
        horizontal_spacing=0.08,
    )
    y_max = max(
        float(cashflows["lp_cumulative_distribution"].max() or 0),
        float((cashflows["lp_cumulative_distribution"] + cashflows[["fund_nav", "lp_remaining_hurdle"]].min(axis=1)).max() or 0),
        float(summary.get("lp_hurdle_amount", pd.Series([0])).max() or 0),
    )

    for index, scenario in enumerate(scenarios):
        row, col = panel_position(index, cols)
        df = cashflows[cashflows["scenario"] == scenario].sort_values("year")
        if df.empty:
            continue
        economic_value = df["lp_cumulative_distribution"] + df[["fund_nav", "lp_remaining_hurdle"]].min(axis=1)
        fig.add_trace(
            go.Scatter(x=df["year"], y=economic_value, mode="lines", name="LP economic position", line=dict(color="#355c7d", dash="dash"), showlegend=index == 0),
            row=row,
            col=col,
        )
        fig.add_trace(
            go.Scatter(x=df["year"], y=df["lp_cumulative_distribution"], mode="lines", name="LP cash distributions", fill="tonexty", line=dict(color="#2f6f95"), showlegend=index == 0),
            row=row,
            col=col,
        )
        hurdle = scenario_hurdle(summary, scenario)
        fig.add_hline(y=hurdle, line_dash="dot", line_color="#555", row=row, col=col)

    fig.update_yaxes(range=[0, y_max * 1.08], tickprefix="$", tickformat="~s")
    fig.update_xaxes(title_text="Year")
    style_chart_layout(fig, "LP cash versus economic value over time.", selected)
    return fig


def build_cashflow_chart(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None, notes: list[str]):
    """Annual source-of-cash stacked bars with LP distributions overlaid."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    required = ["scenario", "year", "net_re_cashflow", "hf_harvest", "refinance_proceeds", "re_asset_mgmt_fee", "lp_distribution"]
    if not require_columns(cashflows, required, "Annual cashflow chart", notes):
        return None

    df_all = cashflows.copy()
    if "reserve_opening_nav" in df_all.columns and "reserve_closing_nav" in df_all.columns:
        df_all["reserve_drawdown_inferred"] = (df_all["reserve_opening_nav"] - df_all["reserve_closing_nav"]).clip(lower=0)
    else:
        df_all["reserve_drawdown_inferred"] = 0.0
        notes.append("Annual cashflow chart: reserve drawdown column was not explicit; set reserve drawdown to zero.")
    df_all["fees_taken_negative"] = -df_all["re_asset_mgmt_fee"].abs()

    components = [
        ("net_re_cashflow", "RE net cashflow", "#4c78a8"),
        ("hf_harvest", "HF harvested gains", "#72b7b2"),
        ("refinance_proceeds", "Refinance proceeds", "#f58518"),
        ("reserve_drawdown_inferred", "Reserve drawdown inferred", "#54a24b"),
        ("fees_taken_negative", "Fees taken", "#b279a2"),
    ]
    scenarios = [selected] if selected else scenario_order(summary)
    rows, cols = panel_shape(scenarios)
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=[display_name(s) for s in scenarios],
        vertical_spacing=0.16 if not selected else 0.10,
        horizontal_spacing=0.08,
    )
    y_max = max(float(df_all[[name for name, _, _ in components if name != "fees_taken_negative"]].sum(axis=1).max() or 0), float(df_all["lp_distribution"].max() or 0))

    for index, scenario in enumerate(scenarios):
        row, col = panel_position(index, cols)
        df = df_all[df_all["scenario"] == scenario].sort_values("year")
        for component, label, color in components:
            fig.add_trace(
                go.Bar(x=df["year"], y=df[component], name=label, marker_color=color, showlegend=index == 0),
                row=row,
                col=col,
            )
        fig.add_trace(
            go.Scatter(x=df["year"], y=df["lp_distribution"], mode="lines+markers", name="LP distribution paid", line=dict(color="#111", width=2), showlegend=index == 0),
            row=row,
            col=col,
        )

    style_chart_layout(fig, "Where the cash came from each year.", selected, barmode="relative")
    fig.update_yaxes(range=[min(0, -y_max * 0.15), y_max * 1.15], tickprefix="$", tickformat="~s")
    fig.update_xaxes(title_text="Year")
    return fig


def build_nav_chart(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None, notes: list[str]):
    """Stacked area chart showing where value lived over time."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    required = ["scenario", "year", "re_closing_nav", "hf_closing_nav", "reserve_closing_nav", "retained_cash"]
    if not require_columns(cashflows, required, "NAV chart", notes):
        return None

    scenarios = [selected] if selected else scenario_order(summary)
    rows, cols = panel_shape(scenarios)
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=[display_name(s) for s in scenarios],
        vertical_spacing=0.16 if not selected else 0.10,
        horizontal_spacing=0.08,
    )
    components = [
        ("re_closing_nav", "Real estate NAV", "#4c78a8"),
        ("hf_closing_nav", "Hedge fund NAV", "#72b7b2"),
        ("reserve_closing_nav", "Reserve NAV", "#54a24b"),
        ("retained_cash", "Retained cash", "#f58518"),
    ]
    y_max = float(cashflows[[component for component, _, _ in components]].sum(axis=1).max() or 0)

    for index, scenario in enumerate(scenarios):
        row, col = panel_position(index, cols)
        df = cashflows[cashflows["scenario"] == scenario].sort_values("year")
        for component, label, color in components:
            fig.add_trace(
                go.Scatter(
                    x=df["year"],
                    y=df[component],
                    mode="lines",
                    stackgroup=f"group-{index}",
                    name=label,
                    line=dict(width=0.5, color=color),
                    showlegend=index == 0,
                ),
                row=row,
                col=col,
            )

    style_chart_layout(fig, "Where the value lived each year.", selected)
    fig.update_yaxes(range=[0, y_max * 1.08], tickprefix="$", tickformat="~s")
    fig.update_xaxes(title_text="Year")
    return fig


def panel_shape(scenarios: list[str]) -> tuple[int, int]:
    if len(scenarios) == 1:
        return 1, 1
    return 2, 4


def panel_position(index: int, cols: int) -> tuple[int, int]:
    return (index // cols) + 1, (index % cols) + 1


def chart_height(selected: str | None) -> int:
    return 560 if selected else 880


def style_chart_layout(fig: Any, title: str, selected: str | None, **extra_layout: Any) -> None:
    """Apply consistent light chart styling and title spacing.

    Plotly subplot titles sit inside the plot area by default. The extra top
    margin and annotation shift keep the main chart title and per-panel titles
    from colliding on Streamlit's responsive canvas.
    """
    fig.update_layout(
        title=dict(text=title, y=0.985, x=0.01, xanchor="left"),
        height=chart_height(selected),
        plot_bgcolor="white",
        paper_bgcolor="white",
        legend_orientation="h",
        margin=dict(l=70, r=35, t=135, b=65),
        **extra_layout,
    )
    fig.update_annotations(yshift=16)


def scenario_hurdle(summary: pd.DataFrame, scenario: str) -> float:
    row = summary[summary["scenario"] == scenario]
    if row.empty or "lp_hurdle_amount" not in row.columns:
        return 20_000_000.0
    return float(row.iloc[0]["lp_hurdle_amount"])


def render_metric_cards(summary_row: pd.Series) -> None:
    """Render six headline cards for single-scenario mode."""
    import streamlit as st

    columns = st.columns(6)
    cards = [
        ("LP cash MOIC", format_multiple(summary_row.get("lp_cash_moic")), "Cash returned to LP."),
        ("LP economic MOIC", format_multiple(summary_row.get("lp_economic_moic")), "Cash plus remaining claim."),
        ("LP cash IRR", format_percent(summary_row.get("lp_cash_irr")), "Actual cash timing."),
        ("GP total economics", format_money(summary_row.get("gp_total_economics")), "Fees plus residual value."),
        ("Hurdle year", hurdle_year_label(summary_row), "When 2x cash hurdle is met."),
        ("End fund NAV", format_money(summary_row.get("final_fund_nav")), "Value left at model end."),
    ]
    for column, (label, value, caption) in zip(columns, cards):
        with column:
            st.metric(label, value)
            st.caption(caption)


def render_selected_assumptions(
    selected: str,
    model_config: dict[str, Any],
    scenarios: dict[str, Any],
    assumption_notes: list[str],
) -> None:
    """Show the YAML assumptions for the selected scenario in a tidy expander."""
    import streamlit as st

    scenario_assumptions = scenarios.get(selected)
    with st.expander("Selected scenario assumptions", expanded=False):
        if assumption_notes:
            for note in assumption_notes:
                st.warning(note)
        if not scenario_assumptions:
            st.write("No scenario assumptions were found for this selection.")
            return

        st.caption("These are the YAML assumptions that generated the pre-baked scenario output. The dashboard does not edit or re-run them.")
        left, right = st.columns(2)
        with left:
            st.markdown("**Scenario-specific assumptions**")
            st.dataframe(flatten_assumptions(scenario_assumptions), width="stretch", hide_index=True)
        with right:
            st.markdown("**Global assumptions used unless overridden**")
            global_sections = {
                "model": model_config.get("model", {}),
                "allocation": model_config.get("allocation", {}),
                "waterfall": model_config.get("waterfall", {}),
                "liquidity": model_config.get("liquidity", {}),
                "fees": model_config.get("fees", {}),
                "distribution_policy": model_config.get("distribution_policy", {}),
                "lp_cash_yield_policy": model_config.get("lp_cash_yield_policy", {}),
                "gp_survivability": model_config.get("gp_survivability", {}),
            }
            st.dataframe(flatten_assumptions(global_sections), width="stretch", hide_index=True)


def flatten_assumptions(data: dict[str, Any], prefix: str = "") -> pd.DataFrame:
    """Flatten nested YAML into a two-column table for non-technical review."""
    rows: list[dict[str, str]] = []

    def walk(value: Any, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                walk(child, f"{path}.{key}" if path else str(key))
        elif isinstance(value, list):
            rows.append({"assumption": path, "value": ", ".join(str(item) for item in value)})
        else:
            rows.append({"assumption": path, "value": str(value)})

    walk(data, prefix)
    return pd.DataFrame(rows)


def hurdle_year_label(summary_row: pd.Series) -> str:
    value = summary_row.get("year_hurdle_achieved")
    if pd.isna(value) or value == "":
        return "not reached"
    return f"year {int(float(value))}"


def render_captions(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None) -> None:
    """Render data-generated narrative captions."""
    import streamlit as st

    if selected:
        row = summary[summary["scenario"] == selected].iloc[0]
        st.write(generate_scenario_caption(cashflows[cashflows["scenario"] == selected], row))
        render_flags(row)
        return

    st.subheader("Plain English scenario notes")
    for _, row in summary.sort_values("lp_cash_moic", ascending=True).iterrows():
        with st.expander(display_name(row["scenario"])):
            st.write(generate_scenario_caption(cashflows[cashflows["scenario"] == row["scenario"]], row))
            render_flags(row)


def render_flags(summary_row: pd.Series) -> None:
    """Render active flags as translated plain-English statements."""
    import streamlit as st

    flags = parse_flags(summary_row.get("all_flags", ""))
    if not flags:
        st.caption("No active diagnostic flags.")
        return
    st.markdown("**Active diagnostic flags**")
    for flag in flags:
        item = FLAG_TRANSLATIONS.get(flag, {"tone": "amber", "text": flag.replace("_", " ").title()})
        bg, fg = TONE_STYLES[item["tone"]]
        st.markdown(
            f"<div style='background:{bg}; color:{fg}; padding:8px 10px; margin:4px 0; border-radius:6px;'>{item['text']}</div>",
            unsafe_allow_html=True,
        )


def download_cashflows_button(cashflows: pd.DataFrame) -> None:
    import streamlit as st

    st.download_button(
        label="Download raw cashflows CSV",
        data=cashflows.to_csv(index=False).encode("utf-8"),
        file_name="scenario_cashflows.csv",
        mime="text/csv",
    )


def main() -> None:
    import streamlit as st

    st.set_page_config(page_title="Fund Model Scenario Explorer", layout="wide")
    st.title("Fund Model — Scenario Explorer (Stage 1)")
    st.write(
        "This dashboard presents the eight pre-baked fund model scenarios as charts and plain-English diagnostics. "
        "It does not run new assumptions or edit the model; it reads the existing output files and makes them legible. "
        "Stage 2 will add live input editing and assumption transparency."
    )

    try:
        cashflows, summary, notes = read_dashboard_data()
        model_config, scenario_assumptions, assumption_notes = read_assumption_yaml()
    except Exception as exc:
        st.error(f"Could not load dashboard data: {exc}")
        st.stop()

    if notes:
        with st.expander("Data read notes and fallbacks"):
            for note in notes:
                st.write(note)

    outcome_fig = build_outcome_chart(summary, notes)
    if outcome_fig is not None:
        st.plotly_chart(outcome_fig, width="stretch")

    options = ["All scenarios (small multiples)"] + [display_name(s) for s in scenario_order(summary)]
    label_to_scenario = {display_name(s): s for s in summary["scenario"]}
    selected_label = st.selectbox("Scenario selector", options=options, index=0)
    selected = None if selected_label == "All scenarios (small multiples)" else label_to_scenario[selected_label]

    if selected:
        render_metric_cards(summary[summary["scenario"] == selected].iloc[0])
        render_selected_assumptions(selected, model_config, scenario_assumptions, assumption_notes)

    lp_value_fig = build_lp_value_chart(cashflows, summary, selected, notes)
    if lp_value_fig is not None:
        st.plotly_chart(lp_value_fig, width="stretch")
        st.caption("Dashed line shows LP economic position: cumulative LP cash plus remaining LP claim value, capped by fund NAV.")
    render_captions(cashflows, summary, selected)

    cashflow_fig = build_cashflow_chart(cashflows, summary, selected, notes)
    if cashflow_fig is not None:
        st.plotly_chart(cashflow_fig, width="stretch")
        st.caption("Reserve drawdown is inferred from reserve opening NAV less reserve closing NAV when no explicit drawdown column exists.")
    render_captions(cashflows, summary, selected)

    nav_fig = build_nav_chart(cashflows, summary, selected, notes)
    if nav_fig is not None:
        st.plotly_chart(nav_fig, width="stretch")
    render_captions(cashflows, summary, selected)

    st.divider()
    download_cashflows_button(cashflows)
    st.caption(f"{APP_VERSION}. Stage 2 will add live input editing and assumption transparency.")


if __name__ == "__main__":
    main()
