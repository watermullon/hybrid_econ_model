from __future__ import annotations

import pytest
from pydantic import ValidationError

from src.engine import run_scenario
from src.model_types import CashflowRoute, ModelConfig, Scenario


def routing_config(*, hf_harvest_rate: float = 0.0) -> ModelConfig:
    return ModelConfig.model_validate(
        {
            "model": {
                "currency": "USD",
                "periods_per_year": 1,
                "max_years": 3,
                "initial_lp_capital": 10_000_000,
                "gp_co_investment": 0,
            },
            "allocation": {
                "method": "fixed",
                "hedge_fund_allocation_pct": 0.50,
                "real_estate_allocation_pct": 0.50,
                "reserve_allocation_pct": 0.0,
            },
            "waterfall": {
                "lp_hurdle_moic": 3.0,
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
                "real_estate_asset_management_fee": {"enabled": False, "rate": 0.0, "basis": "gross_rent"},
                "hedge_fund_fees": {
                    "model_as_net_returns": True,
                    "management_fee_rate": 0.0,
                    "performance_fee_rate": 0.0,
                },
            },
            "distribution_policy": {
                "distribute_re_cashflow_annually": True,
                "distribute_hf_realized_gains_annually": False,
                "hf_positive_return_harvest_rate": hf_harvest_rate,
                "retain_cash_until_hurdle_redemption": False,
            },
            "cashflow_routing": {
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
            },
            "reserve": {"annual_return": 0.0},
            "reporting": {"output_excel": True, "output_csv": True, "output_markdown": True},
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
                "long_zero_distribution_years": 3,
            },
            "gp_survivability": {
                "first_n_years": 5,
                "minimum_cumulative_fees": 0,
                "minimum_average_annual_fees": 0,
            },
        }
    )


def routing_scenario(*, years: int = 1, noi_yield: float = 0.20, hf_returns: list[float] | None = None) -> Scenario:
    return Scenario.model_validate(
        {
            "description": "Synthetic routing test scenario.",
            "years": years,
            "real_estate": {
                "initial_noi_yield": noi_yield,
                "annual_noi_growth": 0.0,
                "annual_nav_appreciation": 0.0,
                "gross_rent_yield": 0.0,
            },
            "hedge_fund": {"annual_returns": hf_returns or [0.0] * years},
        }
    )


def test_routing_percentages_must_sum_to_one() -> None:
    with pytest.raises(ValidationError):
        CashflowRoute(lp_distribution_pct=0.50, hf_reinvestment_pct=0.30, reserve_pct=0.10)


def test_re_cashflow_routes_to_lp_hf_and_reserve() -> None:
    result = run_scenario("re_routing", routing_scenario(), routing_config())
    row = result.cashflows[0]

    assert row.re_cashflow_generated == pytest.approx(1_000_000)
    assert row.re_cashflow_to_lp == pytest.approx(500_000)
    assert row.re_cashflow_to_hf == pytest.approx(300_000)
    assert row.re_cashflow_to_reserve == pytest.approx(200_000)


def test_hf_harvest_routes_to_lp_hf_and_reserve() -> None:
    config = routing_config(hf_harvest_rate=1.0)
    result = run_scenario("hf_routing", routing_scenario(noi_yield=0.0, hf_returns=[0.40]), config)
    row = result.cashflows[0]

    assert row.hf_harvest_generated == pytest.approx(2_000_000)
    assert row.hf_harvest_to_lp == pytest.approx(1_400_000)
    assert row.hf_harvest_to_hf == pytest.approx(400_000)
    assert row.hf_harvest_to_reserve == pytest.approx(200_000)


def test_hf_reinvestment_increases_future_hf_nav() -> None:
    result = run_scenario("reinvestment_compounding", routing_scenario(years=2), routing_config())

    assert result.cashflows[0].hf_closing_nav == pytest.approx(5_300_000)
    assert result.cashflows[1].hf_opening_nav == pytest.approx(5_300_000)


def test_lp_cumulative_distributions_include_routed_cashflows() -> None:
    result = run_scenario("lp_distribution_timing", routing_scenario(), routing_config())
    row = result.cashflows[0]

    assert row.lp_distribution == pytest.approx(500_000)
    assert row.lp_cumulative_distribution == pytest.approx(500_000)
    assert result.summary["total_distributed_to_lp"] == pytest.approx(500_000)


def test_large_hf_nav_and_reserve_liquidity_extinguishes_lp_and_creates_gp_residual() -> None:
    config_data = routing_config(hf_harvest_rate=0.0).model_dump()
    config_data["allocation"] = {
        "method": "fixed",
        "hedge_fund_allocation_pct": 1.0,
        "real_estate_allocation_pct": 0.0,
        "reserve_allocation_pct": 0.0,
    }
    config_data["waterfall"]["lp_hurdle_moic"] = 2.0
    config = ModelConfig.model_validate(config_data)
    scenario = routing_scenario(years=1, noi_yield=0.0, hf_returns=[1.5])

    result = run_scenario("hf_liquidity_redemption", scenario, config)

    assert result.summary["lp_hurdle_achieved"] is True
    assert result.summary["lp_cash_moic"] == pytest.approx(2.0)
    assert result.summary["gp_residual_nav"] == pytest.approx(5_000_000)
