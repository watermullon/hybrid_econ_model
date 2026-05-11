from __future__ import annotations

import math

import numpy_financial as npf


def moic(distributions: float, initial_capital: float) -> float:
    if initial_capital <= 0:
        raise ValueError("Initial capital must be positive for MOIC.")
    return distributions / initial_capital


def economic_moic(distributions: float, remaining_nav_claim: float, initial_capital: float) -> float:
    if initial_capital <= 0:
        raise ValueError("Initial capital must be positive for economic MOIC.")
    return (distributions + remaining_nav_claim) / initial_capital


def annual_irr(cashflows: list[float]) -> float | None:
    """Return annual IRR, or None when the series has no valid solution."""
    if len(cashflows) < 2 or not any(value > 0 for value in cashflows) or not any(value < 0 for value in cashflows):
        return None
    result = float(npf.irr(cashflows))
    if math.isnan(result) or math.isinf(result):
        return None
    return result
