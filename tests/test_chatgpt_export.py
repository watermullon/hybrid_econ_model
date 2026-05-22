from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest
import yaml

from src.chatgpt_export import build_chatgpt_context


def test_build_chatgpt_context_creates_compact_markdown(tmp_path: Path) -> None:
    root = tmp_path
    (root / "inputs").mkdir()
    (root / "outputs").mkdir()

    _write_yaml(
        root / "inputs" / "model_config.yaml",
        {
            "model": {"currency": "USD", "max_years": 1, "initial_lp_capital": 10_000_000, "gp_co_investment": 0},
            "allocation": {
                "method": "fixed",
                "hedge_fund_allocation_pct": 0.1,
                "real_estate_allocation_pct": 0.85,
                "reserve_allocation_pct": 0.05,
            },
            "waterfall": {
                "lp_hurdle_moic": 2.0,
                "include_unrealized_nav_in_hurdle_test": True,
                "require_liquidity_for_lp_redemption": True,
            },
            "liquidity": {
                "hf_liquidation_capacity_pct_per_year": 1.0,
                "reserve_liquidation_capacity_pct_per_year": 1.0,
                "max_refinance_or_sale_capacity_pct_of_re_nav": 0.25,
            },
            "fees": {"real_estate_asset_management_fee": {"rate": 0.03, "basis": "gross_rent"}},
            "distribution_policy": {"hf_positive_return_harvest_rate": 0.0},
            "cashflow_routing": {
                "re_cashflow": {"lp_distribution_pct": 0.2, "hf_reinvestment_pct": 0.5, "reserve_pct": 0.3},
                "hf_harvest": {"lp_distribution_pct": 0.2, "hf_reinvestment_pct": 0.7, "reserve_pct": 0.1},
            },
            "lp_cash_yield_policy": {"enabled": False},
            "gp_survivability": {"minimum_cumulative_fees": 500_000},
        },
    )
    _write_yaml(
        root / "inputs" / "scenarios.yaml",
        {
            "scenarios": {
                "test_case": {
                    "description": "Simple test scenario",
                    "years": 1,
                    "real_estate": {
                        "initial_noi_yield": 0.07,
                        "annual_noi_growth": 0.02,
                        "annual_nav_appreciation": 0.03,
                        "gross_rent_yield": 0.11,
                    },
                    "hedge_fund": {"annual_returns": [0.1]},
                }
            }
        },
    )
    pd.DataFrame(
        [
            {
                "scenario": "test_case",
                "description": "Simple test scenario",
                "years_modelled": 1,
                "lp_cash_moic": 0.1,
                "lp_economic_moic": 1.1,
                "lp_cash_irr": -0.9,
                "lp_economic_irr": 0.1,
                "lp_hurdle_achieved": False,
                "year_hurdle_achieved": "",
                "liquidity_constrained": False,
                "final_fund_nav": 11_000_000,
                "total_distributed_to_lp": 1_000_000,
                "total_reinvested_into_hf": 500_000,
                "total_added_to_reserve": 300_000,
                "years_until_lp_2x_cash_return": "",
                "gp_residual_nav": 0,
                "gp_total_economics": 250_000,
                "primary_flag": "LP_HURDLE_NOT_ACHIEVED",
            }
        ]
    ).to_csv(root / "outputs" / "scenario_summary.csv", index=False)
    pd.DataFrame(
        [
            {
                "scenario": "test_case",
                "year": 1,
                "lp_distribution": 1_000_000,
                "lp_cumulative_distribution": 1_000_000,
                "lp_remaining_hurdle": 19_000_000,
                "re_cashflow_to_lp": 700_000,
                "re_cashflow_to_hf": 200_000,
                "re_cashflow_to_reserve": 100_000,
                "hf_harvest_to_lp": 300_000,
                "hf_harvest_to_hf": 0,
                "hf_harvest_to_reserve": 0,
                "refinance_proceeds": 0,
                "re_closing_nav": 8_755_000,
                "hf_closing_nav": 1_100_000,
                "reserve_closing_nav": 600_000,
                "retained_cash": 0,
                "fund_nav": 10_455_000,
                "liquidity_available": 3_888_750,
                "event_flag": "",
            }
        ]
    ).to_csv(root / "outputs" / "scenario_cashflows.csv", index=False)
    pd.DataFrame(
        [
            {
                "scenario": "test_case",
                "flag": "LP_HURDLE_NOT_ACHIEVED",
                "severity": "high",
                "explanation": "LP did not reach the target cash hurdle.",
            }
        ]
    ).to_csv(root / "outputs" / "scenario_flags.csv", index=False)

    output_path = build_chatgpt_context(root)

    text = output_path.read_text(encoding="utf-8")
    assert "Hybrid Fund Model Context for ChatGPT Analysis" in text
    assert "The LP 2.0x hurdle means actual cash distributions received by LPs." in text
    assert "test_case" in text
    assert "scenario_summary.csv" in text
    assert "Simple test scenario" in text


def test_build_chatgpt_context_requires_existing_model_outputs(tmp_path: Path) -> None:
    (tmp_path / "inputs").mkdir()
    _write_yaml(tmp_path / "inputs" / "model_config.yaml", {"model": {"initial_lp_capital": 10_000_000}})
    _write_yaml(tmp_path / "inputs" / "scenarios.yaml", {"scenarios": {}})

    with pytest.raises(FileNotFoundError, match="Run python run_model.py"):
        build_chatgpt_context(tmp_path)


def _write_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data), encoding="utf-8")
