# Scenario Report

Deterministic annual model. LP hurdle achievement is based on actual cash distributions received, not NAV appreciation.

## Summary

| scenario | years_modelled | lp_cash_moic | lp_economic_moic | lp_cash_irr | lp_economic_irr | lp_hurdle_achieved | years_until_lp_2x_cash_return | lp_cashflow_profile_type | hurdle_trigger_executed | hurdle_trigger_year | total_trigger_cash_from_hf_liquidation | total_trigger_cash_from_refi | total_distributed_to_lp | total_reinvested_into_hf | gp_survivability_risk | gp_residual_nav | primary_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| base_hit_everyone_happy | 8 | 0.06 | 2.00 | -0.38 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 616,518.36 | 4,623,887.67 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| fast_success_crypto_bull | 5 | 0.03 | 2.00 | -0.59 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 314,277.22 | 2,357,079.16 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| slow_grind | 15 | 0.10 | 2.00 | -0.20 | 0.05 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,024,351.88 | 7,682,639.13 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hedge_fund_failure_re_survival | 12 | 0.09 | 2.00 | -0.24 | 0.06 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 949,980.81 | 7,124,856.07 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| real_estate_distress_crypto_success | 10 | 0.03 | 2.00 | -0.39 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 303,066.04 | 2,272,995.29 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| exceptional_dynasty_outcome | 10 | 2.00 | 2.00 | 0.07 | 0.07 | True | 10.00 | BACKEND_HEAVY | True | 10.00 | 9,978,060.02 | 6,422,801.87 | 20,000,000.00 | 9,297,414.33 | True | 30,185,570.70 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| liquidity_trap | 10 | 0.09 | 2.00 | -0.28 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 919,123.14 | 6,893,423.57 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| failure_never_reaches_hurdle | 12 | 0.04 | 1.73 | -0.32 | 0.05 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 411,400.38 | 3,085,502.85 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |

## Scenario Notes

### base_hit_everyone_happy

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.06x
- LP economic MOIC: 2.00x
- LP cash IRR: -37.7%
- LP economic IRR: 9.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $616,518
- Total cash reinvested into HF: $4,623,888
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### fast_success_crypto_bull

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.03x
- LP economic MOIC: 2.00x
- LP cash IRR: -59.3%
- LP economic IRR: 15.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $314,277
- Total cash reinvested into HF: $2,357,079
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### slow_grind

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 0.10x
- LP economic MOIC: 2.00x
- LP cash IRR: -19.6%
- LP economic IRR: 4.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,024,352
- Total cash reinvested into HF: $7,682,639
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hedge_fund_failure_re_survival

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.09x
- LP economic MOIC: 2.00x
- LP cash IRR: -24.3%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $949,981
- Total cash reinvested into HF: $7,124,856
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### real_estate_distress_crypto_success

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.03x
- LP economic MOIC: 2.00x
- LP cash IRR: -39.4%
- LP economic IRR: 7.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $303,066
- Total cash reinvested into HF: $2,272,995
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### exceptional_dynasty_outcome

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: 10
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 10
- Trigger HF liquidation used: $9,978,060
- Trigger refi used: $6,422,802
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $9,297,414
- GP residual NAV: $30,185,571
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### liquidity_trap

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 0.09x
- LP economic MOIC: 2.00x
- LP cash IRR: -27.6%
- LP economic IRR: 7.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $919,123
- Total cash reinvested into HF: $6,893,424
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### failure_never_reaches_hurdle

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.04x
- LP economic MOIC: 1.73x
- LP cash IRR: -31.7%
- LP economic IRR: 4.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $411,400
- Total cash reinvested into HF: $3,085,503
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV
