# Scenario Report

Deterministic annual phase 2 model. Cash MOIC, economic MOIC, cash IRR, and economic IRR are reported separately.

## Summary

| scenario | years_modelled | lp_cash_moic | lp_economic_moic | lp_cash_irr | lp_economic_irr | lp_hurdle_achieved | gp_survivability_risk | gp_residual_nav | primary_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_20 | 8 | 0.54 | 2.00 | -0.11 | 0.10 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_30 | 8 | 0.47 | 2.00 | -0.13 | 0.10 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_allocation_sensitivity__base_hit_everyone_happy__hf_40 | 8 | 0.40 | 2.00 | -0.16 | 0.10 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_20 | 5 | 0.28 | 2.00 | -0.31 | 0.16 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_30 | 4 | 2.00 | 2.00 | 0.20 | 0.20 | True | True | 6,698,925.27 | FAST_GP_DYNASTY_OUTCOME |
| hf_allocation_sensitivity__fast_success_crypto_bull__hf_40 | 2 | 2.00 | 2.00 | 0.42 | 0.42 | True | True | 5,087,586.50 | FAST_GP_DYNASTY_OUTCOME |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_20 | 7 | 2.00 | 2.00 | 0.12 | 0.12 | True | True | 11,310,127.05 | LP_GOOD_IRR_GP_LARGE_RESIDUAL |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_30 | 5 | 2.00 | 2.00 | 0.16 | 0.16 | True | True | 7,965,646.99 | LP_HURDLE_ACHIEVED |
| hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_40 | 4 | 2.00 | 2.00 | 0.20 | 0.20 | True | True | 6,978,866.69 | FAST_GP_DYNASTY_OUTCOME |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_25 | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_50 | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_harvest_sensitivity__base_hit_everyone_happy__harvest_75 | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_25 | 5 | 0.31 | 1.88 | -0.29 | 0.15 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_50 | 5 | 0.31 | 1.82 | -0.29 | 0.14 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| hf_harvest_sensitivity__fast_success_crypto_bull__harvest_75 | 5 | 0.31 | 1.76 | -0.29 | 0.13 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_25 | 9 | 2.00 | 2.00 | 0.10 | 0.10 | True | True | 13,534,671.97 | LP_HURDLE_ACHIEVED |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_50 | 10 | 2.00 | 2.00 | 0.10 | 0.10 | True | True | 16,150,046.13 | LP_HURDLE_ACHIEVED |
| hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_75 | 10 | 2.00 | 2.00 | 0.10 | 0.10 | True | True | 15,298,044.11 | LP_HURDLE_ACHIEVED |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_50x | 8 | 0.62 | 1.50 | -0.09 | 0.06 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_75x | 8 | 0.62 | 1.75 | -0.09 | 0.09 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_2_00x | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_50x | 5 | 0.31 | 1.50 | -0.29 | 0.09 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_75x | 5 | 0.31 | 1.75 | -0.29 | 0.13 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_2_00x | 5 | 0.31 | 1.95 | -0.29 | 0.15 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| lp_hurdle_sensitivity__slow_grind__hurdle_1_50x | 15 | 1.50 | 1.50 | 0.04 | 0.04 | True | True | 8,705,133.79 | LP_HURDLE_ACHIEVED |
| lp_hurdle_sensitivity__slow_grind__hurdle_1_75x | 15 | 1.02 | 1.75 | 0.00 | 0.05 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__slow_grind__hurdle_2_00x | 15 | 1.02 | 2.00 | 0.00 | 0.06 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_50x | 7 | 1.50 | 1.50 | 0.07 | 0.07 | True | True | 12,994,213.19 | LP_HURDLE_ACHIEVED |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_75x | 8 | 1.75 | 1.75 | 0.09 | 0.09 | True | True | 13,701,117.03 | LP_HURDLE_ACHIEVED |
| lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_2_00x | 9 | 2.00 | 2.00 | 0.10 | 0.10 | True | True | 14,734,964.86 | LP_HURDLE_ACHIEVED |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_25 | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_40 | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_60 | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__slow_grind__re_liquidity_25 | 15 | 1.02 | 2.00 | 0.00 | 0.06 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__slow_grind__re_liquidity_40 | 15 | 1.02 | 2.00 | 0.00 | 0.06 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__slow_grind__re_liquidity_60 | 15 | 1.02 | 2.00 | 0.00 | 0.06 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_25 | 10 | 0.92 | 2.00 | -0.01 | 0.09 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_40 | 10 | 0.92 | 2.00 | -0.01 | 0.09 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| re_liquidity_sensitivity__liquidity_trap__re_liquidity_60 | 10 | 2.00 | 2.00 | 0.09 | 0.09 | True | True | 8,149,584.53 | LP_HURDLE_ACHIEVED |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_25 | 9 | 2.00 | 2.00 | 0.10 | 0.10 | True | True | 14,734,964.86 | LP_HURDLE_ACHIEVED |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_40 | 8 | 2.00 | 2.00 | 0.11 | 0.11 | True | True | 11,201,117.03 | LP_HURDLE_ACHIEVED |
| re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_60 | 7 | 2.00 | 2.00 | 0.12 | 0.12 | True | True | 7,994,213.19 | LP_HURDLE_ACHIEVED |
| twenty_year_horizon__base_hit_everyone_happy__years_20 | 14 | 2.00 | 2.00 | 0.07 | 0.07 | True | True | 11,736,595.63 | LP_HURDLE_ACHIEVED |
| twenty_year_horizon__slow_grind__years_20 | 20 | 2.00 | 2.00 | 0.06 | 0.06 | True | True | 9,947,853.53 | LP_HURDLE_ACHIEVED |
| twenty_year_horizon__hedge_fund_failure_re_survival__years_20 | 18 | 2.00 | 2.00 | 0.07 | 0.07 | True | True | 10,786,927.42 | LP_HURDLE_ACHIEVED |
| twenty_year_horizon__failure_never_reaches_hurdle__years_20 | 20 | 0.66 | 1.47 | -0.04 | 0.03 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |

## Scenario Notes

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_20

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.54x
- LP economic MOIC: 2.00x
- LP cash IRR: -11.2%
- LP economic IRR: 10.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_30

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.47x
- LP economic MOIC: 2.00x
- LP cash IRR: -13.5%
- LP economic IRR: 10.3%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_allocation_sensitivity__base_hit_everyone_happy__hf_40

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.40x
- LP economic MOIC: 2.00x
- LP cash IRR: -16.0%
- LP economic IRR: 10.1%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_20

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.28x
- LP economic MOIC: 2.00x
- LP cash IRR: -31.0%
- LP economic IRR: 16.0%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_30

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 19.8%
- LP economic IRR: 19.8%
- GP residual NAV: $6,698,925
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; FAST_GP_DYNASTY_OUTCOME; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_allocation_sensitivity__fast_success_crypto_bull__hf_40

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 42.0%
- LP economic IRR: 42.0%
- GP residual NAV: $5,087,586
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; FAST_GP_DYNASTY_OUTCOME; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_20

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 12.2%
- LP economic IRR: 12.2%
- GP residual NAV: $11,310,127
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN; LP_GOOD_IRR_GP_LARGE_RESIDUAL

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_30

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 16.1%
- LP economic IRR: 16.1%
- GP residual NAV: $7,965,647
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_allocation_sensitivity__exceptional_dynasty_outcome__hf_40

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 19.9%
- LP economic IRR: 19.9%
- GP residual NAV: $6,978,867
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; FAST_GP_DYNASTY_OUTCOME; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_25

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_50

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__base_hit_everyone_happy__harvest_75

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_25

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.31x
- LP economic MOIC: 1.88x
- LP cash IRR: -28.7%
- LP economic IRR: 14.6%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_50

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.31x
- LP economic MOIC: 1.82x
- LP cash IRR: -28.7%
- LP economic IRR: 13.8%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__fast_success_crypto_bull__harvest_75

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.31x
- LP economic MOIC: 1.76x
- LP cash IRR: -28.7%
- LP economic IRR: 13.1%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_25

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.4%
- LP economic IRR: 10.4%
- GP residual NAV: $13,534,672
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_50

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.8%
- LP economic IRR: 9.8%
- GP residual NAV: $16,150,046
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### hf_harvest_sensitivity__exceptional_dynasty_outcome__harvest_75

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.8%
- LP economic IRR: 9.8%
- GP residual NAV: $15,298,044
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_50x

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 1.50x
- LP cash IRR: -9.1%
- LP economic IRR: 6.4%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_1_75x

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 1.75x
- LP cash IRR: -9.1%
- LP economic IRR: 8.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__base_hit_everyone_happy__hurdle_2_00x

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_50x

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.31x
- LP economic MOIC: 1.50x
- LP cash IRR: -28.7%
- LP economic IRR: 9.3%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_1_75x

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.31x
- LP economic MOIC: 1.75x
- LP cash IRR: -28.7%
- LP economic IRR: 12.9%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__fast_success_crypto_bull__hurdle_2_00x

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.31x
- LP economic MOIC: 1.95x
- LP cash IRR: -28.7%
- LP economic IRR: 15.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### lp_hurdle_sensitivity__slow_grind__hurdle_1_50x

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 1.50x
- LP economic MOIC: 1.50x
- LP cash IRR: 4.0%
- LP economic IRR: 4.0%
- GP residual NAV: $8,705,134
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### lp_hurdle_sensitivity__slow_grind__hurdle_1_75x

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 1.02x
- LP economic MOIC: 1.75x
- LP cash IRR: 0.3%
- LP economic IRR: 5.4%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK

### lp_hurdle_sensitivity__slow_grind__hurdle_2_00x

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 1.02x
- LP economic MOIC: 2.00x
- LP cash IRR: 0.3%
- LP economic IRR: 6.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_50x

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 1.50x
- LP economic MOIC: 1.50x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- GP residual NAV: $12,994,213
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_1_75x

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 1.75x
- LP economic MOIC: 1.75x
- LP cash IRR: 9.2%
- LP economic IRR: 9.2%
- GP residual NAV: $13,701,117
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### lp_hurdle_sensitivity__exceptional_dynasty_outcome__hurdle_2_00x

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.4%
- LP economic IRR: 10.4%
- GP residual NAV: $14,734,965
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_25

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_40

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__base_hit_everyone_happy__re_liquidity_60

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__slow_grind__re_liquidity_25

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 1.02x
- LP economic MOIC: 2.00x
- LP cash IRR: 0.3%
- LP economic IRR: 6.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK

### re_liquidity_sensitivity__slow_grind__re_liquidity_40

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 1.02x
- LP economic MOIC: 2.00x
- LP cash IRR: 0.3%
- LP economic IRR: 6.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK

### re_liquidity_sensitivity__slow_grind__re_liquidity_60

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 1.02x
- LP economic MOIC: 2.00x
- LP cash IRR: 0.3%
- LP economic IRR: 6.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_25

Economic hurdle is reached on NAV, but liquid resources are insufficient to redeem LPs.

- LP cash MOIC: 0.92x
- LP economic MOIC: 2.00x
- LP cash IRR: -1.3%
- LP economic IRR: 9.1%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_40

Economic hurdle is reached on NAV, but liquid resources are insufficient to redeem LPs.

- LP cash MOIC: 0.92x
- LP economic MOIC: 2.00x
- LP cash IRR: -1.3%
- LP economic IRR: 9.1%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### re_liquidity_sensitivity__liquidity_trap__re_liquidity_60

Economic hurdle is reached on NAV, but liquid resources are insufficient to redeem LPs.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 9.1%
- LP economic IRR: 9.1%
- GP residual NAV: $8,149,585
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_25

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.4%
- LP economic IRR: 10.4%
- GP residual NAV: $14,734,965
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_40

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 11.3%
- LP economic IRR: 11.3%
- GP residual NAV: $11,201,117
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### re_liquidity_sensitivity__exceptional_dynasty_outcome__re_liquidity_60

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 12.4%
- LP economic IRR: 12.4%
- GP residual NAV: $7,994,213
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### twenty_year_horizon__base_hit_everyone_happy__years_20

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 7.4%
- LP economic IRR: 7.4%
- GP residual NAV: $11,736,596
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### twenty_year_horizon__slow_grind__years_20

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 5.6%
- LP economic IRR: 5.6%
- GP residual NAV: $9,947,854
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### twenty_year_horizon__hedge_fund_failure_re_survival__years_20

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 6.5%
- LP economic IRR: 6.5%
- GP residual NAV: $10,786,927
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### twenty_year_horizon__failure_never_reaches_hurdle__years_20

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.66x
- LP economic MOIC: 1.47x
- LP cash IRR: -3.8%
- LP economic IRR: 2.6%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV
