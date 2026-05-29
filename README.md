# Hybrid Fund Economic Model

Deterministic annual scenario model for a hybrid fund structure with real estate, hedge fund, reserve, and a non-standard LP/GP waterfall.

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python run_model.py
```

For a step-by-step runbook and full input field reference, see [`MODEL_RUNBOOK_AND_INPUTS.md`](MODEL_RUNBOOK_AND_INPUTS.md).

Outputs are written to `outputs/`:

- `scenario_summary.csv`
- `scenario_summary.xlsx`
- `scenario_cashflows.csv`
- `scenario_flags.csv`
- `scenario_report.md`
- `chatgpt_model_context.md`

`chatgpt_model_context.md` is a compact Markdown package for uploading to ChatGPT or another reviewer. It includes selected YAML assumptions, the most important scenario outputs, a compact annual cashflow/NAV table, flags, and short generated observations. It is intentionally smaller than the full workbook.

You can rebuild only that review file from existing inputs and outputs with:

```bash
python build_chatgpt_context.py
```

## Edit Assumptions

All human-editable assumptions live in YAML:

- `inputs/model_config.yaml` for global assumptions, waterfall settings, fees, liquidity, distribution policy, and flag thresholds.
- `inputs/scenarios.yaml` for named scenario assumptions.

The Python code contains logic, validation, calculations, and output formatting only.

## Interpret Results

Cash MOIC is based only on actual LP distributions. Economic MOIC may include the LP's remaining NAV claim when the hurdle has not been redeemed. The model separately tests whether the 2.0x hurdle is economically reached and whether sufficient liquidity exists to redeem LPs.

The default scenarios now use a 20-year diagnostic horizon. This does not force every scenario to run for 20 years: the engine stops a scenario early once the LP cash hurdle is achieved. Use `years_modelled`, `year_hurdle_achieved`, and `years_until_lp_2x_cash_return` to see how long each scenario actually took.

Phase 2 adds explicit cash/economic IRRs, optional LP cash yield policy, optional refinance events, GP fee survivability metrics, and LP experience metrics. These assumptions are YAML-editable:

- `lp_cash_yield_policy` in `inputs/model_config.yaml`
- `cashflow_routing` in `inputs/model_config.yaml`
- `gp_survivability` in `inputs/model_config.yaml`
- `backend_liquidity_strategy` in `inputs/model_config.yaml`
- optional `refinance_events` on individual scenarios in `inputs/scenarios.yaml`

Cashflow routing makes generated RE cashflow and harvested HF gains explicit. Each source is routed to LP distributions, HF reinvestment, and reserve according to percentages that must sum to 100%.

Refinance proceeds do not reduce gross RE NAV directly, but they do create an explicit refinance liability. Fund NAV, economic hurdle tests, and GP residual NAV are shown net of that liability.

The active LP hurdle completion trigger is configured under `hurdle_completion_trigger`. It tests whether the GP can deliberately finish the LP cash hurdle using retained cash, reserve, partial HF liquidation, refinance proceeds, and, only if enabled, partial RE sale. This is separate from the passive liquidity test. The trigger can retry after an unsuccessful year as long as its eligibility conditions are met.

The backend liquidity strategy models Asher's intended low-interim-distribution structure: RE cashflow is mostly reinvested into the HF sleeve during the hold period, then scheduled backend years apply refi-led liquidity assumptions plus reserve/HF support to test whether the LP cash hurdle can be completed. Outside backend target years, the ordinary hurdle trigger can still evaluate using the standard trigger caps.

Version 2 still intentionally excludes frontend, database, Monte Carlo, tax modelling, property-level debt amortisation, and monthly periods.

## Calibration Runs

Calibration variants live in `inputs/calibration_tests.yaml`. They generate deterministic scenario variants for HF allocation, HF harvesting, LP hurdle, RE liquidity, and 20-year horizon checks without changing the base scenarios.

The calibration suite also includes three policy-set variants:

- backend-heavy compounding
- balanced LP yield plus compounding
- aggressive LP extinguishment

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
