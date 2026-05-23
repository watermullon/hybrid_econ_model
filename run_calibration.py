from __future__ import annotations

from pathlib import Path

from src.calibration import load_calibration_suite, run_calibration_suite, write_calibration_outputs
from src.config_loader import ConfigError, load_inputs


def main() -> None:
    root = Path(__file__).resolve().parent
    try:
        config, scenarios, _ = load_inputs(root / "inputs")
        suite = load_calibration_suite(root / "inputs" / "calibration_tests.yaml")
        results = run_calibration_suite(config=config, scenarios=scenarios, suite=suite)
        write_calibration_outputs(results=results, config=config, scenarios=scenarios, output_dir=root / "outputs")
    except PermissionError as exc:
        raise SystemExit(
            "Calibration failed: could not write one or more output files. "
            "If an output workbook or CSV is open, close it and run python run_calibration.py again."
        ) from exc
    except (ConfigError, ValueError) as exc:
        raise SystemExit(f"Calibration failed: {exc}") from exc

    print(f"Ran {len(results)} calibration scenario variants.")
    print("Calibration outputs written to outputs/")


if __name__ == "__main__":
    main()
