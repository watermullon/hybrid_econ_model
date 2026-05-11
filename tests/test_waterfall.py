from src.model_types import LiquiditySettings
from src.waterfall import available_liquidity, pay_lp_distribution, redeem_lp


def test_lp_receives_100_percent_before_hurdle() -> None:
    payment, retained = pay_lp_distribution(500_000, 2_000_000)
    assert payment == 500_000
    assert retained == 0


def test_distribution_stops_at_hurdle() -> None:
    payment, retained = pay_lp_distribution(3_000_000, 2_000_000)
    assert payment == 2_000_000
    assert retained == 1_000_000


def test_gp_receives_residual_after_hurdle() -> None:
    liquidity = LiquiditySettings(
        hf_liquidation_allowed=True,
        hf_liquidation_capacity_pct_per_year=1.0,
        reserve_liquidation_capacity_pct_per_year=1.0,
        real_estate_liquidation_capacity_pct_per_year=0.0,
        max_refinance_or_sale_capacity_pct_of_re_nav=0.25,
    )
    result = redeem_lp(
        lp_remaining_hurdle=1_000_000,
        retained_cash=250_000,
        reserve_nav=250_000,
        hf_nav=1_000_000,
        re_nav=10_000_000,
        liquidity=liquidity,
    )
    assert result.lp_distribution == 1_000_000
    assert result.gp_residual_nav > 0
    assert result.event_flag == "LP_HURDLE_ACHIEVED"


def test_liquidity_constrained_math() -> None:
    liquidity = LiquiditySettings(
        hf_liquidation_allowed=True,
        hf_liquidation_capacity_pct_per_year=0.0,
        reserve_liquidation_capacity_pct_per_year=0.0,
        real_estate_liquidation_capacity_pct_per_year=0.0,
        max_refinance_or_sale_capacity_pct_of_re_nav=0.05,
    )
    assert available_liquidity(reserve_nav=0, hf_nav=0, re_nav=10_000_000, retained_cash=0, liquidity=liquidity) == 500_000
