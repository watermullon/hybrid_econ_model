from __future__ import annotations

from dataclasses import asdict, is_dataclass
from copy import deepcopy
from typing import Any, TypeVar

from pydantic import BaseModel


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


def deep_merge_dict(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge overrides into base without mutating either input."""
    merged = deepcopy(base)
    for key, override_value in overrides.items():
        base_value = merged.get(key)
        if isinstance(base_value, dict) and isinstance(override_value, dict):
            merged[key] = deep_merge_dict(base_value, override_value)
        else:
            merged[key] = deepcopy(override_value)
    return merged


T = TypeVar("T", bound=BaseModel)


def merge_model(base: T, overrides: dict[str, Any] | None) -> T:
    """Return a Pydantic model copy with nested overrides applied and revalidated."""
    if not overrides:
        return base
    merged = deep_merge_dict(base.model_dump(), overrides)
    return type(base).model_validate(merged)
