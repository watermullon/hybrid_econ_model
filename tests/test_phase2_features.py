from __future__ import annotations

import pytest

from src.engine import run_scenario
from src.metrics import annual_irr
from src.model_types import ModelConfig, Scenario


def phase2_config(
    *,
    allocation: tuple[float, float, float],
    lp_hurdle_moic: float = 3.0,
    cash_yield_enabled: bool = False,
    cash_yield_target: float = 0.0,
    distribute_re_cashflow_annually: bool = False,
    distribute_hf_realized_gains_annually: bool = False,
    hf_harvest_rate: float = 0.0,
    gp_fee_threshold: float = 500_000,
) -> ModelConfig:
    hf_pct, re_pct, reserve_pct = allocation
    return ModelConfig.model_validate(
        {
            "model": {
                "currency": "USD",
                "periods_per_year": 1,
                "max_years": 10,
                "initial_lp_capital": 10_000_000,
                "gp_co_investment": 0,
            },
            "allocation": {
                "method": "fixed",
                "hedge_fund_allocation_pct": hf_pct,
                "real_estate_allocation_pct": re_pct,
                "reserve_allocation_pct": reserve_pct,
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
                    "enabled": False,
                    "rate": 0.0,
                    "basis": "gross_rent",
                },
                "hedge_fund_fees": {
                    "model_as_net_returns": True,
                    "management_fee_rate": 0.0,
                    "performance_fee_rate": 0.0,
                },
            },
            "distribution_policy": {
                "distribute_re_cashflow_annually": distribute_re_cashflow_annually,
                "distribute_hf_realized_gains_annually": distribute_hf_realized_gains_annually,
                "hf_positive_return_harvest_rate": hf_harvest_rate,
                "retain_cash_until_hurdle_redemption": False,
            },
            "lp_cash_yield_policy": {
                "enabled": cash_yield_enabled,
                "target_annual_yield_on_unreturned_capital": cash_yield_target,
                "source_priority": ["net_re_cashflow", "hf_harvest", "retained_cash", "reserve"],
                "reduce_lp_hurdle": True,
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
                "long_zero_distribution_years": 3,
            },
            "gp_survivability": {
                "first_n_years": 5,
                "minimum_cumulative_fees": gp_fee_threshold,
                "minimum_average_annual_fees": gp_fee_threshold / 5,
            },
        }
    )


def scenario(
    *,
    years: int,
    noi_yield: float = 0.0,
    hf_returns: list[float] | None = None,
    refinance_events: list[dict] | None = None,
) -> Scenario:
    return Scenario.model_validate(
        {
            "description": "Synthetic Phase 2 test scenario.",
            "years": years,
            "real_estate": {
                "initial_noi_yield": noi_yield,
                "annual_noi_growth": 0.0,
                "annual_nav_appreciation": 0.0,
                "gross_rent_yield": 0.0,
            },
            "hedge_fund": {"annual_returns": hf_returns or [0.0] * years},
            "refinance_events": refinance_events or [],
        }
    )


def test_lp_cash_irr_for_100_to_200_in_year_4() -> None:
    assert annual_irr([-100, 0, 0, 0, 200]) == pytest.approx(0.1892, abs=0.0001)


def test_cash_yield_shortfall_uses_available_re_cash() -> None:
    config = phase2_config(allocation=(0.0, 1.0, 0.0), cash_yield_enabled=True, cash_yield_target=0.05)
    result = run_scenario("cash_yield_shortfall", scenario(years=1, noi_yield=0.03), config)
    row = result.cashflows[0]

    assert row.lp_cash_yield_target == pytest.approx(500_000)
    assert row.lp_cash_yield_paid == pytest.approx(300_000)
    assert row.lp_cash_yield_shortfall == pytest.approx(200_000)
    assert "LP_CASH_YIELD_SHORTFALL" in result.summary["all_flags"]


def test_cash_yield_full_coverage_does_not_flag_shortfall() -> None:
    config = phase2_config(allocation=(0.0, 1.0, 0.0), cash_yield_enabled=True, cash_yield_target=0.05)
    result = run_scenario("cash_yield_full", scenario(years=1, noi_yield=0.07), config)
    row = result.cashflows[0]

    assert row.lp_cash_yield_target == pytest.approx(500_000)
    assert row.lp_cash_yield_paid == pytest.approx(500_000)
    assert row.lp_cash_yield_shortfall == pytest.approx(0)
    assert "LP_CASH_YIELD_SHORTFALL" not in result.summary["all_flags"]


def test_refinance_event_distributes_proceeds_to_lp() -> None:
    config = phase2_config(allocation=(0.0, 1.0, 0.0), lp_hurdle_moic=3.0)
    result = run_scenario(
        "refi_distribution",
        scenario(
            years=1,
            refinance_events=[
                {
                    "year": 1,
                    "pct_of_re_nav": 0.20,
                    "use_of_proceeds": "lp_distribution",
                    "description": "Synthetic refi event.",
                }
            ],
        ),
        config,
    )
    row = result.cashflows[0]

    assert row.refinance_proceeds == pytest.approx(2_000_000)
    assert row.refinance_liability == pytest.approx(2_000_000)
    assert row.re_closing_nav == pytest.approx(10_000_000)
    assert row.fund_nav == pytest.approx(8_000_000)
    assert row.lp_cumulative_distribution == pytest.approx(2_000_000)
    assert "REFINANCE_EVENT_OCCURRED" in result.summary["all_flags"]
    assert result.summary["final_refinance_liability"] == pytest.approx(2_000_000)


def test_refinance_event_to_reserve_updates_annual_and_summary_reserved_cash() -> None:
    config = phase2_config(allocation=(0.0, 1.0, 0.0), lp_hurdle_moic=3.0)
    result = run_scenario(
        "refi_to_reserve",
        scenario(
            years=1,
            refinance_events=[
                {
                    "year": 1,
                    "pct_of_re_nav": 0.20,
                    "use_of_proceeds": "reserve",
                    "description": "Synthetic reserve refi event.",
                }
            ],
        ),
        config,
    )
    row = result.cashflows[0]

    assert row.refinance_proceeds == pytest.approx(2_000_000)
    assert row.reserve_closing_nav == pytest.approx(2_000_000)
    assert row.total_cash_reserved == pytest.approx(2_000_000)
    assert row.cumulative_cash_added_to_reserve == pytest.approx(2_000_000)
    assert result.summary["total_added_to_reserve"] == pytest.approx(2_000_000)
    assert result.summary["total_distributed_to_lp"] == pytest.approx(row.lp_cumulative_distribution)


def test_cash_yield_policy_cannot_ignore_cash_hurdle_reduction() -> None:
    with pytest.raises(ValueError, match="cash yield distributions must reduce the LP hurdle"):
        ModelConfig.model_validate(
            {
                **phase2_config(allocation=(0.0, 1.0, 0.0)).model_dump(),
                "lp_cash_yield_policy": {
                    "enabled": True,
                    "target_annual_yield_on_unreturned_capital": 0.05,
                    "source_priority": ["net_re_cashflow"],
                    "reduce_lp_hurdle": False,
                },
            }
        )


def test_gp_survivability_risk_triggers_when_first_five_year_fees_are_low() -> None:
    config = phase2_config(allocation=(0.0, 1.0, 0.0), gp_fee_threshold=500_000)
    result = run_scenario("gp_survivability", scenario(years=5, noi_yield=0.0), config)

    assert result.summary["gp_cumulative_fees_first_n_years"] == pytest.approx(0)
    assert result.summary["gp_survivability_risk"] is True
    assert "GP_SURVIVABILITY_RISK" in result.summary["all_flags"]


def test_lp_experience_profile_tracks_zero_distribution_streak() -> None:
    config = phase2_config(
        allocation=(1.0, 0.0, 0.0),
        distribute_hf_realized_gains_annually=True,
        hf_harvest_rate=1.0,
    )
    result = run_scenario("lp_experience", scenario(years=4, hf_returns=[0.0, 0.0, 0.0, 1.0]), config)

    assert result.summary["longest_zero_distribution_streak"] == 3
    assert result.summary["years_until_first_distribution"] == 4
    assert "LONG_ZERO_DISTRIBUTION_PERIOD" in result.summary["all_flags"]
