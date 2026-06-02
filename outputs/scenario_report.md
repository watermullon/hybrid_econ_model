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
| jon_base_case | Y9 | 2.00x | 2.00x | 8.5% | 8.5% | Yes | Y9 | Backend-heavy | Yes | Y9 | $11,332,919 | $0 | $20,000,000 | $1,583,940 | Yes | $13,931,349 | Hurdle trigger executed |
| jon_downside_case | Y18 | 2.00x | 2.00x | 4.2% | 4.2% | Yes | Y18 | Backend-heavy | Yes | Y18 | $14,874,343 | $760,597 | $20,000,000 | $1,455,020 | Yes | $12,936,519 | Hurdle trigger executed |
| jon_property_shock_25 | Y11 | 2.00x | 2.00x | 7.3% | 7.3% | Yes | Y11 | Backend-heavy | Yes | Y11 | $10,266,122 | $0 | $20,000,000 | $2,536,073 | Yes | $16,072,128 | Hurdle trigger executed |
| jon_property_shock_40 | Y11 | 2.00x | 2.00x | 7.5% | 7.5% | Yes | Y11 | Backend-heavy | Yes | Y11 | $6,685,702 | $0 | $20,000,000 | $3,015,795 | Yes | $12,713,960 | Hurdle trigger executed |
| jon_upside_case | Y6 | 2.00x | 2.00x | 13.0% | 13.0% | Yes | Y6 | Backend-heavy | Yes | Y6 | $11,876,237 | $0 | $20,000,000 | $1,437,689 | Yes | $13,040,413 | Hurdle trigger executed |

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

Deal 1 base case — 116-unit Class C value-add multifamily, Southwest US. $23M purchase, $3.5M equity, $16M senior + $2.5M assumed liabilities. NOI $1.28M Y1 ramping to $2.15M stabilized. 7.5% IO debt. Refi Y4/Y7 at 70% LTV. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 8.5%
- LP economic IRR: 8.5%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $11,332,919
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,583,940
- GP residual NAV: $13,931,349
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $23,000,000; assumed debt $16,000,000; other liabilities $2,500,000; new equity required $3,500,000; entry equity cushion $1,000,000; current NOI $1,278,000; refi LTV capacity $97,500

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 23,000,000.00 | 16,000,000.00 | 2,500,000.00 | 1,278,000.00 | 1.06 | -473,120.00 | 0.00 | 4,500,000.00 |
| 2.00 | 23,690,000.00 | 16,000,000.00 | 2,500,000.00 | 1,568,666.67 | 1.31 | -94,080.00 | 0.00 | 5,190,000.00 |
| 3.00 | 24,400,700.00 | 16,000,000.00 | 2,500,000.00 | 1,859,333.33 | 1.55 | 334,960.00 | 0.00 | 5,900,700.00 |
| 4.00 | 25,132,721.00 | 16,000,000.00 | 2,500,000.00 | 2,150,000.00 | 1.79 | 714,000.00 | 1,553,082.08 | 6,632,721.00 |
| 5.00 | 25,886,702.63 | 16,000,000.00 | 2,500,000.00 | 2,214,500.00 | 1.85 | 925,920.00 | 0.00 | 7,386,702.63 |
| 6.00 | 26,663,303.71 | 16,000,000.00 | 2,500,000.00 | 2,280,935.00 | 1.90 | 989,697.60 | 0.00 | 8,163,303.71 |
| 7.00 | 27,463,202.82 | 16,000,000.00 | 2,500,000.00 | 2,349,363.05 | 1.96 | 1,055,388.53 | 1,629,380.89 | 8,963,202.82 |
| 8.00 | 28,287,098.90 | 16,000,000.00 | 2,500,000.00 | 2,419,843.94 | 2.02 | 1,123,050.18 | 0.00 | 9,787,098.90 |
| 9.00 | 29,135,711.87 | 16,000,000.00 | 2,500,000.00 | 2,492,439.26 | 2.08 | 1,192,741.69 | 0.00 | 10,635,711.87 |

### jon_downside_case

Deal 1 downside — slower lease-up, lower NOI ramp, higher capex, tighter refi. HF -15% Y1 then recovery.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.2%
- LP economic IRR: 4.2%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $14,874,343
- Trigger refi used: $760,597
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,455,020
- GP residual NAV: $12,936,519
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Long zero-distribution period

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $23,000,000; assumed debt $16,000,000; other liabilities $2,500,000; new equity required $3,500,000; entry equity cushion $1,000,000; current NOI $1,000,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 23,000,000.00 | 16,000,000.00 | 2,500,000.00 | 1,000,000.00 | 0.83 | -850,000.00 | 0.00 | 4,500,000.00 |
| 2.00 | 23,230,000.00 | 16,000,000.00 | 2,500,000.00 | 1,150,000.00 | 0.96 | -607,500.00 | 0.00 | 4,730,000.00 |
| 3.00 | 23,462,300.00 | 16,000,000.00 | 2,500,000.00 | 1,300,000.00 | 1.08 | -315,000.00 | 0.00 | 4,962,300.00 |
| 4.00 | 23,696,923.00 | 16,000,000.00 | 2,500,000.00 | 1,450,000.00 | 1.21 | -22,500.00 | 0.00 | 5,196,923.00 |
| 5.00 | 23,933,892.23 | 16,000,000.00 | 2,500,000.00 | 1,600,000.00 | 1.33 | 220,000.00 | 0.00 | 5,433,892.23 |
| 6.00 | 24,173,231.15 | 16,000,000.00 | 2,500,000.00 | 1,616,000.00 | 1.35 | 335,200.00 | 0.00 | 5,673,231.15 |
| 7.00 | 24,414,963.46 | 16,000,000.00 | 2,500,000.00 | 1,632,160.00 | 1.36 | 350,552.00 | 0.00 | 5,914,963.46 |
| 8.00 | 24,659,113.10 | 16,000,000.00 | 2,500,000.00 | 1,648,481.60 | 1.37 | 366,057.52 | 0.00 | 6,159,113.10 |
| 9.00 | 24,905,704.23 | 16,000,000.00 | 2,500,000.00 | 1,664,966.42 | 1.39 | 381,718.10 | 0.00 | 6,405,704.23 |
| 10.00 | 25,154,761.27 | 16,000,000.00 | 2,500,000.00 | 1,681,616.08 | 1.40 | 397,535.28 | 0.00 | 6,654,761.27 |
| 11.00 | 25,406,308.88 | 16,000,000.00 | 2,500,000.00 | 1,698,432.24 | 1.42 | 413,510.63 | 0.00 | 6,906,308.88 |
| 12.00 | 25,660,371.97 | 16,000,000.00 | 2,500,000.00 | 1,715,416.56 | 1.43 | 429,645.74 | 0.00 | 7,160,371.97 |
| 13.00 | 25,916,975.69 | 16,000,000.00 | 2,500,000.00 | 1,732,570.73 | 1.44 | 445,942.19 | 0.00 | 7,416,975.69 |
| 14.00 | 26,176,145.45 | 16,000,000.00 | 2,500,000.00 | 1,749,896.44 | 1.46 | 462,401.61 | 0.00 | 7,676,145.45 |
| 15.00 | 26,437,906.90 | 16,000,000.00 | 2,500,000.00 | 1,767,395.40 | 1.47 | 479,025.63 | 0.00 | 7,937,906.90 |
| 16.00 | 26,702,285.97 | 16,000,000.00 | 2,500,000.00 | 1,785,069.35 | 1.49 | 495,815.89 | 0.00 | 8,202,285.97 |
| 17.00 | 26,969,308.83 | 16,000,000.00 | 2,500,000.00 | 1,802,920.05 | 1.50 | 512,774.05 | 0.00 | 8,469,308.83 |
| 18.00 | 27,239,001.92 | 16,000,000.00 | 2,500,000.00 | 1,820,949.25 | 1.52 | 529,901.79 | 0.00 | 8,739,001.92 |

### jon_property_shock_25

Deal 1 property shock — 25% value drop in Year 2 (market correction), 5-year recovery back to pre-shock trajectory. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.3%
- LP economic IRR: 7.3%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $10,266,122
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,536,073
- GP residual NAV: $16,072,128
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Covenant Breach Hf Injection, Refinance event occurred, RE NAV impairment

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $23,000,000; assumed debt $16,000,000; other liabilities $2,500,000; new equity required $3,500,000; entry equity cushion $1,000,000; current NOI $1,278,000; refi LTV capacity $97,500

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 23,000,000.00 | 16,000,000.00 | 2,500,000.00 | 1,278,000.00 | 1.06 | -473,120.00 | 0.00 | 4,500,000.00 |
| 2.00 | 23,690,000.00 | 16,000,000.00 | 2,500,000.00 | 1,568,666.67 | 1.31 | -94,080.00 | 0.00 | 5,190,000.00 |
| 3.00 | 17,767,500.00 | 14,214,000.00 | 2,500,000.00 | 1,859,333.33 | 1.74 | 468,910.00 | 0.00 | 1,053,500.00 |
| 4.00 | 18,815,782.50 | 14,214,000.00 | 2,500,000.00 | 2,150,000.00 | 2.02 | 847,950.00 | 0.00 | 2,101,782.50 |
| 5.00 | 19,925,913.67 | 14,214,000.00 | 2,500,000.00 | 2,214,500.00 | 2.08 | 1,059,870.00 | 0.00 | 3,211,913.67 |
| 6.00 | 21,101,542.57 | 14,214,000.00 | 2,500,000.00 | 2,280,935.00 | 2.14 | 1,123,647.60 | 0.00 | 4,387,542.57 |
| 7.00 | 22,346,533.59 | 14,214,000.00 | 2,500,000.00 | 2,349,363.05 | 2.20 | 1,189,338.53 | 1,392,859.17 | 5,632,533.59 |
| 8.00 | 23,664,979.07 | 14,214,000.00 | 2,500,000.00 | 2,419,843.94 | 2.27 | 1,257,000.18 | 0.00 | 6,950,979.07 |
| 9.00 | 24,374,928.44 | 14,214,000.00 | 2,500,000.00 | 2,492,439.26 | 2.34 | 1,326,691.69 | 0.00 | 7,660,928.44 |
| 10.00 | 25,106,176.29 | 14,214,000.00 | 2,500,000.00 | 2,567,212.44 | 2.41 | 1,398,473.94 | 0.00 | 8,392,176.29 |
| 11.00 | 25,859,361.58 | 14,214,000.00 | 2,500,000.00 | 2,644,228.81 | 2.48 | 1,472,409.66 | 0.00 | 9,145,361.58 |

### jon_property_shock_40

Deal 1 severe shock — 40% value drop in Year 2, property deeply underwater (debt > value). 5-year recovery at 10.8%/yr. Tests LP resilience when all scheduled refis fail. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.5%
- LP economic IRR: 7.5%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $6,685,702
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,015,795
- GP residual NAV: $12,713,960
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Covenant Breach Hf Injection, Refinance event occurred, HF major drawdown, RE NAV impairment

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $23,000,000; assumed debt $16,000,000; other liabilities $2,500,000; new equity required $3,500,000; entry equity cushion $1,000,000; current NOI $1,278,000; refi LTV capacity $97,500

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 23,000,000.00 | 16,000,000.00 | 2,500,000.00 | 1,278,000.00 | 1.06 | -473,120.00 | 0.00 | 4,500,000.00 |
| 2.00 | 23,690,000.00 | 16,000,000.00 | 2,500,000.00 | 1,568,666.67 | 1.31 | -94,080.00 | 0.00 | 5,190,000.00 |
| 3.00 | 14,214,000.00 | 11,371,200.00 | 2,500,000.00 | 1,859,333.33 | 2.18 | 682,120.00 | 0.00 | 342,800.00 |
| 4.00 | 15,749,112.00 | 11,371,200.00 | 2,500,000.00 | 2,150,000.00 | 2.52 | 1,061,160.00 | 0.00 | 1,877,912.00 |
| 5.00 | 17,450,016.10 | 11,371,200.00 | 2,500,000.00 | 2,214,500.00 | 2.60 | 1,273,080.00 | 0.00 | 3,578,816.10 |
| 6.00 | 19,334,617.83 | 11,371,200.00 | 2,500,000.00 | 2,280,935.00 | 2.67 | 1,336,857.60 | 0.00 | 5,463,417.83 |
| 7.00 | 21,422,756.56 | 11,371,200.00 | 2,500,000.00 | 2,349,363.05 | 2.75 | 1,402,548.53 | 3,534,111.35 | 7,551,556.56 |
| 8.00 | 23,736,414.27 | 11,371,200.00 | 2,500,000.00 | 2,419,843.94 | 2.84 | 1,470,210.18 | 0.00 | 9,865,214.27 |
| 9.00 | 24,448,506.70 | 11,371,200.00 | 2,500,000.00 | 2,492,439.26 | 2.92 | 1,539,901.69 | 0.00 | 10,577,306.70 |
| 10.00 | 25,181,961.90 | 11,371,200.00 | 2,500,000.00 | 2,567,212.44 | 3.01 | 1,611,683.94 | 0.00 | 11,310,761.90 |
| 11.00 | 25,937,420.75 | 11,371,200.00 | 2,500,000.00 | 2,644,228.81 | 3.10 | 1,685,619.66 | 0.00 | 12,066,220.75 |

### jon_upside_case

Deal 1 upside — faster lease-up, stronger NOI, 5% value growth, better HF returns (25%).

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 13.0%
- LP economic IRR: 13.0%
- Years until LP 2x cash return: 6
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 6
- Trigger HF liquidation used: $11,876,237
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,437,689
- GP residual NAV: $13,040,413
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Good LP IRR with large GP residual

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $23,000,000; assumed debt $16,000,000; other liabilities $2,500,000; new equity required $3,500,000; entry equity cushion $1,000,000; current NOI $1,500,000; refi LTV capacity $98,500

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 23,000,000.00 | 16,000,000.00 | 2,500,000.00 | 1,500,000.00 | 1.25 | -87,500.00 | 0.00 | 4,500,000.00 |
| 2.00 | 24,150,000.00 | 16,000,000.00 | 2,500,000.00 | 2,000,000.00 | 1.67 | 500,000.00 | 0.00 | 5,650,000.00 |
| 3.00 | 25,357,500.00 | 16,000,000.00 | 2,500,000.00 | 2,500,000.00 | 2.08 | 1,087,500.00 | 0.00 | 6,857,500.00 |
| 4.00 | 26,625,375.00 | 16,000,000.00 | 2,500,000.00 | 2,600,000.00 | 2.17 | 1,185,000.00 | 2,598,196.06 | 8,125,375.00 |
| 5.00 | 27,956,643.75 | 16,000,000.00 | 2,500,000.00 | 2,704,000.00 | 2.25 | 1,436,400.00 | 0.00 | 9,456,643.75 |
| 6.00 | 29,354,475.94 | 16,000,000.00 | 2,500,000.00 | 2,812,160.00 | 2.34 | 1,541,856.00 | 0.00 | 10,854,475.94 |
