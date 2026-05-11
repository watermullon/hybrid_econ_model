from src.metrics import annual_irr, economic_moic, moic


def test_moic_calculation() -> None:
    assert moic(20_000_000, 10_000_000) == 2.0


def test_economic_moic_calculation() -> None:
    assert economic_moic(5_000_000, 8_000_000, 10_000_000) == 1.3


def test_irr_simple_cashflows() -> None:
    result = annual_irr([-100, 60, 60])
    assert result is not None
    assert round(result, 4) == 0.1307


def test_irr_handles_no_positive_return() -> None:
    assert annual_irr([-100, 0, 0]) is None
