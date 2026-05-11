# Phase 2 Validation Notes

## Added Features

Phase 2 adds:

- explicit `lp_cash_irr` and `lp_economic_irr`;
- optional GP co-investment IRR and value multiple outputs;
- optional LP interim cash yield policy;
- optional scenario-level refinance events;
- GP fee survivability analysis;
- LP experience profile metrics.

## Assumption Handling

New editable assumptions were added to YAML rather than hard-coded production defaults:

- `lp_cash_yield_policy` in `inputs/model_config.yaml`
- `gp_survivability` in `inputs/model_config.yaml`
- optional `refinance_events` inside scenarios

The LP cash yield policy is disabled by default, preserving existing Phase 1 scenario behavior unless explicitly enabled.

## Verification

Commands run:

```powershell
..\.venv\Scripts\python.exe -m pytest
..\.venv\Scripts\python.exe run_model.py
```

Result:

```text
35 passed
Ran 8 scenarios.
Outputs written to outputs/
```

## Feature-Specific Test Coverage

Added tests cover:

- LP cash IRR for an investment of 100 returning 200 in year 4;
- partial LP cash yield coverage and shortfall flagging;
- full LP cash yield coverage with no shortfall flag;
- refinance proceeds distributed to LPs;
- GP survivability risk when early fee income is below threshold;
- LP zero-distribution streak and first-distribution timing;
- regression coverage for existing Phase 1 scenarios and HF harvesting behavior.

## Caveats

`lp_cash_irr` uses actual LP cash distributions only. `lp_economic_irr` adds terminal LP claim value only when LPs have not been redeemed by model end. If LPs are redeemed, the two IRRs should match.

Refinance proceeds do not reduce RE NAV in Version 2. They are tracked as proceeds and applied according to `use_of_proceeds`.

GP co-investment IRR is reported only when `gp_co_investment` is greater than zero. The current model does not yet add GP co-investment to initial fund capital; it only reports GP economics relative to the configured GP co-investment amount.
