from __future__ import annotations

from src.deal_types import DealSet
from src.model_types import ModelConfig, Scenario
from src.utils import merge_model


def validate_scenario_against_config(
    name: str,
    scenario: Scenario,
    config: ModelConfig,
    deals: DealSet | None = None,
) -> None:
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
    real_estate_settings = merge_model(config.real_estate, scenario.real_estate_model)
    if real_estate_settings.mode == "bottom_up":
        if deals is None:
            raise ValueError(f"Scenario '{name}' uses bottom_up real estate mode but inputs/deals.yaml was not loaded.")
        if not any(deal.enabled for deal in deals.deals.values()):
            raise ValueError(f"Scenario '{name}' uses bottom_up real estate mode but no enabled deals were provided.")
        if len(scenario.hedge_fund.annual_returns) < scenario.years:
            raise ValueError(
                f"Scenario '{name}' requires {scenario.years} hedge fund returns but only "
                f"{len(scenario.hedge_fund.annual_returns)} were provided."
            )


def validate_all_scenarios(config: ModelConfig, scenarios: dict[str, Scenario], deals: DealSet | None = None) -> None:
    for name, scenario in scenarios.items():
        validate_scenario_against_config(name, scenario, config, deals)
