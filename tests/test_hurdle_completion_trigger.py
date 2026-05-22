from __future__ import annotations

import pytest

from src.engine import run_scenario
from src.model_types import ModelConfig, Scenario


def trigger_config(
    *,
    allocation: dict[str, float],
    lp_hurdle_moic: float = 2.0,
    minimum_cash_moic: float = 0.0,
    max_hf_liquidation_pct: float = 1.0,
    max_refi_pct: float = 0.0,
    allow_refi: bool = False,
    reserve_liquidity_pct: float = 1.0,
    passive_liquidity_pct: float = 0.0,
    backend_liquidity_strategy: dict | None = None,
) -> ModelConfig:
    config_data = {
            "model": {
                "currency": "USD",
                "periods_per_year": 1,
                "max_years": 1,
                "initial_lp_capital": 10_000_000,
                "gp_co_investment": 0,
            },
            "allocation": {"method": "fixed", **allocation},
            "waterfall": {
                "lp_hurdle_moic": lp_hurdle_moic,
                "lp_receives_100_percent_until_hurdle": True,
                "gp_receives_residual_after_lp_hurdle": True,
                "include_unrealized_nav_in_hurdle_test": True,
                "require_liquidity_for_lp_redemption": True,
            },
            "liquidity": {
                "hf_liquidation_allowed": False,
                "hf_liquidation_capacity_pct_per_year": 0.0,
                "reserve_liquidation_capacity_pct_per_year": reserve_liquidity_pct,
                "real_estate_liquidation_capacity_pct_per_year": 0.0,
                "max_refinance_or_sale_capacity_pct_of_re_nav": passive_liquidity_pct,
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
                "distribute_re_cashflow_annually": False,
                "distribute_hf_realized_gains_annually": False,
                "hf_positive_return_harvest_rate": 0.0,
                "retain_cash_until_hurdle_redemption": True,
            },
            "cashflow_routing": {
                "enabled": False,
                "re_cashflow": {"lp_distribution_pct": 1.0, "hf_reinvestment_pct": 0.0, "reserve_pct": 0.0},
                "hf_harvest": {"lp_distribution_pct": 0.0, "hf_reinvestment_pct": 0.0, "reserve_pct": 1.0},
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
            "hurdle_completion_trigger": {
                "enabled": True,
                "trigger_when_economic_hurdle_passed": True,
                "minimum_lp_cash_moic_before_trigger": minimum_cash_moic,
                "max_hf_liquidation_pct": max_hf_liquidation_pct,
                "max_refi_pct_of_re_nav": max_refi_pct,
                "allow_retained_cash_use": True,
                "allow_reserve_use": True,
                "allow_hf_liquidation": True,
                "allow_refi": allow_refi,
                "allow_partial_re_sale": False,
                "max_partial_re_sale_pct_of_re_nav": 0.0,
                "execute_only_if_lp_fully_redeemed": True,
            },
        }
    if backend_liquidity_strategy is not None:
        config_data["backend_liquidity_strategy"] = backend_liquidity_strategy
    return ModelConfig.model_validate(config_data)


def scenario(
    *,
    noi_yield: float = 0.0,
    re_appreciation: float = 0.0,
    hf_return: float = 0.0,
) -> Scenario:
    return Scenario.model_validate(
        {
            "description": "Synthetic hurdle trigger scenario.",
            "years": 1,
            "real_estate": {
                "initial_noi_yield": noi_yield,
                "annual_noi_growth": 0.0,
                "annual_nav_appreciation": re_appreciation,
                "gross_rent_yield": 0.0,
            },
            "hedge_fund": {"annual_returns": [hf_return]},
        }
    )


def test_trigger_executes_using_retained_cash_only() -> None:
    config = trigger_config(
        allocation={
            "hedge_fund_allocation_pct": 0.0,
            "real_estate_allocation_pct": 1.0,
            "reserve_allocation_pct": 0.0,
        }
    )

    result = run_scenario("retained_cash_trigger", scenario(noi_yield=2.0), config)
    row = result.cashflows[0]

    assert row.hurdle_trigger_executed is True
    assert row.trigger_cash_from_retained_cash == pytest.approx(20_000_000)
    assert row.lp_cumulative_distribution == pytest.approx(20_000_000)
    assert result.summary["lp_cash_moic"] == pytest.approx(2.0)


def test_trigger_executes_using_reserve_and_hf_liquidation() -> None:
    config = trigger_config(
        allocation={
            "hedge_fund_allocation_pct": 0.50,
            "real_estate_allocation_pct": 0.0,
            "reserve_allocation_pct": 0.50,
        },
        lp_hurdle_moic=1.5,
        max_hf_liquidation_pct=1.0,
    )

    result = run_scenario("reserve_hf_trigger", scenario(hf_return=1.0), config)
    row = result.cashflows[0]

    assert row.hurdle_trigger_executed is True
    assert row.trigger_cash_from_reserve == pytest.approx(5_000_000)
    assert row.trigger_cash_from_hf_liquidation == pytest.approx(10_000_000)
    assert row.reserve_closing_nav == pytest.approx(0)
    assert row.hf_closing_nav == pytest.approx(0)


def test_trigger_executes_using_reserve_hf_and_refi_without_re_nav_reduction() -> None:
    config = trigger_config(
        allocation={
            "hedge_fund_allocation_pct": 0.25,
            "real_estate_allocation_pct": 0.50,
            "reserve_allocation_pct": 0.25,
        },
        lp_hurdle_moic=1.5,
        max_hf_liquidation_pct=1.0,
        max_refi_pct=0.25,
        allow_refi=True,
    )

    result = run_scenario("reserve_hf_refi_trigger", scenario(re_appreciation=1.0, hf_return=3.0), config)
    row = result.cashflows[0]

    assert row.hurdle_trigger_executed is True
    assert row.trigger_cash_from_reserve == pytest.approx(2_500_000)
    assert row.trigger_cash_from_hf_liquidation == pytest.approx(10_000_000)
    assert row.trigger_cash_from_refi == pytest.approx(2_500_000)
    assert row.re_closing_nav == pytest.approx(10_000_000)
    assert row.refinance_liability == pytest.approx(2_500_000)
    assert row.fund_nav == pytest.approx(7_500_000)
    assert result.summary["gp_residual_nav"] == pytest.approx(7_500_000)
    assert row.refi_proceeds_for_hurdle == pytest.approx(2_500_000)


def test_trigger_does_not_execute_if_total_funding_is_insufficient() -> None:
    config = trigger_config(
        allocation={
            "hedge_fund_allocation_pct": 0.50,
            "real_estate_allocation_pct": 0.0,
            "reserve_allocation_pct": 0.50,
        },
        lp_hurdle_moic=2.0,
        max_hf_liquidation_pct=0.25,
    )

    result = run_scenario("insufficient_trigger", scenario(hf_return=3.0), config)
    row = result.cashflows[0]

    assert row.hurdle_trigger_attempted is True
    assert row.hurdle_trigger_executed is False
    assert row.lp_hurdle_shortfall_after_trigger == pytest.approx(10_000_000)
    assert result.summary["lp_hurdle_achieved"] is False
    assert "HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT" in result.summary["all_flags"]


def test_trigger_does_not_execute_below_minimum_lp_cash_moic_threshold() -> None:
    config = trigger_config(
        allocation={
            "hedge_fund_allocation_pct": 0.50,
            "real_estate_allocation_pct": 0.0,
            "reserve_allocation_pct": 0.50,
        },
        lp_hurdle_moic=1.5,
        minimum_cash_moic=1.0,
    )

    result = run_scenario("below_threshold_trigger", scenario(hf_return=1.0), config)
    row = result.cashflows[0]

    assert row.hurdle_trigger_eligible is False
    assert row.hurdle_trigger_attempted is False
    assert row.hurdle_trigger_executed is False
    assert result.summary["lp_hurdle_achieved"] is False


def test_trigger_minimum_cash_moic_cannot_exceed_lp_hurdle() -> None:
    with pytest.raises(ValueError, match="Trigger minimum LP cash MOIC"):
        trigger_config(
            allocation={
                "hedge_fund_allocation_pct": 1.0,
                "real_estate_allocation_pct": 0.0,
                "reserve_allocation_pct": 0.0,
            },
            lp_hurdle_moic=1.5,
            minimum_cash_moic=1.75,
        )


def test_backend_strategy_executes_only_in_target_year() -> None:
    config = trigger_config(
        allocation={
            "hedge_fund_allocation_pct": 0.0,
            "real_estate_allocation_pct": 1.0,
            "reserve_allocation_pct": 0.0,
        },
        allow_refi=True,
        backend_liquidity_strategy={
            "enabled": True,
            "target_years": [2],
            "refi_first": True,
            "max_refi_pct_of_re_nav": 1.0,
            "max_hf_liquidation_pct": 0.0,
            "use_retained_cash": True,
            "use_reserve": False,
            "execute_only_if_lp_hurdle_completed": True,
        },
    )

    result = run_scenario("backend_not_target_year", scenario(re_appreciation=1.0), config)
    row = result.cashflows[0]

    assert row.economic_hurdle_passed is True
    assert row.hurdle_trigger_attempted is False
    assert row.hurdle_trigger_executed is False


def test_backend_strategy_is_refi_led_before_hf_liquidation() -> None:
    config = trigger_config(
        allocation={
            "hedge_fund_allocation_pct": 0.50,
            "real_estate_allocation_pct": 0.50,
            "reserve_allocation_pct": 0.0,
        },
        lp_hurdle_moic=1.5,
        max_hf_liquidation_pct=1.0,
        allow_refi=True,
        backend_liquidity_strategy={
            "enabled": True,
            "target_years": [1],
            "refi_first": True,
            "max_refi_pct_of_re_nav": 1.0,
            "max_hf_liquidation_pct": 1.0,
            "use_retained_cash": True,
            "use_reserve": False,
            "execute_only_if_lp_hurdle_completed": True,
        },
    )

    result = run_scenario("backend_refi_first", scenario(re_appreciation=1.0, hf_return=1.0), config)
    row = result.cashflows[0]

    assert row.hurdle_trigger_executed is True
    assert row.trigger_cash_from_refi == pytest.approx(10_000_000)
    assert row.trigger_cash_from_hf_liquidation == pytest.approx(5_000_000)
    assert row.refinance_liability == pytest.approx(10_000_000)
