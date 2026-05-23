from pathlib import Path

import pytest

from src.config_loader import load_inputs
from src.engine import calculate_initial_allocation, run_scenario
from src.model_types import Scenario, legacy_cashflow_routing
from src.waterfall import redeem_lp


ROOT = Path(__file__).resolve().parents[1]


def load_base_inputs():
    return load_inputs(ROOT / "inputs")


def test_default_fixed_allocation_matches_yaml_percentages() -> None:
    config, scenario_set, _ = load_base_inputs()
    scenario = scenario_set.scenarios["base_hit_everyone_happy"]

    re_nav, hf_nav, reserve_nav = calculate_initial_allocation(config, scenario)

    assert re_nav == pytest.approx(8_500_000)
    assert hf_nav == pytest.approx(1_000_000)
    assert reserve_nav == pytest.approx(500_000)


def test_cap_rate_sized_allocation_matches_documented_formula() -> None:
    config, scenario_set, _ = load_base_inputs()
    config = config.model_copy(
        update={
            "allocation": config.allocation.model_copy(
                update={
                    "method": "cap_rate_sized",
                    "hedge_fund_allocation_pct": 0.0,
                    "real_estate_allocation_pct": 0.0,
                    "reserve_allocation_pct": 0.05,
                }
            )
        }
    )
    scenario = scenario_set.scenarios["base_hit_everyone_happy"]

    re_nav, hf_nav, reserve_nav = calculate_initial_allocation(config, scenario)

    assert hf_nav == pytest.approx(10_000_000 * scenario.real_estate.initial_noi_yield)
    assert reserve_nav == pytest.approx(500_000)
    assert re_nav == pytest.approx(8_750_000)


def test_real_estate_year_one_noi_fee_and_nav_math() -> None:
    config, scenario_set, _ = load_base_inputs()
    scenario = scenario_set.scenarios["base_hit_everyone_happy"]

    result = run_scenario("base_hit_everyone_happy", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.re_noi_yield == pytest.approx(0.075)
    assert year_one.re_noi == pytest.approx(8_500_000 * 0.075)
    assert year_one.gross_rent == pytest.approx(8_500_000 * 0.12)
    assert year_one.re_asset_mgmt_fee == pytest.approx((8_500_000 * 0.12) * 0.03)
    assert year_one.net_re_cashflow == pytest.approx(year_one.re_noi - year_one.re_asset_mgmt_fee)
    assert year_one.re_closing_nav == pytest.approx(8_500_000 * 1.04)


def test_noi_yield_compounds_by_annual_noi_growth() -> None:
    config, scenario_set, _ = load_base_inputs()
    scenario = scenario_set.scenarios["base_hit_everyone_happy"]

    result = run_scenario("base_hit_everyone_happy", scenario, config)

    assert result.cashflows[1].re_noi_yield == pytest.approx(0.075 * 1.025)
    assert result.cashflows[2].re_noi_yield == pytest.approx(0.075 * (1.025**2))


def test_hf_returns_are_compounded_without_harvest_by_default() -> None:
    config, scenario_set, _ = load_base_inputs()
    config = config.model_copy(update={"cashflow_routing": legacy_cashflow_routing()})
    scenario = scenario_set.scenarios["base_hit_everyone_happy"]

    result = run_scenario("base_hit_everyone_happy", scenario, config)

    assert result.cashflows[0].hf_opening_nav == pytest.approx(1_000_000)
    assert result.cashflows[0].hf_harvest == pytest.approx(0)
    assert result.cashflows[0].hf_closing_nav == pytest.approx(1_000_000 * (1 + scenario.hedge_fund.annual_returns[0]))
    assert result.cashflows[1].hf_opening_nav == pytest.approx(result.cashflows[0].hf_closing_nav)
    assert result.cashflows[1].hf_closing_nav == pytest.approx(result.cashflows[1].hf_opening_nav * (1 + scenario.hedge_fund.annual_returns[1]))


def test_hf_positive_return_harvest_moves_gain_to_retained_cash_when_not_distributed() -> None:
    config, scenario_set, _ = load_base_inputs()
    config = config.model_copy(update={"cashflow_routing": legacy_cashflow_routing()})
    base = scenario_set.scenarios["base_hit_everyone_happy"]
    scenario = base.model_copy(
        update={
            "years": 1,
            "distribution_policy": {
                "hf_positive_return_harvest_rate": 0.50,
                "distribute_hf_realized_gains_annually": False,
            },
        }
    )

    result = run_scenario("hf_harvest_check", scenario, config)
    year_one = result.cashflows[0]

    expected_gain = 1_000_000 * base.hedge_fund.annual_returns[0]
    expected_harvest = expected_gain * 0.50
    assert year_one.hf_harvest == pytest.approx(expected_harvest)
    assert year_one.hf_closing_nav == pytest.approx(1_000_000 + expected_gain - expected_harvest)
    assert year_one.retained_cash == pytest.approx(expected_harvest)


def test_retain_cash_policy_prevents_annual_lp_distributions() -> None:
    config, scenario_set, _ = load_base_inputs()
    config = config.model_copy(update={"cashflow_routing": legacy_cashflow_routing()})
    base = scenario_set.scenarios["base_hit_everyone_happy"]
    scenario = base.model_copy(update={"years": 1, "distribution_policy": {"retain_cash_until_hurdle_redemption": True}})

    result = run_scenario("retain_cash_check", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.lp_distribution == pytest.approx(0)
    assert year_one.retained_cash == pytest.approx(year_one.net_re_cashflow)


def test_reserve_return_compounds_only_inside_reserve_not_retained_cash() -> None:
    config, scenario_set, _ = load_base_inputs()
    config = config.model_copy(
        update={
            "allocation": config.allocation.model_copy(
                update={
                    "hedge_fund_allocation_pct": 0.0,
                    "real_estate_allocation_pct": 0.0,
                    "reserve_allocation_pct": 1.0,
                }
            ),
            "fees": config.fees.model_copy(
                update={
                    "real_estate_asset_management_fee": config.fees.real_estate_asset_management_fee.model_copy(
                        update={"enabled": False}
                    )
                }
            ),
            "reserve": config.reserve.model_copy(update={"annual_return": 0.10}),
        }
    )
    base = scenario_set.scenarios["base_hit_everyone_happy"]
    scenario = base.model_copy(
        update={
            "years": 1,
            "real_estate": base.real_estate.model_copy(
                update={
                    "initial_noi_yield": 0.0,
                    "annual_noi_growth": 0.0,
                    "annual_nav_appreciation": 0.0,
                    "gross_rent_yield": 0.0,
                }
            ),
        }
    )

    result = run_scenario("reserve_return_check", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.reserve_closing_nav == pytest.approx(11_000_000)
    assert year_one.retained_cash == pytest.approx(0)
    assert year_one.fund_nav == pytest.approx(11_000_000)


def test_top_down_negative_re_cashflow_reduces_reserve_not_silently_disappears() -> None:
    config, scenario_set, _ = load_base_inputs()
    config = config.model_copy(
        update={
            "allocation": config.allocation.model_copy(
                update={
                    "hedge_fund_allocation_pct": 0.0,
                    "real_estate_allocation_pct": 0.50,
                    "reserve_allocation_pct": 0.50,
                }
            ),
            "fees": config.fees.model_copy(
                update={
                    "real_estate_asset_management_fee": config.fees.real_estate_asset_management_fee.model_copy(
                        update={"enabled": True, "rate": 0.10, "basis": "re_nav"}
                    )
                }
            ),
        }
    )
    base = scenario_set.scenarios["base_hit_everyone_happy"]
    scenario = base.model_copy(
        update={
            "years": 1,
            "real_estate": base.real_estate.model_copy(
                update={
                    "initial_noi_yield": 0.0,
                    "annual_noi_growth": 0.0,
                    "annual_nav_appreciation": 0.0,
                    "gross_rent_yield": 0.0,
                }
            ),
        }
    )

    result = run_scenario("top_down_re_shortfall_check", scenario, config)
    year_one = result.cashflows[0]

    assert year_one.net_re_cashflow == pytest.approx(-500_000)
    assert year_one.re_cashflow_generated == pytest.approx(0)
    assert year_one.lp_distribution == pytest.approx(0)
    assert year_one.reserve_closing_nav == pytest.approx(4_500_000)
    assert year_one.re_cashflow_shortfall == pytest.approx(0)
    assert year_one.fund_nav == pytest.approx(9_500_000)


def test_redemption_funding_order_uses_retained_cash_then_reserve_then_hf_then_re() -> None:
    config, _, _ = load_base_inputs()

    redemption = redeem_lp(
        lp_remaining_hurdle=1_100_000,
        retained_cash=100_000,
        reserve_nav=200_000,
        hf_nav=900_000,
        re_nav=10_000_000,
        liquidity=config.liquidity,
    )

    assert redemption.retained_cash == pytest.approx(0)
    assert redemption.reserve_nav == pytest.approx(0)
    assert redemption.hf_nav == pytest.approx(100_000)
    assert redemption.re_nav == pytest.approx(10_000_000)
    assert redemption.gp_residual_nav == pytest.approx(10_100_000)


def test_economic_hurdle_can_be_reached_before_liquidity_redemption() -> None:
    config, scenario_set, _ = load_base_inputs()
    # Disable the active trigger to test passive liquidity constraints
    config = config.model_copy(
        update={"hurdle_completion_trigger": config.hurdle_completion_trigger.model_copy(update={"enabled": False})}
    )
    scenario = scenario_set.scenarios["liquidity_trap"]

    result = run_scenario("liquidity_trap", scenario, config)

    constrained_rows = [row for row in result.cashflows if row.event_flag == "HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED"]
    assert constrained_rows
    assert result.summary["liquidity_constrained"] is True
    assert result.summary["lp_hurdle_achieved"] is False


def test_successful_redemption_stops_model_at_hurdle_year() -> None:
    config, scenario_set, _ = load_base_inputs()
    # Disable the active trigger to test standard passive redemption
    config = config.model_copy(
        update={
            "hurdle_completion_trigger": config.hurdle_completion_trigger.model_copy(update={"enabled": False}),
            "backend_liquidity_strategy": config.backend_liquidity_strategy.model_copy(update={"enabled": False}),
        }
    )
    scenario = scenario_set.scenarios["exceptional_dynasty_outcome"]

    result = run_scenario("exceptional_dynasty_outcome", scenario, config)

    assert result.summary["lp_hurdle_achieved"] is True
    assert result.summary["lp_cash_moic"] == pytest.approx(2.0)
    assert result.summary["years_modelled"] == result.summary["year_hurdle_achieved"]
    assert result.cashflows[-1].event_flag == "LP_HURDLE_ACHIEVED"
