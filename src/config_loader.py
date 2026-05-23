from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from src.deal_types import DealSet
from src.model_types import ModelConfig, ScenarioSet, pydantic_error_message


class ConfigError(RuntimeError):
    """Raised when YAML assumptions are missing, malformed, or fail validation."""


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Required input file not found: {path}")
    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        raise ConfigError(f"Could not parse YAML file {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ConfigError(f"YAML file must contain a mapping at top level: {path}")
    return data


def load_model_config(path: Path) -> ModelConfig:
    try:
        return ModelConfig.model_validate(load_yaml(path))
    except ValidationError as exc:
        raise ConfigError(pydantic_error_message(str(path), exc)) from exc


def load_scenarios(path: Path) -> ScenarioSet:
    try:
        return ScenarioSet.model_validate(load_yaml(path))
    except ValidationError as exc:
        raise ConfigError(pydantic_error_message(str(path), exc)) from exc


def load_deals(path: Path) -> DealSet | None:
    if not path.exists():
        return None
    try:
        return DealSet.model_validate(load_yaml(path))
    except ValidationError as exc:
        raise ConfigError(pydantic_error_message(str(path), exc)) from exc


def load_inputs(input_dir: Path) -> tuple[ModelConfig, ScenarioSet, DealSet | None]:
    return (
        load_model_config(input_dir / "model_config.yaml"),
        load_scenarios(input_dir / "scenarios.yaml"),
        load_deals(input_dir / "deals.yaml"),
    )
