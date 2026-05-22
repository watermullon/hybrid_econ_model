from __future__ import annotations

from pathlib import Path
import pandas as pd

from dashboard.app import (
    FLAG_TRANSLATIONS,
    calculate_implied_re_allocation,
    build_traditional_statement,
    comparison_table,
    flatten_assumptions,
    format_statement_for_display,
    format_money,
    generate_scenario_caption,
    parse_hf_returns,
    parse_flags,
    panel_shape,
    read_dashboard_data,
    run_custom_scenario_in_memory,
)

ROOT = Path(__file__).resolve().parents[1]


def test_flag_dictionary_covers_current_known_flags() -> None:
    expected_flags = {
        "LP_HURDLE_ACHIEVED",
        "LP_HURDLE_NOT_ACHIEVED",
        "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED",
        "FAST_GP_DYNASTY_OUTCOME",
        "SLOW_TIME_HORIZON_DRIFT",
        "GP_SURVIVABILITY_RISK",
        "FUND_NAV_IMPAIRED",
        "HF_MAJOR_DRAWDOWN",
        "RE_NAV_IMPAIRMENT",
        "LP_GOOD_IRR_GP_LARGE_RESIDUAL",
        "LP_CASH_YIELD_SHORTFALL",
        "REFINANCE_EVENT_OCCURRED",
        "REFI_DEPENDENT_LP_OUTCOME",
        "LONG_ZERO_DISTRIBUTION_PERIOD",
        "LP_STILL_BELOW_1X_CASH_MOIC_AT_END",
        "LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV",
        "HURDLE_COMPLETION_TRIGGER_EXECUTED",
        "HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT",
        "LP_REDEEMED_VIA_HF_LIQUIDATION",
        "LP_REDEEMED_VIA_REFI",
        "LP_REDEEMED_VIA_PARTIAL_RE_SALE",
    }
    assert expected_flags.issubset(FLAG_TRANSLATIONS.keys())


def test_parse_flags_splits_semicolon_values() -> None:
    assert parse_flags("LP_HURDLE_NOT_ACHIEVED; GP_SURVIVABILITY_RISK") == [
        "LP_HURDLE_NOT_ACHIEVED",
        "GP_SURVIVABILITY_RISK",
    ]


def test_format_money_uses_compact_units() -> None:
    assert format_money(10_000_000) == "$10.0m"
    assert format_money(250_000) == "$250k"


def test_generate_caption_uses_data_not_hardcoded_text() -> None:
    scenario_df = pd.DataFrame(
        {
            "scenario": ["base_hit_everyone_happy"],
            "year": [1],
            "lp_distribution": [500_000],
            "re_closing_nav": [8_000_000],
            "hf_closing_nav": [1_000_000],
            "retained_cash": [0],
            "reserve_closing_nav": [500_000],
        }
    )
    summary_row = pd.Series(
        {
            "scenario": "base_hit_everyone_happy",
            "lp_initial_capital": 10_000_000,
            "lp_cash_distributions": 500_000,
            "years_modelled": 1,
            "lp_cash_moic": 0.05,
            "lp_economic_moic": 0.95,
            "lp_hurdle_achieved": False,
            "liquidity_constrained": False,
            "all_flags": "LP_HURDLE_NOT_ACHIEVED",
        }
    )

    caption = generate_scenario_caption(scenario_df, summary_row)

    assert "$10.0m" in caption
    assert "$500k" in caption
    assert "0.05x" in caption
    assert "The LP hurdle was not reached" in caption


def test_dashboard_reads_current_outputs() -> None:
    cashflows, summary, _ = read_dashboard_data()

    assert len(summary["scenario"].unique()) == 8
    assert len(cashflows["scenario"].unique()) == 8


def test_streamlit_app_exposes_routing_controls(monkeypatch) -> None:
    from streamlit.testing.v1 import AppTest

    monkeypatch.setenv("STREAMLIT_BROWSER_GATHER_USAGE_STATS", "false")
    # Point to the app.py in the root dashboard directory
    app = AppTest.from_file(str(ROOT / "dashboard" / "app.py"))
    app.run(timeout=30)

    slider_labels = {slider.label for slider in app.slider}
    assert "RE cashflow to LP" in slider_labels
    assert "HF harvest to reserve" in slider_labels
    assert "Initial HF allocation (%)" in slider_labels
    assert "Minimum LP cash MOIC before trigger" in slider_labels


def test_parse_hf_returns_repeats_last_value_to_match_years() -> None:
    assert parse_hf_returns("10, -5", 4) == [0.10, -0.05, -0.05, -0.05]


def test_custom_scenario_runs_in_memory() -> None:
    routing = {
        "re_cashflow": {
            "lp_distribution_pct": 0.50,
            "hf_reinvestment_pct": 0.30,
            "reserve_pct": 0.20,
        },
        "hf_harvest": {
            "lp_distribution_pct": 0.70,
            "hf_reinvestment_pct": 0.20,
            "reserve_pct": 0.10,
        },
    }
    custom_inputs = {
        "years": 3,
        "initial_noi_yield": 0.075,
        "annual_noi_growth": 0.02,
        "annual_nav_appreciation": 0.04,
        "gross_rent_yield": 0.12,
        "hf_allocation_pct": 0.20,
        "reserve_allocation_pct": 0.05,
        "re_allocation_pct": 0.75,
        "hf_harvest_rate": 0.50,
        "re_liquidity_pct": 0.25,
        "hf_returns": [0.20, 0.15, 0.10],
    }

    trigger = {
        "enabled": True,
        "trigger_when_economic_hurdle_passed": True,
        "minimum_lp_cash_moic_before_trigger": 0.0,
        "max_hf_liquidation_pct": 0.75,
        "max_refi_pct_of_re_nav": 0.20,
        "allow_retained_cash_use": True,
        "allow_reserve_use": True,
        "allow_hf_liquidation": True,
        "allow_refi": True,
        "allow_partial_re_sale": False,
        "max_partial_re_sale_pct_of_re_nav": 0.0,
        "execute_only_if_lp_fully_redeemed": True,
    }

    cashflows, summary = run_custom_scenario_in_memory(custom_inputs, routing, trigger)

    assert summary.iloc[0]["scenario"] == "custom_dashboard_scenario"
    assert len(cashflows) >= 1


def test_panel_shape_expands_for_custom_scenario() -> None:
    scenarios = [f"scenario_{index}" for index in range(9)]
    assert panel_shape(scenarios) == (3, 4)


def test_implied_re_allocation_keeps_total_at_100() -> None:
    implied_re, warning = calculate_implied_re_allocation(20, 20)

    assert implied_re == 60
    assert warning is None


def test_implied_re_allocation_warns_when_invalid() -> None:
    implied_re, warning = calculate_implied_re_allocation(80, 30)

    assert implied_re == 0
    assert warning is not None


def test_comparison_table_uses_readable_column_names() -> None:
    _, summary, _ = read_dashboard_data()

    table = comparison_table(summary)

    assert "Scenario" in table.columns
    assert "LP cash multiple" in table.columns
    assert "Years to LP 2x cash" in table.columns
    assert "Trigger executed" in table.columns


def test_traditional_statement_includes_year_zero_and_routing_columns() -> None:
    cashflows, summary, _ = read_dashboard_data()

    statement = build_traditional_statement(cashflows, summary, "base_hit_everyone_happy")

    assert statement.iloc[0]["Year"] == 0
    assert statement.iloc[0]["Event"] == "Initial allocation"
    assert "RE cashflow to LP" in statement.columns
    assert "Trigger HF liquidation used" in statement.columns
    assert "Closing HF NAV" in statement.columns


def test_traditional_statement_display_formats_whole_numbers_with_commas() -> None:
    cashflows, summary, _ = read_dashboard_data()
    statement = build_traditional_statement(cashflows, summary, "base_hit_everyone_happy")

    display = format_statement_for_display(statement)

    assert "." not in str(display.iloc[0]["Closing RE NAV"])
    assert "," in str(display.iloc[0]["Closing RE NAV"])


def test_assumptions_use_friendly_names_and_values() -> None:
    assumptions = {
        "real_estate": {"initial_noi_yield": 0.075},
        "hedge_fund": {"annual_returns": [0.2, -0.05]},
    }

    table = flatten_assumptions(assumptions)

    assert "Initial real estate NOI yield" in set(table["assumption"])
    assert "real_estate.initial_noi_yield" not in set(table["assumption"])
    assert "20.0%, -5.0%" in set(table["value"])
