# Model Validation Notes: HF Harvesting

## Summary

Focused tests confirm that hedge fund harvesting is working correctly in the current phase 1 engine.

No model logic fix was required for the HF harvest path. The calibration result where 25%, 50%, and 75% harvest rates did not materially change LP cash MOIC appears to be driven by scenario economics rather than a broken harvest flow.

## Verified Flow

The tests verify the following mechanics:

1. HF gain is calculated as the positive difference between pre-harvest HF NAV and opening HF NAV.
2. HF harvest equals positive HF gain multiplied by `hf_positive_return_harvest_rate`.
3. Harvested value is subtracted from HF closing NAV.
4. If `distribute_hf_realized_gains_annually: true`, harvested HF gains enter annual distributable cash and are paid to LPs before the hurdle.
5. If `distribute_hf_realized_gains_annually: false`, harvested HF gains are added to retained cash.
6. Retained cash is included in fund NAV and liquidity.
7. LP cumulative distributions update correctly when harvested gains are distributed.
8. If the LP hurdle is reached and liquidity is available, retained cash and liquid HF NAV are used in the final LP redemption.

## Tests Added

Added `tests/test_hf_harvesting_distribution.py` with synthetic HF-only scenarios:

- Harvest disabled
- Harvest enabled with annual HF distributions disabled
- Harvest enabled with annual HF distributions enabled
- Harvest plus final LP hurdle redemption

The tests use isolated assumptions inside test fixtures and do not change production defaults.

## Verification Run

Commands run:

```powershell
..\.venv\Scripts\python.exe -m pytest
..\.venv\Scripts\python.exe run_model.py
```

Result:

```text
29 passed
Ran 8 scenarios.
Outputs written to outputs/
```

## Remaining Caveats

The current default calibration cases can still show little or no LP cash MOIC movement from HF harvest sensitivity because:

- the default HF sleeve is only 10% of initial LP capital;
- harvested gains retained as cash improve liquidity and NAV composition but do not become LP cash distributions unless annual HF gain distributions are enabled or final redemption occurs;
- a scenario can be economically above the hurdle but still fail the liquidity test;
- LP cash MOIC only moves when cash is actually distributed to LPs, not merely when NAV is reclassified from HF NAV to retained cash.

This is expected behavior under the current phase 1 model design.
