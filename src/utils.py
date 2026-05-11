from __future__ import annotations

from dataclasses import asdict, is_dataclass
from typing import Any


def value_for_year(value: float | list[float], year: int) -> float:
    """Return a scalar assumption for a one-indexed model year."""
    if isinstance(value, list):
        if year > len(value):
            raise ValueError(f"Missing year {year} value for yearly assumption.")
        return float(value[year - 1])
    return float(value)


def dataclass_to_dict(item: Any) -> dict[str, Any]:
    if is_dataclass(item):
        return asdict(item)
    raise TypeError(f"Expected dataclass instance, got {type(item)!r}.")


def merge_model(base: Any, overrides: dict[str, Any] | None) -> Any:
    """Return a Pydantic model copy with scenario-level overrides applied."""
    if not overrides:
        return base
    return base.model_copy(update=overrides)
