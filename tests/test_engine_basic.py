from pathlib import Path

from src.config_loader import load_inputs
from src.engine import calculate_initial_allocation, run_all_scenarios
from src.outputs import SUMMARY_COLUMNS


ROOT = Path(__file__).resolve().parents[1]


def test_base_scenario_runs_without_error() -> None:
    config, scenario_set = load_inputs(ROOT / "inputs")
    result = run_all_scenarios(config, {"base_hit_everyone_happy": scenario_set.scenarios["base_hit_everyone_happy"]})[0]
    assert result.summary["scenario"] == "base_hit_everyone_happy"
    assert result.cashflows


def test_all_scenarios_produce_summary_rows() -> None:
    config, scenario_set = load_inputs(ROOT / "inputs")
    results = run_all_scenarios(config, scenario_set.scenarios)
    assert len(results) == len(scenario_set.scenarios)


def test_summary_columns_exist() -> None:
    config, scenario_set = load_inputs(ROOT / "inputs")
    result = run_all_scenarios(config, {"base_hit_everyone_happy": scenario_set.scenarios["base_hit_everyone_happy"]})[0]
    assert set(SUMMARY_COLUMNS).issubset(result.summary.keys())


def test_allocation_percentages_sum_to_capital() -> None:
    config, scenario_set = load_inputs(ROOT / "inputs")
    re_nav, hf_nav, reserve_nav = calculate_initial_allocation(config, scenario_set.scenarios["base_hit_everyone_happy"])
    assert round(re_nav + hf_nav + reserve_nav, 2) == config.model.initial_lp_capital
