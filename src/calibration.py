from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
from pydantic import BaseModel, Field, ValidationError, field_validator

from src.config_loader import ConfigError, load_yaml
from src.engine import run_scenario
from src.model_types import ModelConfig, Scenario, ScenarioResult, ScenarioSet, pydantic_error_message
from src.outputs import write_excel
from src.reporting import write_markdown_report


class CalibrationVariant(BaseModel):
    label: str
    description: str = ""
    config_overrides: dict[str, Any] = Field(default_factory=dict)
    scenario_overrides: dict[str, Any] = Field(default_factory=dict)
    extend_hf_returns_by_repeating_last: bool = False


class CalibrationTest(BaseModel):
    description: str
    base_scenarios: list[str]
    variants: list[CalibrationVariant]

    @field_validator("base_scenarios", "variants")
    @classmethod
    def non_empty(cls, value: list[Any]) -> list[Any]:
        if not value:
            raise ValueError("Calibration tests require at least one base scenario and one variant.")
        return value


class CalibrationSuite(BaseModel):
    calibration_tests: dict[str, CalibrationTest]

    @field_validator("calibration_tests")
    @classmethod
    def tests_required(cls, value: dict[str, CalibrationTest]) -> dict[str, CalibrationTest]:
        if not value:
            raise ValueError("calibration_tests.yaml must contain at least one calibration test.")
        return value


def load_calibration_suite(path: Path) -> CalibrationSuite:
    try:
        return CalibrationSuite.model_validate(load_yaml(path))
    except ValidationError as exc:
        raise ConfigError(pydantic_error_message(str(path), exc)) from exc


def run_calibration_suite(
    *,
    config: ModelConfig,
    scenarios: ScenarioSet,
    suite: CalibrationSuite,
) -> list[ScenarioResult]:
    results: list[ScenarioResult] = []
    for test_name, test in suite.calibration_tests.items():
        for base_name in test.base_scenarios:
            if base_name not in scenarios.scenarios:
                raise ConfigError(f"Calibration test '{test_name}' references unknown scenario '{base_name}'.")
            base_scenario = scenarios.scenarios[base_name]
            for variant in test.variants:
                variant_config = build_variant_config(config, variant)
                variant_scenario = build_variant_scenario(base_scenario, variant)
                scenario_name = f"{test_name}__{base_name}__{variant.label}"
                result = run_scenario(scenario_name, variant_scenario, variant_config)
                result.summary["description"] = combined_description(test, base_scenario, variant)
                results.append(result)
    return results


def build_variant_config(config: ModelConfig, variant: CalibrationVariant) -> ModelConfig:
    if not variant.config_overrides:
        return config
    config_data = deep_merge(config.model_dump(), variant.config_overrides)
    return ModelConfig.model_validate(config_data)


def build_variant_scenario(scenario: Scenario, variant: CalibrationVariant) -> Scenario:
    scenario_data = deep_merge(scenario.model_dump(), variant.scenario_overrides)
    if variant.extend_hf_returns_by_repeating_last:
        years = int(scenario_data["years"])
        returns = list(scenario_data["hedge_fund"]["annual_returns"])
        if len(returns) < years:
            returns.extend([returns[-1]] * (years - len(returns)))
            scenario_data["hedge_fund"]["annual_returns"] = returns
    return Scenario.model_validate(scenario_data)


def deep_merge(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in overrides.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def combined_description(test: CalibrationTest, base_scenario: Scenario, variant: CalibrationVariant) -> str:
    parts = [test.description, base_scenario.description]
    if variant.description:
        parts.append(variant.description)
    return " | ".join(parts)


def write_calibration_outputs(
    *,
    results: list[ScenarioResult],
    config: ModelConfig,
    scenarios: ScenarioSet,
    output_dir: Path,
) -> dict[str, pd.DataFrame]:
    from src.engine import result_dicts
    from src.outputs import CASHFLOW_COLUMNS, DEAL_CASHFLOW_COLUMNS, SUMMARY_COLUMNS

    output_dir.mkdir(parents=True, exist_ok=True)
    summaries, cashflows, flags, deal_cashflows = result_dicts(results)
    summary_df = pd.DataFrame(summaries).reindex(columns=SUMMARY_COLUMNS)
    cashflow_df = pd.DataFrame(cashflows).reindex(columns=CASHFLOW_COLUMNS)
    flags_df = pd.DataFrame(flags).reindex(columns=["scenario", "flag", "severity", "explanation"])
    deal_cashflow_df = pd.DataFrame(deal_cashflows).reindex(columns=DEAL_CASHFLOW_COLUMNS)

    summary_df.to_csv(output_dir / "calibration_summary.csv", index=False)
    cashflow_df.to_csv(output_dir / "calibration_cashflows.csv", index=False)
    flags_df.to_csv(output_dir / "calibration_flags.csv", index=False)
    deal_cashflow_df.to_csv(output_dir / "calibration_deal_cashflows.csv", index=False)
    write_excel(output_dir / "calibration_summary.xlsx", summary_df, cashflow_df, flags_df, deal_cashflow_df, config, scenarios)
    write_markdown_report(results, summary_df, output_dir / "calibration_report.md")
    return {"summary": summary_df, "cashflows": cashflow_df, "flags": flags_df}
