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
| jon_base_case | Y11 | 2.00x | 2.00x | 7.1% | 7.1% | Yes | Y11 | Backend-heavy | Yes | Y11 | $8,966,045 | $3,418,351 | $20,000,000 | $2,091,792 | Yes | $20,356,185 | Hurdle trigger executed |
| jon_downside_case | Y15 | 2.00x | 2.00x | 5.3% | 5.3% | Yes | Y15 | Backend-heavy | Yes | Y15 | $7,124,333 | $5,822,838 | $20,000,000 | $2,350,943 | Yes | $27,597,321 | Hurdle trigger executed |
| jon_property_shock_25 | Y12 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y12 | Backend-heavy | Yes | Y12 | $8,505,930 | $3,153,630 | $20,000,000 | $2,578,283 | Yes | $22,466,957 | Hurdle trigger executed |
| jon_property_shock_40 | Y12 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y12 | Backend-heavy | Yes | Y12 | $5,679,324 | $4,354,007 | $20,000,000 | $2,810,033 | Yes | $20,664,356 | Hurdle trigger executed |
| five_million_fund | Y12 | 2.00x | 2.00x | 6.5% | 6.5% | Yes | Y12 | Backend-heavy | Yes | Y12 | $7,483,231 | $513,907 | $10,000,000 | $667,621 | Yes | $6,257,786 | Hurdle trigger executed |
| jon_upside_case | Y9 | 2.00x | 2.00x | 8.7% | 8.7% | Yes | Y9 | Backend-heavy | Yes | Y9 | $9,533,742 | $2,288,272 | $20,000,000 | $1,938,908 | Yes | $18,050,088 | Hurdle trigger executed |
| oak_cliff_base_no_refi | Y7 | 0.12x | 2.00x | -30.6% | 10.6% | No |  | Moderate yield | No |  | $0 | $0 | $1,189,194 | $495,497 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_base_year4_refi | Y7 | 0.12x | 2.00x | -30.6% | 10.6% | No |  | Moderate yield | No |  | $0 | $0 | $1,189,194 | $495,497 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_year4_refi_to_lp | Y7 | 0.30x | 2.00x | -22.0% | 11.1% | No |  | Moderate yield | No |  | $0 | $0 | $3,035,012 | $495,497 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_6m_year5_sale_to_lp | Y7 | 1.19x | 2.00x | 3.5% | 12.7% | No |  | Aggressive distribution | No |  | $0 | $0 | $7,157,772 | $495,497 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_6m_year5_sale_plus_refi_to_lp | Y7 | 1.19x | 2.00x | 3.7% | 13.1% | No |  | Aggressive distribution | No |  | $0 | $0 | $7,157,772 | $495,497 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation | Y7 | 2.00x | 2.00x | 12.7% | 12.7% | Yes | Y7 | Aggressive distribution | Yes | Y7 | $4,544,930 | $0 | $12,000,000 | $495,497 | Yes | $5,893,952 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_y6 | Y7 | 2.00x | 2.00x | 12.7% | 12.7% | Yes | Y7 | Aggressive distribution | Yes | Y7 | $4,544,930 | $0 | $12,000,000 | $495,497 | Yes | $5,893,952 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_y5 | Y7 | 2.00x | 2.00x | 12.7% | 12.7% | Yes | Y7 | Aggressive distribution | Yes | Y7 | $4,544,930 | $0 | $12,000,000 | $495,497 | Yes | $5,893,952 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_100pct | Y6 | 2.00x | 2.00x | 13.7% | 13.7% | Yes | Y6 | Backend-heavy | Yes | Y6 | $4,969,690 | $0 | $12,000,000 | $353,911 | Yes | $2,424,254 | Hurdle trigger executed |
| oak_cliff_downside_no_refi | Y7 | 0.09x | 1.20x | -33.5% | 2.7% | No |  | Backend-heavy | No |  | $0 | $0 | $874,896 | $364,540 | Yes | $0 | LP 2x not achieved |

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
- LP cash IRR: 7.1%
- LP economic IRR: 7.1%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $8,966,045
- Trigger refi used: $3,418,351
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,091,792
- GP residual NAV: $20,356,185
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,075,000.00 | 0.00 | 1,256,409.00 | 1.32 | -735,497.52 | 0.00 | 5,175,000.00 |
| 2.00 | 18,354,358.50 | 12,075,000.00 | 0.00 | 1,454,001.00 | 1.52 | -302,905.52 | 0.00 | 6,279,358.50 |
| 3.00 | 19,556,957.36 | 12,075,000.00 | 0.00 | 1,651,593.00 | 1.73 | 254,686.48 | 0.00 | 7,481,957.36 |
| 4.00 | 20,867,967.44 | 12,075,000.00 | 0.00 | 1,849,185.00 | 1.94 | 692,278.48 | 632,861.77 | 8,792,967.44 |
| 5.00 | 22,298,666.15 | 12,075,000.00 | 0.00 | 1,949,677.00 | 2.04 | 920,654.48 | 0.00 | 10,223,666.15 |
| 6.00 | 23,861,559.61 | 12,075,000.00 | 0.00 | 2,008,167.31 | 2.10 | 1,013,995.31 | 0.00 | 11,786,559.61 |
| 7.00 | 25,570,518.21 | 12,075,000.00 | 0.00 | 2,068,412.33 | 2.17 | 1,073,056.36 | 707,366.69 | 13,495,518.21 |
| 8.00 | 27,440,927.35 | 12,075,000.00 | 0.00 | 2,130,464.70 | 2.23 | 1,133,889.25 | 0.00 | 15,365,927.35 |
| 9.00 | 29,489,854.77 | 12,075,000.00 | 0.00 | 2,194,378.64 | 2.30 | 1,196,547.12 | 0.00 | 17,414,854.77 |
| 10.00 | 31,736,236.49 | 12,075,000.00 | 0.00 | 2,260,210.00 | 2.37 | 1,261,084.73 | 0.00 | 19,661,236.49 |
| 11.00 | 34,201,083.28 | 12,075,000.00 | 0.00 | 2,328,016.30 | 2.44 | 1,327,558.47 | 0.00 | 22,126,083.28 |

### jon_downside_case

Deal 1 downside — slower lease-up, lower NOI ramp, higher capex, tighter refi. HF -15% Y1 then recovery.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.3%
- LP economic IRR: 5.3%
- Years until LP 2x cash return: 15
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $7,124,333
- Trigger refi used: $5,822,838
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,350,943
- GP residual NAV: $27,597,321
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Long zero-distribution period

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $435,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,075,000.00 | 0.00 | 1,136,409.00 | 1.19 | -900,047.52 | 0.00 | 5,175,000.00 |
| 2.00 | 18,154,358.50 | 12,075,000.00 | 0.00 | 1,274,001.00 | 1.33 | -520,705.52 | 0.00 | 6,079,358.50 |
| 3.00 | 19,148,957.36 | 12,075,000.00 | 0.00 | 1,411,593.00 | 1.48 | -26,363.52 | 0.00 | 7,073,957.36 |
| 4.00 | 20,243,707.44 | 12,075,000.00 | 0.00 | 1,549,185.00 | 1.62 | 372,978.48 | 0.00 | 8,168,707.44 |
| 5.00 | 21,449,618.15 | 12,075,000.00 | 0.00 | 1,686,777.00 | 1.77 | 619,320.48 | 0.00 | 9,374,618.15 |
| 6.00 | 22,778,919.36 | 12,075,000.00 | 0.00 | 1,723,480.31 | 1.81 | 733,676.29 | 0.00 | 10,703,919.36 |
| 7.00 | 24,245,196.75 | 12,075,000.00 | 0.00 | 1,761,145.72 | 1.84 | 770,990.72 | 0.00 | 12,170,196.75 |
| 8.00 | 25,863,542.21 | 12,075,000.00 | 0.00 | 1,799,800.70 | 1.89 | 809,291.22 | 0.00 | 13,788,542.21 |
| 9.00 | 27,650,721.02 | 12,075,000.00 | 0.00 | 1,839,473.54 | 1.93 | 848,606.03 | 0.00 | 15,575,721.02 |
| 10.00 | 29,625,357.38 | 12,075,000.00 | 0.00 | 1,880,193.35 | 1.97 | 888,964.23 | 0.00 | 17,550,357.38 |
| 11.00 | 31,808,140.74 | 12,075,000.00 | 0.00 | 1,921,990.11 | 2.01 | 930,395.76 | 0.00 | 19,733,140.74 |
| 12.00 | 34,222,054.88 | 12,075,000.00 | 0.00 | 1,964,894.68 | 2.06 | 972,931.46 | 0.00 | 22,147,054.88 |
| 13.00 | 36,892,632.41 | 12,075,000.00 | 0.00 | 2,008,938.84 | 2.10 | 1,016,603.05 | 0.00 | 24,817,632.41 |
| 14.00 | 39,848,237.61 | 12,075,000.00 | 0.00 | 2,054,155.30 | 2.15 | 1,061,443.22 | 0.00 | 27,773,237.61 |
| 15.00 | 43,120,380.53 | 12,075,000.00 | 0.00 | 2,100,577.73 | 2.20 | 1,107,485.59 | 0.00 | 31,045,380.53 |

### jon_property_shock_25

Deal 1 property shock — 25% value drop in Year 2 (market correction), 5-year recovery back to pre-shock trajectory. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.7%
- LP economic IRR: 6.7%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $8,505,930
- Trigger refi used: $3,153,630
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,578,283
- GP residual NAV: $22,466,957
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Covenant Breach Hf Injection, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,075,000.00 | 0.00 | 1,256,409.00 | 1.32 | -735,497.52 | 0.00 | 5,175,000.00 |
| 2.00 | 18,354,358.50 | 12,075,000.00 | 0.00 | 1,454,001.00 | 1.52 | -302,905.52 | 0.00 | 6,279,358.50 |
| 3.00 | 16,672,957.36 | 11,255,000.00 | 0.00 | 1,651,593.00 | 1.85 | 316,186.48 | 0.00 | 5,417,957.36 |
| 4.00 | 18,121,472.44 | 11,255,000.00 | 0.00 | 1,849,185.00 | 2.07 | 753,778.48 | 0.00 | 6,866,472.44 |
| 5.00 | 19,707,018.78 | 11,255,000.00 | 0.00 | 1,949,677.00 | 2.18 | 982,154.48 | 0.00 | 8,452,018.78 |
| 6.00 | 21,443,402.59 | 11,255,000.00 | 0.00 | 2,008,167.31 | 2.25 | 1,075,495.31 | 0.00 | 10,188,402.59 |
| 7.00 | 23,345,879.41 | 11,255,000.00 | 0.00 | 2,068,412.33 | 2.32 | 1,134,556.36 | 605,590.94 | 12,090,879.41 |
| 8.00 | 25,431,310.03 | 11,255,000.00 | 0.00 | 2,130,464.70 | 2.39 | 1,195,389.25 | 0.00 | 14,176,310.03 |
| 9.00 | 27,419,948.93 | 11,255,000.00 | 0.00 | 2,194,378.64 | 2.46 | 1,258,047.12 | 0.00 | 16,164,948.93 |
| 10.00 | 29,604,233.48 | 11,255,000.00 | 0.00 | 2,260,210.00 | 2.53 | 1,322,584.73 | 0.00 | 18,349,233.48 |
| 11.00 | 32,005,120.18 | 11,255,000.00 | 0.00 | 2,328,016.30 | 2.61 | 1,389,058.47 | 0.00 | 20,750,120.18 |
| 12.00 | 34,645,868.12 | 11,255,000.00 | 0.00 | 2,397,856.79 | 2.68 | 1,457,526.42 | 0.00 | 23,390,868.12 |

### jon_property_shock_40

Deal 1 severe shock — 40% value drop in Year 2, property deeply underwater (debt > value). 5-year recovery at 10.8%/yr. Tests LP resilience when all scheduled refis fail. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $5,679,324
- Trigger refi used: $4,354,007
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,810,033
- GP residual NAV: $20,664,356
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Covenant Breach Hf Injection, Refinance event occurred, HF major drawdown

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,075,000.00 | 0.00 | 1,256,409.00 | 1.32 | -735,497.52 | 0.00 | 5,175,000.00 |
| 2.00 | 18,354,358.50 | 12,075,000.00 | 0.00 | 1,454,001.00 | 1.52 | -302,905.52 | 0.00 | 6,279,358.50 |
| 3.00 | 15,127,957.36 | 10,019,000.00 | 0.00 | 1,651,593.00 | 2.06 | 408,886.48 | 0.00 | 5,108,957.36 |
| 4.00 | 16,788,137.44 | 10,019,000.00 | 0.00 | 1,849,185.00 | 2.31 | 846,478.48 | 0.00 | 6,769,137.44 |
| 5.00 | 18,630,541.57 | 10,019,000.00 | 0.00 | 1,949,677.00 | 2.44 | 1,074,854.48 | 0.00 | 8,611,541.57 |
| 6.00 | 20,675,174.44 | 10,019,000.00 | 0.00 | 2,008,167.31 | 2.51 | 1,168,195.31 | 0.00 | 10,656,174.44 |
| 7.00 | 22,944,237.22 | 10,019,000.00 | 0.00 | 2,068,412.33 | 2.58 | 1,227,256.36 | 1,536,570.15 | 12,925,237.22 |
| 8.00 | 25,462,368.81 | 10,019,000.00 | 0.00 | 2,130,464.70 | 2.66 | 1,288,089.25 | 0.00 | 15,443,368.81 |
| 9.00 | 27,451,939.48 | 10,019,000.00 | 0.00 | 2,194,378.64 | 2.74 | 1,350,747.12 | 0.00 | 17,432,939.48 |
| 10.00 | 29,637,183.74 | 10,019,000.00 | 0.00 | 2,260,210.00 | 2.82 | 1,415,284.73 | 0.00 | 19,618,183.74 |
| 11.00 | 32,039,058.95 | 10,019,000.00 | 0.00 | 2,328,016.30 | 2.91 | 1,481,758.47 | 0.00 | 22,020,058.95 |
| 12.00 | 34,680,825.05 | 10,019,000.00 | 0.00 | 2,397,856.79 | 3.00 | 1,550,226.42 | 0.00 | 24,661,825.05 |

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
- LP cash IRR: 8.7%
- LP economic IRR: 8.7%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $9,533,742
- Trigger refi used: $2,288,272
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,938,908
- GP residual NAV: $18,050,088
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $655,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,075,000; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $701,409; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,075,000.00 | 0.00 | 1,356,409.00 | 1.42 | -569,672.52 | 0.00 | 5,175,000.00 |
| 2.00 | 18,554,358.50 | 12,075,000.00 | 0.00 | 1,644,001.00 | 1.72 | -42,455.52 | 0.00 | 6,479,358.50 |
| 3.00 | 19,972,957.36 | 12,075,000.00 | 0.00 | 1,931,593.00 | 2.02 | 584,761.48 | 0.00 | 7,897,957.36 |
| 4.00 | 21,516,947.44 | 12,075,000.00 | 0.00 | 2,047,585.00 | 2.14 | 899,668.48 | 1,086,824.38 | 9,441,947.44 |
| 5.00 | 23,198,640.55 | 12,075,000.00 | 0.00 | 2,165,313.00 | 2.27 | 1,145,268.08 | 0.00 | 11,123,640.55 |
| 6.00 | 25,031,634.49 | 12,075,000.00 | 0.00 | 2,242,007.75 | 2.35 | 1,256,789.29 | 0.00 | 12,956,634.49 |
| 7.00 | 27,030,951.65 | 12,075,000.00 | 0.00 | 2,321,472.76 | 2.43 | 1,335,033.82 | 1,274,437.43 | 14,955,951.65 |
| 8.00 | 29,213,192.92 | 12,075,000.00 | 0.00 | 2,403,809.90 | 2.52 | 1,416,101.68 | 0.00 | 17,138,192.92 |
| 9.00 | 31,596,708.40 | 12,075,000.00 | 0.00 | 2,489,124.89 | 2.61 | 1,500,096.59 | 0.00 | 19,521,708.40 |

### oak_cliff_base_no_refi

Oak Cliff base case using independent underwriting, no deal-level refi.

- LP cash multiple: 0.12x
- LP economic multiple: 2.00x
- LP cash IRR: -30.6%
- LP economic IRR: 10.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,189,194
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

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

- LP cash multiple: 0.12x
- LP economic multiple: 2.00x
- LP cash IRR: -30.6%
- LP economic IRR: 10.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,189,194
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

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

- LP cash multiple: 0.30x
- LP economic multiple: 2.00x
- LP cash IRR: -22.0%
- LP economic IRR: 11.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,035,012
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

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

- LP cash multiple: 1.19x
- LP economic multiple: 2.00x
- LP cash IRR: 3.5%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,157,772
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, Refinance event occurred

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

- LP cash multiple: 1.19x
- LP economic multiple: 2.00x
- LP cash IRR: 3.7%
- LP economic IRR: 13.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,157,772
- Total cash reinvested into HF: $495,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, Refinance event occurred

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

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 12.7%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: 7
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $4,544,930
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $495,497
- GP residual NAV: $5,893,952
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

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

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 12.7%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: 7
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $4,544,930
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $495,497
- GP residual NAV: $5,893,952
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

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

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 12.7%
- LP economic IRR: 12.7%
- Years until LP 2x cash return: 7
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $4,544,930
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $495,497
- GP residual NAV: $5,893,952
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

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

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 13.7%
- LP economic IRR: 13.7%
- Years until LP 2x cash return: 6
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 6
- Trigger HF liquidation used: $4,969,690
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $353,911
- GP residual NAV: $2,424,254
- GP survivability risk: True
- Key flags: LP 2x achieved, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

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

### oak_cliff_downside_no_refi

Oak Cliff downside case with slower value growth, weaker HF returns, and no refi.

- LP cash multiple: 0.09x
- LP economic multiple: 1.20x
- LP cash IRR: -33.5%
- LP economic IRR: 2.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $874,896
- Total cash reinvested into HF: $364,540
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Slow time horizon drift, GP survivability risk, Long zero-distribution period, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

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
