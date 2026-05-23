from pathlib import Path

from src.calibration import build_variant_scenario, load_calibration_suite, run_calibration_suite
from src.config_loader import load_inputs


ROOT = Path(__file__).resolve().parents[1]


def test_calibration_suite_loads() -> None:
    suite = load_calibration_suite(ROOT / "inputs" / "calibration_tests.yaml")
    assert "lp_distribution_strategy_sweep" in suite.calibration_tests
    assert "hf_allocation_sensitivity" in suite.calibration_tests
    assert "twenty_year_horizon" in suite.calibration_tests


def test_twenty_year_variant_extends_hf_returns() -> None:
    _, scenario_set, _ = load_inputs(ROOT / "inputs")
    suite = load_calibration_suite(ROOT / "inputs" / "calibration_tests.yaml")
    variant = suite.calibration_tests["twenty_year_horizon"].variants[0]

    scenario = build_variant_scenario(scenario_set.scenarios["base_hit_everyone_happy"], variant)

    assert scenario.years == 20
    assert len(scenario.hedge_fund.annual_returns) == 20
    assert scenario.hedge_fund.annual_returns[-1] == scenario_set.scenarios["base_hit_everyone_happy"].hedge_fund.annual_returns[-1]


def test_calibration_suite_runs_expected_number_of_variants() -> None:
    config, scenario_set, _ = load_inputs(ROOT / "inputs")
    suite = load_calibration_suite(ROOT / "inputs" / "calibration_tests.yaml")
    expected_count = sum(
        len(test.base_scenarios) * len(test.variants)
        for test in suite.calibration_tests.values()
    )

    results = run_calibration_suite(config=config, scenarios=scenario_set, suite=suite)

    assert len(results) == expected_count
    assert all("__" in result.scenario for result in results)


def test_lp_distribution_strategy_sweep_has_eight_variants() -> None:
    suite = load_calibration_suite(ROOT / "inputs" / "calibration_tests.yaml")
    test = suite.calibration_tests["lp_distribution_strategy_sweep"]

    labels = [variant.label for variant in test.variants]

    assert labels == [
        "lp_distribution_20",
        "lp_distribution_30",
        "lp_distribution_40",
        "lp_distribution_50",
        "lp_distribution_60",
        "lp_distribution_70",
        "lp_distribution_80",
        "lp_distribution_90",
    ]
