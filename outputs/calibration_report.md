# Scenario Report

Deterministic annual model. LP hurdle achievement is based on actual cash distributions received, not NAV appreciation.

## Summary

| scenario | years_modelled | lp_cash_moic | lp_economic_moic | lp_cash_irr | lp_economic_irr | lp_hurdle_achieved | years_until_lp_2x_cash_return | lp_cashflow_profile_type | hurdle_trigger_executed | hurdle_trigger_year | total_trigger_cash_from_hf_liquidation | total_trigger_cash_from_refi | total_distributed_to_lp | total_reinvested_into_hf | gp_survivability_risk | gp_residual_nav | primary_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| policy_set_comparison__base_hit_everyone_happy__backend_heavy_compounding | 8 | 0.31 | 2.00 | -0.20 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,104,429.38 | 4,819,670.89 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__base_hit_everyone_happy__balanced_yield_compounding | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 6,210,656.38 | 2,697,358.80 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__base_hit_everyone_happy__aggressive_lp_extinguishment | 8 | 0.92 | 2.00 | -0.02 | 0.12 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 9,183,804.48 | 1,132,507.91 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__fast_success_crypto_bull__backend_heavy_compounding | 5 | 0.24 | 2.00 | -0.27 | 0.15 | False |  | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 2,379,901.22 | 2,842,116.49 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| policy_set_comparison__fast_success_crypto_bull__balanced_yield_compounding | 5 | 0.46 | 1.86 | -0.18 | 0.14 | False |  | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 4,579,989.23 | 1,773,101.42 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| policy_set_comparison__fast_success_crypto_bull__aggressive_lp_extinguishment | 5 | 0.68 | 1.75 | -0.11 | 0.14 | False |  | AGGRESSIVE_DISTRIBUTION | False |  | 0.00 | 0.00 | 6,791,899.05 | 693,295.25 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| policy_set_comparison__slow_grind__backend_heavy_compounding | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 6,909,515.46 | True | 11,007,357.34 | LP_HURDLE_ACHIEVED |
| policy_set_comparison__slow_grind__balanced_yield_compounding | 14 | 2.00 | 2.00 | 0.07 | 0.07 | True | 14.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 4,185,311.21 | True | 8,805,811.42 | LP_HURDLE_ACHIEVED |
| policy_set_comparison__slow_grind__aggressive_lp_extinguishment | 15 | 1.31 | 2.00 | 0.03 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 13,057,822.61 | 1,838,038.32 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__hedge_fund_failure_re_survival__backend_heavy_compounding | 12 | 0.34 | 2.00 | -0.14 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,410,714.10 | 5,938,609.41 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__hedge_fund_failure_re_survival__balanced_yield_compounding | 12 | 0.69 | 2.00 | -0.05 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 6,853,102.12 | 2,993,785.72 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__hedge_fund_failure_re_survival__aggressive_lp_extinguishment | 12 | 1.02 | 2.00 | 0.00 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 10,197,293.62 | 1,454,600.01 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__real_estate_distress_crypto_success__backend_heavy_compounding | 10 | 0.23 | 2.00 | -0.22 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,280,437.40 | 3,846,364.28 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__real_estate_distress_crypto_success__balanced_yield_compounding | 10 | 0.49 | 1.85 | -0.11 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 4,910,865.16 | 2,457,747.81 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| policy_set_comparison__real_estate_distress_crypto_success__aggressive_lp_extinguishment | 10 | 0.72 | 1.54 | -0.06 | 0.06 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 7,213,983.08 | 796,741.12 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| policy_set_comparison__exceptional_dynasty_outcome__backend_heavy_compounding | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 6,992,728.70 | True | 16,212,549.23 | LP_HURDLE_ACHIEVED |
| policy_set_comparison__exceptional_dynasty_outcome__balanced_yield_compounding | 8 | 2.00 | 2.00 | 0.11 | 0.11 | True | 8.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 3,934,316.68 | True | 12,585,323.97 | LP_HURDLE_ACHIEVED |
| policy_set_comparison__exceptional_dynasty_outcome__aggressive_lp_extinguishment | 10 | 2.00 | 2.00 | 0.12 | 0.12 | True | 10.00 | AGGRESSIVE_DISTRIBUTION | True | 10.00 | 2,604,185.82 | 0.00 | 20,000,000.00 | 2,244,783.48 | True | 17,384,756.50 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| policy_set_comparison__liquidity_trap__backend_heavy_compounding | 10 | 2.00 | 2.00 | 0.08 | 0.08 | True | 10.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 7,027,253.65 | True | 16,054,959.61 | LP_HURDLE_ACHIEVED |
| policy_set_comparison__liquidity_trap__balanced_yield_compounding | 10 | 0.83 | 2.00 | -0.03 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 8,321,040.28 | 3,830,238.73 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__liquidity_trap__aggressive_lp_extinguishment | 10 | 1.22 | 2.00 | 0.04 | 0.10 | False |  | AGGRESSIVE_DISTRIBUTION | False |  | 0.00 | 0.00 | 12,237,048.75 | 1,625,581.43 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| policy_set_comparison__failure_never_reaches_hurdle__backend_heavy_compounding | 12 | 0.22 | 1.66 | -0.20 | 0.05 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,242,946.97 | 3,195,120.91 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| policy_set_comparison__failure_never_reaches_hurdle__balanced_yield_compounding | 12 | 0.43 | 1.53 | -0.12 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 4,332,932.53 | 1,761,599.18 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| policy_set_comparison__failure_never_reaches_hurdle__aggressive_lp_extinguishment | 12 | 0.64 | 1.45 | -0.07 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 6,424,260.31 | 745,546.54 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_20 | 8 | 0.12 | 2.00 | -0.31 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,233,036.71 | 3,082,591.78 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_30 | 8 | 0.18 | 2.00 | -0.26 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,849,555.07 | 2,697,267.81 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_40 | 8 | 0.25 | 2.00 | -0.23 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,466,073.43 | 2,311,943.84 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_50 | 8 | 0.31 | 2.00 | -0.20 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,082,591.78 | 1,926,619.86 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_60 | 8 | 0.37 | 2.00 | -0.17 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,699,110.14 | 1,541,295.89 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_70 | 8 | 0.43 | 2.00 | -0.15 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 4,315,628.49 | 1,155,971.92 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_80 | 8 | 0.49 | 2.00 | -0.13 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 4,932,146.85 | 770,647.95 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_90 | 8 | 0.55 | 2.00 | -0.11 | 0.11 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 5,548,665.21 | 385,323.97 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_20 | 5 | 0.06 | 2.00 | -0.52 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 628,554.44 | 1,571,386.10 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_30 | 5 | 0.09 | 1.99 | -0.47 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 942,831.66 | 1,374,962.84 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_40 | 5 | 0.13 | 1.97 | -0.44 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,257,108.88 | 1,178,539.58 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_50 | 5 | 0.16 | 1.96 | -0.40 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,571,386.10 | 982,116.31 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_60 | 5 | 0.19 | 1.94 | -0.38 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,885,663.32 | 785,693.05 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_70 | 5 | 0.22 | 1.93 | -0.35 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,199,940.54 | 589,269.79 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_80 | 5 | 0.25 | 1.92 | -0.33 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,514,217.77 | 392,846.53 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_90 | 5 | 0.28 | 1.90 | -0.31 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,828,494.99 | 196,423.26 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_20 | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 10,908,389.82 | 4,319,189.97 | 20,000,000.00 | 4,272,420.21 | True | 10,312,596.33 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_30 | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 9,966,933.65 | 4,726,593.61 | 20,000,000.00 | 3,738,367.68 | True | 9,591,373.96 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_40 | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 9,025,477.48 | 5,133,997.26 | 20,000,000.00 | 3,204,315.16 | True | 8,870,151.60 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_50 | 14 | 2.00 | 2.00 | 0.06 | 0.06 | True | 14.00 | BACKEND_HEAVY | True | 14.00 | 9,330,497.30 | 3,721,302.14 | 20,000,000.00 | 2,931,000.25 | True | 10,604,433.11 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_60 | 14 | 2.00 | 2.00 | 0.06 | 0.06 | True | 14.00 | BACKEND_HEAVY | True | 14.00 | 8,227,541.19 | 4,238,058.20 | 20,000,000.00 | 2,344,800.20 | True | 9,720,025.01 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_70 | 14 | 2.00 | 2.00 | 0.06 | 0.06 | True | 14.00 | BACKEND_HEAVY | True | 14.00 | 7,124,585.07 | 4,754,814.27 | 20,000,000.00 | 1,758,600.15 | True | 8,835,616.91 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_80 | 14 | 2.00 | 2.00 | 0.06 | 0.06 | True | 14.00 | BACKEND_HEAVY | True | 14.00 | 6,021,628.95 | 5,271,570.33 | 20,000,000.00 | 1,172,400.10 | True | 7,951,208.80 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__slow_grind__lp_distribution_90 | 15 | 2.00 | 2.00 | 0.06 | 0.06 | True | 15.00 | BACKEND_HEAVY | True | 15.00 | 5,254,308.11 | 4,642,392.98 | 20,000,000.00 | 640,219.93 | True | 8,548,923.94 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_20 | 12 | 0.19 | 2.00 | -0.18 | 0.06 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,899,961.62 | 4,749,904.05 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_30 | 12 | 0.28 | 2.00 | -0.15 | 0.06 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,849,942.43 | 4,156,166.04 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_40 | 12 | 0.38 | 2.00 | -0.12 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,799,923.24 | 3,562,428.04 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_50 | 12 | 0.47 | 2.00 | -0.09 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 4,749,904.05 | 2,968,690.03 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_60 | 12 | 0.57 | 2.00 | -0.07 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 5,699,884.86 | 2,374,952.02 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_70 | 12 | 0.66 | 2.00 | -0.05 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 6,649,865.67 | 1,781,214.02 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_80 | 12 | 0.76 | 2.00 | -0.04 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 7,599,846.48 | 1,187,476.01 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_90 | 12 | 0.85 | 2.00 | -0.02 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 8,549,827.29 | 593,738.01 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_20 | 10 | 0.06 | 2.00 | -0.34 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 606,132.08 | 1,515,330.19 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_30 | 10 | 0.09 | 2.00 | -0.31 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 909,198.12 | 1,325,913.92 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_40 | 10 | 0.12 | 2.00 | -0.28 | 0.07 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,212,264.15 | 1,136,497.64 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_50 | 10 | 0.15 | 2.00 | -0.26 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,515,330.19 | 947,081.37 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_60 | 10 | 0.18 | 2.00 | -0.24 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,818,396.23 | 757,665.10 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_70 | 10 | 0.21 | 2.00 | -0.22 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,121,462.27 | 568,248.82 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_80 | 10 | 0.24 | 2.00 | -0.21 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,424,528.31 | 378,832.55 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_90 | 10 | 0.27 | 2.00 | -0.19 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,727,594.35 | 189,416.27 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_20 | 8 | 2.00 | 2.00 | 0.09 | 0.09 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 11,608,931.13 | 3,571,902.67 | 20,000,000.00 | 4,319,166.20 | True | 16,030,647.83 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_30 | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 10,839,821.78 | 3,801,116.24 | 20,000,000.00 | 3,779,270.43 | True | 15,545,064.47 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_40 | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 10,070,712.43 | 4,030,329.82 | 20,000,000.00 | 3,239,374.65 | True | 15,059,481.11 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_50 | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 9,301,603.08 | 4,259,543.39 | 20,000,000.00 | 2,699,478.88 | True | 14,573,897.75 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_60 | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 8,532,493.72 | 4,488,756.97 | 20,000,000.00 | 2,159,583.10 | True | 14,088,314.39 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_70 | 8 | 2.00 | 2.00 | 0.11 | 0.11 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 7,763,384.37 | 4,717,970.55 | 20,000,000.00 | 1,619,687.33 | True | 13,602,731.03 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_80 | 8 | 2.00 | 2.00 | 0.11 | 0.11 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 6,994,275.02 | 4,947,184.12 | 20,000,000.00 | 1,079,791.55 | True | 13,117,147.67 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_90 | 8 | 2.00 | 2.00 | 0.11 | 0.11 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 6,225,165.67 | 5,176,397.70 | 20,000,000.00 | 539,895.78 | True | 12,631,564.31 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_20 | 9 | 2.00 | 2.00 | 0.08 | 0.08 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 9,438,415.03 | 6,153,819.62 | 20,000,000.00 | 3,907,765.35 | True | 12,619,222.03 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_30 | 9 | 2.00 | 2.00 | 0.08 | 0.08 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 8,705,435.03 | 6,398,328.95 | 20,000,000.00 | 3,419,294.68 | True | 12,130,386.03 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_40 | 9 | 2.00 | 2.00 | 0.09 | 0.09 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 7,972,455.02 | 6,642,838.29 | 20,000,000.00 | 2,930,824.01 | True | 11,641,550.02 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_50 | 9 | 2.00 | 2.00 | 0.09 | 0.09 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 7,239,475.02 | 6,887,347.62 | 20,000,000.00 | 2,442,353.34 | True | 11,152,714.02 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_60 | 9 | 2.00 | 2.00 | 0.09 | 0.09 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 6,506,495.01 | 7,131,856.96 | 20,000,000.00 | 1,953,882.68 | True | 10,663,878.02 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_70 | 9 | 2.00 | 2.00 | 0.09 | 0.09 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 5,773,515.01 | 7,376,366.30 | 20,000,000.00 | 1,465,412.01 | True | 10,175,042.01 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_80 | 9 | 2.00 | 2.00 | 0.09 | 0.09 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 5,040,535.00 | 7,620,875.63 | 20,000,000.00 | 976,941.34 | True | 9,686,206.01 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_90 | 10 | 2.00 | 2.00 | 0.09 | 0.09 | True | 10.00 | BACKEND_HEAVY | True | 10.00 | 4,544,343.17 | 6,338,877.37 | 20,000,000.00 | 574,451.96 | True | 11,896,690.23 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_20 | 12 | 0.08 | 1.64 | -0.27 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 822,800.76 | 2,057,001.90 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_30 | 12 | 0.12 | 1.61 | -0.23 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,234,201.14 | 1,799,876.66 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_40 | 12 | 0.16 | 1.59 | -0.21 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,645,601.52 | 1,542,751.42 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_50 | 12 | 0.21 | 1.57 | -0.19 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,057,001.90 | 1,285,626.19 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_60 | 12 | 0.25 | 1.55 | -0.17 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,468,402.28 | 1,028,500.95 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_70 | 12 | 0.29 | 1.53 | -0.16 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,879,802.66 | 771,375.71 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_80 | 12 | 0.33 | 1.50 | -0.14 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,291,203.04 | 514,250.47 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_90 | 12 | 0.37 | 1.48 | -0.13 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 3,702,603.42 | 257,125.24 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_20 | 8 | 0.11 | 2.00 | -0.32 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,087,973.57 | 2,719,933.92 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_30 | 7 | 2.00 | 2.00 | 0.11 | 0.11 | True | 7.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 1,991,391.56 | True | 7,549,576.41 | LP_HURDLE_ACHIEVED |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_40 | 7 | 2.00 | 2.00 | 0.11 | 0.11 | True | 7.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 1,685,023.63 | True | 9,582,181.67 | LP_HURDLE_ACHIEVED |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_20 | 5 | 0.06 | 2.00 | -0.54 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 554,606.86 | 1,386,517.15 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_30 | 5 | 2.00 | 2.00 | 0.15 | 0.15 | True | 5.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 1,201,648.20 | True | 7,437,718.65 | LP_HURDLE_ACHIEVED |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_40 | 4 | 2.00 | 2.00 | 0.19 | 0.19 | True | 4.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 792,473.00 | True | 7,519,607.41 | FAST_GP_DYNASTY_OUTCOME |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_20 | 7 | 2.00 | 2.00 | 0.11 | 0.11 | True | 7.00 | BACKEND_HEAVY | True | 7.00 | 12,359,973.80 | 4,022,801.69 | 20,000,000.00 | 3,117,224.52 | True | 12,950,871.59 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_30 | 5 | 2.00 | 2.00 | 0.15 | 0.15 | True | 5.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 1,691,807.24 | True | 7,215,387.06 | LP_HURDLE_ACHIEVED |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_40 | 5 | 2.00 | 2.00 | 0.15 | 0.15 | True | 5.00 | BACKEND_HEAVY | False |  | 0.00 | 0.00 | 20,000,000.00 | 1,431,529.21 | True | 9,398,127.51 | LP_HURDLE_ACHIEVED |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_25 | 8 | 0.15 | 2.00 | -0.28 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,527,407.62 | 4,112,889.97 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_50 | 8 | 0.18 | 2.00 | -0.26 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,797,443.68 | 5,058,016.16 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_75 | 8 | 0.20 | 2.00 | -0.24 | 0.10 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 2,044,814.92 | 5,923,815.52 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_25 | 5 | 0.09 | 1.97 | -0.48 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 890,933.23 | 2,489,711.86 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_50 | 5 | 0.11 | 1.95 | -0.45 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,129,315.66 | 3,324,050.37 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_75 | 5 | 0.13 | 1.93 | -0.43 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,345,174.75 | 4,079,557.18 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_25 | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 10,641,691.91 | 3,819,972.45 | 20,000,000.00 | 5,997,228.22 | True | 15,460,164.98 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_50 | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 9,761,285.66 | 4,061,451.43 | 20,000,000.00 | 7,488,058.52 | True | 14,925,217.25 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_75 | 8 | 2.00 | 2.00 | 0.10 | 0.10 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 8,960,543.79 | 4,295,966.46 | 20,000,000.00 | 8,809,254.46 | True | 14,423,788.25 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_50x | 7 | 1.50 | 1.50 | 0.06 | 0.06 | True | 7.00 | BACKEND_HEAVY | True | 7.00 | 6,896,113.75 | 4,999,758.82 | 15,000,000.00 | 2,604,127.43 | True | 8,484,365.89 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_75x | 8 | 0.12 | 1.75 | -0.31 | 0.08 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,233,036.71 | 3,082,591.78 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_2_00x | 8 | 0.12 | 2.00 | -0.31 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,233,036.71 | 3,082,591.78 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_50x | 5 | 0.06 | 1.50 | -0.52 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 628,554.44 | 1,571,386.10 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_75x | 5 | 0.06 | 1.75 | -0.52 | 0.12 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 628,554.44 | 1,571,386.10 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_2_00x | 5 | 0.06 | 2.00 | -0.52 | 0.15 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 628,554.44 | 1,571,386.10 | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_hurdle_sensitivity__slow_grind__hurdle_1_50x | 11 | 1.50 | 1.50 | 0.04 | 0.04 | True | 11.00 | BACKEND_HEAVY | True | 11.00 | 6,739,594.13 | 4,279,453.97 | 15,000,000.00 | 3,480,951.90 | True | 8,535,759.03 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_hurdle_sensitivity__slow_grind__hurdle_1_75x | 12 | 1.75 | 1.75 | 0.05 | 0.05 | True | 12.00 | BACKEND_HEAVY | True | 12.00 | 7,974,700.87 | 5,155,595.81 | 17,500,000.00 | 3,869,703.32 | True | 8,282,693.06 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_hurdle_sensitivity__slow_grind__hurdle_2_00x | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 10,908,389.82 | 4,319,189.97 | 20,000,000.00 | 4,272,420.21 | True | 10,312,596.33 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_50x | 6 | 1.50 | 1.50 | 0.07 | 0.07 | True | 6.00 | BACKEND_HEAVY | True | 6.00 | 7,349,507.92 | 4,316,689.88 | 15,000,000.00 | 2,833,802.20 | True | 11,621,577.84 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_75x | 7 | 1.75 | 1.75 | 0.09 | 0.09 | True | 7.00 | BACKEND_HEAVY | True | 7.00 | 8,608,747.90 | 4,858,397.65 | 17,500,000.00 | 3,532,854.45 | True | 12,578,691.27 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_2_00x | 8 | 2.00 | 2.00 | 0.09 | 0.09 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 11,608,931.13 | 3,571,902.67 | 20,000,000.00 | 4,319,166.20 | True | 16,030,647.83 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_25 | 8 | 0.12 | 2.00 | -0.31 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,233,036.71 | 3,082,591.78 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_40 | 8 | 0.12 | 2.00 | -0.31 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,233,036.71 | 3,082,591.78 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_60 | 8 | 0.12 | 2.00 | -0.31 | 0.09 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,233,036.71 | 3,082,591.78 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__slow_grind__re_liquidity_25 | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 10,908,389.82 | 4,319,189.97 | 20,000,000.00 | 4,272,420.21 | True | 10,312,596.33 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__slow_grind__re_liquidity_40 | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 10,908,389.82 | 4,319,189.97 | 20,000,000.00 | 4,272,420.21 | True | 10,312,596.33 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__slow_grind__re_liquidity_60 | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 10,908,389.82 | 4,319,189.97 | 20,000,000.00 | 4,272,420.21 | True | 10,312,596.33 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_25 | 9 | 2.00 | 2.00 | 0.08 | 0.08 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 9,438,415.03 | 6,153,819.62 | 20,000,000.00 | 3,907,765.35 | True | 12,619,222.03 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_40 | 9 | 2.00 | 2.00 | 0.08 | 0.08 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 9,438,415.03 | 6,153,819.62 | 20,000,000.00 | 3,907,765.35 | True | 12,619,222.03 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_60 | 9 | 2.00 | 2.00 | 0.08 | 0.08 | True | 9.00 | BACKEND_HEAVY | True | 9.00 | 9,438,415.03 | 6,153,819.62 | 20,000,000.00 | 3,907,765.35 | True | 12,619,222.03 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_25 | 8 | 2.00 | 2.00 | 0.09 | 0.09 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 11,608,931.13 | 3,571,902.67 | 20,000,000.00 | 4,319,166.20 | True | 16,030,647.83 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_40 | 8 | 2.00 | 2.00 | 0.09 | 0.09 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 11,608,931.13 | 3,571,902.67 | 20,000,000.00 | 4,319,166.20 | True | 16,030,647.83 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_60 | 8 | 2.00 | 2.00 | 0.09 | 0.09 | True | 8.00 | BACKEND_HEAVY | True | 8.00 | 11,608,931.13 | 3,571,902.67 | 20,000,000.00 | 4,319,166.20 | True | 16,030,647.83 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| twenty_year_horizon__base_hit_everyone_happy__years_20 | 10 | 2.00 | 2.00 | 0.07 | 0.07 | True | 10.00 | BACKEND_HEAVY | True | 10.00 | 9,431,090.28 | 5,930,943.18 | 20,000,000.00 | 4,137,966.54 | True | 9,794,830.01 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| twenty_year_horizon__slow_grind__years_20 | 13 | 2.00 | 2.00 | 0.06 | 0.06 | True | 13.00 | BACKEND_HEAVY | True | 13.00 | 10,908,389.82 | 4,319,189.97 | 20,000,000.00 | 4,272,420.21 | True | 10,312,596.33 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| twenty_year_horizon__hedge_fund_failure_re_survival__years_20 | 16 | 2.00 | 2.00 | 0.05 | 0.05 | True | 16.00 | BACKEND_HEAVY | True | 16.00 | 7,137,145.75 | 5,363,602.45 | 20,000,000.00 | 6,999,251.80 | True | 9,633,743.91 | HURDLE_COMPLETION_TRIGGER_EXECUTED |
| twenty_year_horizon__failure_never_reaches_hurdle__years_20 | 20 | 0.13 | 2.00 | -0.15 | 0.04 | False |  | MODERATE_YIELD | False |  | 0.00 | 0.00 | 1,318,717.96 | 3,296,794.89 | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |

## Scenario Notes

### policy_set_comparison__base_hit_everyone_happy__backend_heavy_compounding

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.31x
- LP economic MOIC: 2.00x
- LP cash IRR: -19.9%
- LP economic IRR: 9.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,104,429
- Total cash reinvested into HF: $4,819,671
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__base_hit_everyone_happy__balanced_yield_compounding

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -8.9%
- LP economic IRR: 10.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $6,210,656
- Total cash reinvested into HF: $2,697,359
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__base_hit_everyone_happy__aggressive_lp_extinguishment

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.92x
- LP economic MOIC: 2.00x
- LP cash IRR: -1.8%
- LP economic IRR: 11.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $9,183,804
- Total cash reinvested into HF: $1,132,508
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__fast_success_crypto_bull__backend_heavy_compounding

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.24x
- LP economic MOIC: 2.00x
- LP cash IRR: -27.4%
- LP economic IRR: 15.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,379,901
- Total cash reinvested into HF: $2,842,116
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__fast_success_crypto_bull__balanced_yield_compounding

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.46x
- LP economic MOIC: 1.86x
- LP cash IRR: -17.5%
- LP economic IRR: 14.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $4,579,989
- Total cash reinvested into HF: $1,773,101
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__fast_success_crypto_bull__aggressive_lp_extinguishment

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.68x
- LP economic MOIC: 1.75x
- LP cash IRR: -10.8%
- LP economic IRR: 14.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $6,791,899
- Total cash reinvested into HF: $693,295
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__slow_grind__backend_heavy_compounding

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.1%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $6,909,515
- GP residual NAV: $11,007,357
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME

### policy_set_comparison__slow_grind__balanced_yield_compounding

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.5%
- LP economic IRR: 6.5%
- Years until LP 2x cash return: 14
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,185,311
- GP residual NAV: $8,805,811
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME; HF_MAJOR_DRAWDOWN

### policy_set_comparison__slow_grind__aggressive_lp_extinguishment

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 1.31x
- LP economic MOIC: 2.00x
- LP cash IRR: 3.5%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $13,057,823
- Total cash reinvested into HF: $1,838,038
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; REFINANCE_EVENT_OCCURRED

### policy_set_comparison__hedge_fund_failure_re_survival__backend_heavy_compounding

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.34x
- LP economic MOIC: 2.00x
- LP cash IRR: -14.5%
- LP economic IRR: 6.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,410,714
- Total cash reinvested into HF: $5,938,609
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__hedge_fund_failure_re_survival__balanced_yield_compounding

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.69x
- LP economic MOIC: 2.00x
- LP cash IRR: -5.4%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $6,853,102
- Total cash reinvested into HF: $2,993,786
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__hedge_fund_failure_re_survival__aggressive_lp_extinguishment

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 1.02x
- LP economic MOIC: 2.00x
- LP cash IRR: 0.3%
- LP economic IRR: 8.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $10,197,294
- Total cash reinvested into HF: $1,454,600
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; REFINANCE_EVENT_OCCURRED; HF_MAJOR_DRAWDOWN

### policy_set_comparison__real_estate_distress_crypto_success__backend_heavy_compounding

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.23x
- LP economic MOIC: 2.00x
- LP cash IRR: -21.6%
- LP economic IRR: 7.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,280,437
- Total cash reinvested into HF: $3,846,364
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__real_estate_distress_crypto_success__balanced_yield_compounding

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.49x
- LP economic MOIC: 1.85x
- LP cash IRR: -11.4%
- LP economic IRR: 7.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $4,910,865
- Total cash reinvested into HF: $2,457,748
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__real_estate_distress_crypto_success__aggressive_lp_extinguishment

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.72x
- LP economic MOIC: 1.54x
- LP cash IRR: -6.1%
- LP economic IRR: 6.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,213,983
- Total cash reinvested into HF: $796,741
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__exceptional_dynasty_outcome__backend_heavy_compounding

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.0%
- LP economic IRR: 10.0%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $6,992,729
- GP residual NAV: $16,212,549
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME

### policy_set_comparison__exceptional_dynasty_outcome__balanced_yield_compounding

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 11.2%
- LP economic IRR: 11.2%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,934,317
- GP residual NAV: $12,585,324
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME; HF_MAJOR_DRAWDOWN

### policy_set_comparison__exceptional_dynasty_outcome__aggressive_lp_extinguishment

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 12.0%
- LP economic IRR: 12.0%
- Years until LP 2x cash return: 10
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: True
- Hurdle trigger year: 10
- Trigger HF liquidation used: $2,604,186
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,244,783
- GP residual NAV: $17,384,757
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME

### policy_set_comparison__liquidity_trap__backend_heavy_compounding

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.0%
- LP economic IRR: 8.0%
- Years until LP 2x cash return: 10
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,027,254
- GP residual NAV: $16,054,960
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; REFI_DEPENDENT_LP_OUTCOME

### policy_set_comparison__liquidity_trap__balanced_yield_compounding

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 0.83x
- LP economic MOIC: 2.00x
- LP cash IRR: -3.0%
- LP economic IRR: 9.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $8,321,040
- Total cash reinvested into HF: $3,830,239
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__liquidity_trap__aggressive_lp_extinguishment

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 1.22x
- LP economic MOIC: 2.00x
- LP cash IRR: 3.7%
- LP economic IRR: 10.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: AGGRESSIVE_DISTRIBUTION
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $12,237,049
- Total cash reinvested into HF: $1,625,581
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; REFINANCE_EVENT_OCCURRED

### policy_set_comparison__failure_never_reaches_hurdle__backend_heavy_compounding

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.22x
- LP economic MOIC: 1.66x
- LP cash IRR: -20.1%
- LP economic IRR: 4.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,242,947
- Total cash reinvested into HF: $3,195,121
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__failure_never_reaches_hurdle__balanced_yield_compounding

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.43x
- LP economic MOIC: 1.53x
- LP cash IRR: -11.8%
- LP economic IRR: 4.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $4,332,933
- Total cash reinvested into HF: $1,761,599
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### policy_set_comparison__failure_never_reaches_hurdle__aggressive_lp_extinguishment

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.64x
- LP economic MOIC: 1.45x
- LP cash IRR: -6.9%
- LP economic IRR: 4.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $6,424,260
- Total cash reinvested into HF: $745,547
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; REFINANCE_EVENT_OCCURRED; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_20

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.12x
- LP economic MOIC: 2.00x
- LP cash IRR: -30.8%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,233,037
- Total cash reinvested into HF: $3,082,592
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_30

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.18x
- LP economic MOIC: 2.00x
- LP cash IRR: -26.2%
- LP economic IRR: 9.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,849,555
- Total cash reinvested into HF: $2,697,268
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_40

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.25x
- LP economic MOIC: 2.00x
- LP cash IRR: -22.6%
- LP economic IRR: 9.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,466,073
- Total cash reinvested into HF: $2,311,944
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_50

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.31x
- LP economic MOIC: 2.00x
- LP cash IRR: -19.7%
- LP economic IRR: 9.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,082,592
- Total cash reinvested into HF: $1,926,620
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_60

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.37x
- LP economic MOIC: 2.00x
- LP cash IRR: -17.1%
- LP economic IRR: 10.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,699,110
- Total cash reinvested into HF: $1,541,296
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_70

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.43x
- LP economic MOIC: 2.00x
- LP cash IRR: -14.8%
- LP economic IRR: 10.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $4,315,628
- Total cash reinvested into HF: $1,155,972
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_80

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.49x
- LP economic MOIC: 2.00x
- LP cash IRR: -12.7%
- LP economic IRR: 10.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $4,932,147
- Total cash reinvested into HF: $770,648
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__base_hit_everyone_happy__lp_distribution_90

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.55x
- LP economic MOIC: 2.00x
- LP cash IRR: -10.8%
- LP economic IRR: 10.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $5,548,665
- Total cash reinvested into HF: $385,324
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_20

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.06x
- LP economic MOIC: 2.00x
- LP cash IRR: -52.2%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $628,554
- Total cash reinvested into HF: $1,571,386
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_30

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.09x
- LP economic MOIC: 1.99x
- LP cash IRR: -47.4%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $942,832
- Total cash reinvested into HF: $1,374,963
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_40

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.13x
- LP economic MOIC: 1.97x
- LP cash IRR: -43.6%
- LP economic IRR: 15.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,257,109
- Total cash reinvested into HF: $1,178,540
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_50

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.16x
- LP economic MOIC: 1.96x
- LP cash IRR: -40.4%
- LP economic IRR: 15.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,571,386
- Total cash reinvested into HF: $982,116
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_60

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.19x
- LP economic MOIC: 1.94x
- LP cash IRR: -37.6%
- LP economic IRR: 14.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,885,663
- Total cash reinvested into HF: $785,693
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_70

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.22x
- LP economic MOIC: 1.93x
- LP cash IRR: -35.1%
- LP economic IRR: 14.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,199,941
- Total cash reinvested into HF: $589,270
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_80

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.25x
- LP economic MOIC: 1.92x
- LP cash IRR: -32.8%
- LP economic IRR: 14.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,514,218
- Total cash reinvested into HF: $392,847
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__fast_success_crypto_bull__lp_distribution_90

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.28x
- LP economic MOIC: 1.90x
- LP cash IRR: -30.7%
- LP economic IRR: 14.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,828,495
- Total cash reinvested into HF: $196,423
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_20

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.7%
- LP economic IRR: 5.7%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $10,908,390
- Trigger refi used: $4,319,190
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,272,420
- GP residual NAV: $10,312,596
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_30

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.9%
- LP economic IRR: 5.9%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $9,966,934
- Trigger refi used: $4,726,594
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,738,368
- GP residual NAV: $9,591,374
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_40

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.0%
- LP economic IRR: 6.0%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $9,025,477
- Trigger refi used: $5,133,997
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,204,315
- GP residual NAV: $8,870,152
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_50

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.8%
- LP economic IRR: 5.8%
- Years until LP 2x cash return: 14
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $9,330,497
- Trigger refi used: $3,721,302
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,931,000
- GP residual NAV: $10,604,433
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_60

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.0%
- LP economic IRR: 6.0%
- Years until LP 2x cash return: 14
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $8,227,541
- Trigger refi used: $4,238,058
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,344,800
- GP residual NAV: $9,720,025
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_70

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.1%
- LP economic IRR: 6.1%
- Years until LP 2x cash return: 14
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $7,124,585
- Trigger refi used: $4,754,814
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,758,600
- GP residual NAV: $8,835,617
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_80

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.3%
- LP economic IRR: 6.3%
- Years until LP 2x cash return: 14
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 14
- Trigger HF liquidation used: $6,021,629
- Trigger refi used: $5,271,570
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,172,400
- GP residual NAV: $7,951,209
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__slow_grind__lp_distribution_90

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 15
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 15
- Trigger HF liquidation used: $5,254,308
- Trigger refi used: $4,642,393
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $640,220
- GP residual NAV: $8,548,924
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_20

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.19x
- LP economic MOIC: 2.00x
- LP cash IRR: -18.5%
- LP economic IRR: 6.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,899,962
- Total cash reinvested into HF: $4,749,904
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_30

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.28x
- LP economic MOIC: 2.00x
- LP cash IRR: -14.7%
- LP economic IRR: 6.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,849,942
- Total cash reinvested into HF: $4,156,166
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_40

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.38x
- LP economic MOIC: 2.00x
- LP cash IRR: -11.8%
- LP economic IRR: 6.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,799,923
- Total cash reinvested into HF: $3,562,428
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_50

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.47x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.3%
- LP economic IRR: 6.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $4,749,904
- Total cash reinvested into HF: $2,968,690
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_60

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.57x
- LP economic MOIC: 2.00x
- LP cash IRR: -7.2%
- LP economic IRR: 7.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $5,699,885
- Total cash reinvested into HF: $2,374,952
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_70

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.66x
- LP economic MOIC: 2.00x
- LP cash IRR: -5.4%
- LP economic IRR: 7.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $6,649,866
- Total cash reinvested into HF: $1,781,214
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_80

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.76x
- LP economic MOIC: 2.00x
- LP cash IRR: -3.7%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $7,599,846
- Total cash reinvested into HF: $1,187,476
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__hedge_fund_failure_re_survival__lp_distribution_90

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.85x
- LP economic MOIC: 2.00x
- LP cash IRR: -2.2%
- LP economic IRR: 7.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $8,549,827
- Total cash reinvested into HF: $593,738
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_20

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.06x
- LP economic MOIC: 2.00x
- LP cash IRR: -34.0%
- LP economic IRR: 7.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $606,132
- Total cash reinvested into HF: $1,515,330
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_30

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.09x
- LP economic MOIC: 2.00x
- LP cash IRR: -30.6%
- LP economic IRR: 7.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $909,198
- Total cash reinvested into HF: $1,325,914
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_40

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.12x
- LP economic MOIC: 2.00x
- LP cash IRR: -27.9%
- LP economic IRR: 7.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,212,264
- Total cash reinvested into HF: $1,136,498
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_50

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.15x
- LP economic MOIC: 2.00x
- LP cash IRR: -25.7%
- LP economic IRR: 7.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,515,330
- Total cash reinvested into HF: $947,081
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_60

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.18x
- LP economic MOIC: 2.00x
- LP cash IRR: -23.9%
- LP economic IRR: 7.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,818,396
- Total cash reinvested into HF: $757,665
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_70

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.21x
- LP economic MOIC: 2.00x
- LP cash IRR: -22.2%
- LP economic IRR: 7.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,121,462
- Total cash reinvested into HF: $568,249
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_80

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.24x
- LP economic MOIC: 2.00x
- LP cash IRR: -20.7%
- LP economic IRR: 7.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,424,528
- Total cash reinvested into HF: $378,833
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__real_estate_distress_crypto_success__lp_distribution_90

Real estate underperforms while hedge fund returns are strong; tests whether liquid gains can offset property stress.

- LP cash MOIC: 0.27x
- LP economic MOIC: 2.00x
- LP cash IRR: -19.4%
- LP economic IRR: 7.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,727,594
- Total cash reinvested into HF: $189,416
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_20

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $11,608,931
- Trigger refi used: $3,571,903
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,319,166
- GP residual NAV: $16,030,648
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_30

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.6%
- LP economic IRR: 9.6%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $10,839,822
- Trigger refi used: $3,801,116
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,779,270
- GP residual NAV: $15,545,064
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_40

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.8%
- LP economic IRR: 9.8%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $10,070,712
- Trigger refi used: $4,030,330
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,239,375
- GP residual NAV: $15,059,481
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_50

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.0%
- LP economic IRR: 10.0%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $9,301,603
- Trigger refi used: $4,259,543
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,699,479
- GP residual NAV: $14,573,898
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_60

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.3%
- LP economic IRR: 10.3%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $8,532,494
- Trigger refi used: $4,488,757
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,159,583
- GP residual NAV: $14,088,314
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_70

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.5%
- LP economic IRR: 10.5%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $7,763,384
- Trigger refi used: $4,717,971
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,619,687
- GP residual NAV: $13,602,731
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_80

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.7%
- LP economic IRR: 10.7%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $6,994,275
- Trigger refi used: $4,947,184
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,079,792
- GP residual NAV: $13,117,148
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__exceptional_dynasty_outcome__lp_distribution_90

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 11.0%
- LP economic IRR: 11.0%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $6,225,166
- Trigger refi used: $5,176,398
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $539,896
- GP residual NAV: $12,631,564
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_20

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.3%
- LP economic IRR: 8.3%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $9,438,415
- Trigger refi used: $6,153,820
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,907,765
- GP residual NAV: $12,619,222
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_30

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.5%
- LP economic IRR: 8.5%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $8,705,435
- Trigger refi used: $6,398,329
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,419,295
- GP residual NAV: $12,130,386
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_40

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.6%
- LP economic IRR: 8.6%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $7,972,455
- Trigger refi used: $6,642,838
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,930,824
- GP residual NAV: $11,641,550
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_50

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.8%
- LP economic IRR: 8.8%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $7,239,475
- Trigger refi used: $6,887,348
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $2,442,353
- GP residual NAV: $11,152,714
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_60

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.0%
- LP economic IRR: 9.0%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $6,506,495
- Trigger refi used: $7,131,857
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,953,883
- GP residual NAV: $10,663,878
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_70

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.2%
- LP economic IRR: 9.2%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $5,773,515
- Trigger refi used: $7,376,366
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,465,412
- GP residual NAV: $10,175,042
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_80

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $5,040,535
- Trigger refi used: $7,620,876
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $976,941
- GP residual NAV: $9,686,206
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__liquidity_trap__lp_distribution_90

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.9%
- LP economic IRR: 8.9%
- Years until LP 2x cash return: 10
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 10
- Trigger HF liquidation used: $4,544,343
- Trigger refi used: $6,338,877
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $574,452
- GP residual NAV: $11,896,690
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_20

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.08x
- LP economic MOIC: 1.64x
- LP cash IRR: -26.6%
- LP economic IRR: 4.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $822,801
- Total cash reinvested into HF: $2,057,002
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_30

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.12x
- LP economic MOIC: 1.61x
- LP cash IRR: -23.4%
- LP economic IRR: 4.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,234,201
- Total cash reinvested into HF: $1,799,877
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_40

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.16x
- LP economic MOIC: 1.59x
- LP cash IRR: -20.9%
- LP economic IRR: 4.2%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,645,602
- Total cash reinvested into HF: $1,542,751
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_50

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.21x
- LP economic MOIC: 1.57x
- LP cash IRR: -18.8%
- LP economic IRR: 4.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,057,002
- Total cash reinvested into HF: $1,285,626
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_60

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.25x
- LP economic MOIC: 1.55x
- LP cash IRR: -17.1%
- LP economic IRR: 4.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,468,402
- Total cash reinvested into HF: $1,028,501
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_70

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.29x
- LP economic MOIC: 1.53x
- LP cash IRR: -15.6%
- LP economic IRR: 4.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,879,803
- Total cash reinvested into HF: $771,376
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_80

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.33x
- LP economic MOIC: 1.50x
- LP cash IRR: -14.2%
- LP economic IRR: 3.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,291,203
- Total cash reinvested into HF: $514,250
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_distribution_strategy_sweep__failure_never_reaches_hurdle__lp_distribution_90

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.37x
- LP economic MOIC: 1.48x
- LP cash IRR: -12.9%
- LP economic IRR: 3.8%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $3,702,603
- Total cash reinvested into HF: $257,125
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_20

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.11x
- LP economic MOIC: 2.00x
- LP cash IRR: -32.1%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,087,974
- Total cash reinvested into HF: $2,719,934
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_30

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.6%
- LP economic IRR: 10.6%
- Years until LP 2x cash return: 7
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,991,392
- GP residual NAV: $7,549,576
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_40

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.6%
- LP economic IRR: 10.6%
- Years until LP 2x cash return: 7
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,685,024
- GP residual NAV: $9,582,182
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_20

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.06x
- LP economic MOIC: 2.00x
- LP cash IRR: -53.6%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $554,607
- Total cash reinvested into HF: $1,386,517
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_30

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 15.1%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: 5
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,201,648
- GP residual NAV: $7,437,719
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_40

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 19.1%
- LP economic IRR: 19.1%
- Years until LP 2x cash return: 4
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $792,473
- GP residual NAV: $7,519,607
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; FAST_GP_DYNASTY_OUTCOME; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_20

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.7%
- LP economic IRR: 10.7%
- Years until LP 2x cash return: 7
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $12,359,974
- Trigger refi used: $4,022,802
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,117,225
- GP residual NAV: $12,950,872
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_30

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 15.1%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: 5
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,691,807
- GP residual NAV: $7,215,387
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_40

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 15.1%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: 5
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $1,431,529
- GP residual NAV: $9,398,128
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_25

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.15x
- LP economic MOIC: 2.00x
- LP cash IRR: -28.1%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,527,408
- Total cash reinvested into HF: $4,112,890
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_50

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.18x
- LP economic MOIC: 2.00x
- LP cash IRR: -26.0%
- LP economic IRR: 9.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,797,444
- Total cash reinvested into HF: $5,058,016
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_75

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.20x
- LP economic MOIC: 2.00x
- LP cash IRR: -24.4%
- LP economic IRR: 9.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $2,044,815
- Total cash reinvested into HF: $5,923,816
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_25

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.09x
- LP economic MOIC: 1.97x
- LP cash IRR: -48.3%
- LP economic IRR: 14.9%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $890,933
- Total cash reinvested into HF: $2,489,712
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_50

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.11x
- LP economic MOIC: 1.95x
- LP cash IRR: -45.5%
- LP economic IRR: 14.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,129,316
- Total cash reinvested into HF: $3,324,050
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_75

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.13x
- LP economic MOIC: 1.93x
- LP cash IRR: -43.2%
- LP economic IRR: 14.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,345,175
- Total cash reinvested into HF: $4,079,557
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_25

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.5%
- LP economic IRR: 9.5%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $10,641,692
- Trigger refi used: $3,819,972
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $5,997,228
- GP residual NAV: $15,460,165
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_50

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.6%
- LP economic IRR: 9.6%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $9,761,286
- Trigger refi used: $4,061,451
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $7,488,059
- GP residual NAV: $14,925,217
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_75

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.7%
- LP economic IRR: 9.7%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $8,960,544
- Trigger refi used: $4,295,966
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $8,809,254
- GP residual NAV: $14,423,788
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_50x

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 1.50x
- LP economic MOIC: 1.50x
- LP cash IRR: 6.2%
- LP economic IRR: 6.2%
- Years until LP 2x cash return: 7
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $6,896,114
- Trigger refi used: $4,999,759
- Total cash distributed to LP: $15,000,000
- Total cash reinvested into HF: $2,604,127
- GP residual NAV: $8,484,366
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_75x

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.12x
- LP economic MOIC: 1.75x
- LP cash IRR: -30.8%
- LP economic IRR: 7.5%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,233,037
- Total cash reinvested into HF: $3,082,592
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_2_00x

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.12x
- LP economic MOIC: 2.00x
- LP cash IRR: -30.8%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,233,037
- Total cash reinvested into HF: $3,082,592
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_50x

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.06x
- LP economic MOIC: 1.50x
- LP cash IRR: -52.2%
- LP economic IRR: 8.6%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $628,554
- Total cash reinvested into HF: $1,571,386
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_75x

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.06x
- LP economic MOIC: 1.75x
- LP cash IRR: -52.2%
- LP economic IRR: 12.0%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $628,554
- Total cash reinvested into HF: $1,571,386
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_2_00x

Strong hedge fund sleeve over a shorter horizon; tests whether liquid alpha can accelerate LP cash returns.

- LP cash MOIC: 0.06x
- LP economic MOIC: 2.00x
- LP cash IRR: -52.2%
- LP economic IRR: 15.1%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $628,554
- Total cash reinvested into HF: $1,571,386
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__slow_grind__hurdle_1_50x

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 1.50x
- LP economic MOIC: 1.50x
- LP cash IRR: 3.9%
- LP economic IRR: 3.9%
- Years until LP 2x cash return: 11
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 11
- Trigger HF liquidation used: $6,739,594
- Trigger refi used: $4,279,454
- Total cash distributed to LP: $15,000,000
- Total cash reinvested into HF: $3,480,952
- GP residual NAV: $8,535,759
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_hurdle_sensitivity__slow_grind__hurdle_1_75x

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 1.75x
- LP economic MOIC: 1.75x
- LP cash IRR: 5.0%
- LP economic IRR: 5.0%
- Years until LP 2x cash return: 12
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 12
- Trigger HF liquidation used: $7,974,701
- Trigger refi used: $5,155,596
- Total cash distributed to LP: $17,500,000
- Total cash reinvested into HF: $3,869,703
- GP residual NAV: $8,282,693
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_hurdle_sensitivity__slow_grind__hurdle_2_00x

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.7%
- LP economic IRR: 5.7%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $10,908,390
- Trigger refi used: $4,319,190
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,272,420
- GP residual NAV: $10,312,596
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_50x

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 1.50x
- LP economic MOIC: 1.50x
- LP cash IRR: 7.2%
- LP economic IRR: 7.2%
- Years until LP 2x cash return: 6
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 6
- Trigger HF liquidation used: $7,349,508
- Trigger refi used: $4,316,690
- Total cash distributed to LP: $15,000,000
- Total cash reinvested into HF: $2,833,802
- GP residual NAV: $11,621,578
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_75x

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 1.75x
- LP economic MOIC: 1.75x
- LP cash IRR: 8.6%
- LP economic IRR: 8.6%
- Years until LP 2x cash return: 7
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 7
- Trigger HF liquidation used: $8,608,748
- Trigger refi used: $4,858,398
- Total cash distributed to LP: $17,500,000
- Total cash reinvested into HF: $3,532,854
- GP residual NAV: $12,578,691
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_2_00x

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $11,608,931
- Trigger refi used: $3,571,903
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,319,166
- GP residual NAV: $16,030,648
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_25

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.12x
- LP economic MOIC: 2.00x
- LP cash IRR: -30.8%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,233,037
- Total cash reinvested into HF: $3,082,592
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_40

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.12x
- LP economic MOIC: 2.00x
- LP cash IRR: -30.8%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,233,037
- Total cash reinvested into HF: $3,082,592
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_60

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 0.12x
- LP economic MOIC: 2.00x
- LP cash IRR: -30.8%
- LP economic IRR: 9.3%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,233,037
- Total cash reinvested into HF: $3,082,592
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__slow_grind__re_liquidity_25

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.7%
- LP economic IRR: 5.7%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $10,908,390
- Trigger refi used: $4,319,190
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,272,420
- GP residual NAV: $10,312,596
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__slow_grind__re_liquidity_40

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.7%
- LP economic IRR: 5.7%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $10,908,390
- Trigger refi used: $4,319,190
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,272,420
- GP residual NAV: $10,312,596
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__slow_grind__re_liquidity_60

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.7%
- LP economic IRR: 5.7%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $10,908,390
- Trigger refi used: $4,319,190
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,272,420
- GP residual NAV: $10,312,596
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_25

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.3%
- LP economic IRR: 8.3%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $9,438,415
- Trigger refi used: $6,153,820
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,907,765
- GP residual NAV: $12,619,222
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_40

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.3%
- LP economic IRR: 8.3%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $9,438,415
- Trigger refi used: $6,153,820
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,907,765
- GP residual NAV: $12,619,222
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_60

High real estate NAV growth with low refinance capacity; tests the gap between paper value and LP cash liquidity.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 8.3%
- LP economic IRR: 8.3%
- Years until LP 2x cash return: 9
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 9
- Trigger HF liquidation used: $9,438,415
- Trigger refi used: $6,153,820
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $3,907,765
- GP residual NAV: $12,619,222
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_25

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $11,608,931
- Trigger refi used: $3,571,903
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,319,166
- GP residual NAV: $16,030,648
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_40

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $11,608,931
- Trigger refi used: $3,571,903
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,319,166
- GP residual NAV: $16,030,648
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_60

Both sleeves perform strongly; tests the upper-end residual asset outcome after LP cash extinguishment.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.4%
- LP economic IRR: 9.4%
- Years until LP 2x cash return: 8
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 8
- Trigger HF liquidation used: $11,608,931
- Trigger refi used: $3,571,903
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,319,166
- GP residual NAV: $16,030,648
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### twenty_year_horizon__base_hit_everyone_happy__years_20

Moderate real estate and hedge fund performance baseline; tests whether ordinary cash routing can reach the LP cash hurdle.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 7.5%
- LP economic IRR: 7.5%
- Years until LP 2x cash return: 10
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 10
- Trigger HF liquidation used: $9,431,090
- Trigger refi used: $5,930,943
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,137,967
- GP residual NAV: $9,794,830
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### twenty_year_horizon__slow_grind__years_20

Slow real estate growth and uneven hedge fund returns; tests long-duration cash distribution drift.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.7%
- LP economic IRR: 5.7%
- Years until LP 2x cash return: 13
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 13
- Trigger HF liquidation used: $10,908,390
- Trigger refi used: $4,319,190
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $4,272,420
- GP residual NAV: $10,312,596
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### twenty_year_horizon__hedge_fund_failure_re_survival__years_20

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 4.8%
- LP economic IRR: 4.8%
- Years until LP 2x cash return: 16
- LP cashflow profile type: BACKEND_HEAVY
- Hurdle completion trigger executed: True
- Hurdle trigger year: 16
- Trigger HF liquidation used: $7,137,146
- Trigger refi used: $5,363,602
- Total cash distributed to LP: $20,000,000
- Total cash reinvested into HF: $6,999,252
- GP residual NAV: $9,633,744
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_COMPLETION_TRIGGER_EXECUTED; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_REDEEMED_VIA_HF_LIQUIDATION; LP_REDEEMED_VIA_REFI

### twenty_year_horizon__failure_never_reaches_hurdle__years_20

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.13x
- LP economic MOIC: 2.00x
- LP cash IRR: -14.8%
- LP economic IRR: 3.7%
- Years until LP 2x cash return: not reached
- LP cashflow profile type: MODERATE_YIELD
- Hurdle completion trigger executed: False
- Hurdle trigger year: not triggered
- Trigger HF liquidation used: $0
- Trigger refi used: $0
- Total cash distributed to LP: $1,318,718
- Total cash reinvested into HF: $3,296,795
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HURDLE_TRIGGER_ATTEMPTED_BUT_INSUFFICIENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV
