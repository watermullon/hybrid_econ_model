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
| jon_base_case | Y11 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $14,952,218 | $0 | $20,000,000 | $1,089,784 | Yes | $14,831,028 | Hurdle trigger executed |
| jon_downside_case | Y20 | 2.00x | 2.00x | 3.6% | 3.6% | Yes | Y20 | Backend-heavy | Yes | Y20 | $17,739,608 | $145,661 | $20,000,000 | $675,119 | Yes | $11,472,958 | Hurdle trigger executed |
| jon_property_shock_25 | Y11 | 2.00x | 2.00x | 6.9% | 6.9% | Yes | Y11 | Backend-heavy | Yes | Y11 | $13,364,158 | $649,734 | $20,000,000 | $1,421,547 | Yes | $9,599,878 | Hurdle trigger executed |
| jon_property_shock_40 | Y12 | 2.00x | 2.00x | 6.5% | 6.5% | Yes | Y12 | Backend-heavy | Yes | Y12 | $11,248,096 | $0 | $20,000,000 | $1,940,054 | Yes | $10,880,366 | Hurdle trigger executed |
| five_million_fund | Y12 | 2.00x | 2.00x | 6.5% | 6.5% | Yes | Y12 | Backend-heavy | Yes | Y12 | $7,483,231 | $513,907 | $10,000,000 | $667,621 | Yes | $6,257,786 | Hurdle trigger executed |
| jon_upside_case | Y8 | 2.00x | 2.00x | 9.5% | 9.5% | Yes | Y8 | Backend-heavy | Yes | Y8 | $13,056,082 | $0 | $20,000,000 | $1,165,108 | Yes | $15,865,766 | Hurdle trigger executed |

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

Deal 1 base case — 116-unit Class C value-add multifamily, Southwest US. $13M purchase, $3M equity, $10M senior debt. NOI $720k Y1 ramping to $1.21M stabilized. 7.5% IO debt. Refi Y4/Y7 at 70% LTV. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $14,952,218
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,089,784
- GP residual NAV: $14,831,028
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $13,000,000; assumed debt $10,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $720,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 13,000,000.00 | 10,000,000.00 | 0.00 | 720,000.00 | 0.96 | -338,800.00 | 0.00 | 3,000,000.00 |
| 2.00 | 13,390,000.00 | 10,000,000.00 | 0.00 | 883,333.33 | 1.18 | -127,000.00 | 0.00 | 3,390,000.00 |
| 3.00 | 13,791,700.00 | 10,000,000.00 | 0.00 | 1,046,666.67 | 1.40 | 114,800.00 | 0.00 | 3,791,700.00 |
| 4.00 | 14,205,451.00 | 10,000,000.00 | 0.00 | 1,210,000.00 | 1.61 | 326,600.00 | 0.00 | 4,205,451.00 |
| 5.00 | 14,631,614.53 | 10,000,000.00 | 0.00 | 1,246,300.00 | 1.66 | 446,448.00 | 0.00 | 4,631,614.53 |
| 6.00 | 15,070,562.97 | 10,000,000.00 | 0.00 | 1,283,689.00 | 1.71 | 482,341.44 | 0.00 | 5,070,562.97 |
| 7.00 | 15,522,679.85 | 10,000,000.00 | 0.00 | 1,322,199.67 | 1.76 | 519,311.68 | 844,229.00 | 5,522,679.85 |
| 8.00 | 15,988,360.25 | 10,000,000.00 | 0.00 | 1,361,865.66 | 1.82 | 557,391.03 | 0.00 | 5,988,360.25 |
| 9.00 | 16,468,011.06 | 10,000,000.00 | 0.00 | 1,402,721.63 | 1.87 | 596,612.76 | 0.00 | 6,468,011.06 |
| 10.00 | 16,962,051.39 | 10,000,000.00 | 0.00 | 1,444,803.28 | 1.93 | 637,011.15 | 0.00 | 6,962,051.39 |
| 11.00 | 17,470,912.93 | 10,000,000.00 | 0.00 | 1,488,147.38 | 1.98 | 678,621.48 | 0.00 | 7,470,912.93 |

### jon_downside_case

Deal 1 downside — slower lease-up, lower NOI ramp, higher capex, tighter refi. HF -15% Y1 then recovery.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 3.6%
- LP economic IRR: 3.6%
- Years until LP 2x cash return: 20
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 20
- Trigger HF liquidation used: $17,739,608
- Trigger refi used: $145,661
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $675,119
- GP residual NAV: $11,472,958
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Long zero-distribution period

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $13,000,000; assumed debt $10,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $565,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 13,000,000.00 | 10,000,000.00 | 0.00 | 565,000.00 | 0.75 | -553,250.00 | 0.00 | 3,000,000.00 |
| 2.00 | 13,130,000.00 | 10,000,000.00 | 0.00 | 648,750.00 | 0.86 | -413,687.50 | 0.00 | 3,130,000.00 |
| 3.00 | 13,261,300.00 | 10,000,000.00 | 0.00 | 732,500.00 | 0.98 | -254,125.00 | 0.00 | 3,261,300.00 |
| 4.00 | 13,393,913.00 | 10,000,000.00 | 0.00 | 816,250.00 | 1.09 | -89,562.50 | 0.00 | 3,393,913.00 |
| 5.00 | 13,527,852.13 | 10,000,000.00 | 0.00 | 900,000.00 | 1.20 | 50,000.00 | 0.00 | 3,527,852.13 |
| 6.00 | 13,663,130.65 | 10,000,000.00 | 0.00 | 909,000.00 | 1.21 | 113,550.00 | 0.00 | 3,663,130.65 |
| 7.00 | 13,799,761.96 | 10,000,000.00 | 0.00 | 918,090.00 | 1.22 | 122,185.50 | 0.00 | 3,799,761.96 |
| 8.00 | 13,937,759.58 | 10,000,000.00 | 0.00 | 927,270.90 | 1.24 | 130,907.36 | 0.00 | 3,937,759.58 |
| 9.00 | 14,077,137.17 | 10,000,000.00 | 0.00 | 936,543.61 | 1.25 | 139,716.43 | 0.00 | 4,077,137.17 |
| 10.00 | 14,217,908.54 | 10,000,000.00 | 0.00 | 945,909.05 | 1.26 | 148,613.59 | 0.00 | 4,217,908.54 |
| 11.00 | 14,360,087.63 | 10,000,000.00 | 0.00 | 955,368.14 | 1.27 | 157,599.73 | 0.00 | 4,360,087.63 |
| 12.00 | 14,503,688.51 | 10,000,000.00 | 0.00 | 964,921.82 | 1.29 | 166,675.73 | 0.00 | 4,503,688.51 |
| 13.00 | 14,648,725.39 | 10,000,000.00 | 0.00 | 974,571.04 | 1.30 | 175,842.48 | 0.00 | 4,648,725.39 |
| 14.00 | 14,795,212.65 | 10,000,000.00 | 0.00 | 984,316.75 | 1.31 | 185,100.91 | 0.00 | 4,795,212.65 |
| 15.00 | 14,943,164.77 | 10,000,000.00 | 0.00 | 994,159.91 | 1.33 | 194,451.92 | 0.00 | 4,943,164.77 |
| 16.00 | 15,092,596.42 | 10,000,000.00 | 0.00 | 1,004,101.51 | 1.34 | 203,896.44 | 0.00 | 5,092,596.42 |
| 17.00 | 15,243,522.38 | 10,000,000.00 | 0.00 | 1,014,142.53 | 1.35 | 213,435.40 | 0.00 | 5,243,522.38 |
| 18.00 | 15,395,957.61 | 10,000,000.00 | 0.00 | 1,024,283.95 | 1.37 | 223,069.75 | 0.00 | 5,395,957.61 |
| 19.00 | 15,549,917.18 | 10,000,000.00 | 0.00 | 1,034,526.79 | 1.38 | 232,800.45 | 0.00 | 5,549,917.18 |
| 20.00 | 15,705,416.36 | 10,000,000.00 | 0.00 | 1,044,872.06 | 1.39 | 242,628.46 | 0.00 | 5,705,416.36 |

### jon_property_shock_25

Deal 1 property shock — 25% value drop in Year 2 (market correction), 5-year recovery back to pre-shock trajectory. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.9%
- LP economic IRR: 6.9%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $13,364,158
- Trigger refi used: $649,734
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,421,547
- GP residual NAV: $9,599,878
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Covenant Breach Hf Injection, Refinance event occurred, RE NAV impairment

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $13,000,000; assumed debt $10,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $720,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 13,000,000.00 | 10,000,000.00 | 0.00 | 720,000.00 | 0.96 | -338,800.00 | 0.00 | 3,000,000.00 |
| 2.00 | 13,390,000.00 | 10,000,000.00 | 0.00 | 883,333.33 | 1.18 | -127,000.00 | 0.00 | 3,390,000.00 |
| 3.00 | 10,042,500.00 | 8,034,000.00 | 0.00 | 1,046,666.67 | 1.74 | 262,250.00 | 0.00 | 2,008,500.00 |
| 4.00 | 10,635,007.50 | 8,034,000.00 | 0.00 | 1,210,000.00 | 2.01 | 474,050.00 | 0.00 | 2,601,007.50 |
| 5.00 | 11,262,472.94 | 8,034,000.00 | 0.00 | 1,246,300.00 | 2.07 | 593,898.00 | 0.00 | 3,228,472.94 |
| 6.00 | 11,926,958.85 | 8,034,000.00 | 0.00 | 1,283,689.00 | 2.13 | 629,791.44 | 0.00 | 3,892,958.85 |
| 7.00 | 12,630,649.42 | 8,034,000.00 | 0.00 | 1,322,199.67 | 2.19 | 666,761.68 | 787,268.23 | 4,596,649.42 |
| 8.00 | 13,375,857.73 | 8,034,000.00 | 0.00 | 1,361,865.66 | 2.26 | 704,841.03 | 0.00 | 5,341,857.73 |
| 9.00 | 13,777,133.47 | 8,034,000.00 | 0.00 | 1,402,721.63 | 2.33 | 744,062.76 | 0.00 | 5,743,133.47 |
| 10.00 | 14,190,447.47 | 8,034,000.00 | 0.00 | 1,444,803.28 | 2.40 | 784,461.15 | 0.00 | 6,156,447.47 |
| 11.00 | 14,616,160.89 | 8,034,000.00 | 0.00 | 1,488,147.38 | 2.47 | 826,071.48 | 0.00 | 6,582,160.89 |

### jon_property_shock_40

Deal 1 severe shock — 40% value drop in Year 2, property deeply underwater (debt > value). 5-year recovery at 10.8%/yr. Tests LP resilience when all scheduled refis fail. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.5%
- LP economic IRR: 6.5%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $11,248,096
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,940,054
- GP residual NAV: $10,880,366
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Covenant Breach Hf Injection, Refinance event occurred, RE NAV impairment

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $13,000,000; assumed debt $10,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $720,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 13,000,000.00 | 10,000,000.00 | 0.00 | 720,000.00 | 0.96 | -338,800.00 | 0.00 | 3,000,000.00 |
| 2.00 | 13,390,000.00 | 10,000,000.00 | 0.00 | 883,333.33 | 1.18 | -127,000.00 | 0.00 | 3,390,000.00 |
| 3.00 | 8,034,000.00 | 6,427,200.00 | 0.00 | 1,046,666.67 | 2.17 | 382,760.00 | 0.00 | 1,606,800.00 |
| 4.00 | 8,901,672.00 | 6,427,200.00 | 0.00 | 1,210,000.00 | 2.51 | 594,560.00 | 0.00 | 2,474,472.00 |
| 5.00 | 9,863,052.58 | 6,427,200.00 | 0.00 | 1,246,300.00 | 2.59 | 714,408.00 | 0.00 | 3,435,852.58 |
| 6.00 | 10,928,262.25 | 6,427,200.00 | 0.00 | 1,283,689.00 | 2.66 | 750,301.44 | 0.00 | 4,501,062.25 |
| 7.00 | 12,108,514.58 | 6,427,200.00 | 0.00 | 1,322,199.67 | 2.74 | 787,271.68 | 1,997,541.20 | 5,681,314.58 |
| 8.00 | 13,416,234.15 | 6,427,200.00 | 0.00 | 1,361,865.66 | 2.83 | 825,351.03 | 0.00 | 6,989,034.15 |
| 9.00 | 13,818,721.18 | 6,427,200.00 | 0.00 | 1,402,721.63 | 2.91 | 864,572.76 | 0.00 | 7,391,521.18 |
| 10.00 | 14,233,282.81 | 6,427,200.00 | 0.00 | 1,444,803.28 | 3.00 | 904,971.15 | 0.00 | 7,806,082.81 |
| 11.00 | 14,660,281.30 | 6,427,200.00 | 0.00 | 1,488,147.38 | 3.09 | 946,581.48 | 0.00 | 8,233,081.30 |
| 12.00 | 15,100,089.74 | 6,427,200.00 | 0.00 | 1,532,791.80 | 3.18 | 989,440.13 | 0.00 | 8,672,889.74 |

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
- Trigger HF liquidation used: $13,056,082
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,165,108
- GP residual NAV: $15,865,766
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $13,000,000; assumed debt $10,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $850,000; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 13,000,000.00 | 10,000,000.00 | 0.00 | 850,000.00 | 1.13 | -121,250.00 | 0.00 | 3,000,000.00 |
| 2.00 | 13,650,000.00 | 10,000,000.00 | 0.00 | 1,130,000.00 | 1.51 | 211,750.00 | 0.00 | 3,650,000.00 |
| 3.00 | 14,332,500.00 | 10,000,000.00 | 0.00 | 1,410,000.00 | 1.88 | 539,750.00 | 0.00 | 4,332,500.00 |
| 4.00 | 15,049,125.00 | 10,000,000.00 | 0.00 | 1,466,400.00 | 1.96 | 594,740.00 | 526,371.69 | 5,049,125.00 |
| 5.00 | 15,801,581.25 | 10,000,000.00 | 0.00 | 1,525,056.00 | 2.03 | 736,929.60 | 0.00 | 5,801,581.25 |
| 6.00 | 16,591,660.31 | 10,000,000.00 | 0.00 | 1,586,058.24 | 2.11 | 796,406.78 | 0.00 | 6,591,660.31 |
| 7.00 | 17,421,243.33 | 10,000,000.00 | 0.00 | 1,649,500.57 | 2.20 | 858,263.06 | 1,643,471.16 | 7,421,243.33 |
| 8.00 | 18,292,305.49 | 10,000,000.00 | 0.00 | 1,715,480.59 | 2.29 | 922,593.58 | 0.00 | 8,292,305.49 |
