from __future__ import annotations

from src.model_types import ModelConfig, Scenario


def validate_scenario_against_config(name: str, scenario: Scenario, config: ModelConfig) -> None:
    if scenario.years > config.model.max_years:
        raise ValueError(
            f"Scenario '{name}' has years={scenario.years}, greater than max_years={config.model.max_years}."
        )
    if config.allocation.method == "cap_rate_sized":
        hf_pct = scenario.real_estate.initial_noi_yield
        reserve_pct = config.allocation.reserve_allocation_pct
        if hf_pct + reserve_pct > 1:
            raise ValueError(
                f"Scenario '{name}' cap_rate_sized allocation is invalid: "
                "initial_noi_yield plus reserve allocation exceeds 100%."
            )


def validate_all_scenarios(config: ModelConfig, scenarios: dict[str, Scenario]) -> None:
    for name, scenario in scenarios.items():
        validate_scenario_against_config(name, scenario, config)
