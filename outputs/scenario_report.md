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
| jon_base_case | Y11 | 2.00x | 2.00x | 7.4% | 7.4% | Yes | Y11 | Backend-heavy | Yes | Y11 | $9,478,415 | $1,620,941 | $20,000,000 | $2,330,538 | Yes | $22,609,471 | Hurdle trigger executed |
| jon_downside_case | Y14 | 2.00x | 2.00x | 5.7% | 5.7% | Yes | Y14 | Backend-heavy | Yes | Y14 | $6,591,238 | $6,226,813 | $20,000,000 | $2,224,136 | Yes | $24,028,589 | Hurdle trigger executed |
| jon_property_shock_25 | Y11 | 2.00x | 2.00x | 7.4% | 7.4% | Yes | Y11 | Backend-heavy | Yes | Y11 | $7,808,692 | $3,610,177 | $20,000,000 | $2,468,913 | Yes | $19,422,335 | Hurdle trigger executed |
| jon_property_shock_40 | Y12 | 2.00x | 2.00x | 7.0% | 7.0% | Yes | Y12 | Backend-heavy | Yes | Y12 | $6,256,695 | $2,498,027 | $20,000,000 | $3,046,636 | Yes | $22,997,877 | Hurdle trigger executed |
| five_million_fund | Y12 | 2.00x | 2.00x | 6.5% | 6.5% | Yes | Y12 | Backend-heavy | Yes | Y12 | $7,483,231 | $513,907 | $10,000,000 | $667,621 | Yes | $6,257,786 | Hurdle trigger executed |
| jon_upside_case | Y9 | 2.00x | 2.00x | 9.1% | 9.1% | Yes | Y9 | Backend-heavy | Yes | Y9 | $10,204,963 | $0 | $20,000,000 | $2,288,325 | Yes | $20,901,254 | Hurdle trigger executed |
| oak_cliff_base_no_refi | Y7 | 0.32x | 2.00x | -21.2% | 11.3% | No |  | Moderate yield | No |  | $0 | $0 | $1,933,950 | $805,812 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_base_year4_refi | Y7 | 0.32x | 2.00x | -21.2% | 11.3% | No |  | Moderate yield | No |  | $0 | $0 | $1,933,950 | $805,812 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_year4_refi_to_lp | Y7 | 0.64x | 2.00x | -9.8% | 12.4% | No |  | Moderate yield | No |  | $0 | $0 | $3,863,051 | $805,812 | Yes | $0 | Value hurdle reached but liquidity constrained |
| oak_cliff_6m_year5_sale_to_lp | Y6 | 2.00x | 2.00x | 14.5% | 14.5% | Yes | Y6 | Backend-heavy | Yes | Y6 | $3,404,022 | $0 | $12,000,000 | $666,075 | Yes | $4,715,191 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_plus_refi_to_lp | Y6 | 2.00x | 2.00x | 15.1% | 15.1% | Yes | Y6 | Backend-heavy | Yes | Y6 | $3,408,904 | $0 | $12,000,000 | $666,075 | Yes | $4,715,191 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation | Y5 | 2.00x | 2.00x | 15.6% | 15.6% | Yes | Y5 | Backend-heavy | Yes | Y5 | $3,801,637 | $0 | $12,000,000 | $533,537 | Yes | $1,607,510 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_y6 | Y5 | 2.00x | 2.00x | 15.6% | 15.6% | Yes | Y5 | Backend-heavy | Yes | Y5 | $3,801,637 | $0 | $12,000,000 | $533,537 | Yes | $1,607,510 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_y5 | Y5 | 2.00x | 2.00x | 15.6% | 15.6% | Yes | Y5 | Backend-heavy | Yes | Y5 | $3,801,637 | $0 | $12,000,000 | $533,537 | Yes | $1,607,510 | Hurdle trigger executed |
| oak_cliff_6m_year5_sale_hf25_backend_liquidation_100pct | Y5 | 2.00x | 2.00x | 15.6% | 15.6% | Yes | Y5 | Backend-heavy | Yes | Y5 | $3,801,637 | $0 | $12,000,000 | $533,537 | Yes | $1,607,510 | Hurdle trigger executed |
| oak_cliff_downside_no_refi | Y7 | 0.17x | 1.49x | -26.6% | 6.1% | No |  | Moderate yield | No |  | $0 | $0 | $1,024,374 | $426,822 | Yes | $0 | LP 2x not achieved |

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
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $9,478,415
- Trigger refi used: $1,620,941
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,330,538
- GP residual NAV: $22,609,471
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,025,918.48 | 0.00 | 1,347,765.97 | 1.41 | 155,859.45 | 0.00 | 5,224,081.52 |
| 2.00 | 18,354,358.50 | 11,973,155.84 | 0.00 | 1,547,461.15 | 1.62 | 390,554.63 | 0.00 | 6,381,202.66 |
| 3.00 | 19,556,957.36 | 11,916,436.01 | 0.00 | 1,747,838.05 | 1.83 | 650,931.53 | 0.00 | 7,640,521.35 |
| 4.00 | 20,867,967.44 | 11,855,462.19 | 0.00 | 1,896,946.09 | 1.99 | 840,039.57 | 632,861.77 | 9,012,505.25 |
| 5.00 | 22,298,666.15 | 11,789,915.33 | 0.00 | 1,949,677.36 | 2.04 | 956,654.84 | 0.00 | 10,508,750.82 |
| 6.00 | 23,861,559.61 | 11,789,915.33 | 0.00 | 2,008,167.68 | 2.10 | 1,013,995.68 | 0.00 | 12,071,644.28 |
| 7.00 | 25,570,518.21 | 11,789,915.33 | 0.00 | 2,068,412.71 | 2.17 | 1,073,056.75 | 707,366.69 | 13,780,602.88 |
| 8.00 | 27,440,927.35 | 11,789,915.33 | 0.00 | 2,130,465.09 | 2.23 | 1,133,889.64 | 0.00 | 15,651,012.02 |
| 9.00 | 29,489,854.77 | 11,789,915.33 | 0.00 | 2,194,379.05 | 2.30 | 1,196,547.53 | 0.00 | 17,699,939.44 |
| 10.00 | 31,736,236.49 | 11,789,915.33 | 0.00 | 2,260,210.42 | 2.37 | 1,261,085.15 | 0.00 | 19,946,321.16 |
| 11.00 | 34,201,083.28 | 11,789,915.33 | 0.00 | 2,328,016.73 | 2.44 | 1,327,558.90 | 0.00 | 22,411,167.95 |

### jon_downside_case

Deal 1 downside — slower lease-up, lower NOI ramp, higher capex, tighter refi. HF -15% Y1 then recovery.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.7%
- LP economic IRR: 5.7%
- Years until LP 2x cash return: 14
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $6,591,238
- Trigger refi used: $6,226,813
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,224,136
- GP residual NAV: $24,028,589
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $435,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,025,918.48 | 0.00 | 1,227,765.97 | 1.29 | -8,690.55 | 0.00 | 5,224,081.52 |
| 2.00 | 18,154,358.50 | 11,973,155.84 | 0.00 | 1,367,461.15 | 1.43 | 172,754.63 | 0.00 | 6,181,202.66 |
| 3.00 | 19,148,957.36 | 11,916,436.01 | 0.00 | 1,507,838.05 | 1.58 | 369,881.53 | 0.00 | 7,232,521.35 |
| 4.00 | 20,243,707.44 | 11,855,462.19 | 0.00 | 1,596,946.09 | 1.67 | 520,739.57 | 0.00 | 8,388,245.25 |
| 5.00 | 21,449,618.15 | 11,789,915.33 | 0.00 | 1,686,777.36 | 1.77 | 655,320.84 | 0.00 | 9,659,702.82 |
| 6.00 | 22,778,919.36 | 11,789,915.33 | 0.00 | 1,723,480.68 | 1.81 | 733,676.66 | 0.00 | 10,989,004.03 |
| 7.00 | 24,245,196.75 | 11,789,915.33 | 0.00 | 1,761,146.10 | 1.84 | 770,991.11 | 0.00 | 12,455,281.42 |
| 8.00 | 25,863,542.21 | 11,789,915.33 | 0.00 | 1,799,801.09 | 1.89 | 809,291.61 | 0.00 | 14,073,626.88 |
| 9.00 | 27,650,721.02 | 11,789,915.33 | 0.00 | 1,839,473.94 | 1.93 | 848,606.43 | 0.00 | 15,860,805.69 |
| 10.00 | 29,625,357.38 | 11,789,915.33 | 0.00 | 1,880,193.77 | 1.97 | 888,964.65 | 0.00 | 17,835,442.05 |
| 11.00 | 31,808,140.74 | 11,789,915.33 | 0.00 | 1,921,990.54 | 2.01 | 930,396.19 | 0.00 | 20,018,225.41 |
| 12.00 | 34,222,054.88 | 11,789,915.33 | 0.00 | 1,964,895.13 | 2.06 | 972,931.90 | 0.00 | 22,432,139.55 |
| 13.00 | 36,892,632.41 | 11,789,915.33 | 0.00 | 2,008,939.30 | 2.10 | 1,016,603.51 | 0.00 | 25,102,717.08 |
| 14.00 | 39,848,237.61 | 11,789,915.33 | 0.00 | 2,054,155.77 | 2.15 | 1,061,443.68 | 0.00 | 28,058,322.28 |

### jon_property_shock_25

Deal 1 property shock — 25% value drop in Year 2 (market correction), 5-year recovery back to pre-shock trajectory. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $7,808,692
- Trigger refi used: $3,610,177
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,468,913
- GP residual NAV: $19,422,335
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Covenant Breach Hf Injection, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,025,918.48 | 0.00 | 1,347,765.97 | 1.41 | 155,859.45 | 0.00 | 5,224,081.52 |
| 2.00 | 18,354,358.50 | 11,973,155.84 | 0.00 | 1,547,461.15 | 1.62 | 390,554.63 | 0.00 | 6,381,202.66 |
| 3.00 | 16,672,957.36 | 11,096,436.01 | 0.00 | 1,747,838.05 | 1.96 | 712,431.53 | 0.00 | 5,576,521.35 |
| 4.00 | 18,121,472.44 | 11,035,462.19 | 0.00 | 1,896,946.09 | 2.12 | 901,539.57 | 0.00 | 7,086,010.25 |
| 5.00 | 19,707,018.78 | 10,969,915.33 | 0.00 | 1,949,677.36 | 2.18 | 1,018,154.84 | 0.00 | 8,737,103.45 |
| 6.00 | 21,443,402.59 | 10,969,915.33 | 0.00 | 2,008,167.68 | 2.25 | 1,075,495.68 | 0.00 | 10,473,487.26 |
| 7.00 | 23,345,879.41 | 10,969,915.33 | 0.00 | 2,068,412.71 | 2.32 | 1,134,556.75 | 605,590.94 | 12,375,964.08 |
| 8.00 | 25,431,310.03 | 10,969,915.33 | 0.00 | 2,130,465.09 | 2.39 | 1,195,389.64 | 0.00 | 14,461,394.70 |
| 9.00 | 27,419,948.93 | 10,969,915.33 | 0.00 | 2,194,379.05 | 2.46 | 1,258,047.53 | 0.00 | 16,450,033.60 |
| 10.00 | 29,604,233.48 | 10,969,915.33 | 0.00 | 2,260,210.42 | 2.53 | 1,322,585.15 | 0.00 | 18,634,318.15 |
| 11.00 | 32,005,120.18 | 10,969,915.33 | 0.00 | 2,328,016.73 | 2.61 | 1,389,058.90 | 0.00 | 21,035,204.85 |

### jon_property_shock_40

Deal 1 severe shock — 40% value drop in Year 2, property deeply underwater (debt > value). 5-year recovery at 10.8%/yr. Tests LP resilience when all scheduled refis fail. HF 13% base. Cashflow routing 60/25/15.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.0%
- LP economic IRR: 7.0%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $6,256,695
- Trigger refi used: $2,498,027
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,046,636
- GP residual NAV: $22,997,877
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Covenant Breach Hf Injection, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $555,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,025,918.48 | 0.00 | 1,347,765.97 | 1.41 | 155,859.45 | 0.00 | 5,224,081.52 |
| 2.00 | 18,354,358.50 | 11,973,155.84 | 0.00 | 1,547,461.15 | 1.62 | 390,554.63 | 0.00 | 6,381,202.66 |
| 3.00 | 15,127,957.36 | 9,860,436.01 | 0.00 | 1,747,838.05 | 2.18 | 805,131.53 | 0.00 | 5,267,521.35 |
| 4.00 | 16,788,137.44 | 9,799,462.19 | 0.00 | 1,896,946.09 | 2.37 | 994,239.57 | 0.00 | 6,988,675.25 |
| 5.00 | 18,630,541.57 | 9,733,915.33 | 0.00 | 1,949,677.36 | 2.44 | 1,110,854.84 | 0.00 | 8,896,626.24 |
| 6.00 | 20,675,174.44 | 9,733,915.33 | 0.00 | 2,008,167.68 | 2.51 | 1,168,195.68 | 0.00 | 10,941,259.11 |
| 7.00 | 22,944,237.22 | 9,733,915.33 | 0.00 | 2,068,412.71 | 2.58 | 1,227,256.75 | 1,536,570.15 | 13,210,321.89 |
| 8.00 | 25,462,368.81 | 9,733,915.33 | 0.00 | 2,130,465.09 | 2.66 | 1,288,089.64 | 0.00 | 15,728,453.48 |
| 9.00 | 27,451,939.48 | 9,733,915.33 | 0.00 | 2,194,379.05 | 2.74 | 1,350,747.53 | 0.00 | 17,718,024.15 |
| 10.00 | 29,637,183.74 | 9,733,915.33 | 0.00 | 2,260,210.42 | 2.82 | 1,415,285.15 | 0.00 | 19,903,268.41 |
| 11.00 | 32,039,058.95 | 9,733,915.33 | 0.00 | 2,328,016.73 | 2.91 | 1,481,758.90 | 0.00 | 22,305,143.62 |
| 12.00 | 34,680,825.05 | 9,733,915.33 | 0.00 | 2,397,857.23 | 3.00 | 1,550,226.86 | 0.00 | 24,946,909.72 |

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
- LP cash IRR: 9.1%
- LP economic IRR: 9.1%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $10,204,963
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,288,325
- GP residual NAV: $20,901,254
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred

#### Bottom-Up Deal Summary

- jon_deal_1: gross assets $10,000,000; assumed debt $7,000,000; other liabilities $0; new equity required $3,000,000; entry equity cushion $0; current NOI $655,000; refi LTV capacity $0
- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 17,250,000.00 | 12,025,918.48 | 0.00 | 1,447,765.97 | 1.52 | 321,684.45 | 0.00 | 5,224,081.52 |
| 2.00 | 18,554,358.50 | 11,973,155.84 | 0.00 | 1,737,461.15 | 1.82 | 651,004.63 | 0.00 | 6,581,202.66 |
| 3.00 | 19,972,957.36 | 11,916,436.01 | 0.00 | 2,027,838.05 | 2.12 | 981,006.53 | 0.00 | 8,056,521.35 |
| 4.00 | 21,516,947.44 | 11,855,462.19 | 0.00 | 2,095,346.09 | 2.19 | 1,047,429.57 | 1,086,824.38 | 9,661,485.25 |
| 5.00 | 23,198,640.55 | 11,789,915.33 | 0.00 | 2,165,313.36 | 2.27 | 1,181,268.44 | 0.00 | 11,408,725.22 |
| 6.00 | 25,031,634.49 | 11,789,915.33 | 0.00 | 2,242,008.12 | 2.35 | 1,256,789.66 | 0.00 | 13,241,719.16 |
| 7.00 | 27,030,951.65 | 11,789,915.33 | 0.00 | 2,321,473.14 | 2.43 | 1,335,034.21 | 1,274,437.43 | 15,241,036.32 |
| 8.00 | 29,213,192.92 | 11,789,915.33 | 0.00 | 2,403,810.30 | 2.52 | 1,416,102.07 | 0.00 | 17,423,277.59 |
| 9.00 | 31,596,708.40 | 11,789,915.33 | 0.00 | 2,489,125.29 | 2.61 | 1,500,096.99 | 0.00 | 19,806,793.07 |

### oak_cliff_base_no_refi

Oak Cliff base case using independent underwriting, no deal-level refi.

- LP cash multiple: 0.32x
- LP economic multiple: 2.00x
- LP cash IRR: -21.2%
- LP economic IRR: 11.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,933,950
- Total cash reinvested into HF: $805,812
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |
| 6.00 | 12,268,818.86 | 4,789,915.33 | 0.00 | 1,021,530.68 | 2.38 | 591,824.16 | 0.00 | 7,478,903.53 |
| 7.00 | 13,629,995.24 | 4,789,915.33 | 0.00 | 1,052,176.60 | 2.45 | 622,470.08 | 0.00 | 8,840,079.91 |

### oak_cliff_base_year4_refi

Oak Cliff base case with year-4 refi using independent valuation ramp.

- LP cash multiple: 0.32x
- LP economic multiple: 2.00x
- LP cash IRR: -21.2%
- LP economic IRR: 11.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,933,950
- Total cash reinvested into HF: $805,812
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $48,100

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 2,060,965.49 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |
| 6.00 | 12,268,818.86 | 4,789,915.33 | 0.00 | 1,021,530.68 | 2.38 | 591,824.16 | 0.00 | 7,478,903.53 |
| 7.00 | 13,629,995.24 | 4,789,915.33 | 0.00 | 1,052,176.60 | 2.45 | 622,470.08 | 0.00 | 8,840,079.91 |

### oak_cliff_year4_refi_to_lp

Oak Cliff base case with year-4 refi proceeds distributed directly to LPs.

- LP cash multiple: 0.64x
- LP economic multiple: 2.00x
- LP cash IRR: -9.8%
- LP economic IRR: 12.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,863,051
- Total cash reinvested into HF: $805,812
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |
| 6.00 | 12,268,818.86 | 4,789,915.33 | 0.00 | 1,021,530.68 | 2.38 | 591,824.16 | 0.00 | 7,478,903.53 |
| 7.00 | 13,629,995.24 | 4,789,915.33 | 0.00 | 1,052,176.60 | 2.45 | 622,470.08 | 0.00 | 8,840,079.91 |

### oak_cliff_6m_year5_sale_to_lp

Oak Cliff $6m fund case with year-5 sale proceeds proxied by a scenario-level liquidity event to LPs.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 14.5%
- LP economic IRR: 14.5%
- Years until LP 2x cash return: 6
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 6
- Trigger HF liquidation used: $3,404,022
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $666,075
- GP residual NAV: $4,715,191
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |
| 6.00 | 12,268,818.86 | 4,789,915.33 | 0.00 | 1,021,530.68 | 2.38 | 591,824.16 | 0.00 | 7,478,903.53 |

### oak_cliff_6m_year5_sale_plus_refi_to_lp

Oak Cliff $6m fund case with year-4 refi to LPs and year-5 sale proceeds net of refi liability proxied to LPs.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 15.1%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: 6
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 6
- Trigger HF liquidation used: $3,408,904
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $666,075
- GP residual NAV: $4,715,191
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |
| 6.00 | 12,268,818.86 | 4,789,915.33 | 0.00 | 1,021,530.68 | 2.38 | 591,824.16 | 0.00 | 7,478,903.53 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-7 backend HF liquidation capped at 75%.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 15.6%
- LP economic IRR: 15.6%
- Years until LP 2x cash return: 5
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 5
- Trigger HF liquidation used: $3,801,637
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $533,537
- GP residual NAV: $1,607,510
- GP survivability risk: True
- Key flags: LP 2x achieved, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation_y6

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-6 backend HF liquidation capped at 75%.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 15.6%
- LP economic IRR: 15.6%
- Years until LP 2x cash return: 5
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 5
- Trigger HF liquidation used: $3,801,637
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $533,537
- GP residual NAV: $1,607,510
- GP survivability risk: True
- Key flags: LP 2x achieved, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation_y5

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-5 backend HF liquidation capped at 75%.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 15.6%
- LP economic IRR: 15.6%
- Years until LP 2x cash return: 5
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 5
- Trigger HF liquidation used: $3,801,637
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $533,537
- GP residual NAV: $1,607,510
- GP survivability risk: True
- Key flags: LP 2x achieved, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |

### oak_cliff_6m_year5_sale_hf25_backend_liquidation_100pct

Oak Cliff $6m fund case with year-5 sale proxy to LPs and year-7 backend HF liquidation capped at 100%.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 15.6%
- LP economic IRR: 15.6%
- Years until LP 2x cash return: 5
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 5
- Trigger HF liquidation used: $3,801,637
- Trigger refi used: $0
- Total cash distributed to LP: $12,000,000
- Total cash reinvested into HF: $533,537
- GP residual NAV: $1,607,510
- GP survivability risk: True
- Key flags: LP 2x achieved, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | 363,059.45 | 0.00 | 2,224,081.52 |
| 2.00 | 8,054,358.50 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | 437,754.63 | 0.00 | 3,081,202.66 |
| 3.00 | 8,947,957.36 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 513,131.53 | 0.00 | 4,031,521.35 |
| 4.00 | 9,940,697.44 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 537,239.57 | 0.00 | 5,085,235.25 |
| 5.00 | 11,043,578.05 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 562,070.84 | 0.00 | 6,253,662.72 |

### oak_cliff_downside_no_refi

Oak Cliff downside case with slower value growth, weaker HF returns, and no refi.

- LP cash multiple: 0.17x
- LP economic multiple: 1.49x
- LP cash IRR: -26.6%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,024,374
- Total cash reinvested into HF: $426,822
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Slow time horizon drift, GP survivability risk, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

#### Bottom-Up Deal Summary

- oak_cliff: gross assets $7,250,000; assumed debt $5,025,918; other liabilities $0; new equity required $4,156,000; entry equity cushion $-1,981,000; current NOI $792,766; refi LTV capacity $0

Annual bottom-up RE portfolio:

| Year | Gross assets | Debt | Liabilities | NOI | DSCR | Free cashflow | Refi proceeds | Deal NAV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.00 | 7,250,000.00 | 5,025,918.48 | 0.00 | 792,765.97 | 1.84 | -536,940.55 | 0.00 | 2,224,081.52 |
| 2.00 | 7,685,000.00 | 4,973,155.84 | 0.00 | 867,461.15 | 2.02 | -262,245.37 | 0.00 | 2,711,844.16 |
| 3.00 | 8,146,100.00 | 4,916,436.01 | 0.00 | 942,838.05 | 2.19 | 113,131.53 | 0.00 | 3,229,663.99 |
| 4.00 | 8,634,866.00 | 4,855,462.19 | 0.00 | 966,946.09 | 2.25 | 387,239.57 | 0.00 | 3,779,403.81 |
| 5.00 | 9,152,957.96 | 4,789,915.33 | 0.00 | 991,777.36 | 2.31 | 512,070.84 | 0.00 | 4,363,042.63 |
| 6.00 | 9,702,135.44 | 4,789,915.33 | 0.00 | 918,000.00 | 2.14 | 488,293.48 | 0.00 | 4,912,220.11 |
| 7.00 | 10,284,263.56 | 4,789,915.33 | 0.00 | 936,360.00 | 2.18 | 506,653.48 | 0.00 | 5,494,348.23 |
