from __future__ import annotations

import pytest

from src.engine import run_scenario
from src.model_types import ModelConfig, Scenario


def hf_only_config(*, lp_hurdle_moic: float) -> ModelConfig:
    return ModelConfig.model_validate(
        {
            "model": {
                "currency": "USD",
                "periods_per_year": 1,
                "max_years": 1,
                "initial_lp_capital": 10_000_000,
                "gp_co_investment": 0,
            },
            "allocation": {
                "method": "fixed",
                "hedge_fund_allocation_pct": 1.0,
                "real_estate_allocation_pct": 0.0,
                "reserve_allocation_pct": 0.0,
            },
            "waterfall": {
                "lp_hurdle_moic": lp_hurdle_moic,
                "lp_receives_100_percent_until_hurdle": True,
                "gp_receives_residual_after_lp_hurdle": True,
                "include_unrealized_nav_in_hurdle_test": True,
                "require_liquidity_for_lp_redemption": True,
            },
            "liquidity": {
                "hf_liquidation_allowed": True,
                "hf_liquidation_capacity_pct_per_year": 1.0,
                "reserve_liquidation_capacity_pct_per_year": 1.0,
                "real_estate_liquidation_capacity_pct_per_year": 0.0,
                "max_refinance_or_sale_capacity_pct_of_re_nav": 0.0,
            },
            "fees": {
                "real_estate_asset_management_fee": {
                    "enabled": True,
                    "rate": 0.03,
                    "basis": "gross_rent",
                },
                "hedge_fund_fees": {
                    "model_as_net_returns": True,
                    "management_fee_rate": 0.0,
                    "performance_fee_rate": 0.0,
                },
            },
            "distribution_policy": {
                "distribute_re_cashflow_annually": True,
                "distribute_hf_realized_gains_annually": False,
                "hf_positive_return_harvest_rate": 0.0,
                "retain_cash_until_hurdle_redemption": False,
            },
            "reserve": {"annual_return": 0.0},
            "reporting": {
                "output_excel": True,
                "output_csv": True,
                "output_markdown": True,
            },
            "flag_thresholds": {
                "fast_gp_dynasty_max_year": 4,
                "fast_gp_dynasty_residual_multiple": 0.5,
                "slow_time_horizon_year": 8,
                "gp_survivability_first_years": 5,
                "gp_survivability_fee_threshold": 0,
                "hf_major_drawdown_pct": 0.50,
                "re_nav_impairment_pct": 0.20,
                "lp_good_irr_threshold": 0.12,
                "lp_good_irr_gp_residual_multiple": 1.0,
            },
        }
    )


def hf_only_scenario(
    *,
    hf_return: float,
    harvest_rate: float,
    distribute_hf_realized_gains_annually: bool,
) -> Scenario:
    return Scenario.model_validate(
        {
            "description": "Synthetic HF-only harvest test scenario.",
            "years": 1,
            "real_estate": {
                "initial_noi_yield": 0.0,
                "annual_noi_growth": 0.0,
                "annual_nav_appreciation": 0.0,
                "gross_rent_yield": 0.0,
            },
            "hedge_fund": {"annual_returns": [hf_return]},
            "distribution_policy": {
                "hf_positive_return_harvest_rate": harvest_rate,
                "distribute_hf_realized_gains_annually": distribute_hf_realized_gains_annually,
            },
        }
    )


def test_harvest_disabled_keeps_full_hf_gain_in_hf_nav() -> None:
    config = hf_only_config(lp_hurdle_moic=3.0)
    scenario = hf_only_scenario(
        hf_return=1.0,
        harvest_rate=0.0,
        distribute_hf_realized_gains_annually=False,
    )

    result = run_scenario("harvest_disabled", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.hf_harvest == pytest.approx(0)
    assert year_one.hf_closing_nav == pytest.approx(20_000_000)
    assert year_one.lp_distribution == pytest.approx(0)
    assert year_one.fund_nav == pytest.approx(20_000_000)
    assert result.summary["lp_hurdle_achieved"] is False


def test_harvest_enabled_and_hf_distributions_disabled_moves_harvest_to_retained_cash() -> None:
    config = hf_only_config(lp_hurdle_moic=3.0)
    scenario = hf_only_scenario(
        hf_return=1.0,
        harvest_rate=0.50,
        distribute_hf_realized_gains_annually=False,
    )

    result = run_scenario("harvest_retained", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.hf_harvest == pytest.approx(5_000_000)
    assert year_one.hf_closing_nav == pytest.approx(15_000_000)
    assert year_one.retained_cash == pytest.approx(5_000_000)
    assert year_one.lp_distribution == pytest.approx(0)
    assert year_one.fund_nav == pytest.approx(20_000_000)
    assert result.summary["lp_hurdle_achieved"] is False


def test_harvest_enabled_and_hf_distributions_enabled_pays_lp_before_hurdle() -> None:
    config = hf_only_config(lp_hurdle_moic=3.0)
    scenario = hf_only_scenario(
        hf_return=1.0,
        harvest_rate=0.50,
        distribute_hf_realized_gains_annually=True,
    )

    result = run_scenario("harvest_distributed", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.hf_harvest == pytest.approx(5_000_000)
    assert year_one.hf_closing_nav == pytest.approx(15_000_000)
    assert year_one.retained_cash == pytest.approx(0)
    assert year_one.lp_distribution == pytest.approx(5_000_000)
    assert year_one.lp_cumulative_distribution == pytest.approx(5_000_000)
    assert result.summary["lp_cash_moic"] == pytest.approx(0.5)
    assert result.summary["lp_hurdle_achieved"] is False


def test_harvest_distribution_then_hurdle_redemption_assigns_residual_to_gp() -> None:
    config = hf_only_config(lp_hurdle_moic=2.0)
    scenario = hf_only_scenario(
        hf_return=1.5,
        harvest_rate=1.0,
        distribute_hf_realized_gains_annually=True,
    )

    result = run_scenario("harvest_redemption", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.hf_harvest == pytest.approx(15_000_000)
    assert year_one.lp_distribution == pytest.approx(20_000_000)
    assert year_one.lp_cumulative_distribution == pytest.approx(20_000_000)
    assert year_one.hf_closing_nav == pytest.approx(5_000_000)
    assert year_one.fund_nav == pytest.approx(5_000_000)
    assert result.summary["lp_cash_moic"] == pytest.approx(2.0)
    assert result.summary["lp_hurdle_achieved"] is True
    assert result.summary["gp_residual_nav"] == pytest.approx(5_000_000)
