# Asher Economic Model

Deterministic annual scenario model for a hybrid fund structure with real estate, hedge fund, reserve, and a non-standard LP/GP waterfall.

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python run_model.py
```

Outputs are written to `outputs/`:

- `scenario_summary.csv`
- `scenario_summary.xlsx`
- `scenario_cashflows.csv`
- `scenario_flags.csv`
- `scenario_report.md`

## Edit Assumptions

All human-editable assumptions live in YAML:

- `inputs/model_config.yaml` for global assumptions, waterfall settings, fees, liquidity, distribution policy, and flag thresholds.
- `inputs/scenarios.yaml` for named scenario assumptions.

The Python code contains logic, validation, calculations, and output formatting only.

## Interpret Results

Cash MOIC is based only on actual LP distributions. Economic MOIC may include the LP's remaining NAV claim when the hurdle has not been redeemed. The model separately tests whether the 2.0x hurdle is economically reached and whether sufficient liquidity exists to redeem LPs.

Phase 2 adds explicit cash/economic IRRs, optional LP cash yield policy, optional refinance events, GP fee survivability metrics, and LP experience metrics. These assumptions are YAML-editable:

- `lp_cash_yield_policy` in `inputs/model_config.yaml`
- `gp_survivability` in `inputs/model_config.yaml`
- optional `refinance_events` on individual scenarios in `inputs/scenarios.yaml`

Version 2 still intentionally excludes frontend, database, Monte Carlo, tax modelling, property-level debt amortisation, and monthly periods.

## Calibration Runs

Calibration variants live in `inputs/calibration_tests.yaml`. They generate deterministic scenario variants for HF allocation, HF harvesting, LP hurdle, RE liquidity, and 20-year horizon checks without changing the base scenarios.

Run:

```bash
python run_calibration.py
```

Calibration outputs are written separately:

- `outputs/calibration_summary.csv`
- `outputs/calibration_summary.xlsx`
- `outputs/calibration_cashflows.csv`
- `outputs/calibration_flags.csv`
- `outputs/calibration_report.md`
