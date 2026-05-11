# Scenario Report

Deterministic annual phase 2 model. Cash MOIC, economic MOIC, cash IRR, and economic IRR are reported separately.

## Summary

| scenario | years_modelled | lp_cash_moic | lp_economic_moic | lp_cash_irr | lp_economic_irr | lp_hurdle_achieved | gp_survivability_risk | gp_residual_nav | primary_flag |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| base_hit_everyone_happy | 8 | 0.62 | 2.00 | -0.09 | 0.11 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| fast_success_crypto_bull | 5 | 0.31 | 1.95 | -0.29 | 0.15 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| slow_grind | 15 | 1.02 | 2.00 | 0.00 | 0.06 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| hedge_fund_failure_re_survival | 12 | 0.95 | 2.00 | -0.01 | 0.08 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| real_estate_distress_crypto_success | 8 | 0.25 | 1.38 | -0.24 | 0.05 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |
| exceptional_dynasty_outcome | 9 | 2.00 | 2.00 | 0.10 | 0.10 | True | True | 14,734,964.86 | LP_HURDLE_ACHIEVED |
| liquidity_trap | 10 | 0.92 | 2.00 | -0.01 | 0.09 | False | True | 0.00 | HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED |
| failure_never_reaches_hurdle | 12 | 0.41 | 1.27 | -0.12 | 0.02 | False | True | 0.00 | LP_HURDLE_NOT_ACHIEVED |

## Scenario Notes

### base_hit_everyone_happy

LP reaches 2.0x in a reasonable period; GP retains meaningful residual assets.

- LP cash MOIC: 0.62x
- LP economic MOIC: 2.00x
- LP cash IRR: -9.1%
- LP economic IRR: 10.7%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### fast_success_crypto_bull

Crypto sleeve accelerates LP 2.0x outcome quickly; tests GP convexity and fairness optics.

- LP cash MOIC: 0.31x
- LP economic MOIC: 1.95x
- LP cash IRR: -28.7%
- LP economic IRR: 15.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### slow_grind

Moderate real estate performance and weak crypto; LP eventually does okay but time horizon drifts.

- LP cash MOIC: 1.02x
- LP economic MOIC: 2.00x
- LP cash IRR: 0.3%
- LP economic IRR: 6.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK

### hedge_fund_failure_re_survival

Hedge fund sleeve suffers major impairment, while real estate survives and cash-flows.

- LP cash MOIC: 0.95x
- LP economic MOIC: 2.00x
- LP cash IRR: -0.7%
- LP economic IRR: 7.9%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### real_estate_distress_crypto_success

Real estate underperforms but crypto performs strongly enough to protect LP outcome.

- LP cash MOIC: 0.25x
- LP economic MOIC: 1.38x
- LP cash IRR: -24.1%
- LP economic IRR: 4.5%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; RE_NAV_IMPAIRMENT; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### exceptional_dynasty_outcome

Both sleeves perform strongly; LP receives excellent return and GP retains very large residual value.

- LP cash MOIC: 2.00x
- LP economic MOIC: 2.00x
- LP cash IRR: 10.4%
- LP economic IRR: 10.4%
- GP residual NAV: $14,734,965
- GP survivability risk: True
- Key flags: LP_HURDLE_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN

### liquidity_trap

Economic hurdle is reached on NAV, but liquid resources are insufficient to redeem LPs.

- LP cash MOIC: 0.92x
- LP economic MOIC: 2.00x
- LP cash IRR: -1.3%
- LP economic IRR: 9.1%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; HURDLE_REACHED_BUT_LIQUIDITY_CONSTRAINED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV

### failure_never_reaches_hurdle

Both sleeves disappoint; LP never reaches 2.0x.

- LP cash MOIC: 0.41x
- LP economic MOIC: 1.27x
- LP cash IRR: -11.7%
- LP economic IRR: 2.4%
- GP residual NAV: $0
- GP survivability risk: True
- Key flags: LP_HURDLE_NOT_ACHIEVED; SLOW_TIME_HORIZON_DRIFT; GP_SURVIVABILITY_RISK; HF_MAJOR_DRAWDOWN; LP_STILL_BELOW_1X_CASH_MOIC_AT_END; LP_EXPERIENCE_WEAK_DESPITE_POSITIVE_NAV
