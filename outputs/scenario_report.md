# Scenario Report

Deterministic annual model. LP hurdle achievement is based on actual cash distributions received, not NAV appreciation.

Scenarios are run on a diagnostic horizon set in the YAML inputs, currently 20 years. The engine stops a scenario early once the LP cash hurdle is achieved, so `years_modelled` shows the actual time required to reach 2.0x or the full diagnostic horizon if the hurdle is not reached.

## Summary

| Scenario | Years modelled | LP cash multiple | LP economic multiple | LP cash IRR | LP economic IRR | LP 2x achieved? | Years to LP 2x cash | LP cashflow profile | Trigger executed? | Trigger year | HF liquidation used | Refi used | Total paid to LP | Total reinvested into HF | GP survivability risk? | GP residual NAV | Primary diagnostic flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| base_hit_everyone_happy | Y12 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y12 | Backend-heavy | Yes | Y12 | $15,159,420 | $1,670,786 | $20,000,000 | $8,009,380 | Yes | $16,991,128 | Hurdle trigger executed |
| fast_success_crypto_bull | Y13 | 2.00x | 2.00x | 5.6% | 5.6% | Yes | Y13 | Backend-heavy | Yes | Y13 | $16,964,636 | $0 | $20,000,000 | $7,606,092 | Yes | $32,995,925 | Hurdle trigger executed |
| slow_grind | Y15 | 2.00x | 2.00x | 4.9% | 4.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $16,939,120 | $0 | $20,000,000 | $7,682,639 | Yes | $19,248,014 | Hurdle trigger executed |
| hedge_fund_failure_re_survival | Y18 | 2.00x | 2.00x | 4.1% | 4.1% | Yes | Y18 | Backend-heavy | Yes | Y18 | $12,883,156 | $2,473,938 | $20,000,000 | $12,428,720 | Yes | $15,077,547 | Hurdle trigger executed |
| real_estate_distress_crypto_success | Y20 | 0.05x | 2.00x | -20.9% | 3.6% | No |  | Moderate yield | No |  | $0 | $0 | $503,926 | $3,779,443 | Yes | $0 | Value hurdle reached but liquidity constrained |
| exceptional_dynasty_outcome | Y9 | 2.00x | 2.00x | 8.2% | 8.2% | Yes | Y9 | Backend-heavy | Yes | Y9 | $16,855,162 | $43,049 | $20,000,000 | $7,805,368 | Yes | $22,566,878 | Hurdle trigger executed |
| liquidity_trap | Y11 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y11 | Backend-heavy | Yes | Y11 | $15,038,310 | $1,784,428 | $20,000,000 | $8,031,785 | Yes | $21,119,584 | Hurdle trigger executed |
| failure_never_reaches_hurdle | Y20 | 0.07x | 2.00x | -18.5% | 3.6% | No |  | Moderate yield | No |  | $0 | $0 | $659,359 | $4,945,192 | Yes | $0 | Value hurdle reached but liquidity constrained |
| jon_base_case | Y11 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $14,655,263 | $0 | $20,000,000 | $952,969 | Yes | $13,409,674 | Hurdle trigger executed |
| jon_downside_case | Y19 | 2.00x | 2.00x | 3.8% | 3.8% | Yes | Y19 | Backend-heavy | Yes | Y19 | $16,211,425 | $1,151,843 | $20,000,000 | $677,744 | Yes | $9,213,440 | Hurdle trigger executed |
| jon_property_shock_25 | Y11 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $14,974,776 | $0 | $20,000,000 | $1,091,344 | Yes | $10,222,538 | Hurdle trigger executed |
| jon_property_shock_40 | Y12 | 2.00x | 2.00x | 6.4% | 6.4% | Yes | Y12 | Backend-heavy | Yes | Y12 | $12,847,942 | $0 | $20,000,000 | $1,489,962 | Yes | $12,120,867 | Hurdle trigger executed |
| five_million_fund | Y12 | 2.00x | 2.00x | 6.5% | 6.5% | Yes | Y12 | Backend-heavy | Yes | Y12 | $7,483,231 | $513,907 | $10,000,000 | $667,621 | Yes | $6,257,786 | Hurdle trigger executed |
| jon_upside_case | Y8 | 2.00x | 2.00x | 9.5% | 9.5% | Yes | Y8 | Backend-heavy | Yes | Y8 | $13,317,532 | $0 | $20,000,000 | $987,527 | Yes | $13,949,149 | Hurdle trigger executed |

## Scenario Notes

### base_hit_everyone_happy

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.1%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $15,159,420
- Trigger refi used: $1,670,786
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,009,380
- GP residual NAV: $16,991,128
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, LP redeemed via refi

### fast_success_crypto_bull

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.6%
- LP economic IRR: 5.6%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $16,964,636
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,606,092
- GP residual NAV: $32,995,925
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### slow_grind

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.9%
- LP economic IRR: 4.9%
- Years until LP 2x cash return: 15
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $16,939,120
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,682,639
- GP residual NAV: $19,248,014
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hedge_fund_failure_re_survival

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.1%
- LP economic IRR: 4.1%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $12,883,156
- Trigger refi used: $2,473,938
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $12,428,720
- GP residual NAV: $15,077,547
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### real_estate_distress_crypto_success

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 0.05x
- LP economic multiple: 2.00x
- LP cash IRR: -20.9%
- LP economic IRR: 3.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $503,926
- Total cash reinvested into HF: $3,779,443
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, RE NAV impairment, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### exceptional_dynasty_outcome

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 8.2%
- LP economic IRR: 8.2%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $16,855,162
- Trigger refi used: $43,049
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,805,368
- GP residual NAV: $22,566,878
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, LP redeemed via refi

### liquidity_trap

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.7%
- LP economic IRR: 6.7%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $15,038,310
- Trigger refi used: $1,784,428
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,031,785
- GP residual NAV: $21,119,584
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, LP redeemed via refi

### failure_never_reaches_hurdle

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.07x
- LP economic multiple: 2.00x
- LP cash IRR: -18.5%
- LP economic IRR: 3.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $659,359
- Total cash reinvested into HF: $4,945,192
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### jon_base_case

Deal 1 base case — 116-unit Class C value-add multifamily, Southwest US. $10M purchase, $3M equity, $7M senior debt at 70% LTV. NOI $555k Y1 ramping to $930k stabilized. 7.5% IO debt. Refi Y4/Y7 at 70% LTV. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $14,655,263
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $952,969
- GP residual NAV: $13,409,674
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 10,000,000.00 | 7,000,000.00 | 0.00 | 555,000.00 | 1.06 | -207,200.00 | 0.00 | 3,000,000.00 |
| 2.00 | 10,300,000.00 | 7,000,000.00 | 0.00 | 680,000.00 | 1.30 | -47,200.00 | 0.00 | 3,300,000.00 |
| 3.00 | 10,609,000.00 | 7,000,000.00 | 0.00 | 805,000.00 | 1.53 | 137,800.00 | 0.00 | 3,609,000.00 |
| 4.00 | 10,927,270.00 | 7,000,000.00 | 0.00 | 930,000.00 | 1.77 | 302,800.00 | 632,861.77 | 3,927,270.00 |
| 5.00 | 11,255,088.10 | 7,000,000.00 | 0.00 | 957,900.00 | 1.82 | 394,584.00 | 0.00 | 4,255,088.10 |
| 6.00 | 11,592,740.74 | 7,000,000.00 | 0.00 | 986,637.00 | 1.88 | 422,171.52 | 0.00 | 4,592,740.74 |
| 7.00 | 11,940,522.97 | 7,000,000.00 | 0.00 | 1,016,236.11 | 1.94 | 450,586.67 | 707,366.69 | 4,940,522.97 |
| 8.00 | 12,298,738.65 | 7,000,000.00 | 0.00 | 1,046,723.19 | 1.99 | 479,854.27 | 0.00 | 5,298,738.65 |
| 9.00 | 12,667,700.81 | 7,000,000.00 | 0.00 | 1,078,124.89 | 2.05 | 509,999.89 | 0.00 | 5,667,700.81 |
| 10.00 | 13,047,731.84 | 7,000,000.00 | 0.00 | 1,110,468.64 | 2.12 | 541,049.89 | 0.00 | 6,047,731.84 |
| 11.00 | 13,439,163.79 | 7,000,000.00 | 0.00 | 1,143,782.69 | 2.18 | 573,031.39 | 0.00 | 6,439,163.79 |

### jon_downside_case

Deal 1 downside — slower lease-up, lower NOI ramp, higher capex, tighter refi. HF -15% Y1 then recovery.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 3.8%
- LP economic IRR: 3.8%
- Years until LP 2x cash return: 19
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 19
- Trigger HF liquidation used: $16,211,425
- Trigger refi used: $1,151,843
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $677,744
- GP residual NAV: $9,213,440
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Long zero-distribution period

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $435,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 10,000,000.00 | 7,000,000.00 | 0.00 | 435,000.00 | 0.83 | -371,750.00 | 0.00 | 3,000,000.00 |
| 2.00 | 10,100,000.00 | 7,000,000.00 | 0.00 | 500,000.00 | 0.95 | -265,000.00 | 0.00 | 3,100,000.00 |
| 3.00 | 10,201,000.00 | 7,000,000.00 | 0.00 | 565,000.00 | 1.08 | -143,250.00 | 0.00 | 3,201,000.00 |
| 4.00 | 10,303,010.00 | 7,000,000.00 | 0.00 | 630,000.00 | 1.20 | -16,500.00 | 0.00 | 3,303,010.00 |
| 5.00 | 10,406,040.10 | 7,000,000.00 | 0.00 | 695,000.00 | 1.32 | 93,250.00 | 0.00 | 3,406,040.10 |
| 6.00 | 10,510,100.50 | 7,000,000.00 | 0.00 | 701,950.00 | 1.34 | 141,852.50 | 0.00 | 3,510,100.50 |
| 7.00 | 10,615,201.51 | 7,000,000.00 | 0.00 | 708,969.50 | 1.35 | 148,521.02 | 0.00 | 3,615,201.51 |
| 8.00 | 10,721,353.52 | 7,000,000.00 | 0.00 | 716,059.20 | 1.36 | 155,256.24 | 0.00 | 3,721,353.52 |
| 9.00 | 10,828,567.06 | 7,000,000.00 | 0.00 | 723,219.79 | 1.38 | 162,058.80 | 0.00 | 3,828,567.06 |
| 10.00 | 10,936,852.73 | 7,000,000.00 | 0.00 | 730,451.98 | 1.39 | 168,929.39 | 0.00 | 3,936,852.73 |
| 11.00 | 11,046,221.25 | 7,000,000.00 | 0.00 | 737,756.50 | 1.41 | 175,868.68 | 0.00 | 4,046,221.25 |
| 12.00 | 11,156,683.47 | 7,000,000.00 | 0.00 | 745,134.07 | 1.42 | 182,877.37 | 0.00 | 4,156,683.47 |
| 13.00 | 11,268,250.30 | 7,000,000.00 | 0.00 | 752,585.41 | 1.43 | 189,956.14 | 0.00 | 4,268,250.30 |
| 14.00 | 11,380,932.80 | 7,000,000.00 | 0.00 | 760,111.26 | 1.45 | 197,105.70 | 0.00 | 4,380,932.80 |
| 15.00 | 11,494,742.13 | 7,000,000.00 | 0.00 | 767,712.38 | 1.46 | 204,326.76 | 0.00 | 4,494,742.13 |
| 16.00 | 11,609,689.55 | 7,000,000.00 | 0.00 | 775,389.50 | 1.48 | 211,620.03 | 0.00 | 4,609,689.55 |
| 17.00 | 11,725,786.45 | 7,000,000.00 | 0.00 | 783,143.40 | 1.49 | 218,986.23 | 0.00 | 4,725,786.45 |
| 18.00 | 11,843,044.31 | 7,000,000.00 | 0.00 | 790,974.83 | 1.51 | 226,426.09 | 0.00 | 4,843,044.31 |
| 19.00 | 11,961,474.76 | 7,000,000.00 | 0.00 | 798,884.58 | 1.52 | 233,940.35 | 0.00 | 4,961,474.76 |

### jon_property_shock_25

Deal 1 property shock — 25% value drop in Year 2 (market correction), 5-year recovery back to pre-shock trajectory. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $14,974,776
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,091,344
- GP residual NAV: $10,222,538
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Covenant Breach Hf Injection, Refinance event occurred, RE NAV impairment

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 10,000,000.00 | 7,000,000.00 | 0.00 | 555,000.00 | 1.06 | -207,200.00 | 0.00 | 3,000,000.00 |
| 2.00 | 10,300,000.00 | 7,000,000.00 | 0.00 | 680,000.00 | 1.30 | -47,200.00 | 0.00 | 3,300,000.00 |
| 3.00 | 7,725,000.00 | 6,180,000.00 | 0.00 | 805,000.00 | 1.74 | 199,300.00 | 0.00 | 1,545,000.00 |
| 4.00 | 8,180,775.00 | 6,180,000.00 | 0.00 | 930,000.00 | 2.01 | 364,300.00 | 0.00 | 2,000,775.00 |
| 5.00 | 8,663,440.72 | 6,180,000.00 | 0.00 | 957,900.00 | 2.07 | 456,084.00 | 0.00 | 2,483,440.72 |
| 6.00 | 9,174,583.73 | 6,180,000.00 | 0.00 | 986,637.00 | 2.13 | 483,671.52 | 0.00 | 2,994,583.73 |
| 7.00 | 9,715,884.17 | 6,180,000.00 | 0.00 | 1,016,236.11 | 2.19 | 512,086.67 | 605,590.94 | 3,535,884.17 |
| 8.00 | 10,289,121.33 | 6,180,000.00 | 0.00 | 1,046,723.19 | 2.26 | 541,354.27 | 0.00 | 4,109,121.33 |
| 9.00 | 10,597,794.97 | 6,180,000.00 | 0.00 | 1,078,124.89 | 2.33 | 571,499.89 | 0.00 | 4,417,794.97 |
| 10.00 | 10,915,728.82 | 6,180,000.00 | 0.00 | 1,110,468.64 | 2.40 | 602,549.89 | 0.00 | 4,735,728.82 |
| 11.00 | 11,243,200.69 | 6,180,000.00 | 0.00 | 1,143,782.69 | 2.47 | 634,531.39 | 0.00 | 5,063,200.69 |

### jon_property_shock_40

Deal 1 severe shock — 40% value drop in Year 2, property deeply underwater (debt > value). 5-year recovery at 10.8%/yr. Tests LP resilience when all scheduled refis fail. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.4%
- LP economic IRR: 6.4%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $12,847,942
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,489,962
- GP residual NAV: $12,120,867
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Covenant Breach Hf Injection, Refinance event occurred, RE NAV impairment

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 10,000,000.00 | 7,000,000.00 | 0.00 | 555,000.00 | 1.06 | -207,200.00 | 0.00 | 3,000,000.00 |
| 2.00 | 10,300,000.00 | 7,000,000.00 | 0.00 | 680,000.00 | 1.30 | -47,200.00 | 0.00 | 3,300,000.00 |
| 3.00 | 6,180,000.00 | 4,944,000.00 | 0.00 | 805,000.00 | 2.17 | 292,000.00 | 0.00 | 1,236,000.00 |
| 4.00 | 6,847,440.00 | 4,944,000.00 | 0.00 | 930,000.00 | 2.51 | 457,000.00 | 0.00 | 1,903,440.00 |
| 5.00 | 7,586,963.52 | 4,944,000.00 | 0.00 | 957,900.00 | 2.58 | 548,784.00 | 0.00 | 2,642,963.52 |
| 6.00 | 8,406,355.58 | 4,944,000.00 | 0.00 | 986,637.00 | 2.66 | 576,371.52 | 0.00 | 3,462,355.58 |
| 7.00 | 9,314,241.98 | 4,944,000.00 | 0.00 | 1,016,236.11 | 2.74 | 604,786.67 | 1,536,570.15 | 4,370,241.98 |
| 8.00 | 10,320,180.12 | 4,944,000.00 | 0.00 | 1,046,723.19 | 2.82 | 634,054.27 | 0.00 | 5,376,180.12 |
| 9.00 | 10,629,785.52 | 4,944,000.00 | 0.00 | 1,078,124.89 | 2.91 | 664,199.89 | 0.00 | 5,685,785.52 |
| 10.00 | 10,948,679.09 | 4,944,000.00 | 0.00 | 1,110,468.64 | 2.99 | 695,249.89 | 0.00 | 6,004,679.09 |
| 11.00 | 11,277,139.46 | 4,944,000.00 | 0.00 | 1,143,782.69 | 3.08 | 727,231.39 | 0.00 | 6,333,139.46 |
| 12.00 | 11,615,453.64 | 4,944,000.00 | 0.00 | 1,178,096.18 | 3.18 | 760,172.33 | 0.00 | 6,671,453.64 |

### five_million_fund

$5M LP raise — $3M deployed into real estate equity, $2M into hedge fund. No initial reserve. LP hurdle $10M (2x). Same RE and HF assumptions as jon_base_case. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.5%
- LP economic IRR: 6.5%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $7,483,231
- Trigger refi used: $513,907
- Total cash distributed to LP: $10,000,000
- Total cash reinvested into HF: $667,621
- GP residual NAV: $6,257,786
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### jon_upside_case

Deal 1 upside — faster lease-up, stronger NOI, 5% value growth, better HF returns (25%).

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.5%
- LP economic IRR: 9.5%
- Years until LP 2x cash return: 8
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $13,317,532
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $987,527
- GP residual NAV: $13,949,149
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $655,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 10,000,000.00 | 7,000,000.00 | 0.00 | 655,000.00 | 1.25 | -41,375.00 | 0.00 | 3,000,000.00 |
| 2.00 | 10,500,000.00 | 7,000,000.00 | 0.00 | 870,000.00 | 1.66 | 213,250.00 | 0.00 | 3,500,000.00 |
| 3.00 | 11,025,000.00 | 7,000,000.00 | 0.00 | 1,085,000.00 | 2.07 | 467,875.00 | 0.00 | 4,025,000.00 |
| 4.00 | 11,576,250.00 | 7,000,000.00 | 0.00 | 1,128,400.00 | 2.15 | 510,190.00 | 1,086,824.38 | 4,576,250.00 |
| 5.00 | 12,155,062.50 | 7,000,000.00 | 0.00 | 1,173,536.00 | 2.24 | 619,197.60 | 0.00 | 5,155,062.50 |
| 6.00 | 12,762,815.63 | 7,000,000.00 | 0.00 | 1,220,477.44 | 2.32 | 664,965.50 | 0.00 | 5,762,815.63 |
| 7.00 | 13,400,956.41 | 7,000,000.00 | 0.00 | 1,269,296.54 | 2.42 | 712,564.12 | 1,274,437.43 | 6,400,956.41 |
| 8.00 | 14,071,004.23 | 7,000,000.00 | 0.00 | 1,320,068.40 | 2.51 | 762,066.69 | 0.00 | 7,071,004.23 |
