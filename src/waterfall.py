from __future__ import annotations

from dataclasses import dataclass

from src.model_types import LiquiditySettings


@dataclass
class RedemptionResult:
    lp_distribution: float
    retained_cash: float
    reserve_nav: float
    hf_nav: float
    re_nav: float
    gp_residual_nav: float
    fund_nav: float
    event_flag: str


def pay_lp_distribution(distributable_cash: float, lp_remaining_hurdle: float) -> tuple[float, float]:
    """LP receives available annual distributions until the hurdle is reached."""
    payment = max(0.0, min(distributable_cash, lp_remaining_hurdle))
    retained_excess = max(0.0, distributable_cash - payment)
    return payment, retained_excess


def available_liquidity(
    *,
    reserve_nav: float,
    hf_nav: float,
    re_nav: float,
    retained_cash: float,
    liquidity: LiquiditySettings,
    refinance_liability: float = 0.0,
) -> float:
    hf_capacity = liquidity.hf_liquidation_capacity_pct_per_year if liquidity.hf_liquidation_allowed else 0.0
    re_capacity = max(0.0, re_nav * liquidity.max_refinance_or_sale_capacity_pct_of_re_nav - refinance_liability)
    return (
        reserve_nav * liquidity.reserve_liquidation_capacity_pct_per_year
        + hf_nav * hf_capacity
        + re_capacity
        + retained_cash
    )


def redeem_lp(
    *,
    lp_remaining_hurdle: float,
    retained_cash: float,
    reserve_nav: float,
    hf_nav: float,
    re_nav: float,
    liquidity: LiquiditySettings,
    refinance_liability: float = 0.0,
) -> RedemptionResult:
    """Fund final LP redemption in the required order and assign residual NAV to GP."""
    remaining = max(0.0, lp_remaining_hurdle)
    payment = remaining

    use_retained = min(retained_cash, remaining)
    retained_cash -= use_retained
    remaining -= use_retained

    reserve_capacity = reserve_nav * liquidity.reserve_liquidation_capacity_pct_per_year
    use_reserve = min(reserve_capacity, remaining)
    reserve_nav -= use_reserve
    remaining -= use_reserve

    hf_capacity_pct = liquidity.hf_liquidation_capacity_pct_per_year if liquidity.hf_liquidation_allowed else 0.0
    hf_capacity = hf_nav * hf_capacity_pct
    use_hf = min(hf_capacity, remaining)
    hf_nav -= use_hf
    remaining -= use_hf

    re_capacity = max(0.0, re_nav * liquidity.max_refinance_or_sale_capacity_pct_of_re_nav - refinance_liability)
    use_re = min(re_capacity, remaining)
    re_nav -= use_re
    remaining -= use_re

    if remaining > 1e-6:
        raise ValueError("LP redemption attempted without enough available liquidity.")

    fund_nav = re_nav + hf_nav + reserve_nav + retained_cash
    return RedemptionResult(
        lp_distribution=payment,
        retained_cash=retained_cash,
        reserve_nav=reserve_nav,
        hf_nav=hf_nav,
        re_nav=re_nav,
        gp_residual_nav=fund_nav,
        fund_nav=fund_nav,
        event_flag="LP_HURDLE_ACHIEVED",
    )
