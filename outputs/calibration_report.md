# Scenario Report

Deterministic annual model. LP hurdle achievement is based on actual cash distributions received, not NAV appreciation.

Scenarios are run on a diagnostic horizon set in the YAML inputs, currently 20 years. The engine stops a scenario early once the LP cash hurdle is achieved, so `years_modelled` shows the actual time required to reach 2.0x or the full diagnostic horizon if the hurdle is not reached.

## Summary

| Scenario | Years modelled | LP cash multiple | LP economic multiple | LP cash IRR | LP economic IRR | LP 2x achieved? | Years to LP 2x cash | LP cashflow profile | Trigger executed? | Trigger year | HF liquidation used | Refi used | Total paid to LP | Total reinvested into HF | GP survivability risk? | GP residual NAV | Primary diagnostic flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| policy_set_comparison__base_hit_everyone_happy__backend_heavy_compounding | Y20 | 0.74x | 2.00x | -2.6% | 4.5% | No |  | Moderate yield | No |  | $0 | $0 | $7,399,618 | $18,058,371 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__base_hit_everyone_happy__balanced_yield_compounding | Y15 | 2.00x | 2.00x | 6.9% | 6.9% | Yes | Y15 | Aggressive distribution | Yes | Y15 | $4,743,878 | $0 | $20,000,000 | $5,971,537 | Yes | $19,204,694 | Hurdle trigger executed |
| policy_set_comparison__base_hit_everyone_happy__aggressive_lp_extinguishment | Y14 | 2.00x | 2.00x | 8.9% | 8.9% | Yes | Y14 | Aggressive distribution | Yes | Y14 | $2,916,394 | $0 | $20,000,000 | $2,311,694 | Yes | $13,626,660 | Hurdle trigger executed |
| policy_set_comparison__fast_success_crypto_bull__backend_heavy_compounding | Y20 | 0.90x | 2.00x | -0.9% | 4.5% | No |  | Moderate yield | No |  | $0 | $0 | $8,956,322 | $24,269,292 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__fast_success_crypto_bull__balanced_yield_compounding | Y14 | 2.00x | 2.00x | 7.3% | 7.3% | Yes | Y14 | Backend-heavy | Yes | Y14 | $4,886,194 | $0 | $20,000,000 | $6,556,929 | Yes | $21,526,363 | Hurdle trigger executed |
| policy_set_comparison__fast_success_crypto_bull__aggressive_lp_extinguishment | Y13 | 2.00x | 2.00x | 9.6% | 9.6% | Yes | Y13 | Aggressive distribution | Yes | Y13 | $3,594,278 | $176,771 | $20,000,000 | $2,045,330 | Yes | $11,112,152 | Hurdle trigger executed |
| policy_set_comparison__slow_grind__backend_heavy_compounding | Y20 | 0.54x | 2.00x | -5.3% | 4.2% | No |  | Moderate yield | No |  | $0 | $0 | $5,419,310 | $12,535,304 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__slow_grind__balanced_yield_compounding | Y19 | 2.00x | 2.00x | 5.4% | 5.4% | Yes | Y19 | Moderate yield | Yes | Y19 | $4,870,881 | $0 | $20,000,000 | $6,164,405 | Yes | $17,547,060 | Hurdle trigger executed |
| policy_set_comparison__slow_grind__aggressive_lp_extinguishment | Y18 | 2.00x | 2.00x | 7.0% | 7.0% | Yes | Y18 | Moderate yield | Yes | Y18 | $2,933,161 | $0 | $20,000,000 | $2,308,913 | Yes | $11,296,290 | Hurdle trigger executed |
| policy_set_comparison__hedge_fund_failure_re_survival__backend_heavy_compounding | Y20 | 0.56x | 2.00x | -5.1% | 4.3% | No |  | Moderate yield | No |  | $0 | $0 | $5,559,905 | $12,471,979 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__hedge_fund_failure_re_survival__balanced_yield_compounding | Y19 | 2.00x | 2.00x | 5.4% | 5.4% | Yes | Y19 | Moderate yield | Yes | Y19 | $4,382,453 | $0 | $20,000,000 | $5,804,776 | Yes | $14,341,859 | Hurdle trigger executed |
| policy_set_comparison__hedge_fund_failure_re_survival__aggressive_lp_extinguishment | Y18 | 2.00x | 2.00x | 7.0% | 7.0% | Yes | Y18 | Moderate yield | Yes | Y18 | $2,259,078 | $176,717 | $20,000,000 | $2,556,046 | Yes | $11,487,806 | Hurdle trigger executed |
| policy_set_comparison__real_estate_distress_crypto_success__backend_heavy_compounding | Y20 | 0.80x | 2.00x | -1.6% | 4.2% | No |  | Moderate yield | No |  | $0 | $0 | $7,954,938 | $23,506,257 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__real_estate_distress_crypto_success__balanced_yield_compounding | Y17 | 2.00x | 2.00x | 5.6% | 5.6% | Yes | Y17 | Backend-heavy | Yes | Y17 | $5,836,882 | $0 | $20,000,000 | $7,382,032 | Yes | $21,214,237 | Hurdle trigger executed |
| policy_set_comparison__real_estate_distress_crypto_success__aggressive_lp_extinguishment | Y19 | 2.00x | 2.00x | 6.3% | 6.3% | Yes | Y19 | Moderate yield | Yes | Y19 | $3,931,352 | $0 | $20,000,000 | $1,791,574 | Yes | $5,279,330 | Hurdle trigger executed |
| policy_set_comparison__exceptional_dynasty_outcome__backend_heavy_compounding | Y17 | 2.00x | 2.00x | 5.6% | 5.6% | Yes | Y17 | Backend-heavy | Yes | Y17 | $0 | $0 | $20,000,000 | $34,221,344 | Yes | $122,812,496 | Hurdle trigger executed |
| policy_set_comparison__exceptional_dynasty_outcome__balanced_yield_compounding | Y11 | 2.00x | 2.00x | 9.2% | 9.2% | Yes | Y11 | Aggressive distribution | Yes | Y11 | $3,382,133 | $0 | $20,000,000 | $6,641,022 | Yes | $27,207,092 | Hurdle trigger executed |
| policy_set_comparison__exceptional_dynasty_outcome__aggressive_lp_extinguishment | Y10 | 2.00x | 2.00x | 12.0% | 12.0% | Yes | Y10 | Aggressive distribution | Yes | Y10 | $0 | $3,531,763 | $20,000,000 | $2,244,783 | Yes | $17,384,757 | Hurdle trigger executed |
| policy_set_comparison__liquidity_trap__backend_heavy_compounding | Y20 | 0.94x | 2.00x | -0.5% | 4.6% | No |  | Moderate yield | No |  | $0 | $0 | $9,433,937 | $23,384,676 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__liquidity_trap__balanced_yield_compounding | Y13 | 2.00x | 2.00x | 7.6% | 7.6% | Yes | Y13 | Backend-heavy | Yes | Y13 | $5,249,441 | $0 | $20,000,000 | $5,538,976 | Yes | $22,563,052 | Hurdle trigger executed |
| policy_set_comparison__liquidity_trap__aggressive_lp_extinguishment | Y12 | 2.00x | 2.00x | 9.7% | 9.7% | Yes | Y12 | Aggressive distribution | Yes | Y12 | $3,015,474 | $757,372 | $20,000,000 | $2,125,946 | Yes | $16,605,972 | Hurdle trigger executed |
| policy_set_comparison__failure_never_reaches_hurdle__backend_heavy_compounding | Y20 | 0.30x | 2.00x | -10.7% | 4.0% | No |  | Moderate yield | No |  | $0 | $0 | $3,038,116 | $5,730,253 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__failure_never_reaches_hurdle__balanced_yield_compounding | Y20 | 0.63x | 2.00x | -4.4% | 4.5% | No |  | Moderate yield | No |  | $0 | $0 | $6,328,511 | $3,110,103 | Yes | $0 | Value hurdle reached but liquidity constrained |
| policy_set_comparison__failure_never_reaches_hurdle__aggressive_lp_extinguishment | Y20 | 0.93x | 1.77x | -0.8% | 4.4% | No |  | Moderate yield | No |  | $0 | $0 | $9,278,707 | $1,219,929 | Yes | $0 | LP 2x not achieved |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_20 | Y12 | 2.00x | 2.00x | 6.3% | 6.3% | Yes | Y12 | Backend-heavy | Yes | Y12 | $11,524,148 | $2,636,265 | $20,000,000 | $5,339,587 | Yes | $14,813,892 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_30 | Y12 | 2.00x | 2.00x | 6.5% | 6.5% | Yes | Y12 | Backend-heavy | Yes | Y12 | $10,615,330 | $2,877,634 | $20,000,000 | $4,672,139 | Yes | $14,269,583 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_40 | Y12 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y12 | Backend-heavy | Yes | Y12 | $9,706,512 | $3,119,004 | $20,000,000 | $4,004,690 | Yes | $13,725,274 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_50 | Y12 | 2.00x | 2.00x | 6.9% | 6.9% | Yes | Y12 | Backend-heavy | Yes | Y12 | $8,797,694 | $3,360,374 | $20,000,000 | $3,337,242 | Yes | $13,180,965 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_60 | Y13 | 2.00x | 2.00x | 6.6% | 6.6% | Yes | Y13 | Backend-heavy | Yes | Y13 | $8,610,399 | $1,887,461 | $20,000,000 | $3,000,713 | Yes | $15,135,797 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_70 | Y13 | 2.00x | 2.00x | 6.9% | 6.9% | Yes | Y13 | Backend-heavy | Yes | Y13 | $7,585,004 | $2,162,677 | $20,000,000 | $2,250,535 | Yes | $14,518,782 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_80 | Y13 | 2.00x | 2.00x | 7.1% | 7.1% | Yes | Y13 | Backend-heavy | Yes | Y13 | $6,559,609 | $2,437,893 | $20,000,000 | $1,500,357 | Yes | $13,901,768 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_90 | Y13 | 2.00x | 2.00x | 7.4% | 7.4% | Yes | Y13 | Backend-heavy | Yes | Y13 | $5,534,215 | $2,713,110 | $20,000,000 | $750,178 | Yes | $13,284,753 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_20 | Y11 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $15,439,838 | $0 | $20,000,000 | $4,060,162 | Yes | $18,548,288 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_30 | Y11 | 2.00x | 2.00x | 6.9% | 6.9% | Yes | Y11 | Backend-heavy | Yes | Y11 | $14,932,318 | $0 | $20,000,000 | $3,552,642 | Yes | $17,834,153 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_40 | Y11 | 2.00x | 2.00x | 7.1% | 7.1% | Yes | Y11 | Backend-heavy | Yes | Y11 | $14,424,797 | $0 | $20,000,000 | $3,045,122 | Yes | $17,120,018 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_50 | Y11 | 2.00x | 2.00x | 7.3% | 7.3% | Yes | Y11 | Backend-heavy | Yes | Y11 | $13,917,277 | $0 | $20,000,000 | $2,537,601 | Yes | $16,405,882 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_60 | Y11 | 2.00x | 2.00x | 7.4% | 7.4% | Yes | Y11 | Backend-heavy | Yes | Y11 | $13,001,637 | $408,120 | $20,000,000 | $2,030,081 | Yes | $15,691,747 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_70 | Y11 | 2.00x | 2.00x | 7.6% | 7.6% | Yes | Y11 | Backend-heavy | Yes | Y11 | $12,085,395 | $816,842 | $20,000,000 | $1,522,561 | Yes | $14,977,611 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_80 | Y11 | 2.00x | 2.00x | 7.8% | 7.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $11,169,153 | $1,225,563 | $20,000,000 | $1,015,041 | Yes | $14,263,476 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_90 | Y11 | 2.00x | 2.00x | 8.0% | 8.0% | Yes | Y11 | Backend-heavy | Yes | Y11 | $10,252,912 | $1,634,285 | $20,000,000 | $507,520 | Yes | $13,549,341 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_20 | Y14 | 2.00x | 2.00x | 5.3% | 5.3% | Yes | Y14 | Backend-heavy | Yes | Y14 | $12,639,366 | $2,171,034 | $20,000,000 | $4,689,600 | Yes | $13,257,657 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_30 | Y14 | 2.00x | 2.00x | 5.5% | 5.5% | Yes | Y14 | Backend-heavy | Yes | Y14 | $11,536,410 | $2,687,790 | $20,000,000 | $4,103,400 | Yes | $12,373,249 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_40 | Y15 | 2.00x | 2.00x | 5.3% | 5.3% | Yes | Y15 | Backend-heavy | Yes | Y15 | $11,302,550 | $1,795,251 | $20,000,000 | $3,841,320 | Yes | $13,412,147 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_50 | Y15 | 2.00x | 2.00x | 5.5% | 5.5% | Yes | Y15 | Backend-heavy | Yes | Y15 | $10,092,902 | $2,364,679 | $20,000,000 | $3,201,100 | Yes | $12,439,502 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_60 | Y16 | 2.00x | 2.00x | 5.4% | 5.4% | Yes | Y16 | Backend-heavy | Yes | Y16 | $9,584,125 | $1,561,728 | $20,000,000 | $2,784,716 | Yes | $13,301,659 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_70 | Y16 | 2.00x | 2.00x | 5.6% | 5.6% | Yes | Y16 | Backend-heavy | Yes | Y16 | $8,259,929 | $2,189,746 | $20,000,000 | $2,088,537 | Yes | $12,232,242 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_80 | Y16 | 2.00x | 2.00x | 5.8% | 5.8% | Yes | Y16 | Backend-heavy | Yes | Y16 | $6,935,732 | $2,817,763 | $20,000,000 | $1,392,358 | Yes | $11,162,826 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_90 | Y17 | 2.00x | 2.00x | 5.8% | 5.8% | Yes | Y17 | Backend-heavy | Yes | Y17 | $5,991,703 | $2,196,107 | $20,000,000 | $754,146 | Yes | $11,703,180 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_20 | Y18 | 2.00x | 2.00x | 4.3% | 4.3% | Yes | Y18 | Backend-heavy | Yes | Y18 | $8,703,321 | $2,510,866 | $20,000,000 | $8,285,813 | Yes | $13,647,340 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_30 | Y18 | 2.00x | 2.00x | 4.5% | 4.5% | Yes | Y18 | Backend-heavy | Yes | Y18 | $7,658,362 | $2,520,098 | $20,000,000 | $7,250,087 | Yes | $13,289,789 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_40 | Y18 | 2.00x | 2.00x | 4.7% | 4.7% | Yes | Y18 | Backend-heavy | Yes | Y18 | $6,613,403 | $2,529,330 | $20,000,000 | $6,214,360 | Yes | $12,932,237 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_50 | Y18 | 2.00x | 2.00x | 5.0% | 5.0% | Yes | Y18 | Backend-heavy | Yes | Y18 | $5,568,445 | $2,538,562 | $20,000,000 | $5,178,633 | Yes | $12,574,685 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_60 | Y18 | 2.00x | 2.00x | 5.2% | 5.2% | Yes | Y18 | Backend-heavy | Yes | Y18 | $4,523,486 | $2,547,794 | $20,000,000 | $4,142,907 | Yes | $12,217,134 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_70 | Y18 | 2.00x | 2.00x | 5.5% | 5.5% | Yes | Y18 | Backend-heavy | Yes | Y18 | $3,478,527 | $2,557,026 | $20,000,000 | $3,107,180 | Yes | $11,859,582 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_80 | Y18 | 2.00x | 2.00x | 5.8% | 5.8% | Yes | Y18 | Moderate yield | Yes | Y18 | $2,433,569 | $2,566,258 | $20,000,000 | $2,071,453 | Yes | $11,502,031 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_90 | Y18 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y18 | Moderate yield | Yes | Y18 | $1,388,610 | $2,575,490 | $20,000,000 | $1,035,727 | Yes | $11,144,479 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_20 | Y20 | 2.00x | 2.00x | 3.7% | 3.7% | Yes | Y20 | Backend-heavy | Yes | Y20 | $16,980,371 | $0 | $20,000,000 | $2,519,629 | Yes | $126,366,785 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_30 | Y12 | 2.00x | 2.00x | 6.2% | 6.2% | Yes | Y12 | Backend-heavy | Yes | Y12 | $16,546,966 | $983,673 | $20,000,000 | $1,531,725 | Yes | $10,429,643 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_40 | Y12 | 2.00x | 2.00x | 6.2% | 6.2% | Yes | Y12 | Backend-heavy | Yes | Y12 | $15,889,396 | $1,422,425 | $20,000,000 | $1,312,907 | Yes | $9,771,701 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_50 | Y13 | 2.00x | 2.00x | 5.8% | 5.8% | Yes | Y13 | Backend-heavy | Yes | Y13 | $16,941,006 | $0 | $20,000,000 | $1,163,179 | Yes | $14,235,192 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_60 | Y13 | 2.00x | 2.00x | 5.9% | 5.9% | Yes | Y13 | Backend-heavy | Yes | Y13 | $16,708,370 | $0 | $20,000,000 | $930,543 | Yes | $13,358,060 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_70 | Y13 | 2.00x | 2.00x | 6.0% | 6.0% | Yes | Y13 | Backend-heavy | Yes | Y13 | $16,475,734 | $0 | $20,000,000 | $697,908 | Yes | $12,480,928 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_80 | Y13 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y13 | Backend-heavy | Yes | Y13 | $16,243,098 | $0 | $20,000,000 | $465,272 | Yes | $11,603,796 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_90 | Y13 | 2.00x | 2.00x | 6.2% | 6.2% | Yes | Y13 | Backend-heavy | Yes | Y13 | $15,762,297 | $248,165 | $20,000,000 | $232,636 | Yes | $10,726,664 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_20 | Y8 | 2.00x | 2.00x | 9.4% | 9.4% | Yes | Y8 | Backend-heavy | Yes | Y8 | $11,608,931 | $3,571,903 | $20,000,000 | $4,319,166 | Yes | $16,030,648 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_30 | Y8 | 2.00x | 2.00x | 9.6% | 9.6% | Yes | Y8 | Backend-heavy | Yes | Y8 | $10,839,822 | $3,801,116 | $20,000,000 | $3,779,270 | Yes | $15,545,064 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_40 | Y9 | 2.00x | 2.00x | 8.8% | 8.8% | Yes | Y9 | Backend-heavy | Yes | Y9 | $11,373,851 | $1,621,675 | $20,000,000 | $3,902,684 | Yes | $19,161,148 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_50 | Y9 | 2.00x | 2.00x | 9.1% | 9.1% | Yes | Y9 | Backend-heavy | Yes | Y9 | $10,460,300 | $1,884,780 | $20,000,000 | $3,252,237 | Yes | $18,593,526 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_60 | Y9 | 2.00x | 2.00x | 9.3% | 9.3% | Yes | Y9 | Backend-heavy | Yes | Y9 | $9,546,748 | $2,147,884 | $20,000,000 | $2,601,789 | Yes | $18,025,905 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_70 | Y9 | 2.00x | 2.00x | 9.6% | 9.6% | Yes | Y9 | Backend-heavy | Yes | Y9 | $8,633,196 | $2,410,988 | $20,000,000 | $1,951,342 | Yes | $17,458,283 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_80 | Y9 | 2.00x | 2.00x | 9.8% | 9.8% | Yes | Y9 | Backend-heavy | Yes | Y9 | $7,719,644 | $2,674,093 | $20,000,000 | $1,300,895 | Yes | $16,890,661 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_90 | Y9 | 2.00x | 2.00x | 10.1% | 10.1% | Yes | Y9 | Backend-heavy | Yes | Y9 | $6,806,093 | $2,937,197 | $20,000,000 | $650,447 | Yes | $16,323,040 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_20 | Y11 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $11,314,294 | $2,831,183 | $20,000,000 | $5,354,523 | Yes | $18,831,490 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_30 | Y11 | 2.00x | 2.00x | 7.0% | 7.0% | Yes | Y11 | Backend-heavy | Yes | Y11 | $10,383,289 | $3,092,872 | $20,000,000 | $4,685,208 | Yes | $18,259,466 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_40 | Y11 | 2.00x | 2.00x | 7.2% | 7.2% | Yes | Y11 | Backend-heavy | Yes | Y11 | $9,452,285 | $3,354,561 | $20,000,000 | $4,015,892 | Yes | $17,687,443 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_50 | Y11 | 2.00x | 2.00x | 7.4% | 7.4% | Yes | Y11 | Backend-heavy | Yes | Y11 | $8,521,281 | $3,616,249 | $20,000,000 | $3,346,577 | Yes | $17,115,419 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_60 | Y11 | 2.00x | 2.00x | 7.6% | 7.6% | Yes | Y11 | Backend-heavy | Yes | Y11 | $7,590,277 | $3,877,938 | $20,000,000 | $2,677,262 | Yes | $16,543,396 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_70 | Y11 | 2.00x | 2.00x | 7.8% | 7.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $6,659,273 | $4,139,627 | $20,000,000 | $2,007,946 | Yes | $15,971,372 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_80 | Y11 | 2.00x | 2.00x | 8.1% | 8.1% | Yes | Y11 | Backend-heavy | Yes | Y11 | $5,728,269 | $4,401,316 | $20,000,000 | $1,338,631 | Yes | $15,399,349 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_90 | Y12 | 2.00x | 2.00x | 7.9% | 7.9% | Yes | Y12 | Backend-heavy | Yes | Y12 | $5,067,650 | $2,822,723 | $20,000,000 | $773,975 | Yes | $18,010,122 | Hurdle trigger executed |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_20 | Y20 | 0.13x | 2.00x | -14.8% | 3.7% | No |  | Moderate yield | No |  | $0 | $0 | $1,318,718 | $3,296,795 | Yes | $0 | Value hurdle reached but liquidity constrained |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_30 | Y20 | 0.20x | 2.00x | -12.4% | 3.8% | No |  | Moderate yield | No |  | $0 | $0 | $1,978,077 | $2,884,696 | Yes | $0 | Value hurdle reached but liquidity constrained |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_40 | Y20 | 0.26x | 2.00x | -10.5% | 3.8% | No |  | Moderate yield | No |  | $0 | $0 | $2,637,436 | $2,472,596 | Yes | $0 | Value hurdle reached but liquidity constrained |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_50 | Y20 | 0.33x | 2.00x | -9.0% | 3.9% | No |  | Moderate yield | No |  | $0 | $0 | $3,296,795 | $2,060,497 | Yes | $0 | Value hurdle reached but liquidity constrained |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_60 | Y20 | 0.40x | 2.00x | -7.8% | 4.0% | No |  | Moderate yield | No |  | $0 | $0 | $3,956,154 | $1,648,397 | Yes | $0 | Value hurdle reached but liquidity constrained |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_70 | Y20 | 0.46x | 2.00x | -6.6% | 4.1% | No |  | Moderate yield | No |  | $0 | $0 | $4,615,513 | $1,236,298 | Yes | $0 | Value hurdle reached but liquidity constrained |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_80 | Y20 | 0.53x | 1.99x | -5.6% | 4.2% | No |  | Moderate yield | No |  | $0 | $0 | $5,274,872 | $824,199 | Yes | $0 | LP 2x not achieved |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_90 | Y20 | 0.59x | 1.92x | -4.7% | 4.1% | No |  | Moderate yield | No |  | $0 | $0 | $5,934,231 | $412,099 | Yes | $0 | LP 2x not achieved |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_20 | Y13 | 2.00x | 2.00x | 5.6% | 5.6% | Yes | Y13 | Backend-heavy | Yes | Y13 | $16,852,312 | $0 | $20,000,000 | $7,943,065 | Yes | $22,135,420 | Hurdle trigger executed |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_30 | Y14 | 2.00x | 2.00x | 5.2% | 5.2% | Yes | Y14 | Backend-heavy | Yes | Y14 | $16,935,335 | $0 | $20,000,000 | $7,693,995 | Yes | $27,546,730 | Hurdle trigger executed |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_40 | Y16 | 2.00x | 2.00x | 4.5% | 4.5% | Yes | Y16 | Backend-heavy | Yes | Y16 | $16,826,076 | $0 | $20,000,000 | $8,021,771 | Yes | $37,084,825 | Hurdle trigger executed |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_20 | Y15 | 2.00x | 2.00x | 4.9% | 4.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $16,770,071 | $0 | $20,000,000 | $8,189,787 | Yes | $64,569,618 | Hurdle trigger executed |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_30 | Y16 | 2.00x | 2.00x | 4.5% | 4.5% | Yes | Y16 | Backend-heavy | Yes | Y16 | $16,903,903 | $0 | $20,000,000 | $7,788,291 | Yes | $95,356,197 | Hurdle trigger executed |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_40 | Y18 | 2.00x | 2.00x | 4.0% | 4.0% | Yes | Y18 | Backend-heavy | Yes | Y18 | $16,883,293 | $0 | $20,000,000 | $7,850,121 | Yes | $156,181,218 | Hurdle trigger executed |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_20 | Y10 | 2.00x | 2.00x | 7.4% | 7.4% | Yes | Y10 | Backend-heavy | Yes | Y10 | $11,098,288 | $5,667,178 | $20,000,000 | $8,203,601 | Yes | $34,789,649 | Hurdle trigger executed |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_30 | Y11 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y11 | Backend-heavy | Yes | Y11 | $16,702,342 | $0 | $20,000,000 | $8,392,974 | Yes | $50,300,532 | Hurdle trigger executed |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_40 | Y12 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y12 | Backend-heavy | Yes | Y12 | $16,725,737 | $0 | $20,000,000 | $8,322,788 | Yes | $69,901,915 | Hurdle trigger executed |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_25 | Y12 | 2.00x | 2.00x | 6.2% | 6.2% | Yes | Y12 | Backend-heavy | Yes | Y12 | $14,484,969 | $1,802,927 | $20,000,000 | $10,178,625 | Yes | $16,634,170 | Hurdle trigger executed |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_50 | Y12 | 2.00x | 2.00x | 6.2% | 6.2% | Yes | Y12 | Backend-heavy | Yes | Y12 | $13,846,392 | $1,933,540 | $20,000,000 | $12,210,481 | Yes | $16,290,698 | Hurdle trigger executed |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_75 | Y12 | 2.00x | 2.00x | 6.2% | 6.2% | Yes | Y12 | Backend-heavy | Yes | Y12 | $13,241,853 | $2,062,514 | $20,000,000 | $14,112,738 | Yes | $15,960,210 | Hurdle trigger executed |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_25 | Y11 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y11 | Backend-heavy | Yes | Y11 | $16,520,521 | $0 | $20,000,000 | $9,887,837 | Yes | $20,374,279 | Hurdle trigger executed |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_50 | Y11 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $15,668,225 | $0 | $20,000,000 | $13,297,017 | Yes | $19,403,247 | Hurdle trigger executed |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_75 | Y11 | 2.00x | 2.00x | 6.8% | 6.8% | Yes | Y11 | Backend-heavy | Yes | Y11 | $14,904,601 | $0 | $20,000,000 | $16,351,515 | Yes | $18,488,431 | Hurdle trigger executed |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_25 | Y8 | 2.00x | 2.00x | 9.3% | 9.3% | Yes | Y8 | Backend-heavy | Yes | Y8 | $13,928,344 | $2,828,264 | $20,000,000 | $8,813,986 | Yes | $17,547,424 | Hurdle trigger executed |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_50 | Y8 | 2.00x | 2.00x | 9.3% | 9.3% | Yes | Y8 | Backend-heavy | Yes | Y8 | $13,214,827 | $2,998,810 | $20,000,000 | $10,985,869 | Yes | $17,139,039 | Hurdle trigger executed |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_75 | Y8 | 2.00x | 2.00x | 9.4% | 9.4% | Yes | Y8 | Backend-heavy | Yes | Y8 | $12,542,479 | $3,166,546 | $20,000,000 | $13,004,318 | Yes | $16,747,187 | Hurdle trigger executed |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_50x | Y12 | 1.50x | 1.50x | 3.6% | 3.6% | Yes | Y12 | Backend-heavy | Yes | Y12 | $11,830,207 | $0 | $15,000,000 | $8,009,380 | Yes | $21,991,128 | Hurdle trigger executed |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_75x | Y12 | 1.75x | 1.75x | 4.9% | 4.9% | Yes | Y12 | Backend-heavy | Yes | Y12 | $14,330,207 | $0 | $17,500,000 | $8,009,380 | Yes | $19,491,128 | Hurdle trigger executed |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_2_00x | Y12 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y12 | Backend-heavy | Yes | Y12 | $15,159,420 | $1,670,786 | $20,000,000 | $8,009,380 | Yes | $16,991,128 | Hurdle trigger executed |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_50x | Y13 | 1.50x | 1.50x | 3.3% | 3.3% | Yes | Y13 | Backend-heavy | Yes | Y13 | $11,964,636 | $0 | $15,000,000 | $7,606,092 | Yes | $37,995,925 | Hurdle trigger executed |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_75x | Y13 | 1.75x | 1.75x | 4.5% | 4.5% | Yes | Y13 | Backend-heavy | Yes | Y13 | $14,464,636 | $0 | $17,500,000 | $7,606,092 | Yes | $35,495,925 | Hurdle trigger executed |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_2_00x | Y13 | 2.00x | 2.00x | 5.6% | 5.6% | Yes | Y13 | Backend-heavy | Yes | Y13 | $16,964,636 | $0 | $20,000,000 | $7,606,092 | Yes | $32,995,925 | Hurdle trigger executed |
| lp_hurdle_sensitivity__slow_grind__hurdle_1_50x | Y15 | 1.50x | 1.50x | 2.8% | 2.8% | Yes | Y15 | Backend-heavy | Yes | Y15 | $11,939,120 | $0 | $15,000,000 | $7,682,639 | Yes | $24,248,014 | Hurdle trigger executed |
| lp_hurdle_sensitivity__slow_grind__hurdle_1_75x | Y15 | 1.75x | 1.75x | 3.9% | 3.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $14,439,120 | $0 | $17,500,000 | $7,682,639 | Yes | $21,748,014 | Hurdle trigger executed |
| lp_hurdle_sensitivity__slow_grind__hurdle_2_00x | Y15 | 2.00x | 2.00x | 4.9% | 4.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $16,939,120 | $0 | $20,000,000 | $7,682,639 | Yes | $19,248,014 | Hurdle trigger executed |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_50x | Y9 | 1.50x | 1.50x | 4.7% | 4.7% | Yes | Y9 | Backend-heavy | Yes | Y9 | $11,898,211 | $0 | $15,000,000 | $7,805,368 | Yes | $27,566,878 | Hurdle trigger executed |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_75x | Y9 | 1.75x | 1.75x | 6.6% | 6.6% | Yes | Y9 | Backend-heavy | Yes | Y9 | $14,398,211 | $0 | $17,500,000 | $7,805,368 | Yes | $25,066,878 | Hurdle trigger executed |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_2_00x | Y9 | 2.00x | 2.00x | 8.2% | 8.2% | Yes | Y9 | Backend-heavy | Yes | Y9 | $16,855,162 | $43,049 | $20,000,000 | $7,805,368 | Yes | $22,566,878 | Hurdle trigger executed |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_25 | Y12 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y12 | Backend-heavy | Yes | Y12 | $15,159,420 | $1,670,786 | $20,000,000 | $8,009,380 | Yes | $16,991,128 | Hurdle trigger executed |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_40 | Y12 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y12 | Backend-heavy | Yes | Y12 | $15,159,420 | $1,670,786 | $20,000,000 | $8,009,380 | Yes | $16,991,128 | Hurdle trigger executed |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_60 | Y12 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y12 | Backend-heavy | Yes | Y12 | $15,159,420 | $1,670,786 | $20,000,000 | $8,009,380 | Yes | $16,991,128 | Hurdle trigger executed |
| re_liquidity_sensitivity__slow_grind__re_liquidity_25 | Y15 | 2.00x | 2.00x | 4.9% | 4.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $16,939,120 | $0 | $20,000,000 | $7,682,639 | Yes | $19,248,014 | Hurdle trigger executed |
| re_liquidity_sensitivity__slow_grind__re_liquidity_40 | Y15 | 2.00x | 2.00x | 4.9% | 4.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $16,939,120 | $0 | $20,000,000 | $7,682,639 | Yes | $19,248,014 | Hurdle trigger executed |
| re_liquidity_sensitivity__slow_grind__re_liquidity_60 | Y15 | 2.00x | 2.00x | 4.9% | 4.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $16,939,120 | $0 | $20,000,000 | $7,682,639 | Yes | $19,248,014 | Hurdle trigger executed |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_25 | Y11 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y11 | Backend-heavy | Yes | Y11 | $15,038,310 | $1,784,428 | $20,000,000 | $8,031,785 | Yes | $21,119,584 | Hurdle trigger executed |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_40 | Y11 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y11 | Backend-heavy | Yes | Y11 | $15,038,310 | $1,784,428 | $20,000,000 | $8,031,785 | Yes | $21,119,584 | Hurdle trigger executed |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_60 | Y11 | 2.00x | 2.00x | 6.7% | 6.7% | Yes | Y11 | Backend-heavy | Yes | Y11 | $15,038,310 | $1,784,428 | $20,000,000 | $8,031,785 | Yes | $21,119,584 | Hurdle trigger executed |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_25 | Y9 | 2.00x | 2.00x | 8.2% | 8.2% | Yes | Y9 | Backend-heavy | Yes | Y9 | $16,855,162 | $43,049 | $20,000,000 | $7,805,368 | Yes | $22,566,878 | Hurdle trigger executed |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_40 | Y9 | 2.00x | 2.00x | 8.2% | 8.2% | Yes | Y9 | Backend-heavy | Yes | Y9 | $16,855,162 | $43,049 | $20,000,000 | $7,805,368 | Yes | $22,566,878 | Hurdle trigger executed |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_60 | Y9 | 2.00x | 2.00x | 8.2% | 8.2% | Yes | Y9 | Backend-heavy | Yes | Y9 | $16,855,162 | $43,049 | $20,000,000 | $7,805,368 | Yes | $22,566,878 | Hurdle trigger executed |
| twenty_year_horizon__base_hit_everyone_happy__years_20 | Y12 | 2.00x | 2.00x | 6.1% | 6.1% | Yes | Y12 | Backend-heavy | Yes | Y12 | $15,159,420 | $1,670,786 | $20,000,000 | $8,009,380 | Yes | $16,991,128 | Hurdle trigger executed |
| twenty_year_horizon__slow_grind__years_20 | Y15 | 2.00x | 2.00x | 4.9% | 4.9% | Yes | Y15 | Backend-heavy | Yes | Y15 | $16,939,120 | $0 | $20,000,000 | $7,682,639 | Yes | $19,248,014 | Hurdle trigger executed |
| twenty_year_horizon__hedge_fund_failure_re_survival__years_20 | Y18 | 2.00x | 2.00x | 4.1% | 4.1% | Yes | Y18 | Backend-heavy | Yes | Y18 | $12,883,156 | $2,473,938 | $20,000,000 | $12,428,720 | Yes | $15,077,547 | Hurdle trigger executed |
| twenty_year_horizon__failure_never_reaches_hurdle__years_20 | Y20 | 0.07x | 2.00x | -18.5% | 3.6% | No |  | Moderate yield | No |  | $0 | $0 | $659,359 | $4,945,192 | Yes | $0 | Value hurdle reached but liquidity constrained |

## Scenario Notes

### policy_set_comparison__base_hit_everyone_happy__backend_heavy_compounding

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 0.74x
- LP economic multiple: 2.00x
- LP cash IRR: -2.6%
- LP economic IRR: 4.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,399,618
- Total cash reinvested into HF: $18,058,371
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__base_hit_everyone_happy__balanced_yield_compounding

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.9%
- LP economic IRR: 6.9%
- Years until LP 2x cash return: 15
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $4,743,878
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $5,971,537
- GP residual NAV: $19,204,694
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__base_hit_everyone_happy__aggressive_lp_extinguishment

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 8.9%
- LP economic IRR: 8.9%
- Years until LP 2x cash return: 14
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $2,916,394
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,311,694
- GP residual NAV: $13,626,660
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__fast_success_crypto_bull__backend_heavy_compounding

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 0.90x
- LP economic multiple: 2.00x
- LP cash IRR: -0.9%
- LP economic IRR: 4.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $8,956,322
- Total cash reinvested into HF: $24,269,292
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__fast_success_crypto_bull__balanced_yield_compounding

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.3%
- LP economic IRR: 7.3%
- Years until LP 2x cash return: 14
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $4,886,194
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $6,556,929
- GP residual NAV: $21,526,363
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__fast_success_crypto_bull__aggressive_lp_extinguishment

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.6%
- LP economic IRR: 9.6%
- Years until LP 2x cash return: 13
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $3,594,278
- Trigger refi used: $176,771
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,045,330
- GP residual NAV: $11,112,152
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__slow_grind__backend_heavy_compounding

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 0.54x
- LP economic multiple: 2.00x
- LP cash IRR: -5.3%
- LP economic IRR: 4.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $5,419,310
- Total cash reinvested into HF: $12,535,304
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__slow_grind__balanced_yield_compounding

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.4%
- LP economic IRR: 5.4%
- Years until LP 2x cash return: 19
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: True
- Hurdle trigger year: 19
- Trigger HF liquidation used: $4,870,881
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $6,164,405
- GP residual NAV: $17,547,060
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__slow_grind__aggressive_lp_extinguishment

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.0%
- LP economic IRR: 7.0%
- Years until LP 2x cash return: 18
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $2,933,161
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,308,913
- GP residual NAV: $11,296,290
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__hedge_fund_failure_re_survival__backend_heavy_compounding

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 0.56x
- LP economic multiple: 2.00x
- LP cash IRR: -5.1%
- LP economic IRR: 4.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $5,559,905
- Total cash reinvested into HF: $12,471,979
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__hedge_fund_failure_re_survival__balanced_yield_compounding

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.4%
- LP economic IRR: 5.4%
- Years until LP 2x cash return: 19
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: True
- Hurdle trigger year: 19
- Trigger HF liquidation used: $4,382,453
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $5,804,776
- GP residual NAV: $14,341,859
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome, HF major drawdown

### policy_set_comparison__hedge_fund_failure_re_survival__aggressive_lp_extinguishment

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.0%
- LP economic IRR: 7.0%
- Years until LP 2x cash return: 18
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $2,259,078
- Trigger refi used: $176,717
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,556,046
- GP residual NAV: $11,487,806
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Refinance event occurred, Refi-dependent LP outcome, HF major drawdown

### policy_set_comparison__real_estate_distress_crypto_success__backend_heavy_compounding

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 0.80x
- LP economic multiple: 2.00x
- LP cash IRR: -1.6%
- LP economic IRR: 4.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,954,938
- Total cash reinvested into HF: $23,506,257
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, RE NAV impairment, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__real_estate_distress_crypto_success__balanced_yield_compounding

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.6%
- LP economic IRR: 5.6%
- Years until LP 2x cash return: 17
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 17
- Trigger HF liquidation used: $5,836,882
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,382,032
- GP residual NAV: $21,214,237
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome, RE NAV impairment

### policy_set_comparison__real_estate_distress_crypto_success__aggressive_lp_extinguishment

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.3%
- LP economic IRR: 6.3%
- Years until LP 2x cash return: 19
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: True
- Hurdle trigger year: 19
- Trigger HF liquidation used: $3,931,352
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,791,574
- GP residual NAV: $5,279,330
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome, RE NAV impairment

### policy_set_comparison__exceptional_dynasty_outcome__backend_heavy_compounding

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.6%
- LP economic IRR: 5.6%
- Years until LP 2x cash return: 17
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 17
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $34,221,344
- GP residual NAV: $122,812,496
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__exceptional_dynasty_outcome__balanced_yield_compounding

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.2%
- LP economic IRR: 9.2%
- Years until LP 2x cash return: 11
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $3,382,133
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $6,641,022
- GP residual NAV: $27,207,092
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__exceptional_dynasty_outcome__aggressive_lp_extinguishment

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 12.0%
- LP economic IRR: 12.0%
- Years until LP 2x cash return: 10
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 10
- Trigger HF liquidation used: $0
- Trigger refi used: $3,531,763
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,244,783
- GP residual NAV: $17,384,757
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via refi, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__liquidity_trap__backend_heavy_compounding

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 0.94x
- LP economic multiple: 2.00x
- LP cash IRR: -0.5%
- LP economic IRR: 4.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $9,433,937
- Total cash reinvested into HF: $23,384,676
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__liquidity_trap__balanced_yield_compounding

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.6%
- LP economic IRR: 7.6%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $5,249,441
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $5,538,976
- GP residual NAV: $22,563,052
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__liquidity_trap__aggressive_lp_extinguishment

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.7%
- LP economic IRR: 9.7%
- Years until LP 2x cash return: 12
- LP cashflow profile: Aggressive distribution
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $3,015,474
- Trigger refi used: $757,372
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,125,946
- GP residual NAV: $16,605,972
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, Refinance event occurred, Refi-dependent LP outcome

### policy_set_comparison__failure_never_reaches_hurdle__backend_heavy_compounding

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.30x
- LP economic multiple: 2.00x
- LP cash IRR: -10.7%
- LP economic IRR: 4.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,038,116
- Total cash reinvested into HF: $5,730,253
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__failure_never_reaches_hurdle__balanced_yield_compounding

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.63x
- LP economic multiple: 2.00x
- LP cash IRR: -4.4%
- LP economic IRR: 4.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $6,328,511
- Total cash reinvested into HF: $3,110,103
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### policy_set_comparison__failure_never_reaches_hurdle__aggressive_lp_extinguishment

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.93x
- LP economic multiple: 1.77x
- LP cash IRR: -0.8%
- LP economic IRR: 4.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $9,278,707
- Total cash reinvested into HF: $1,219,929
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Slow time horizon drift, GP survivability risk, Refinance event occurred, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_20

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.3%
- LP economic IRR: 6.3%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $11,524,148
- Trigger refi used: $2,636,265
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $5,339,587
- GP residual NAV: $14,813,892
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_30

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.5%
- LP economic IRR: 6.5%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $10,615,330
- Trigger refi used: $2,877,634
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,672,139
- GP residual NAV: $14,269,583
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_40

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.7%
- LP economic IRR: 6.7%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $9,706,512
- Trigger refi used: $3,119,004
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,004,690
- GP residual NAV: $13,725,274
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_50

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.9%
- LP economic IRR: 6.9%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $8,797,694
- Trigger refi used: $3,360,374
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,337,242
- GP residual NAV: $13,180,965
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_60

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.6%
- LP economic IRR: 6.6%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $8,610,399
- Trigger refi used: $1,887,461
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,000,713
- GP residual NAV: $15,135,797
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_70

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.9%
- LP economic IRR: 6.9%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $7,585,004
- Trigger refi used: $2,162,677
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,250,535
- GP residual NAV: $14,518,782
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_80

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.1%
- LP economic IRR: 7.1%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $6,559,609
- Trigger refi used: $2,437,893
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,500,357
- GP residual NAV: $13,901,768
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_90

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $5,534,215
- Trigger refi used: $2,713,110
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $750,178
- GP residual NAV: $13,284,753
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_20

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $15,439,838
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,060,162
- GP residual NAV: $18,548,288
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_30

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.9%
- LP economic IRR: 6.9%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $14,932,318
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,552,642
- GP residual NAV: $17,834,153
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_40

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.1%
- LP economic IRR: 7.1%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $14,424,797
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,045,122
- GP residual NAV: $17,120,018
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_50

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.3%
- LP economic IRR: 7.3%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $13,917,277
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,537,601
- GP residual NAV: $16,405,882
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_60

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $13,001,637
- Trigger refi used: $408,120
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,030,081
- GP residual NAV: $15,691,747
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_70

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.6%
- LP economic IRR: 7.6%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $12,085,395
- Trigger refi used: $816,842
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,522,561
- GP residual NAV: $14,977,611
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_80

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.8%
- LP economic IRR: 7.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $11,169,153
- Trigger refi used: $1,225,563
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,015,041
- GP residual NAV: $14,263,476
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_90

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 8.0%
- LP economic IRR: 8.0%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $10,252,912
- Trigger refi used: $1,634,285
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $507,520
- GP residual NAV: $13,549,341
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_20

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.3%
- LP economic IRR: 5.3%
- Years until LP 2x cash return: 14
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $12,639,366
- Trigger refi used: $2,171,034
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,689,600
- GP residual NAV: $13,257,657
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_30

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.5%
- LP economic IRR: 5.5%
- Years until LP 2x cash return: 14
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $11,536,410
- Trigger refi used: $2,687,790
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,103,400
- GP residual NAV: $12,373,249
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_40

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.3%
- LP economic IRR: 5.3%
- Years until LP 2x cash return: 15
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $11,302,550
- Trigger refi used: $1,795,251
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,841,320
- GP residual NAV: $13,412,147
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_50

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.5%
- LP economic IRR: 5.5%
- Years until LP 2x cash return: 15
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $10,092,902
- Trigger refi used: $2,364,679
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,201,100
- GP residual NAV: $12,439,502
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_60

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.4%
- LP economic IRR: 5.4%
- Years until LP 2x cash return: 16
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 16
- Trigger HF liquidation used: $9,584,125
- Trigger refi used: $1,561,728
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,784,716
- GP residual NAV: $13,301,659
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_70

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.6%
- LP economic IRR: 5.6%
- Years until LP 2x cash return: 16
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 16
- Trigger HF liquidation used: $8,259,929
- Trigger refi used: $2,189,746
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,088,537
- GP residual NAV: $12,232,242
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_80

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.8%
- LP economic IRR: 5.8%
- Years until LP 2x cash return: 16
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 16
- Trigger HF liquidation used: $6,935,732
- Trigger refi used: $2,817,763
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,392,358
- GP residual NAV: $11,162,826
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_90

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.8%
- LP economic IRR: 5.8%
- Years until LP 2x cash return: 17
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 17
- Trigger HF liquidation used: $5,991,703
- Trigger refi used: $2,196,107
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $754,146
- GP residual NAV: $11,703,180
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_20

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.3%
- LP economic IRR: 4.3%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $8,703,321
- Trigger refi used: $2,510,866
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,285,813
- GP residual NAV: $13,647,340
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_30

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.5%
- LP economic IRR: 4.5%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $7,658,362
- Trigger refi used: $2,520,098
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,250,087
- GP residual NAV: $13,289,789
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_40

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.7%
- LP economic IRR: 4.7%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $6,613,403
- Trigger refi used: $2,529,330
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $6,214,360
- GP residual NAV: $12,932,237
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_50

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.0%
- LP economic IRR: 5.0%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $5,568,445
- Trigger refi used: $2,538,562
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $5,178,633
- GP residual NAV: $12,574,685
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, HF major drawdown

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_60

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.2%
- LP economic IRR: 5.2%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $4,523,486
- Trigger refi used: $2,547,794
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,142,907
- GP residual NAV: $12,217,134
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, HF major drawdown

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_70

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.5%
- LP economic IRR: 5.5%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $3,478,527
- Trigger refi used: $2,557,026
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,107,180
- GP residual NAV: $11,859,582
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, HF major drawdown

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_80

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.8%
- LP economic IRR: 5.8%
- Years until LP 2x cash return: 18
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $2,433,569
- Trigger refi used: $2,566,258
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,071,453
- GP residual NAV: $11,502,031
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, HF major drawdown

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_90

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.1%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: 18
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $1,388,610
- Trigger refi used: $2,575,490
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,035,727
- GP residual NAV: $11,144,479
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, HF major drawdown

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_20

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 3.7%
- LP economic IRR: 3.7%
- Years until LP 2x cash return: 20
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 20
- Trigger HF liquidation used: $16,980,371
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,519,629
- GP residual NAV: $126,366,785
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, RE NAV impairment

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_30

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $16,546,966
- Trigger refi used: $983,673
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,531,725
- GP residual NAV: $10,429,643
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, LP redeemed via refi, RE NAV impairment

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_40

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $15,889,396
- Trigger refi used: $1,422,425
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,312,907
- GP residual NAV: $9,771,701
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, RE NAV impairment

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_50

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.8%
- LP economic IRR: 5.8%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $16,941,006
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,163,179
- GP residual NAV: $14,235,192
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, RE NAV impairment

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_60

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.9%
- LP economic IRR: 5.9%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $16,708,370
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $930,543
- GP residual NAV: $13,358,060
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, RE NAV impairment

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_70

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.0%
- LP economic IRR: 6.0%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $16,475,734
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $697,908
- GP residual NAV: $12,480,928
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, RE NAV impairment

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_80

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.1%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $16,243,098
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $465,272
- GP residual NAV: $11,603,796
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, RE NAV impairment

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_90

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $15,762,297
- Trigger refi used: $248,165
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $232,636
- GP residual NAV: $10,726,664
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi, RE NAV impairment

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_20

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 8
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $11,608,931
- Trigger refi used: $3,571,903
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,319,166
- GP residual NAV: $16,030,648
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_30

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.6%
- LP economic IRR: 9.6%
- Years until LP 2x cash return: 8
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $10,839,822
- Trigger refi used: $3,801,116
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,779,270
- GP residual NAV: $15,545,064
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_40

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 8.8%
- LP economic IRR: 8.8%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $11,373,851
- Trigger refi used: $1,621,675
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,902,684
- GP residual NAV: $19,161,148
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_50

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.1%
- LP economic IRR: 9.1%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $10,460,300
- Trigger refi used: $1,884,780
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,252,237
- GP residual NAV: $18,593,526
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_60

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.3%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $9,546,748
- Trigger refi used: $2,147,884
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,601,789
- GP residual NAV: $18,025,905
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_70

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.6%
- LP economic IRR: 9.6%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $8,633,196
- Trigger refi used: $2,410,988
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,951,342
- GP residual NAV: $17,458,283
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_80

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.8%
- LP economic IRR: 9.8%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $7,719,644
- Trigger refi used: $2,674,093
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,300,895
- GP residual NAV: $16,890,661
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_90

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 10.1%
- LP economic IRR: 10.1%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $6,806,093
- Trigger refi used: $2,937,197
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $650,447
- GP residual NAV: $16,323,040
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_20

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $11,314,294
- Trigger refi used: $2,831,183
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $5,354,523
- GP residual NAV: $18,831,490
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_30

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.0%
- LP economic IRR: 7.0%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $10,383,289
- Trigger refi used: $3,092,872
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,685,208
- GP residual NAV: $18,259,466
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_40

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.2%
- LP economic IRR: 7.2%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $9,452,285
- Trigger refi used: $3,354,561
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,015,892
- GP residual NAV: $17,687,443
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_50

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $8,521,281
- Trigger refi used: $3,616,249
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,346,577
- GP residual NAV: $17,115,419
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_60

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.6%
- LP economic IRR: 7.6%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $7,590,277
- Trigger refi used: $3,877,938
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,677,262
- GP residual NAV: $16,543,396
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_70

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.8%
- LP economic IRR: 7.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $6,659,273
- Trigger refi used: $4,139,627
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,007,946
- GP residual NAV: $15,971,372
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_80

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 8.1%
- LP economic IRR: 8.1%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $5,728,269
- Trigger refi used: $4,401,316
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,338,631
- GP residual NAV: $15,399,349
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_90

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.9%
- LP economic IRR: 7.9%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $5,067,650
- Trigger refi used: $2,822,723
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $773,975
- GP residual NAV: $18,010,122
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_20

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.13x
- LP economic multiple: 2.00x
- LP cash IRR: -14.8%
- LP economic IRR: 3.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,318,718
- Total cash reinvested into HF: $3,296,795
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_30

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.20x
- LP economic multiple: 2.00x
- LP cash IRR: -12.4%
- LP economic IRR: 3.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,978,077
- Total cash reinvested into HF: $2,884,696
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_40

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.26x
- LP economic multiple: 2.00x
- LP cash IRR: -10.5%
- LP economic IRR: 3.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,637,436
- Total cash reinvested into HF: $2,472,596
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_50

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.33x
- LP economic multiple: 2.00x
- LP cash IRR: -9.0%
- LP economic IRR: 3.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,296,795
- Total cash reinvested into HF: $2,060,497
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_60

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.40x
- LP economic multiple: 2.00x
- LP cash IRR: -7.8%
- LP economic IRR: 4.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,956,154
- Total cash reinvested into HF: $1,648,397
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_70

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.46x
- LP economic multiple: 2.00x
- LP cash IRR: -6.6%
- LP economic IRR: 4.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $4,615,513
- Total cash reinvested into HF: $1,236,298
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Trigger attempted but insufficient, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_80

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.53x
- LP economic multiple: 1.99x
- LP cash IRR: -5.6%
- LP economic IRR: 4.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $5,274,872
- Total cash reinvested into HF: $824,199
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Slow time horizon drift, GP survivability risk, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_90

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash multiple: 0.59x
- LP economic multiple: 1.92x
- LP cash IRR: -4.7%
- LP economic IRR: 4.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile: Moderate yield
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $5,934,231
- Total cash reinvested into HF: $412,099
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP 2x not achieved, Slow time horizon drift, GP survivability risk, LP still below 1x cash at end, Weak LP cash outcome despite positive NAV

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_20

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.6%
- LP economic IRR: 5.6%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $16,852,312
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,943,065
- GP residual NAV: $22,135,420
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_30

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 5.2%
- LP economic IRR: 5.2%
- Years until LP 2x cash return: 14
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $16,935,335
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,693,995
- GP residual NAV: $27,546,730
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_40

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.5%
- LP economic IRR: 4.5%
- Years until LP 2x cash return: 16
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 16
- Trigger HF liquidation used: $16,826,076
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,021,771
- GP residual NAV: $37,084,825
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_20

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.9%
- LP economic IRR: 4.9%
- Years until LP 2x cash return: 15
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $16,770,071
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,189,787
- GP residual NAV: $64,569,618
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_30

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.5%
- LP economic IRR: 4.5%
- Years until LP 2x cash return: 16
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 16
- Trigger HF liquidation used: $16,903,903
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,788,291
- GP residual NAV: $95,356,197
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_40

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 4.0%
- LP economic IRR: 4.0%
- Years until LP 2x cash return: 18
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 18
- Trigger HF liquidation used: $16,883,293
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,850,121
- GP residual NAV: $156,181,218
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_20

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: 10
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 10
- Trigger HF liquidation used: $11,098,288
- Trigger refi used: $5,667,178
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,203,601
- GP residual NAV: $34,789,649
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, LP redeemed via refi

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_30

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.7%
- LP economic IRR: 6.7%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $16,702,342
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,392,974
- GP residual NAV: $50,300,532
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_40

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.1%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $16,725,737
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,322,788
- GP residual NAV: $69,901,915
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_25

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $14,484,969
- Trigger refi used: $1,802,927
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $10,178,625
- GP residual NAV: $16,634,170
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_50

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $13,846,392
- Trigger refi used: $1,933,540
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $12,210,481
- GP residual NAV: $16,290,698
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_75

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $13,241,853
- Trigger refi used: $2,062,514
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $14,112,738
- GP residual NAV: $15,960,210
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_25

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.7%
- LP economic IRR: 6.7%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $16,520,521
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $9,887,837
- GP residual NAV: $20,374,279
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_50

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $15,668,225
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $13,297,017
- GP residual NAV: $19,403,247
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_75

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 6.8%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: 11
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $14,904,601
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $16,351,515
- GP residual NAV: $18,488,431
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_25

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.3%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: 8
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $13,928,344
- Trigger refi used: $2,828,264
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,813,986
- GP residual NAV: $17,547,424
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation, LP redeemed via refi

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_50

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.3%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: 8
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $13,214,827
- Trigger refi used: $2,998,810
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $10,985,869
- GP residual NAV: $17,139,039
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_75

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 2.00x
- LP economic multiple: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 8
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $12,542,479
- Trigger refi used: $3,166,546
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $13,004,318
- GP residual NAV: $16,747,187
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, Trigger attempted but insufficient, LP redeemed via HF liquidation, LP redeemed via refi

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_50x

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 1.50x
- LP economic multiple: 1.50x
- LP cash IRR: 3.6%
- LP economic IRR: 3.6%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $11,830,207
- Trigger refi used: $0
- Total cash distributed to LP: $15,000,000
- Total cash reinvested into HF: $8,009,380
- GP residual NAV: $21,991,128
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_75x

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash multiple: 1.75x
- LP economic multiple: 1.75x
- LP cash IRR: 4.9%
- LP economic IRR: 4.9%
- Years until LP 2x cash return: 12
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $14,330,207
- Trigger refi used: $0
- Total cash distributed to LP: $17,500,000
- Total cash reinvested into HF: $8,009,380
- GP residual NAV: $19,491,128
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_2_00x

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

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_50x

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 1.50x
- LP economic multiple: 1.50x
- LP cash IRR: 3.3%
- LP economic IRR: 3.3%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $11,964,636
- Trigger refi used: $0
- Total cash distributed to LP: $15,000,000
- Total cash reinvested into HF: $7,606,092
- GP residual NAV: $37,995,925
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_75x

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash multiple: 1.75x
- LP economic multiple: 1.75x
- LP cash IRR: 4.5%
- LP economic IRR: 4.5%
- Years until LP 2x cash return: 13
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $14,464,636
- Trigger refi used: $0
- Total cash distributed to LP: $17,500,000
- Total cash reinvested into HF: $7,606,092
- GP residual NAV: $35,495,925
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_2_00x

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

### lp_hurdle_sensitivity__slow_grind__hurdle_1_50x

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 1.50x
- LP economic multiple: 1.50x
- LP cash IRR: 2.8%
- LP economic IRR: 2.8%
- Years until LP 2x cash return: 15
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $11,939,120
- Trigger refi used: $0
- Total cash distributed to LP: $15,000,000
- Total cash reinvested into HF: $7,682,639
- GP residual NAV: $24,248,014
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__slow_grind__hurdle_1_75x

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash multiple: 1.75x
- LP economic multiple: 1.75x
- LP cash IRR: 3.9%
- LP economic IRR: 3.9%
- Years until LP 2x cash return: 15
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $14,439,120
- Trigger refi used: $0
- Total cash distributed to LP: $17,500,000
- Total cash reinvested into HF: $7,682,639
- GP residual NAV: $21,748,014
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__slow_grind__hurdle_2_00x

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

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_50x

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 1.50x
- LP economic multiple: 1.50x
- LP cash IRR: 4.7%
- LP economic IRR: 4.7%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $11,898,211
- Trigger refi used: $0
- Total cash distributed to LP: $15,000,000
- Total cash reinvested into HF: $7,805,368
- GP residual NAV: $27,566,878
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_75x

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash multiple: 1.75x
- LP economic multiple: 1.75x
- LP cash IRR: 6.6%
- LP economic IRR: 6.6%
- Years until LP 2x cash return: 9
- LP cashflow profile: Backend-heavy
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $14,398,211
- Trigger refi used: $0
- Total cash distributed to LP: $17,500,000
- Total cash reinvested into HF: $7,805,368
- GP residual NAV: $25,066,878
- GP survivability risk: True
- Key flags: LP 2x achieved, Value hurdle reached but liquidity constrained, Slow time horizon drift, GP survivability risk, Hurdle trigger executed, LP redeemed via HF liquidation

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_2_00x

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

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_25

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

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_40

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

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_60

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

### re_liquidity_sensitivity__slow_grind__re_liquidity_25

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

### re_liquidity_sensitivity__slow_grind__re_liquidity_40

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

### re_liquidity_sensitivity__slow_grind__re_liquidity_60

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

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_25

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

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_40

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

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_60

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

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_25

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

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_40

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

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_60

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

### twenty_year_horizon__base_hit_everyone_happy__years_20

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

### twenty_year_horizon__slow_grind__years_20

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

### twenty_year_horizon__hedge_fund_failure_re_survival__years_20

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

### twenty_year_horizon__failure_never_reaches_hurdle__years_20

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
