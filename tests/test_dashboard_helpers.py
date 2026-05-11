from __future__ import annotations

import pandas as pd

from dashboard.app import (
    FLAG_TRANSLATIONS,
    format_money,
    generate_scenario_caption,
    parse_flags,
    read_dashboard_data,
)


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
