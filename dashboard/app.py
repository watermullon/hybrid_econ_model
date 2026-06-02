from __future__ import annotations

from pathlib import Path
import math
import sys
from typing import Any

import pandas as pd
import yaml


# Streamlit and Plotly are imported lazily in main/chart functions so helper
# functions can be unit-tested without requiring a dashboard runtime import.


APP_VERSION = "Stage 1 dashboard v0.2"
ROOT = Path(__file__).resolve().parents[1]
CASHFLOW_PATH = ROOT / "outputs" / "scenario_cashflows.csv"
SUMMARY_CSV_PATH = ROOT / "outputs" / "scenario_summary.csv"
SUMMARY_XLSX_PATH = ROOT / "outputs" / "scenario_summary.xlsx"
MODEL_CONFIG_PATH = ROOT / "inputs" / "model_config.yaml"
SCENARIOS_PATH = ROOT / "inputs" / "scenarios.yaml"

# Streamlit may be launched from the repo root, this dashboard directory, or a
# parent folder. Adding the project root explicitly keeps imports such as
# `from src.engine import ...` stable in all of those cases.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# Display names describe the scenario input shape rather than the outcome. This
# keeps the presentation neutral for a lawyer reviewing whether outcomes match
# intuition, rather than baking the model result into the label.
SCENARIO_DISPLAY_NAMES = {
    "base_hit_everyone_happy": "Moderate RE and HF baseline",
    "fast_success_crypto_bull": "Crypto sleeve strong, short horizon",
    "slow_grind": "Slow growth, weak early HF performance",
    "hedge_fund_failure_re_survival": "HF drawdown, RE survives",
    "real_estate_distress_crypto_success": "RE distress, HF strength",
    "exceptional_dynasty_outcome": "Strong RE and strong HF",
    "liquidity_trap": "High NAV growth, low RE liquidity",
    "failure_never_reaches_hurdle": "Weak RE and weak HF",
    "custom_dashboard_scenario": "Custom dashboard scenario",
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
    "HURDLE_COMPLETION_TRIGGER_EXECUTED": {
        "tone": "green",
        "text": "The GP actively monetized permitted sources to finish the LP cash hurdle.",
    },
    "HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT": {
        "tone": "amber",
        "text": "The active hurdle trigger was eligible, but permitted funding sources were not enough to fully redeem the LP.",
    },
    "LP_REDEEMED_VIA_HF_LIQUIDATION": {
        "tone": "amber",
        "text": "The LP redemption used partial hedge fund liquidation.",
    },
    "LP_REDEEMED_VIA_REFI": {
        "tone": "amber",
        "text": "The LP redemption used refinance proceeds.",
    },
    "LP_REDEEMED_VIA_PARTIAL_RE_SALE": {
        "tone": "amber",
        "text": "The LP redemption used partial real estate sale proceeds.",
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
        "refinance_liability",
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
        "final_refinance_liability",
        "re_cashflow_generated",
        "re_cashflow_to_lp",
        "re_cashflow_to_hf",
        "re_cashflow_to_reserve",
        "hf_harvest_generated",
        "hf_harvest_to_lp",
        "hf_harvest_to_hf",
        "hf_harvest_to_reserve",
        "cumulative_reinvested_into_hf",
        "cumulative_cash_distributed_to_lp",
        "cumulative_cash_added_to_reserve",
        "hf_reinvestment_source_re",
        "hf_reinvestment_source_hf",
        "total_cash_reinvested",
        "total_cash_distributed",
        "total_cash_reserved",
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
        "hurdle_trigger_year",
        "total_trigger_cash_from_retained_cash",
        "total_trigger_cash_from_reserve",
        "total_trigger_cash_from_hf_liquidation",
        "total_trigger_cash_from_refi",
        "total_trigger_cash_from_re_sale",
        "lp_hurdle_shortfall_after_final_trigger",
        "re_noi",
        "re_debt_service",
        "re_capex",
        "re_free_cashflow_after_debt_and_capex",
        "re_gross_asset_value",
        "re_debt_balance",
        "re_assumed_liabilities",
        "re_ending_refi_liability",
        "re_refi_proceeds_from_deals",
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


def run_model_with_routing_override(
    routing: dict[str, dict[str, float]],
    trigger: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Rerun the existing eight scenarios in memory with dashboard routing values.

    This is deliberately not a persistence layer: it does not write YAML, CSV,
    or Excel. It lets presentation users see how routing policy changes the
    already-defined scenarios without creating new model assumptions on disk.
    """
    from src.config_loader import load_inputs
    from src.engine import result_dicts, run_all_scenarios

    config, scenario_set, deals = load_inputs(ROOT / "inputs")
    config_data = config.model_dump()
    config_data["cashflow_routing"] = {
        "re_cashflow": routing["re_cashflow"],
        "hf_harvest": routing["hf_harvest"],
    }
    config_data["hurdle_completion_trigger"] = trigger
    rerun_config = config.__class__.model_validate(config_data)
    results = run_all_scenarios(rerun_config, scenario_set.scenarios, deals)
    summaries, cashflows, _, _ = result_dicts(results)
    summary = normalize_numeric_columns(pd.DataFrame(summaries))
    cashflow_df = normalize_numeric_columns(pd.DataFrame(cashflows))
    summary["scenario_display"] = summary["scenario"].map(display_name)
    cashflow_df["scenario_display"] = cashflow_df["scenario"].map(display_name)
    return cashflow_df, summary


def run_custom_scenario_in_memory(
    custom_inputs: dict[str, Any],
    routing: dict[str, dict[str, float]],
    trigger: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run one user-entered scenario without writing YAML or output files."""
    from src.config_loader import load_inputs
    from src.engine import result_dicts, run_scenario
    from src.model_types import ModelConfig, Scenario

    config, _, deals = load_inputs(ROOT / "inputs")
    config_data = config.model_dump()
    config_data["cashflow_routing"] = {
        "re_cashflow": routing["re_cashflow"],
        "hf_harvest": routing["hf_harvest"],
    }
    config_data["hurdle_completion_trigger"] = trigger
    config_data["allocation"] = {
        "method": "fixed",
        "hedge_fund_allocation_pct": custom_inputs["hf_allocation_pct"],
        "real_estate_allocation_pct": custom_inputs["re_allocation_pct"],
        "reserve_allocation_pct": custom_inputs["reserve_allocation_pct"],
    }
    config_data["liquidity"]["max_refinance_or_sale_capacity_pct_of_re_nav"] = custom_inputs["re_liquidity_pct"]
    config_data["distribution_policy"]["hf_positive_return_harvest_rate"] = custom_inputs["hf_harvest_rate"]
    config_data["distribution_policy"]["distribute_hf_realized_gains_annually"] = False
    rerun_config = ModelConfig.model_validate(config_data)

    scenario = Scenario.model_validate(
        {
            "description": "Custom dashboard scenario. Temporary in-memory run only.",
            "years": custom_inputs["years"],
            "real_estate": {
                "initial_noi_yield": custom_inputs["initial_noi_yield"],
                "annual_noi_growth": custom_inputs["annual_noi_growth"],
                "annual_nav_appreciation": custom_inputs["annual_nav_appreciation"],
                "gross_rent_yield": custom_inputs["gross_rent_yield"],
            },
            "hedge_fund": {"annual_returns": custom_inputs["hf_returns"]},
        }
    )
    result = run_scenario("custom_dashboard_scenario", scenario, rerun_config, deals)
    summaries, cashflows, _, _ = result_dicts([result])
    summary = normalize_numeric_columns(pd.DataFrame(summaries))
    cashflow_df = normalize_numeric_columns(pd.DataFrame(cashflows))
    summary["scenario_display"] = summary["scenario"].map(display_name)
    cashflow_df["scenario_display"] = cashflow_df["scenario"].map(display_name)
    return cashflow_df, summary


def parse_hf_returns(raw_returns: str, years: int) -> list[float]:
    """Parse comma-separated annual returns entered as percentages.

    Example: "20, 15, -5" becomes [0.20, 0.15, -0.05]. If fewer values than
    `years` are supplied, the final supplied return is repeated. If more are
    supplied, extra values are ignored so the scenario horizon remains explicit.
    """
    values: list[float] = []
    for item in raw_returns.split(","):
        stripped = item.strip()
        if not stripped:
            continue
        values.append(float(stripped) / 100)
    if not values:
        raise ValueError("Enter at least one HF annual return percentage.")
    if len(values) < years:
        values.extend([values[-1]] * (years - len(values)))
    return values[:years]


def default_routing_from_config(model_config: dict[str, Any]) -> dict[str, dict[str, float]]:
    """Read default routing percentages from model_config.yaml."""
    routing = model_config.get("cashflow_routing", {})
    return {
        "re_cashflow": {
            "lp_distribution_pct": float(routing.get("re_cashflow", {}).get("lp_distribution_pct", 0.50)),
            "hf_reinvestment_pct": float(routing.get("re_cashflow", {}).get("hf_reinvestment_pct", 0.30)),
            "reserve_pct": float(routing.get("re_cashflow", {}).get("reserve_pct", 0.20)),
        },
        "hf_harvest": {
            "lp_distribution_pct": float(routing.get("hf_harvest", {}).get("lp_distribution_pct", 0.70)),
            "hf_reinvestment_pct": float(routing.get("hf_harvest", {}).get("hf_reinvestment_pct", 0.20)),
            "reserve_pct": float(routing.get("hf_harvest", {}).get("reserve_pct", 0.10)),
        },
    }


def default_trigger_from_config(model_config: dict[str, Any]) -> dict[str, Any]:
    """Read active hurdle trigger defaults from model_config.yaml."""
    trigger = model_config.get("hurdle_completion_trigger", {})
    return {
        "enabled": bool(trigger.get("enabled", True)),
        "trigger_when_economic_hurdle_passed": bool(trigger.get("trigger_when_economic_hurdle_passed", True)),
        "minimum_lp_cash_moic_before_trigger": float(trigger.get("minimum_lp_cash_moic_before_trigger", 1.25)),
        "max_hf_liquidation_pct": float(trigger.get("max_hf_liquidation_pct", 0.75)),
        "max_refi_pct_of_re_nav": float(trigger.get("max_refi_pct_of_re_nav", 0.20)),
        "allow_retained_cash_use": bool(trigger.get("allow_retained_cash_use", True)),
        "allow_reserve_use": bool(trigger.get("allow_reserve_use", True)),
        "allow_hf_liquidation": bool(trigger.get("allow_hf_liquidation", True)),
        "allow_refi": bool(trigger.get("allow_refi", True)),
        "allow_partial_re_sale": bool(trigger.get("allow_partial_re_sale", False)),
        "max_partial_re_sale_pct_of_re_nav": float(trigger.get("max_partial_re_sale_pct_of_re_nav", 0.0)),
        "execute_only_if_lp_fully_redeemed": bool(trigger.get("execute_only_if_lp_fully_redeemed", True)),
    }


def render_trigger_controls(model_config: dict[str, Any]) -> dict[str, Any]:
    """Render active hurdle trigger controls and return normalized values."""
    import streamlit as st

    defaults = default_trigger_from_config(model_config)
    st.sidebar.header("LP hurdle completion trigger")
    st.sidebar.caption("Tests whether permitted liquidity engineering can finish the LP 2x cash hurdle. Does not save YAML.")

    enabled = st.sidebar.checkbox("Enable active trigger", value=defaults["enabled"])
    minimum_cash_moic = st.sidebar.slider(
        "Minimum LP cash MOIC before trigger",
        0.0,
        2.0,
        float(defaults["minimum_lp_cash_moic_before_trigger"]),
        0.05,
    )
    max_hf_liquidation_pct = st.sidebar.slider(
        "Max HF liquidation for trigger",
        0,
        100,
        int(defaults["max_hf_liquidation_pct"] * 100),
        5,
    )
    max_refi_pct = st.sidebar.slider(
        "Max refi for trigger (% RE NAV)",
        0,
        100,
        int(defaults["max_refi_pct_of_re_nav"] * 100),
        5,
    )
    allow_retained = st.sidebar.checkbox("Use retained cash", value=defaults["allow_retained_cash_use"])
    allow_reserve = st.sidebar.checkbox("Use reserve", value=defaults["allow_reserve_use"])
    allow_hf = st.sidebar.checkbox("Use HF liquidation", value=defaults["allow_hf_liquidation"])
    allow_refi = st.sidebar.checkbox("Use refinance", value=defaults["allow_refi"])
    allow_sale = st.sidebar.checkbox("Allow partial RE sale", value=defaults["allow_partial_re_sale"])

    return {
        "enabled": enabled,
        "trigger_when_economic_hurdle_passed": defaults["trigger_when_economic_hurdle_passed"],
        "minimum_lp_cash_moic_before_trigger": minimum_cash_moic,
        "max_hf_liquidation_pct": max_hf_liquidation_pct / 100,
        "max_refi_pct_of_re_nav": max_refi_pct / 100,
        "allow_retained_cash_use": allow_retained,
        "allow_reserve_use": allow_reserve,
        "allow_hf_liquidation": allow_hf,
        "allow_refi": allow_refi,
        "allow_partial_re_sale": allow_sale,
        "max_partial_re_sale_pct_of_re_nav": defaults["max_partial_re_sale_pct_of_re_nav"] if allow_sale else 0.0,
        "execute_only_if_lp_fully_redeemed": True,
    }


def render_routing_controls(model_config: dict[str, Any]) -> tuple[dict[str, dict[str, float]], bool]:
    """Render routing sliders and return normalized fractions plus validity."""
    import streamlit as st

    defaults = default_routing_from_config(model_config)
    st.sidebar.header("Cashflow routing")
    st.sidebar.caption("These controls rerun the eight scenarios in memory. They do not save changes to YAML or output files.")

    re_lp = st.sidebar.slider("RE cashflow to LP", 0, 100, int(defaults["re_cashflow"]["lp_distribution_pct"] * 100), 5)
    re_hf = st.sidebar.slider("RE cashflow to HF", 0, 100, int(defaults["re_cashflow"]["hf_reinvestment_pct"] * 100), 5)
    re_reserve = st.sidebar.slider("RE cashflow to reserve", 0, 100, int(defaults["re_cashflow"]["reserve_pct"] * 100), 5)
    hf_lp = st.sidebar.slider("HF harvest to LP", 0, 100, int(defaults["hf_harvest"]["lp_distribution_pct"] * 100), 5)
    hf_hf = st.sidebar.slider("HF harvest to HF", 0, 100, int(defaults["hf_harvest"]["hf_reinvestment_pct"] * 100), 5)
    hf_reserve = st.sidebar.slider("HF harvest to reserve", 0, 100, int(defaults["hf_harvest"]["reserve_pct"] * 100), 5)

    re_total = re_lp + re_hf + re_reserve
    hf_total = hf_lp + hf_hf + hf_reserve
    valid = re_total == 100 and hf_total == 100
    if not valid:
        st.sidebar.warning(f"Routing must total 100%. RE totals {re_total}%; HF totals {hf_total}%. Saved outputs are shown until routing is valid.")
    else:
        st.sidebar.success("Routing totals 100%. Charts use the in-memory rerun.")

    return (
        {
            "re_cashflow": {
                "lp_distribution_pct": re_lp / 100,
                "hf_reinvestment_pct": re_hf / 100,
                "reserve_pct": re_reserve / 100,
            },
            "hf_harvest": {
                "lp_distribution_pct": hf_lp / 100,
                "hf_reinvestment_pct": hf_hf / 100,
                "reserve_pct": hf_reserve / 100,
            },
        },
        valid,
    )


def render_custom_scenario_controls(
    routing: dict[str, dict[str, float]],
    trigger: dict[str, Any],
    routing_valid: bool,
) -> None:
    """Render a custom scenario form and store the result in session state."""
    import streamlit as st

    st.sidebar.header("Custom scenario")
    st.sidebar.caption("Temporary in-memory run. Does not change YAML or saved outputs.")
    with st.sidebar.form("custom_scenario_form"):
        years = st.number_input("Years", min_value=1, max_value=30, value=8, step=1)
        initial_noi_yield_pct = st.number_input("Initial NOI yield (%)", min_value=-20.0, max_value=30.0, value=7.5, step=0.5)
        annual_noi_growth_pct = st.number_input("Annual NOI growth (%)", min_value=-20.0, max_value=30.0, value=2.0, step=0.5)
        annual_nav_appreciation_pct = st.number_input("Annual RE NAV appreciation (%)", min_value=-30.0, max_value=40.0, value=4.0, step=0.5)
        gross_rent_yield_pct = st.number_input("Gross rent yield (%)", min_value=0.0, max_value=40.0, value=12.0, step=0.5)

        hf_allocation_pct = st.slider("Initial HF allocation (%)", 0, 100, 20, 5)
        reserve_allocation_pct = st.slider("Initial reserve allocation (%)", 0, 100, 5, 5)
        re_allocation_pct, allocation_warning = calculate_implied_re_allocation(
            hf_allocation_pct,
            reserve_allocation_pct,
        )
        st.caption(
            "Allocation: "
            f"HF {hf_allocation_pct}% + "
            f"Reserve {reserve_allocation_pct}% + "
            f"RE {re_allocation_pct}% = "
            f"{hf_allocation_pct + reserve_allocation_pct + re_allocation_pct}%"
        )
        if allocation_warning:
            st.warning(allocation_warning)

        hf_harvest_rate_pct = st.slider("HF positive return harvest rate (%)", 0, 100, 50, 5)
        re_liquidity_pct = st.slider("RE refinance/sale capacity (% of RE NAV)", 0, 100, 25, 5)
        hf_returns_text = st.text_input("HF annual returns, % comma-separated", value="20, 15, 10, 8, 6, 6, 6, 6")

        submitted = st.form_submit_button("Run custom scenario")

    if not submitted:
        return
    if not routing_valid:
        st.sidebar.error("Fix routing totals before running the custom scenario.")
        return
    if allocation_warning:
        st.sidebar.error("HF allocation plus reserve allocation cannot exceed 100%.")
        return

    try:
        custom_inputs = {
            "years": int(years),
            "initial_noi_yield": initial_noi_yield_pct / 100,
            "annual_noi_growth": annual_noi_growth_pct / 100,
            "annual_nav_appreciation": annual_nav_appreciation_pct / 100,
            "gross_rent_yield": gross_rent_yield_pct / 100,
            "hf_allocation_pct": hf_allocation_pct / 100,
            "reserve_allocation_pct": reserve_allocation_pct / 100,
            "re_allocation_pct": re_allocation_pct / 100,
            "hf_harvest_rate": hf_harvest_rate_pct / 100,
            "re_liquidity_pct": re_liquidity_pct / 100,
            "hf_returns": parse_hf_returns(hf_returns_text, int(years)),
        }
        custom_cashflows, custom_summary = run_custom_scenario_in_memory(custom_inputs, routing, trigger)
    except Exception as exc:
        st.sidebar.error(f"Custom scenario failed: {exc}")
        return

    st.session_state["custom_cashflows"] = custom_cashflows
    st.session_state["custom_summary"] = custom_summary
    st.sidebar.success("Custom scenario is available in the scenario selector.")


def calculate_implied_re_allocation(hf_allocation_pct: int, reserve_allocation_pct: int) -> tuple[int, str | None]:
    """Return the RE allocation required for the three sleeves to total 100%.

    If HF plus reserve exceeds 100%, RE cannot be negative in the model, so the
    displayed RE allocation is clipped to zero and a warning is returned.
    """
    implied_re = 100 - hf_allocation_pct - reserve_allocation_pct
    if implied_re < 0:
        return 0, "HF plus reserve exceeds 100%, so no valid RE allocation is possible."
    return implied_re, None


def append_custom_scenario_if_available(cashflows: pd.DataFrame, summary: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Append the session's custom scenario result, replacing any prior copy."""
    import streamlit as st

    custom_cashflows = st.session_state.get("custom_cashflows")
    custom_summary = st.session_state.get("custom_summary")
    if custom_cashflows is None or custom_summary is None:
        return cashflows, summary

    cashflows = cashflows[cashflows["scenario"] != "custom_dashboard_scenario"]
    summary = summary[summary["scenario"] != "custom_dashboard_scenario"]
    return (
        pd.concat([cashflows, custom_cashflows], ignore_index=True),
        pd.concat([summary, custom_summary], ignore_index=True),
    )


def run_deal_scenario_in_memory(
    deal_inputs: dict[str, Any],
    fund_inputs: dict[str, Any],
    routing: dict[str, dict[str, float]],
    trigger: dict[str, Any],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run a bottom-up single-deal scenario from browser form inputs without writing any files."""
    from src.config_loader import load_inputs
    from src.deal_types import (
        DealAcquisition,
        DealCapex,
        DealCapitalStack,
        DealConfig,
        DealDebt,
        DealOperations,
        DealRefinance,
        DealSet,
        DealValuation,
    )
    from src.engine import result_dicts, run_scenario
    from src.model_types import ModelConfig, Scenario

    # Build deal object from form inputs
    refi_years = [int(y.strip()) for y in deal_inputs["refi_target_years"].split(",") if y.strip().isdigit()]
    annual_capex = {}
    for yr, amt in enumerate([
        deal_inputs["capex_y1"], deal_inputs["capex_y2"],
        deal_inputs["capex_y3"], deal_inputs["capex_y4"],
    ], start=1):
        if amt > 0:
            annual_capex[yr] = amt

    deal = DealConfig(
        enabled=True,
        acquisition_year=1,
        description="Custom deal — configured via browser form.",
        acquisition=DealAcquisition(
            asset_value=deal_inputs["purchase_price"],
            value_type="purchase_price",
            purchase_price=deal_inputs["purchase_price"],
            new_equity_required=deal_inputs["new_equity_required"],
        ),
        capital_stack=DealCapitalStack(
            assumed_debt=deal_inputs["assumed_debt"],
            assumed_liabilities=deal_inputs["assumed_liabilities"],
        ),
        operations=DealOperations(
            current_noi=deal_inputs["current_noi"],
            stabilized_noi=deal_inputs["stabilized_noi"],
            years_to_stabilization=deal_inputs["years_to_stabilization"],
            annual_noi_growth_after_stabilization=deal_inputs["noi_growth_post_stab"],
        ),
        debt=DealDebt(
            interest_rate=deal_inputs["debt_rate"],
            maturity_year=deal_inputs["debt_maturity_year"],
            amortization_type="interest_only",
        ),
        capex=DealCapex(
            annual_capex=annual_capex,
            recurring_capex_pct_of_noi=deal_inputs["recurring_capex_pct"],
        ),
        valuation=DealValuation(
            method="growth",
            annual_value_growth=deal_inputs["annual_value_growth"],
        ),
        refinance=DealRefinance(
            enabled=bool(refi_years),
            target_years=refi_years,
            refi_ltv=deal_inputs["refi_ltv"],
            refi_costs_pct=deal_inputs["refi_costs_pct"],
            proceeds_use="fund_liquidity",
        ),
    )
    custom_deals = DealSet(deals={"custom_deal": deal})

    # Build model config
    config, _, _ = load_inputs(ROOT / "inputs")
    config_data = config.model_dump()
    config_data["model"]["initial_lp_capital"] = fund_inputs["lp_capital"]
    config_data["waterfall"]["lp_hurdle_moic"] = fund_inputs["lp_hurdle_moic"]
    config_data["cashflow_routing"] = {
        "re_cashflow": routing["re_cashflow"],
        "hf_harvest": routing["hf_harvest"],
    }
    config_data["hurdle_completion_trigger"] = trigger
    rerun_config = ModelConfig.model_validate(config_data)

    years = fund_inputs["years"]
    hf_returns = parse_hf_returns(fund_inputs["hf_returns_text"], years)

    scenario = Scenario.model_validate({
        "description": "Custom deal scenario — browser form input.",
        "years": years,
        "real_estate_model": {"mode": "bottom_up"},
        "real_estate": {
            "initial_noi_yield": 0.055,
            "annual_noi_growth": deal_inputs["noi_growth_post_stab"],
            "annual_nav_appreciation": deal_inputs["annual_value_growth"],
            "gross_rent_yield": 0.10,
        },
        "hedge_fund": {"annual_returns": hf_returns},
        "cashflow_routing": {
            "enabled": True,
            "re_cashflow": routing["re_cashflow"],
            "hf_harvest": routing["hf_harvest"],
        },
    })

    result = run_scenario("custom_dashboard_scenario", scenario, rerun_config, custom_deals)
    summaries, cashflows, _, _ = result_dicts([result])
    summary_df = normalize_numeric_columns(pd.DataFrame(summaries))
    cashflow_df = normalize_numeric_columns(pd.DataFrame(cashflows))
    summary_df["scenario_display"] = summary_df["scenario"].map(display_name)
    cashflow_df["scenario_display"] = cashflow_df["scenario"].map(display_name)
    return cashflow_df, summary_df


def render_configure_tab(
    routing: dict[str, dict[str, float]],
    trigger: dict[str, Any],
    cashflows: pd.DataFrame,
) -> None:
    """Render the Configure & Run tab — a full bottom-up deal form in the main content area."""
    import streamlit as st

    st.header("Configure & Run a Custom Deal")
    st.write(
        "Enter deal and fund assumptions below. The model runs in-memory — nothing is saved to YAML or output files. "
        "Results appear in the Scenario Explorer and Simulator tabs as the 'Custom' scenario."
    )

    with st.form("configure_run_form"):

        # ── Deal assumptions ──────────────────────────────────────────────────
        st.subheader("The deal")
        d1, d2, d3 = st.columns(3)
        with d1:
            purchase_price = st.number_input("Purchase price ($)", min_value=0, value=23_000_000, step=100_000, format="%d")
            assumed_debt = st.number_input("Assumed / new debt ($)", min_value=0, value=16_000_000, step=100_000, format="%d")
            assumed_liabilities = st.number_input("Assumed liabilities ($)", min_value=0, value=2_500_000, step=50_000, format="%d")
        with d2:
            current_noi = st.number_input("Current NOI ($)", min_value=0, value=1_278_000, step=10_000, format="%d")
            stabilized_noi = st.number_input("Stabilised NOI ($)", min_value=0, value=2_150_000, step=10_000, format="%d")
            years_to_stab = st.number_input("Years to stabilisation", min_value=0, max_value=10, value=4, step=1)
        with d3:
            debt_rate_pct = st.number_input("Debt interest rate (%)", min_value=0.0, max_value=20.0, value=7.5, step=0.25)
            debt_maturity = st.number_input("Debt maturity (year)", min_value=1, max_value=20, value=5, step=1)
            noi_growth_pct = st.number_input("NOI growth post-stabilisation (%/yr)", min_value=-10.0, max_value=20.0, value=3.0, step=0.5)

        st.divider()
        st.markdown("**Capex schedule**")
        cx1, cx2, cx3, cx4, cx5 = st.columns(5)
        with cx1:
            capex_y1 = st.number_input("Year 1 ($)", min_value=0, value=500_000, step=10_000, format="%d")
        with cx2:
            capex_y2 = st.number_input("Year 2 ($)", min_value=0, value=400_000, step=10_000, format="%d")
        with cx3:
            capex_y3 = st.number_input("Year 3 ($)", min_value=0, value=250_000, step=10_000, format="%d")
        with cx4:
            capex_y4 = st.number_input("Year 4 ($)", min_value=0, value=150_000, step=10_000, format="%d")
        with cx5:
            recurring_capex_pct = st.number_input("Recurring (% of NOI)", min_value=0.0, max_value=20.0, value=4.0, step=0.5)

        st.divider()
        st.markdown("**Valuation & refinance**")
        v1, v2, v3, v4 = st.columns(4)
        with v1:
            annual_value_growth_pct = st.number_input("Annual value growth (%)", min_value=-20.0, max_value=30.0, value=3.0, step=0.5)
        with v2:
            refi_target_years_str = st.text_input("Refi target years (comma-separated)", value="4, 7")
        with v3:
            refi_ltv_pct = st.number_input("Refi LTV (%)", min_value=0.0, max_value=90.0, value=70.0, step=5.0)
        with v4:
            refi_costs_pct = st.number_input("Refi costs (%)", min_value=0.0, max_value=10.0, value=2.5, step=0.25)

        # ── Fund structure ────────────────────────────────────────────────────
        st.subheader("Fund structure")
        f1, f2, f3, f4 = st.columns(4)
        with f1:
            lp_capital = st.number_input("LP capital ($)", min_value=100_000, value=10_000_000, step=100_000, format="%d")
        with f2:
            lp_hurdle_moic = st.number_input("LP hurdle (x MOIC)", min_value=1.0, max_value=5.0, value=2.0, step=0.25)
        with f3:
            years = st.number_input("Model horizon (years)", min_value=1, max_value=30, value=20, step=1)
        with f4:
            hf_returns_text = st.text_input("HF annual returns (% comma-separated)", value="13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13")

        st.markdown("**Cashflow routing**")
        r1, r2, r3 = st.columns(3)
        with r1:
            re_lp = st.number_input("RE cashflow to LP (%)", min_value=0, max_value=100, value=int(routing["re_cashflow"]["lp_distribution_pct"] * 100), step=5)
        with r2:
            re_hf = st.number_input("RE cashflow to HF (%)", min_value=0, max_value=100, value=int(routing["re_cashflow"]["hf_reinvestment_pct"] * 100), step=5)
        with r3:
            re_res = st.number_input("RE cashflow to reserve (%)", min_value=0, max_value=100, value=int(routing["re_cashflow"]["reserve_pct"] * 100), step=5)

        routing_total = re_lp + re_hf + re_res
        if routing_total != 100:
            st.warning(f"Routing must total 100%. Currently {routing_total}%.")

        new_equity_required = purchase_price - assumed_debt - assumed_liabilities
        st.caption(f"Implied equity required: ${new_equity_required:,.0f} (purchase price minus debt minus liabilities)")

        submitted = st.form_submit_button("Run scenario", type="primary")

    if not submitted:
        # Show download button for any existing custom results
        custom_cf = st.session_state.get("custom_cashflows")
        if custom_cf is not None:
            st.success("Custom scenario results are loaded. Switch to Explorer or Simulator to view them.")
            csv_bytes = custom_cf.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download results as CSV",
                data=csv_bytes,
                file_name="custom_scenario_cashflows.csv",
                mime="text/csv",
            )
        return

    if routing_total != 100:
        st.error("Fix routing total before running.")
        return

    custom_routing = {
        "re_cashflow": {
            "lp_distribution_pct": re_lp / 100,
            "hf_reinvestment_pct": re_hf / 100,
            "reserve_pct": re_res / 100,
        },
        "hf_harvest": routing["hf_harvest"],
    }

    deal_inputs = {
        "purchase_price": float(purchase_price),
        "assumed_debt": float(assumed_debt),
        "assumed_liabilities": float(assumed_liabilities),
        "new_equity_required": max(float(new_equity_required), 0.0),
        "current_noi": float(current_noi),
        "stabilized_noi": float(stabilized_noi),
        "years_to_stabilization": int(years_to_stab),
        "noi_growth_post_stab": noi_growth_pct / 100,
        "debt_rate": debt_rate_pct / 100,
        "debt_maturity_year": int(debt_maturity),
        "capex_y1": float(capex_y1),
        "capex_y2": float(capex_y2),
        "capex_y3": float(capex_y3),
        "capex_y4": float(capex_y4),
        "recurring_capex_pct": recurring_capex_pct / 100,
        "annual_value_growth": annual_value_growth_pct / 100,
        "refi_target_years": refi_target_years_str,
        "refi_ltv": refi_ltv_pct / 100,
        "refi_costs_pct": refi_costs_pct / 100,
    }
    fund_inputs = {
        "lp_capital": float(lp_capital),
        "lp_hurdle_moic": float(lp_hurdle_moic),
        "years": int(years),
        "hf_returns_text": hf_returns_text,
    }

    with st.spinner("Running scenario..."):
        try:
            custom_cashflows, custom_summary = run_deal_scenario_in_memory(
                deal_inputs, fund_inputs, custom_routing, trigger
            )
        except Exception as exc:
            st.error(f"Scenario failed: {exc}")
            return

    st.session_state["custom_cashflows"] = custom_cashflows
    st.session_state["custom_summary"] = custom_summary

    hurdle_row = custom_summary.iloc[0]
    achieved = str(hurdle_row.get("lp_hurdle_achieved", "False")).lower() == "true"
    year_h = hurdle_row.get("year_hurdle_achieved", "")
    cash_moic = hurdle_row.get("lp_cash_moic", 0)

    if achieved and year_h:
        st.success(f"LP 2x hurdle achieved in Year {int(float(year_h))}. Cash MOIC: {cash_moic:.2f}x. Switch to Simulator to walk through it.")
    else:
        st.warning(f"LP hurdle not achieved within {int(years)} years. Cash MOIC: {cash_moic:.2f}x. Switch to Explorer to investigate.")

    csv_bytes = custom_cashflows.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download results as CSV",
        data=csv_bytes,
        file_name="custom_scenario_cashflows.csv",
        mime="text/csv",
    )


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
        if "hurdle_trigger_executed" in df.columns and bool(df["hurdle_trigger_executed"].fillna(False).any()):
            trigger_year = int(df[df["hurdle_trigger_executed"].fillna(False)]["year"].iloc[0])
            fig.add_vline(x=trigger_year, line_dash="dash", line_color="#b00020", row=row, col=col)

    fig.update_yaxes(range=[0, y_max * 1.08], tickprefix="$", tickformat="~s")
    fig.update_xaxes(title_text="Year")
    style_chart_layout(fig, "LP cash versus economic value over time.", selected, height=multi_panel_chart_height(scenarios, selected))
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

    style_chart_layout(fig, "Where the cash came from each year.", selected, barmode="relative", height=multi_panel_chart_height(scenarios, selected))
    fig.update_yaxes(range=[min(0, -y_max * 0.15), y_max * 1.15], tickprefix="$", tickformat="~s")
    fig.update_xaxes(title_text="Year")
    return fig


def build_routing_chart(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None, notes: list[str]):
    """Stacked bar chart showing where generated cash was routed."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    required = ["scenario", "year", "total_cash_distributed", "total_cash_reinvested", "total_cash_reserved"]
    if not require_columns(cashflows, required, "Cashflow routing chart", notes):
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
        ("total_cash_distributed", "LP distributions", "#2f6f95"),
        ("total_cash_reinvested", "HF reinvestment", "#4c78a8"),
        ("total_cash_reserved", "Reserve allocation", "#f58518"),
    ]
    y_max = float(cashflows[[name for name, _label, _color in components]].sum(axis=1).max() or 0)
    for index, scenario in enumerate(scenarios):
        row, col = panel_position(index, cols)
        df = cashflows[cashflows["scenario"] == scenario].sort_values("year")
        for column, label, color in components:
            fig.add_trace(
                go.Bar(x=df["year"], y=df[column], name=label, marker_color=color, showlegend=index == 0),
                row=row,
                col=col,
            )
    style_chart_layout(fig, "Annual cashflow routing.", selected, barmode="stack", height=multi_panel_chart_height(scenarios, selected))
    fig.update_yaxes(range=[0, y_max * 1.15], tickprefix="$", tickformat="~s")
    fig.update_xaxes(title_text="Year")
    return fig


def build_trigger_funding_chart(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None, notes: list[str]):
    """Show active hurdle trigger funding sources when a trigger executes."""
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    required = [
        "scenario",
        "year",
        "trigger_cash_from_retained_cash",
        "trigger_cash_from_reserve",
        "trigger_cash_from_hf_liquidation",
        "trigger_cash_from_refi",
        "trigger_cash_from_re_sale",
    ]
    if not require_columns(cashflows, required, "Trigger funding chart", notes):
        return None

    scenarios = [selected] if selected else scenario_order(summary)
    rows, cols = panel_shape(scenarios)
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[display_name(s) for s in scenarios])
    source_columns = {
        "trigger_cash_from_retained_cash": ("Retained cash", "#4c78a8"),
        "trigger_cash_from_reserve": ("Reserve", "#f58518"),
        "trigger_cash_from_hf_liquidation": ("HF liquidation", "#54a24b"),
        "trigger_cash_from_refi": ("Refi proceeds", "#e45756"),
        "trigger_cash_from_re_sale": ("RE sale", "#b279a2"),
    }
    for index, scenario in enumerate(scenarios):
        row_index, col_index = panel_position(index, cols)
        scenario_df = cashflows[cashflows["scenario"] == scenario].sort_values("year")
        for column, (label, color) in source_columns.items():
            fig.add_trace(
                go.Bar(
                    x=scenario_df["year"],
                    y=scenario_df[column],
                    name=label,
                    marker_color=color,
                    showlegend=index == 0,
                    hovertemplate=f"{label}: %{{y:$,.0f}}<extra></extra>",
                ),
                row=row_index,
                col=col_index,
            )

    max_value = max(float(cashflows[column].max() or 0.0) for column in source_columns) if not cashflows.empty else 0.0
    fig.update_yaxes(range=[0, max_value * 1.08 if max_value > 0 else 1], tickprefix="$", tickformat="~s")
    style_chart_layout(fig, "Trigger funding source breakdown.", selected, barmode="stack", height=multi_panel_chart_height(scenarios, selected))
    return fig


def build_single_line_chart(
    cashflows: pd.DataFrame,
    summary: pd.DataFrame,
    selected: str | None,
    notes: list[str],
    column: str,
    title: str,
    label: str,
    color: str,
):
    """Reusable small-multiple line chart for a single annual metric."""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    if not require_columns(cashflows, ["scenario", "year", column], title, notes):
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
    y_max = float(cashflows[column].max() or 0)
    for index, scenario in enumerate(scenarios):
        row, col = panel_position(index, cols)
        df = cashflows[cashflows["scenario"] == scenario].sort_values("year")
        fig.add_trace(
            go.Scatter(x=df["year"], y=df[column], mode="lines+markers", name=label, line=dict(color=color), showlegend=index == 0),
            row=row,
            col=col,
        )
    style_chart_layout(fig, title, selected, height=multi_panel_chart_height(scenarios, selected))
    fig.update_yaxes(range=[0, y_max * 1.12], tickprefix="$", tickformat="~s")
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

    style_chart_layout(fig, "Where the value lived each year.", selected, height=multi_panel_chart_height(scenarios, selected))
    fig.update_yaxes(range=[0, y_max * 1.08], tickprefix="$", tickformat="~s")
    fig.update_xaxes(title_text="Year")
    return fig


def panel_shape(scenarios: list[str]) -> tuple[int, int]:
    if len(scenarios) == 1:
        return 1, 1
    # The base presentation has eight scenarios, which fits cleanly in 2x4.
    # A custom dashboard scenario adds a ninth panel, so calculate rows
    # dynamically instead of assuming the base scenario count.
    cols = 4
    rows = math.ceil(len(scenarios) / cols)
    return rows, cols


def panel_position(index: int, cols: int) -> tuple[int, int]:
    return (index // cols) + 1, (index % cols) + 1


def chart_height(selected: str | None) -> int:
    return 560 if selected else 440


def multi_panel_chart_height(scenarios: list[str], selected: str | None) -> int:
    """Scale chart height with the number of subplot rows."""
    if selected:
        return chart_height(selected)
    rows, _ = panel_shape(scenarios)
    return max(880, rows * 420)


def style_chart_layout(fig: Any, title: str, selected: str | None, **extra_layout: Any) -> None:
    """Apply consistent light chart styling and title spacing.

    Plotly subplot titles sit inside the plot area by default. The extra top
    margin and annotation shift keep the main chart title and per-panel titles
    from colliding on Streamlit's responsive canvas.
    """
    fig.update_layout(
        title=dict(text=title, y=0.985, x=0.01, xanchor="left"),
        height=extra_layout.pop("height", chart_height(selected)),
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


def render_routing_summary_cards(summary_row: pd.Series) -> None:
    """Render routing-focused headline metrics for single-scenario mode."""
    import streamlit as st

    columns = st.columns(6)
    cards = [
        ("Years to LP 1x", year_label(summary_row.get("years_until_lp_1x_cash_return")), "Cash distributions reach invested capital."),
        ("Years to LP 2x", year_label(summary_row.get("years_until_lp_2x_cash_return")), "Cash distributions reach the hurdle."),
        ("Cash distributed", format_money(summary_row.get("total_distributed_to_lp")), "Total cash paid to LP."),
        ("Cash reinvested", format_money(summary_row.get("total_reinvested_into_hf")), "Generated cash routed back to HF."),
        ("Reserve built", format_money(summary_row.get("total_added_to_reserve")), "Generated cash routed to reserve."),
        ("Profile type", str(summary_row.get("lp_cashflow_profile_type", "n/a")), "Timing shape of LP cashflows."),
    ]
    for column, (label, value, caption) in zip(columns, cards):
        with column:
            st.metric(label, value)
            st.caption(caption)


def render_trigger_summary_cards(summary_row: pd.Series) -> None:
    """Render active hurdle trigger metrics for single-scenario mode."""
    import streamlit as st

    columns = st.columns(5)
    cards = [
        ("Trigger executed", "yes" if bool(summary_row.get("hurdle_trigger_executed", False)) else "no", "Active monetization used."),
        ("Trigger year", year_label(summary_row.get("hurdle_trigger_year")), "Year active trigger fired."),
        ("HF used", format_money(summary_row.get("total_trigger_cash_from_hf_liquidation")), "HF liquidated for LP."),
        ("Refi used", format_money(summary_row.get("total_trigger_cash_from_refi")), "Refi proceeds for LP."),
        ("Trigger shortfall", format_money(summary_row.get("lp_hurdle_shortfall_after_final_trigger")), "Remaining if attempted but short."),
    ]
    for column, (label, value, caption) in zip(columns, cards):
        with column:
            st.metric(label, value)
            st.caption(caption)


def year_label(value: Any) -> str:
    if pd.isna(value) or value == "":
        return "not reached"
    return f"year {int(float(value))}"


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
                "cashflow_routing": model_config.get("cashflow_routing", {}),
                "lp_cash_yield_policy": model_config.get("lp_cash_yield_policy", {}),
                "reserve": model_config.get("reserve", {}),
                "flag_thresholds": model_config.get("flag_thresholds", {}),
                "gp_survivability": model_config.get("gp_survivability", {}),
                "hurdle_completion_trigger": model_config.get("hurdle_completion_trigger", {}),
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
            rows.append({"assumption": friendly_assumption_name(path), "value": friendly_assumption_list_value(path, value)})
        else:
            rows.append({"assumption": friendly_assumption_name(path), "value": friendly_assumption_value(path, value)})

    walk(data, prefix)
    return pd.DataFrame(rows)


ASSUMPTION_LABELS = {
    "description": "Scenario description",
    "years": "Model years",
    "real_estate.initial_noi_yield": "Initial real estate NOI yield",
    "real_estate.annual_noi_growth": "Annual NOI growth",
    "real_estate.annual_nav_appreciation": "Annual real estate NAV appreciation",
    "real_estate.gross_rent_yield": "Gross rent yield",
    "hedge_fund.annual_returns": "Annual hedge fund returns",
    "model.currency": "Currency",
    "model.periods_per_year": "Periods per year",
    "model.max_years": "Maximum model years",
    "model.initial_lp_capital": "Initial LP capital",
    "model.gp_co_investment": "GP co-investment",
    "allocation.method": "Allocation method",
    "allocation.hedge_fund_allocation_pct": "Initial hedge fund allocation",
    "allocation.real_estate_allocation_pct": "Initial real estate allocation",
    "allocation.reserve_allocation_pct": "Initial reserve allocation",
    "waterfall.lp_hurdle_moic": "LP hurdle multiple",
    "waterfall.lp_receives_100_percent_until_hurdle": "LP receives all distributions before hurdle",
    "waterfall.gp_receives_residual_after_lp_hurdle": "GP receives residual after LP hurdle",
    "waterfall.include_unrealized_nav_in_hurdle_test": "Include unrealised NAV in economic hurdle test",
    "waterfall.require_liquidity_for_lp_redemption": "Require liquidity for LP extinguishment",
    "liquidity.hf_liquidation_allowed": "HF liquidation allowed",
    "liquidity.hf_liquidation_capacity_pct_per_year": "Annual HF liquidation capacity",
    "liquidity.reserve_liquidation_capacity_pct_per_year": "Annual reserve liquidation capacity",
    "liquidity.real_estate_liquidation_capacity_pct_per_year": "Annual real estate liquidation capacity",
    "liquidity.max_refinance_or_sale_capacity_pct_of_re_nav": "Maximum refinance/sale capacity of RE NAV",
    "fees.real_estate_asset_management_fee.enabled": "Real estate asset management fee enabled",
    "fees.real_estate_asset_management_fee.rate": "Real estate asset management fee rate",
    "fees.real_estate_asset_management_fee.basis": "Real estate asset management fee basis",
    "fees.hedge_fund_fees.model_as_net_returns": "HF returns modelled net of fees",
    "fees.hedge_fund_fees.management_fee_rate": "HF management fee rate",
    "fees.hedge_fund_fees.performance_fee_rate": "HF performance fee rate",
    "distribution_policy.distribute_re_cashflow_annually": "Distribute RE cashflow annually",
    "distribution_policy.distribute_hf_realized_gains_annually": "Distribute harvested HF gains annually",
    "distribution_policy.hf_positive_return_harvest_rate": "HF positive return harvest rate",
    "distribution_policy.retain_cash_until_hurdle_redemption": "Retain cash until LP hurdle extinguishment",
    "cashflow_routing.re_cashflow.lp_distribution_pct": "RE cashflow routed to LP",
    "cashflow_routing.re_cashflow.hf_reinvestment_pct": "RE cashflow reinvested into HF",
    "cashflow_routing.re_cashflow.reserve_pct": "RE cashflow routed to reserve",
    "cashflow_routing.hf_harvest.lp_distribution_pct": "HF harvest routed to LP",
    "cashflow_routing.hf_harvest.hf_reinvestment_pct": "HF harvest reinvested into HF",
    "cashflow_routing.hf_harvest.reserve_pct": "HF harvest routed to reserve",
    "lp_cash_yield_policy.enabled": "LP cash yield policy enabled",
    "lp_cash_yield_policy.target_annual_yield_on_unreturned_capital": "Target annual LP cash yield on unreturned capital",
    "lp_cash_yield_policy.source_priority": "LP cash yield source priority",
    "lp_cash_yield_policy.reduce_lp_hurdle": "LP cash yield reduces hurdle",
    "reserve.annual_return": "Reserve annual return",
    "gp_survivability.first_n_years": "GP survivability test years",
    "gp_survivability.minimum_cumulative_fees": "Minimum GP cumulative fees",
    "gp_survivability.minimum_average_annual_fees": "Minimum GP average annual fees",
    "hurdle_completion_trigger.enabled": "Active hurdle completion trigger enabled",
    "hurdle_completion_trigger.trigger_when_economic_hurdle_passed": "Trigger requires economic hurdle passed",
    "hurdle_completion_trigger.minimum_lp_cash_moic_before_trigger": "Minimum LP cash MOIC before trigger",
    "hurdle_completion_trigger.max_hf_liquidation_pct": "Maximum HF liquidation for trigger",
    "hurdle_completion_trigger.max_refi_pct_of_re_nav": "Maximum refinance proceeds for trigger",
    "hurdle_completion_trigger.allow_retained_cash_use": "Trigger can use retained cash",
    "hurdle_completion_trigger.allow_reserve_use": "Trigger can use reserve",
    "hurdle_completion_trigger.allow_hf_liquidation": "Trigger can use HF liquidation",
    "hurdle_completion_trigger.allow_refi": "Trigger can use refinance proceeds",
    "hurdle_completion_trigger.allow_partial_re_sale": "Trigger can use partial real estate sale",
    "hurdle_completion_trigger.max_partial_re_sale_pct_of_re_nav": "Maximum partial RE sale for trigger",
    "hurdle_completion_trigger.execute_only_if_lp_fully_redeemed": "Trigger only executes if LP fully redeemed",
}


def friendly_assumption_name(path: str) -> str:
    """Convert a dotted YAML path into a presentation-friendly label."""
    if path in ASSUMPTION_LABELS:
        return ASSUMPTION_LABELS[path]
    words = path.replace("_pct", " percentage").replace("_", " ").replace(".", " - ")
    return words[:1].upper() + words[1:]


def friendly_assumption_value(path: str, value: Any) -> str:
    """Format assumption values without hiding the underlying meaning."""
    if isinstance(value, bool):
        return "Yes" if value else "No"
    if isinstance(value, (int, float)) and should_format_as_percent(path):
        return f"{float(value):.1%}"
    if isinstance(value, (int, float)) and any(token in path for token in ["capital", "fees", "threshold"]):
        return format_money(value)
    return str(value)


def friendly_assumption_list_value(path: str, values: list[Any]) -> str:
    """Format list assumptions, especially annual return series, for readability."""
    if values and all(isinstance(item, (int, float)) for item in values) and should_format_as_percent(path):
        return ", ".join(f"{float(item):.1%}" for item in values)
    return ", ".join(str(item) for item in values)


def should_format_as_percent(path: str) -> bool:
    percent_tokens = ["yield", "growth", "appreciation", "pct", "rate", "allocation", "capacity", "return"]
    return any(token in path for token in percent_tokens) and "moic" not in path


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


def comparison_table(summary: pd.DataFrame) -> pd.DataFrame:
    """Return scenario comparison with lawyer-readable column names."""
    source_columns = {
        "scenario_display": "Scenario",
        "lp_cash_moic": "LP cash multiple",
        "lp_cash_irr": "LP cash IRR",
        "years_until_lp_2x_cash_return": "Years to LP 2x cash",
        "hurdle_trigger_executed": "Trigger executed",
        "total_trigger_cash_from_hf_liquidation": "HF liquidation used",
        "total_trigger_cash_from_refi": "Refi used",
        "gp_residual_nav": "GP residual NAV",
        "liquidity_constrained": "Liquidity constrained",
        "lp_cashflow_profile_type": "LP cashflow profile",
    }
    available = [column for column in source_columns if column in summary.columns]
    return summary[available].rename(columns=source_columns).sort_values("LP cash multiple")


def comparison_column_config() -> dict[str, Any]:
    """Streamlit column config with tooltips for scenario comparison."""
    import streamlit as st

    return {
        "Scenario": st.column_config.TextColumn("Scenario", help="Input-style scenario name used for presentation."),
        "LP cash multiple": st.column_config.NumberColumn(
            "LP cash multiple",
            help="Actual cumulative cash distributions to LP divided by initial LP capital.",
            format="%.2fx",
        ),
        "LP cash IRR": st.column_config.NumberColumn(
            "LP cash IRR",
            help="IRR using only actual LP cash distributions. No terminal NAV is included.",
            format="%.1f%%",
        ),
        "Years to LP 2x cash": st.column_config.NumberColumn(
            "Years to LP 2x cash",
            help="First model year in which cumulative actual LP cash distributions reach the 2x hurdle. Blank means not reached.",
            format="%d",
        ),
        "Trigger executed": st.column_config.CheckboxColumn(
            "Trigger executed",
            help="True when the active hurdle completion trigger was used to finish LP redemption.",
        ),
        "HF liquidation used": st.column_config.NumberColumn(
            "HF liquidation used",
            help="Hedge fund NAV liquidated by the active hurdle completion trigger.",
            format="$%d",
        ),
        "Refi used": st.column_config.NumberColumn(
            "Refi used",
            help="Refinance proceeds generated by the active hurdle completion trigger. These do not reduce RE NAV in this model version.",
            format="$%d",
        ),
        "GP residual NAV": st.column_config.NumberColumn(
            "GP residual NAV",
            help="Residual fund NAV accruing to GP after LP interests are extinguished.",
            format="$%d",
        ),
        "Liquidity constrained": st.column_config.CheckboxColumn(
            "Liquidity constrained",
            help="True when fund value cleared the hurdle on paper but available cash/liquidity was insufficient for LP extinguishment.",
        ),
        "LP cashflow profile": st.column_config.TextColumn(
            "LP cashflow profile",
            help="Automatic timing classification: backend-heavy, moderate yield, or aggressive distribution.",
        ),
    }


def render_scenario_comparison(summary: pd.DataFrame) -> None:
    """Render the comparison table with readable labels and hover help."""
    import streamlit as st

    table = comparison_table(summary)
    if table.empty:
        return
    if "LP cash IRR" in table.columns:
        table["LP cash IRR"] = table["LP cash IRR"] * 100
    st.subheader("Scenario comparison")
    st.dataframe(
        table,
        width="stretch",
        hide_index=True,
        column_config=comparison_column_config(),
    )


def build_traditional_statement(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None) -> pd.DataFrame:
    """Build a copyable annual cashflow and balance-sheet style table.

    The model output is annual. This presentation table adds a year 0 row from
    the first opening balances, then shows each period's generated cash,
    routing movements, LP distributions, and closing buckets.
    """
    scenarios = [selected] if selected else scenario_order(summary)
    rows: list[dict[str, Any]] = []
    for scenario in scenarios:
        scenario_df = cashflows[cashflows["scenario"] == scenario].sort_values("year")
        if scenario_df.empty:
            continue
        first = scenario_df.iloc[0]
        rows.append(
            {
                "Scenario": display_name(scenario),
                "Year": 0,
                "Opening RE NAV": None,
                "Opening HF NAV": None,
                "Opening reserve": None,
                "Opening retained cash": 0.0,
                "RE cashflow generated": 0.0,
                "HF harvest generated": 0.0,
                "RE cashflow to LP": 0.0,
                "RE cashflow to HF": 0.0,
                "RE cashflow to reserve": 0.0,
                "HF harvest to LP": 0.0,
                "HF harvest to HF": 0.0,
                "HF harvest to reserve": 0.0,
                "Refinance proceeds": 0.0,
                "Refinance liability": 0.0,
                "Trigger retained cash used": 0.0,
                "Trigger reserve used": 0.0,
                "Trigger HF liquidation used": 0.0,
                "Trigger refi used": 0.0,
                "Trigger RE sale used": 0.0,
                "LP distribution": 0.0,
                "Cumulative LP distributions": 0.0,
                "Closing RE NAV": first.get("re_opening_nav", 0.0),
                "Closing HF NAV": first.get("hf_opening_nav", 0.0),
                "Closing reserve": first.get("reserve_opening_nav", 0.0),
                "Closing retained cash": 0.0,
                "Fund NAV": first.get("re_opening_nav", 0.0) + first.get("hf_opening_nav", 0.0) + first.get("reserve_opening_nav", 0.0),
                "Event": "Initial allocation",
            }
        )
        for _, row in scenario_df.iterrows():
            rows.append(
                {
                    "Scenario": display_name(scenario),
                    "Year": int(row.get("year", 0)),
                    "Opening RE NAV": row.get("re_opening_nav"),
                    "Opening HF NAV": row.get("hf_opening_nav"),
                    "Opening reserve": row.get("reserve_opening_nav"),
                    "Opening retained cash": None,
                    "RE cashflow generated": row.get("re_cashflow_generated", row.get("net_re_cashflow", 0.0)),
                    "HF harvest generated": row.get("hf_harvest_generated", row.get("hf_harvest", 0.0)),
                    "RE cashflow to LP": row.get("re_cashflow_to_lp", 0.0),
                    "RE cashflow to HF": row.get("re_cashflow_to_hf", 0.0),
                    "RE cashflow to reserve": row.get("re_cashflow_to_reserve", 0.0),
                    "HF harvest to LP": row.get("hf_harvest_to_lp", 0.0),
                    "HF harvest to HF": row.get("hf_harvest_to_hf", 0.0),
                    "HF harvest to reserve": row.get("hf_harvest_to_reserve", 0.0),
                    "Refinance proceeds": row.get("refinance_proceeds", 0.0),
                    "Refinance liability": row.get("refinance_liability", 0.0),
                    "Trigger retained cash used": row.get("trigger_cash_from_retained_cash", 0.0),
                    "Trigger reserve used": row.get("trigger_cash_from_reserve", 0.0),
                    "Trigger HF liquidation used": row.get("trigger_cash_from_hf_liquidation", 0.0),
                    "Trigger refi used": row.get("trigger_cash_from_refi", 0.0),
                    "Trigger RE sale used": row.get("trigger_cash_from_re_sale", 0.0),
                    "LP distribution": row.get("lp_distribution", 0.0),
                    "Cumulative LP distributions": row.get("lp_cumulative_distribution", 0.0),
                    "Closing RE NAV": row.get("re_closing_nav", 0.0),
                    "Closing HF NAV": row.get("hf_closing_nav", 0.0),
                    "Closing reserve": row.get("reserve_closing_nav", 0.0),
                    "Closing retained cash": row.get("retained_cash", 0.0),
                    "Fund NAV": row.get("fund_nav", 0.0),
                    "Event": row.get("event_flag", ""),
                }
            )
    return pd.DataFrame(rows)


def render_traditional_statement(cashflows: pd.DataFrame, summary: pd.DataFrame, selected: str | None) -> None:
    """Render a bottom-page expander with copyable annual statement data."""
    import streamlit as st

    with st.expander("Traditional cashflow and balance sheet table", expanded=False):
        st.caption(
            "This table starts with the time 0 allocation, then shows annual cash generated, routing between buckets, "
            "LP distributions, and closing balances. Use the table toolbar or select cells to copy data."
        )
        statement = build_traditional_statement(cashflows, summary, selected)
        st.dataframe(format_statement_for_display(statement), width="stretch", hide_index=True)
        st.download_button(
            label="Download statement table CSV",
            data=statement.to_csv(index=False).encode("utf-8"),
            file_name="traditional_cashflow_balance_sheet.csv",
            mime="text/csv",
        )


def format_statement_for_display(statement: pd.DataFrame) -> pd.DataFrame:
    """Render statement numbers as whole dollars with commas for readability."""
    formatted = statement.copy()
    numeric_columns = [
        column
        for column in formatted.columns
        if column not in {"Scenario", "Year", "Event"}
    ]
    for column in numeric_columns:
        formatted[column] = formatted[column].apply(format_statement_number)
    return formatted


def format_statement_number(value: Any) -> str:
    if pd.isna(value):
        return ""
    try:
        return f"{float(value):,.0f}"
    except (TypeError, ValueError):
        return str(value)


def download_cashflows_button(cashflows: pd.DataFrame) -> None:
    import streamlit as st

    st.download_button(
        label="Download raw cashflows CSV",
        data=cashflows.to_csv(index=False).encode("utf-8"),
        file_name="scenario_cashflows.csv",
        mime="text/csv",
    )


def build_nav_composition_pie(row: pd.Series):
    """Render a pie chart of the fund's NAV composition for a specific year."""
    import plotly.graph_objects as go

    components = [
        ("re_closing_nav", "Real Estate"),
        ("hf_closing_nav", "Hedge Fund"),
        ("reserve_closing_nav", "Reserve"),
        ("retained_cash", "Retained Cash"),
    ]
    labels = []
    values = []
    for col, label in components:
        val = float(row.get(col, 0) or 0)
        if val > 0:
            labels.append(label)
            values.append(val)

    if not values:
        return None

    total_nav = sum(values)
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(colors=["#4c78a8", "#72b7b2", "#54a24b", "#f58518"]),
        text=[format_money(v) for v in values],
        textinfo="percent+text+label",
        texttemplate="%{label}<br>%{text} (%{percent})",
        hovertemplate="%{label}: %{value:$,.0f}<extra></extra>"
    )])
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=40),
        height=360,
        showlegend=False,
        title=dict(
            text=f"Total NAV: {format_money(total_nav)}",
            x=0.5,
            xanchor="center",
            font=dict(size=14),
        ),
        annotations=[dict(
            text=format_money(total_nav),
            x=0.5, y=0.5,
            font_size=13,
            showarrow=False,
        )],
    )
    return fig


def build_cashflow_sankey(row: pd.Series):
    """Render a Sankey diagram showing the flow of cash for a specific year."""
    import plotly.graph_objects as go

    # 1. Sources of Cash
    re_cash = float(row.get('re_cashflow_generated', 0) or 0)
    hf_cash = float(row.get('hf_harvest_generated', 0) or 0)
    refi_cash = float(row.get('refinance_proceeds', 0) or 0)
    
    # 2. Destinations of Cash
    lp_dist = float(row.get('total_cash_distributed', 0) or 0)
    hf_reinv = float(row.get('total_cash_reinvested', 0) or 0)
    rs_added = float(row.get('total_cash_reserved', 0) or 0)

    # Threshold for display
    if (re_cash + hf_cash + refi_cash) <= 0:
        return None

    # Node Indices
    # 0: Real Estate, 1: Hedge Fund, 2: Refinance, 3: FUND POOL, 4: LP, 5: HF (Reinvest), 6: Reserve
    
    sources = []
    targets = []
    values = []
    labels = ["Real Estate", "Hedge Fund", "Refinance", "FUND POOL", "LP Distributions", "HF Reinvestment", "Reserve Allocation"]
    colors = ["#4c78a8", "#72b7b2", "#f58518", "#34495e", "#2f6f95", "#4c78a8", "#f58518"]

    # Source -> Pool
    if re_cash > 0:
        sources.append(0); targets.append(3); values.append(re_cash)
    if hf_cash > 0:
        sources.append(1); targets.append(3); values.append(hf_cash)
    if refi_cash > 0:
        sources.append(2); targets.append(3); values.append(refi_cash)

    # Pool -> Destination
    total_out = lp_dist + hf_reinv + rs_added
    if lp_dist > 0:
        sources.append(3); targets.append(4); values.append(lp_dist)
    if hf_reinv > 0:
        sources.append(3); targets.append(5); values.append(hf_reinv)
    if rs_added > 0:
        sources.append(3); targets.append(6); values.append(rs_added)

    # Add pct to destination node labels
    def _pct(v):
        return f" ({v/total_out:.0%})" if total_out > 0 else ""
    labels[4] = f"LP Distributions{_pct(lp_dist)}"
    labels[5] = f"HF Reinvestment{_pct(hf_reinv)}"
    labels[6] = f"Reserve Allocation{_pct(rs_added)}"

    fig = go.Figure(data=[go.Sankey(
        textfont = dict(family="Arial, sans-serif", size=12, color="black"),
        node = dict(
          pad = 20,
          thickness = 30,
          line = dict(color = "black", width = 0.5),
          label = labels,
          color = colors
        ),
        link = dict(
          source = sources,
          target = targets,
          value = values,
          hovertemplate = "Flow: %{value:$,.0f}<extra></extra>",
          color = "rgba(180, 180, 180, 0.4)" # Light grey links for better contrast
        ))])

    fig.update_layout(
        title_text="Yearly Cashflow Routing", 
        font=dict(family="Arial, sans-serif", size=12, color="black"),
        height=400,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig


def render_bridge_item(label: str, value: float, rate: float | None = None, opening: float | None = None, cumulative: float | None = None, note: str | None = None, balance: float | None = None):
    """Render a styled bridge item with yellow background and color-coded text."""
    import streamlit as st
    color = "#1b5e20" if value >= 0 else "#8a1c1c"
    bg = "#fff7e0"

    val_str = format_money(value)
    if value >= 0:
        val_str = f"+{val_str}"

    rate_str = f" ({rate:.1%})" if rate is not None else ""

    st.markdown(
        f"<div style='background:{bg}; padding:10px; border-radius:6px; margin-bottom:8px; border:1px solid #f9e79f;'>"
        f"<div style='color:#7a4b00; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:0.5px;'>{label}</div>"
        f"<div style='color:{color}; font-weight:700; font-size:18px; line-height:1.2;'>{val_str}{rate_str}</div>"
        + (f"<div style='color:#7a4b00; font-size:11px; margin-top:4px;'>Opening: <b>{format_money(opening)}</b></div>" if opening is not None else "")
        + (f"<div style='color:#7a4b00; font-size:11px; margin-top:4px;'>Cumulative: <b>{format_money(cumulative)}</b></div>" if cumulative is not None else "")
        + (f"<div style='color:#7a4b00; font-size:11px; margin-top:4px;'>Balance: <b>{format_money(balance)}</b></div>" if balance is not None else "")
        + (f"<div style='color:#7a4b00; font-size:11px; margin-top:4px; font-style:italic;'>{note}</div>" if note else "")
        + "</div>",
        unsafe_allow_html=True,
    )


def _render_line_item(label: str, value: float) -> None:
    import streamlit as st
    color = "#8a1c1c" if value < 0 else "#1b5e20" if value > 0 else "#555"
    st.markdown(
        f"<div style='display:flex;justify-content:space-between;padding:3px 0;"
        f"border-bottom:1px solid #f0f0f0;font-size:13px;'>"
        f"<span style='color:#444;'>{label}</span>"
        f"<span style='color:{color};font-weight:600;'>{format_money(value)}</span></div>",
        unsafe_allow_html=True,
    )


def render_re_deal_detail(row: pd.Series) -> None:
    """Collapsible real estate deal detail: capital stack and operating cashflow."""
    import streamlit as st

    gross_value = float(row.get("re_gross_asset_value", 0) or 0)
    if gross_value <= 0:
        return
    debt = float(row.get("re_debt_balance", 0) or 0)
    liabilities = float(row.get("re_assumed_liabilities", 0) or 0)
    refi_liability = float(row.get("re_ending_refi_liability", 0) or 0)
    net_equity = gross_value - debt - liabilities - refi_liability
    noi = float(row.get("re_noi", 0) or 0)
    debt_service = float(row.get("re_debt_service", 0) or 0)
    capex = float(row.get("re_capex", 0) or 0)
    net_cf = float(row.get("re_free_cashflow_after_debt_and_capex", 0) or 0)

    with st.expander("Real estate deal detail", expanded=False):
        st.caption(
            "Gross property value, debt, and net equity the fund holds. "
            "The NAV bridge shows net equity change — appreciation on the gross asset is amplified by leverage."
        )
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Capital stack (end of year)**")
            _render_line_item("Property value (gross)", gross_value)
            _render_line_item("Senior debt", -debt)
            _render_line_item("Assumed liabilities", -liabilities)
            if refi_liability > 0:
                _render_line_item("Refinance liability", -refi_liability)
            cf = "#1b5e20" if net_equity >= 0 else "#8a1c1c"
            st.markdown(f"**Fund net equity: <span style='color:{cf};'>{format_money(net_equity)}</span>**", unsafe_allow_html=True)
        with c2:
            if noi > 0 or debt_service > 0:
                st.markdown("**Operating cashflow (this year)**")
                _render_line_item("NOI (rent less operating costs)", noi)
                _render_line_item("Debt service", -debt_service)
                _render_line_item("Capex", -capex)
                cf = "#1b5e20" if net_cf >= 0 else "#8a1c1c"
                st.markdown(f"**Net cashflow: <span style='color:{cf};'>{format_money(net_cf)}</span>**", unsafe_allow_html=True)


def render_event_detail(row: pd.Series, scenario_df: pd.DataFrame, max_hf_liq_pct: float = 0.75) -> None:
    """Events & flags with full numerical working where available."""
    import streamlit as st

    year = int(row.get("year", 0))
    has_event = False

    # Refinance event
    refi_proceeds = float(row.get("re_refi_proceeds_from_deals", 0) or 0)
    if refi_proceeds > 0:
        has_event = True
        gross_value = float(row.get("re_gross_asset_value", 0) or 0)
        existing_debt = float(row.get("re_debt_balance", 0) or 0)
        st.markdown(
            "<div style='background:#e8f5e9;color:#1b5e20;padding:12px;border-radius:6px;margin-bottom:8px;'>"
            f"<b>Refinance event — Year {year}</b><br>"
            f"Property value: <b>{format_money(gross_value)}</b><br>"
            f"Debt capacity (70% LTV): <b>{format_money(gross_value * 0.70)}</b><br>"
            f"Existing debt: <b>{format_money(existing_debt)}</b><br>"
            f"Net proceeds (after costs): <b>{format_money(refi_proceeds)}</b> → held as retained cash<br>"
            f"<span style='font-size:11px;'>Scheduled target year. Proceeds held as dry powder for LP redemption.</span>"
            "</div>", unsafe_allow_html=True,
        )

    # Trigger attempted but insufficient
    trigger_attempted = str(row.get("hurdle_trigger_attempted", "")).lower() == "true"
    trigger_executed = str(row.get("hurdle_trigger_executed", "")).lower() == "true"

    if trigger_attempted and not trigger_executed:
        has_event = True
        remaining_hurdle = float(row.get("lp_remaining_hurdle", 0) or 0)
        hf_nav = float(row.get("hf_closing_nav", 0) or 0)
        retained = float(row.get("retained_cash", 0) or 0)
        reserve = float(row.get("reserve_closing_nav", 0) or 0)
        hf_available = hf_nav * max_hf_liq_pct
        total_available = hf_available + retained + reserve
        shortfall = remaining_hurdle - total_available
        st.markdown(
            "<div style='background:#fff7e0;color:#7a4b00;padding:12px;border-radius:6px;margin-bottom:8px;'>"
            f"<b>LP hurdle trigger attempted — Year {year}</b><br>"
            f"LP still needs: <b>{format_money(remaining_hurdle)}</b><br><br>"
            f"<b>Available liquidity:</b><br>"
            f"HF liquidation ({max_hf_liq_pct:.0%} cap): <b>{format_money(hf_available)}</b><br>"
            f"Retained cash: <b>{format_money(retained)}</b><br>"
            f"Reserve: <b>{format_money(reserve)}</b><br>"
            f"<b>Total available: {format_money(total_available)}</b><br>"
            f"<span style='color:#8a1c1c;'><b>Shortfall: {format_money(shortfall)}</b></span><br>"
            f"<span style='font-size:11px;'>Not enough liquidity this year. Will retry next year.</span>"
            "</div>", unsafe_allow_html=True,
        )

    elif trigger_executed:
        has_event = True
        trigger_retained = float(row.get("trigger_cash_from_retained_cash", 0) or 0)
        trigger_reserve = float(row.get("trigger_cash_from_reserve", 0) or 0)
        trigger_hf = float(row.get("trigger_cash_from_hf_liquidation", 0) or 0)
        trigger_refi = float(row.get("trigger_cash_from_refi", 0) or 0)
        routing_to_lp = float(row.get("re_cashflow_to_lp", 0) or 0)
        total_trigger = trigger_retained + trigger_reserve + trigger_hf + trigger_refi
        total_lp = total_trigger + routing_to_lp

        # LP redemption sources
        lines = ""
        if trigger_retained > 0:
            lines += f"Retained cash: <b>{format_money(trigger_retained)}</b><br>"
        if trigger_reserve > 0:
            lines += f"Reserve: <b>{format_money(trigger_reserve)}</b><br>"
        if trigger_hf > 0:
            lines += f"HF liquidated: <b>{format_money(trigger_hf)}</b><br>"
        if trigger_refi > 0:
            lines += f"Refinance proceeds: <b>{format_money(trigger_refi)}</b><br>"
        if routing_to_lp > 0:
            lines += f"RE cashflow routing (this year): <b>{format_money(routing_to_lp)}</b><br>"

        # GP residual stack
        re_nav = float(row.get("re_closing_nav", 0) or 0)
        refi_liability = float(row.get("re_ending_refi_liability", 0) or 0)
        hf_residual = float(row.get("hf_closing_nav", 0) or 0)
        reserve_residual = float(row.get("reserve_closing_nav", 0) or 0)
        retained_residual = float(row.get("retained_cash", 0) or 0)
        gp_nav = float(row.get("gp_residual_nav", 0) or 0)

        gp_lines = f"RE net equity: <b>{format_money(re_nav)}</b><br>"
        if refi_liability > 0:
            gp_lines += f"Refinance liability: <b>−{format_money(refi_liability)}</b><br>"
        if hf_residual > 0:
            gp_lines += f"HF residual (after liquidation): <b>{format_money(hf_residual)}</b><br>"
        if reserve_residual > 0:
            gp_lines += f"Reserve residual: <b>{format_money(reserve_residual)}</b><br>"
        if retained_residual > 0:
            gp_lines += f"Retained cash residual: <b>{format_money(retained_residual)}</b><br>"

        st.markdown(
            "<div style='background:#e8f5e9;color:#1b5e20;padding:12px;border-radius:6px;margin-bottom:8px;'>"
            f"<b>LP hurdle completed — Year {year}</b><br><br>"
            f"<b>LP redemption sources:</b><br>"
            + lines
            + f"<b>Total paid to LP: {format_money(total_lp)}</b><br><br>"
            f"<b>GP residual NAV: {format_money(gp_nav)}</b><br>"
            + gp_lines
            + "<span style='font-size:11px;'>LP 2.0x hurdle achieved. Remaining fund value belongs to the GP.</span>"
            "</div>", unsafe_allow_html=True,
        )

    # Any other event flags not already rendered above
    event_flag = str(row.get("event_flag", "") or "")
    handled = {"HURDLE_COMPLETION_TRIGGER_EXECUTED", "HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT", "REFINANCE_EVENT_OCCURRED"}
    for part in event_flag.split(";"):
        part = part.strip()
        if part and part not in handled:
            has_event = True
            item = FLAG_TRANSLATIONS.get(part, {"tone": "amber", "text": part.replace("_", " ").title()})
            bg, fg = TONE_STYLES[item["tone"]]
            st.markdown(
                f"<div style='background:{bg};color:{fg};padding:8px 10px;margin:4px 0;"
                f"border-radius:6px;font-size:12px;'>{item['text']}</div>",
                unsafe_allow_html=True,
            )

    if not has_event:
        st.caption("No significant events this year.")


def render_routing_amounts_table(row: pd.Series) -> None:
    """Dollar breakdown of routing destinations below the Sankey."""
    import streamlit as st

    items = [
        ("re_cashflow_to_lp", "RE cashflow → LP distribution"),
        ("re_cashflow_to_hf", "RE cashflow → HF reinvestment"),
        ("re_cashflow_to_reserve", "RE cashflow → Reserve"),
        ("hf_harvest_to_lp", "HF harvest → LP distribution"),
        ("hf_harvest_to_hf", "HF harvest → HF reinvestment"),
        ("hf_harvest_to_reserve", "HF harvest → Reserve"),
    ]
    shown = [(label, float(row.get(col, 0) or 0)) for col, label in items if float(row.get(col, 0) or 0) > 0]
    if not shown:
        return
    st.markdown("**Routing breakdown:**")
    for label, val in shown:
        st.markdown(
            f"<div style='display:flex;justify-content:space-between;padding:3px 6px;"
            f"border-bottom:1px solid #f0f0f0;font-size:13px;'>"
            f"<span style='color:#555;'>{label}</span>"
            f"<span style='font-weight:600;color:#2f6f95;'>{format_money(val)}</span></div>",
            unsafe_allow_html=True,
        )


def render_walkthrough_sidebar(
    selected_scenario: str,
    scenario_assumptions: dict[str, Any],
    model_config: dict[str, Any],
) -> None:
    """Read-only key assumptions panel shown in sidebar during walkthrough mode."""
    import streamlit as st

    st.sidebar.header("Key assumptions")
    st.sidebar.caption("Read-only. Switch off walkthrough mode to adjust routing.")
    scenario = scenario_assumptions.get(selected_scenario, {})
    routing = scenario.get("cashflow_routing", model_config.get("cashflow_routing", {}))
    re_routing = routing.get("re_cashflow", {})
    lp_capital = model_config.get("model", {}).get("initial_lp_capital", 10_000_000)
    hurdle = model_config.get("waterfall", {}).get("lp_hurdle_moic", 2.0)
    hf_returns = scenario.get("hedge_fund", {}).get("annual_returns", [])
    hf_label = friendly_assumption_list_value("annual_returns", hf_returns) if hf_returns else "n/a"
    items = [
        ("LP capital", format_money(lp_capital)),
        ("LP hurdle", f"{hurdle:.1f}x = {format_money(lp_capital * hurdle)}"),
        ("HF annual return", hf_label),
        ("RE cashflow to LP", f"{re_routing.get('lp_distribution_pct', 0):.0%}"),
        ("RE cashflow to HF", f"{re_routing.get('hf_reinvestment_pct', 0):.0%}"),
        ("RE cashflow to reserve", f"{re_routing.get('reserve_pct', 0):.0%}"),
    ]
    for label, val in items:
        st.sidebar.markdown(
            f"<div style='display:flex;justify-content:space-between;padding:4px 0;"
            f"border-bottom:1px solid #eee;font-size:13px;'>"
            f"<span style='color:#555;'>{label}</span>"
            f"<span style='font-weight:600;'>{val}</span></div>",
            unsafe_allow_html=True,
        )


def render_simulator_tab(
    cashflows: pd.DataFrame,
    summary: pd.DataFrame,
    model_config: dict[str, Any] | None = None,
    scenario_assumptions: dict[str, Any] | None = None,
) -> None:
    """Render the Interactive Scenario Simulator walkthrough."""
    import streamlit as st

    model_config = model_config or {}
    scenario_assumptions = scenario_assumptions or {}
    max_hf_liq_pct = float(model_config.get("hurdle_completion_trigger", {}).get("max_hf_liquidation_pct", 0.75))

    st.header("Scenario Walkthrough Simulator")
    st.write("Step through the timeline to see how the fund evolves year-by-year.")

    col1, col2 = st.columns([1, 2])
    with col1:
        options = [display_name(s) for s in scenario_order(summary)]
        label_to_scenario = {display_name(s): s for s in summary["scenario"]}
        selected_label = st.selectbox("Select scenario to simulate", options=options, key="sim_selector")
        selected_scenario = label_to_scenario[selected_label]
        st.session_state["simulator_scenario_select"] = selected_scenario

    scenario_df = cashflows[cashflows["scenario"] == selected_scenario].sort_values("year")
    max_year = int(scenario_df["year"].max())

    # Reset year slider on scenario change
    if "last_sim_scenario" not in st.session_state or st.session_state.last_sim_scenario != selected_scenario:
        st.session_state.year_slider = 0
        st.session_state.last_sim_scenario = selected_scenario
    if "year_slider" not in st.session_state:
        st.session_state.year_slider = 0

    st.write("---")

    btn_col1, slider_col, btn_col2 = st.columns([1, 4, 1])
    nav_change = 0
    with btn_col1:
        if st.button("Previous Year", width="stretch") and st.session_state.year_slider > 0:
            nav_change = -1
    with btn_col2:
        if st.button("Next Year", width="stretch") and st.session_state.year_slider < max_year:
            nav_change = 1
    if nav_change != 0:
        st.session_state.year_slider += nav_change
        st.rerun()
    with slider_col:
        selected_year = st.select_slider(
            "Fund Timeline",
            options=list(range(0, max_year + 1)),
            key="year_slider",
            help="Move the slider or use buttons to step through the fund history.",
        )

    st.divider()

    # Pull summary-level constants
    summary_row = summary[summary["scenario"] == selected_scenario].iloc[0]
    lp_hurdle_amount = float(summary_row.get("lp_hurdle_amount", 20_000_000) or 20_000_000)
    lp_initial_capital = float(summary_row.get("lp_initial_capital", 10_000_000) or 10_000_000)

    # Build current_row and opening_nav
    if selected_year == 0:
        first = scenario_df.iloc[0]
        re_opening = float(first.get("re_opening_nav", 0) or 0)
        hf_opening = float(first.get("hf_opening_nav", 0) or 0)
        rs_opening = float(first.get("reserve_opening_nav", 0) or 0)
        initial_fund_nav = re_opening + hf_opening + rs_opening
        current_row = pd.Series({
            "year": 0,
            "re_closing_nav": re_opening,
            "hf_closing_nav": hf_opening,
            "reserve_closing_nav": rs_opening,
            "retained_cash": 0.0,
            "fund_nav": initial_fund_nav,
            "event_flag": "",
            "lp_cumulative_distribution": 0.0,
            "lp_remaining_hurdle": lp_hurdle_amount,
            "lp_initial_capital": lp_initial_capital,
            "re_gross_asset_value": float(first.get("re_gross_asset_value", 0) or 0),
            "re_debt_balance": float(first.get("re_debt_balance", 0) or 0),
            "re_assumed_liabilities": float(first.get("re_assumed_liabilities", 0) or 0),
        })
        opening_nav = 0.0
        prev_year_rows = pd.DataFrame()
    else:
        current_row = scenario_df[scenario_df["year"] == selected_year].iloc[0]
        prev_year_rows = scenario_df[scenario_df["year"] == selected_year - 1]
        prev_retained = float(prev_year_rows.iloc[0].get("retained_cash", 0) or 0) if not prev_year_rows.empty else 0.0
        opening_nav = (
            float(current_row.get("re_opening_nav", 0) or 0)
            + float(current_row.get("hf_opening_nav", 0) or 0)
            + float(current_row.get("reserve_opening_nav", 0) or 0)
            + prev_retained
        )

    closing_nav = float(current_row.get("fund_nav", 0) or 0)
    nav_change_val = closing_nav - opening_nav if selected_year > 0 else closing_nav

    # ── Headline metrics ──────────────────────────────────────────────────────
    m0, m1, m2, m3, m4 = st.columns(5)
    with m0:
        st.metric("Opening NAV", format_money(opening_nav) if selected_year > 0 else "$0")
        st.caption("Value at start of year.")
    with m1:
        st.metric("Closing NAV", format_money(closing_nav))
        st.caption("Value at end of year.")
    with m2:
        st.metric("Net Change", format_money(nav_change_val), delta=format_money(nav_change_val))
        st.caption("Growth minus payouts.")
    with m3:
        st.metric("LP Cash Returned", format_money(current_row.get("lp_cumulative_distribution", 0)))
        st.caption("Cumulative distributions.")
    with m4:
        remaining = current_row.get("lp_remaining_hurdle", lp_hurdle_amount)
        st.metric("Remaining Hurdle", format_money(remaining))
        st.caption("Target to 2.0x.")

    st.write("---")

    # ── Row 1: Fund NAV composition | NAV bridge ──────────────────────────────
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Fund NAV composition")
        st.caption("Net value held in each sleeve at year end. RE shown net of all debt.")
        pie = build_nav_composition_pie(current_row)
        if pie:
            st.plotly_chart(pie, width="stretch")
        else:
            st.info("No assets held.")

    with c2:
        st.subheader("NAV bridge")
        st.caption("How the fund moved from opening to closing NAV this year.")

        if selected_year == 0:
            equity_cushion = initial_fund_nav - lp_initial_capital
            render_bridge_item("LP capital invested", lp_initial_capital)
            if equity_cushion > 100:
                render_bridge_item(
                    "Entry equity cushion",
                    equity_cushion,
                    note=f"LP paid {format_money(lp_initial_capital)} for {format_money(initial_fund_nav)} of fund value on day 1. The deal was structured below NAV.",
                )
            st.markdown(f"**Starting fund NAV: {format_money(initial_fund_nav)}**")
        else:
            past_df = scenario_df[scenario_df["year"] <= selected_year]

            # RE — show gross appreciation rate, not leveraged equity rate
            re_net_change = float(current_row.get("re_closing_nav", 0) or 0) - float(current_row.get("re_opening_nav", 0) or 0)
            gross_curr = float(current_row.get("re_gross_asset_value", 0) or 0)
            gross_prev = float(prev_year_rows.iloc[0].get("re_gross_asset_value", 0) or 0) if not prev_year_rows.empty else gross_curr
            gross_rate = (gross_curr / gross_prev - 1) if gross_prev > 0 else 0
            cum_re = (past_df["re_closing_nav"] - past_df["re_opening_nav"]).sum()
            re_opening_bal = float(current_row.get("re_opening_nav", 0) or 0)
            re_closing_bal = float(current_row.get("re_closing_nav", 0) or 0)
            render_bridge_item(
                "Real estate net equity change",
                re_net_change,
                rate=gross_rate,
                opening=re_opening_bal,
                cumulative=cum_re,
                note=f"Property appreciated {gross_rate:.1%} on gross {format_money(gross_curr)} asset. Equity change is amplified by leverage.",
                balance=re_closing_bal,
            )

            # HF — split appreciation / reinvestment / liquidation
            hf_reinvestment = float(current_row.get("re_cashflow_to_hf", 0) or 0) + float(current_row.get("hf_harvest_to_hf", 0) or 0)
            hf_liquidated = float(current_row.get("hf_nav_liquidated_for_hurdle", 0) or 0)
            hf_raw_change = float(current_row.get("hf_closing_nav", 0) or 0) - float(current_row.get("hf_opening_nav", 0) or 0)
            hf_appreciation = hf_raw_change - hf_reinvestment + hf_liquidated
            hf_opening_val = float(current_row.get("hf_opening_nav", 0) or 0)
            hf_rate = hf_appreciation / hf_opening_val if hf_opening_val > 0 else 0
            hf_closing_bal = float(current_row.get("hf_closing_nav", 0) or 0)
            render_bridge_item("Hedge fund appreciation", hf_appreciation, rate=hf_rate, opening=hf_opening_val, balance=hf_closing_bal)
            if hf_reinvestment > 0:
                render_bridge_item("RE cashflow reinvested into HF", hf_reinvestment)
            if hf_liquidated > 0:
                render_bridge_item("HF liquidated for LP redemption", -hf_liquidated)

            # Reserve — context-aware label
            rs_opening_bal = float(current_row.get("reserve_opening_nav", 0) or 0)
            rs_closing_bal = float(current_row.get("reserve_closing_nav", 0) or 0)
            rs_change = rs_closing_bal - rs_opening_bal
            trigger_reserve_used = float(current_row.get("trigger_cash_from_reserve", 0) or 0)
            cum_rs = (past_df["reserve_closing_nav"] - past_df["reserve_opening_nav"]).sum()
            if trigger_reserve_used > 0:
                rs_label = "Reserve used for LP redemption"
            elif rs_change < -100:
                rs_label = "Reserve drawdown (covered RE shortfall)"
            elif rs_change > 100:
                rs_label = "Reserve allocation (from cashflow routing)"
            else:
                rs_label = "Reserve"
            render_bridge_item(rs_label, rs_change, opening=rs_opening_bal, cumulative=cum_rs, balance=rs_closing_bal)

            # Retained cash — show refi proceeds or drawdown
            retained_now = float(current_row.get("retained_cash", 0) or 0)
            retained_prev = float(prev_year_rows.iloc[0].get("retained_cash", 0) or 0) if not prev_year_rows.empty else 0.0
            refi_proceeds = float(current_row.get("re_refi_proceeds_from_deals", 0) or 0)
            retained_change = retained_now - retained_prev
            if refi_proceeds > 0:
                render_bridge_item(
                    "Refinance proceeds (held as dry powder)",
                    refi_proceeds,
                    note="Not distributed yet — held to fund LP redemption at a future trigger year.",
                    balance=retained_now,
                )
            elif retained_change < -100:
                render_bridge_item("Retained cash used for LP redemption", retained_change, balance=retained_now)

            # LP distribution
            dist = -float(current_row.get("lp_distribution", 0) or 0)
            cum_dist = -float(current_row.get("lp_cumulative_distribution", 0) or 0)
            if dist != 0:
                render_bridge_item("LP distributions paid", dist, cumulative=cum_dist)

            # GP fees
            fees = -float(current_row.get("re_asset_mgmt_fee", 0) or 0)
            if "re_asset_mgmt_fee" in past_df.columns:
                cum_fees = -past_df["re_asset_mgmt_fee"].sum()
            else:
                cum_fees = 0.0
            if fees != 0:
                render_bridge_item("GP asset management fees", fees, cumulative=cum_fees)

            st.markdown("---")
            st.markdown(f"**Closing fund NAV: {format_money(closing_nav)}**")

    st.write("---")

    # ── Row 2: RE deal detail | Events & flags ────────────────────────────────
    d1, d2 = st.columns(2)
    with d1:
        if selected_year > 0:
            render_re_deal_detail(current_row)
        else:
            with st.expander("Real estate deal detail", expanded=False):
                st.caption("Property acquired at start of Year 1.")

    with d2:
        st.subheader("Events & flags")
        if selected_year == 0:
            equity_cushion = initial_fund_nav - lp_initial_capital
            st.success(
                f"Initial capital allocation complete. "
                f"Fund starts with {format_money(initial_fund_nav)} of value from a {format_money(lp_initial_capital)} LP commitment."
            )
            if equity_cushion > 100:
                st.info(
                    f"Entry equity cushion: {format_money(equity_cushion)}. "
                    "The deal was structured so the LP paid less than the fund's day-one asset value."
                )
        else:
            render_event_detail(current_row, scenario_df, max_hf_liq_pct)

    st.write("---")

    # ── Row 3: Cashflow routing ───────────────────────────────────────────────
    st.subheader("Cashflow routing")
    if selected_year == 0:
        st.info("Initial allocation. No cashflow routing yet.")
    else:
        total_routed = (
            float(current_row.get("total_cash_distributed", 0) or 0)
            + float(current_row.get("total_cash_reinvested", 0) or 0)
            + float(current_row.get("total_cash_reserved", 0) or 0)
        )
        if total_routed > 0:
            st.markdown(f"**Total cash generated and routed this year: {format_money(total_routed)}**")
            sankey = build_cashflow_sankey(current_row)
            if sankey:
                st.plotly_chart(sankey, width="stretch")
            render_routing_amounts_table(current_row)
        else:
            net_re = float(current_row.get("net_re_cashflow", 0) or 0)
            if net_re < 0:
                st.warning(
                    f"RE cashflow negative this year ({format_money(net_re)}). "
                    "No cash routed — shortfall absorbed by reserve."
                )
            else:
                st.info("No cash routed this year.")


def main() -> None:
    import streamlit as st

    st.set_page_config(page_title="Hybrid Fund Model", layout="wide")
    st.title("Hybrid Fund Model")
    st.caption("LP hurdle is based on actual cash distributions received, not NAV appreciation. Nothing here saves to YAML or output files.")

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

    walkthrough_mode = st.sidebar.checkbox(
        "Walkthrough mode",
        value=True,
        help="Hides routing controls and shows key assumptions in the sidebar. Good for walking non-modellers through a scenario.",
    )
    st.session_state["walkthrough_mode"] = walkthrough_mode

    if walkthrough_mode:
        # Render assumptions sidebar now so it appears at the top, before any other sidebar content.
        # Read from the selectbox widget key directly — Streamlit updates this synchronously on rerun,
        # so it reflects the new selection immediately rather than lagging one render.
        _label_to_scenario = {display_name(s): s for s in summary["scenario"]} if not summary.empty else {}
        _sim_label = st.session_state.get("sim_selector")
        if _sim_label and _sim_label in _label_to_scenario:
            _sim_scenario = _label_to_scenario[_sim_label]
        elif not summary.empty:
            _sim_scenario = scenario_order(summary)[0]
        else:
            _sim_scenario = None
        if _sim_scenario:
            render_walkthrough_sidebar(_sim_scenario, scenario_assumptions, model_config)
        routing_override = default_routing_from_config(model_config)
        routing_valid = True
        trigger_override = default_trigger_from_config(model_config)
    else:
        routing_override, routing_valid = render_routing_controls(model_config)
        trigger_override = render_trigger_controls(model_config)

    if routing_valid:
        try:
            cashflows, summary = run_model_with_routing_override(routing_override, trigger_override)
        except Exception as exc:
            st.warning(f"Could not rerun model with dashboard routing controls. Showing saved outputs instead. Error: {exc}")
    cashflows, summary = append_custom_scenario_if_available(cashflows, summary)

    tab_explorer, tab_simulator, tab_configure = st.tabs(["Scenario Explorer", "Simulator", "Configure & Run"])

    with tab_explorer:
        outcome_fig = build_outcome_chart(summary, notes)
        if outcome_fig is not None:
            st.plotly_chart(outcome_fig, width="stretch")

        options = ["All scenarios (small multiples)"] + [display_name(s) for s in scenario_order(summary)]
        label_to_scenario = {display_name(s): s for s in summary["scenario"]}
        selected_label = st.selectbox(
            "Scenario selector",
            options=options,
            index=0,
            help="Select a specific scenario to view detailed charts and diagnostic cards, or choose 'All scenarios' for a high-level comparison."
        )
        selected = None if selected_label == "All scenarios (small multiples)" else label_to_scenario[selected_label]

        if selected:
            render_metric_cards(summary[summary["scenario"] == selected].iloc[0])
            render_routing_summary_cards(summary[summary["scenario"] == selected].iloc[0])
            render_trigger_summary_cards(summary[summary["scenario"] == selected].iloc[0])
            render_selected_assumptions(selected, model_config, scenario_assumptions, assumption_notes)

        render_scenario_comparison(summary)

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

        routing_fig = build_routing_chart(cashflows, summary, selected, notes)
        if routing_fig is not None:
            st.plotly_chart(routing_fig, width="stretch")
            st.caption("This chart shows generated RE cashflow and HF harvest routed to LP distributions, HF reinvestment, and reserve.")

        trigger_fig = build_trigger_funding_chart(cashflows, summary, selected, notes)
        if trigger_fig is not None:
            st.plotly_chart(trigger_fig, width="stretch")
            st.caption("This chart shows only active hurdle completion trigger funding sources. Blank panels mean no trigger funding was used.")

        hf_reinvestment_fig = build_single_line_chart(
            cashflows,
            summary,
            selected,
            notes,
            "hf_closing_nav",
            "HF NAV growth including reinvestments.",
            "HF NAV",
            "#4c78a8",
        )
        if hf_reinvestment_fig is not None:
            st.plotly_chart(hf_reinvestment_fig, width="stretch")

        reserve_fig = build_single_line_chart(
            cashflows,
            summary,
            selected,
            notes,
            "reserve_closing_nav",
            "Reserve NAV growth.",
            "Reserve NAV",
            "#f58518",
        )
        if reserve_fig is not None:
            st.plotly_chart(reserve_fig, width="stretch")

        gp_residual_fig = build_single_line_chart(
            cashflows,
            summary,
            selected,
            notes,
            "gp_residual_nav",
            "GP residual NAV over time.",
            "GP residual NAV",
            "#9b5de5",
        )
        if gp_residual_fig is not None:
            st.plotly_chart(gp_residual_fig, width="stretch")

        nav_fig = build_nav_chart(cashflows, summary, selected, notes)
        if nav_fig is not None:
            st.plotly_chart(nav_fig, width="stretch")
        render_captions(cashflows, summary, selected)

        st.divider()
        render_traditional_statement(cashflows, summary, selected)
        download_cashflows_button(cashflows)

    with tab_simulator:
        render_simulator_tab(cashflows, summary, model_config, scenario_assumptions)

    with tab_configure:
        render_configure_tab(routing_override, trigger_override, cashflows)

    st.caption(f"{APP_VERSION}. Nothing here saves to YAML or output files.")


if __name__ == "__main__":
    main()
