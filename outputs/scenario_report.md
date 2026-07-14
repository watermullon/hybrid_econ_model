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
| oak_cliff_base_no_refi | 7 | 0.12 | 1.87 | -0.31 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,189,193.71 | 495,497.38 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| oak_cliff_base_year4_refi | 7 | 0.12 | 1.87 | -0.31 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,189,193.71 | 495,497.38 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| oak_cliff_year4_refi_to_lp | 7 | 0.30 | 1.87 | -0.22 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,035,012.15 | 495,497.38 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| oak_cliff_6m_year5_sale_to_lp | 7 | 1.19 | 2.00 | 0.04 | 0.13 | False |  | AGGRESSIVE_DISTRIBUTION | False |  | 0.00 | 0.00 | 7,157,771.76 | 495,497.38 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| oak_cliff_6m_year5_sale_plus_refi_to_lp | 7 | 1.19 | 2.00 | 0.04 | 0.13 | False |  | AGGRESSIVE_DISTRIBUTION | False |  | 0.00 | 0.00 | 7,157,771.76 | 495,497.38 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation | 7 | 2.00 | 2.00 | 0.13 | 0.13 | True | 7.00 | AGGRESSIVE_DISTRIBUTION | True | 7.00 | 4,544,929.81 | 0.00 | 12,000,000.00 | 495,497.38 | True | 5,893,952.31 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_y6 | 7 | 1.19 | 2.00 | 0.04 | 0.13 | False |  | AGGRESSIVE_DISTRIBUTION | False |  | 0.00 | 0.00 | 7,157,771.76 | 495,497.38 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_y5 | 7 | 1.19 | 2.00 | 0.04 | 0.13 | False |  | AGGRESSIVE_DISTRIBUTION | False |  | 0.00 | 0.00 | 7,157,771.76 | 495,497.38 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_100pct | 7 | 2.00 | 2.00 | 0.13 | 0.13 | True | 7.00 | AGGRESSIVE_DISTRIBUTION | True | 7.00 | 4,544,929.81 | 0.00 | 12,000,000.00 | 495,497.38 | True | 5,893,952.31 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| oak_cliff_downside_no_refi | 7 | 0.09 | 1.14 | -0.33 | 0.02 | False |  | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 874,895.63 | 364,539.85 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |

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

### oak_cliff_base_no_refi

Oak Cliff base case using independent underwriting, no deal-level refi.

- LP cash MOIC: 0.12x
- LP economic MOIC: 1.87x
- LP cash IRR: -30.6%
- LP economic IRR: 9.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,189,194
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_base_year4_refi

Oak Cliff base case with year-4 refi using independent valuation ramp.

- LP cash MOIC: 0.12x
- LP economic MOIC: 1.87x
- LP cash IRR: -30.6%
- LP economic IRR: 9.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,189,194
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 1,845,818.44 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_year4_refi_to_lp

Oak Cliff base case with year-4 refi proceeds distributed directly to LPs.

- LP cash MOIC: 0.30x
- LP economic MOIC: 1.87x
- LP cash IRR: -22.0%
- LP economic IRR: 10.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,035,012
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_6m_year5_sale_to_lp

Oak Cliff $6m fund case with year-5 sale proceeds proxied by a scenario-level liquidity event to LPs.

- LP cash MOIC: 1.19x
- LP economic MOIC: 2.00x
- LP cash IRR: 3.5%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,157,772
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; REFINANCE_EVENT_OCCURRED

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_6m_year5_sale_plus_refi_to_lp

Oak Cliff $6m fund case with year-4 refi to LPs and year-5 sale proceeds net of refi liability proxied to LPs.

- LP cash MOIC: 1.19x
- LP economic MOIC: 2.00x
- LP cash IRR: 3.7%
- LP economic IRR: 13.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,157,772
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; REFINANCE_EVENT_OCCURRED

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-7 backend HF liquidation capped at 75%.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 12.7%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: 7
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $4,544,930
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $495,497
- GP residual NAV: $5,893,952
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; LP_REDEEMED_VIA_HF_LIQUIDATION; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation_y6

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-6 backend HF liquidation capped at 75%.

- LP cash MOIC: 1.19x
- LP economic MOIC: 2.00x
- LP cash IRR: 3.5%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,157,772
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; REFINANCE_EVENT_OCCURRED

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation_y5

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-5 backend HF liquidation capped at 75%.

- LP cash MOIC: 1.19x
- LP economic MOIC: 2.00x
- LP cash IRR: 3.5%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,157,772
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation_100pct

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-7 backend HF liquidation capped at 100%.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 12.7%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: 7
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $4,544,930
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $495,497
- GP residual NAV: $5,893,952
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; LP_REDEEMED_VIA_HF_LIQUIDATION; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 701,409.00 | 1.63 | -528,297.52 | 0.00 | 2,175,000.00 |
| 2.00 | 8,054,358.50 | 5,075,000.00 | 0.00 | 774,001.00 | 1.80 | -255,705.52 | 0.00 | 2,979,358.50 |
| 3.00 | 8,947,957.36 | 5,075,000.00 | 0.00 | 846,593.00 | 1.97 | 116,886.48 | 0.00 | 3,872,957.36 |
| 4.00 | 9,940,697.44 | 5,075,000.00 | 0.00 | 919,185.00 | 2.14 | 389,478.48 | 0.00 | 4,865,697.44 |
| 5.00 | 11,043,578.05 | 5,075,000.00 | 0.00 | 991,777.00 | 2.31 | 526,070.48 | 0.00 | 5,968,578.05 |
| 6.00 | 12,268,818.86 | 5,075,000.00 | 0.00 | 1,021,530.31 | 2.38 | 591,823.79 | 0.00 | 7,193,818.86 |
| 7.00 | 13,629,995.24 | 5,075,000.00 | 0.00 | 1,052,176.22 | 2.45 | 622,469.70 | 0.00 | 8,554,995.24 |

### oak_cliff_downside_no_refi

Oak Cliff downside case with slower value growth, weaker HF returns, and no refi.

- LP cash MOIC: 0.09x
- LP economic MOIC: 1.14x
- LP cash IRR: -33.5%
- LP economic IRR: 1.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $874,896
- Total cash reinvested into HF: $364,540
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LONG_ZERO_DISTRIBUTION_PERIOD; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $650,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,075,000.00 | 0.00 | 650,000.00 | 1.51 | -679,706.52 | 0.00 | 2,175,000.00 |
| 2.00 | 7,685,000.00 | 5,075,000.00 | 0.00 | 712,500.00 | 1.66 | -417,206.52 | 0.00 | 2,610,000.00 |
| 3.00 | 8,146,100.00 | 5,075,000.00 | 0.00 | 775,000.00 | 1.80 | -54,706.52 | 0.00 | 3,071,100.00 |
| 4.00 | 8,634,866.00 | 5,075,000.00 | 0.00 | 837,500.00 | 1.95 | 257,793.48 | 0.00 | 3,559,866.00 |
| 5.00 | 9,152,957.96 | 5,075,000.00 | 0.00 | 900,000.00 | 2.09 | 420,293.48 | 0.00 | 4,077,957.96 |
| 6.00 | 9,702,135.44 | 5,075,000.00 | 0.00 | 918,000.00 | 2.14 | 488,293.48 | 0.00 | 4,627,135.44 |
| 7.00 | 10,284,263.56 | 5,075,000.00 | 0.00 | 936,360.00 | 2.18 | 506,653.48 | 0.00 | 5,209,263.56 |
