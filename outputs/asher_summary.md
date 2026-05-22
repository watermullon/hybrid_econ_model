# Sensitivity Analysis - Executive Summary for Asher

This report evaluates the impact of liquidity engineering strategies on the fund structure.

## Outcomes by Redemption Timing
| Timing Bucket | count | gp_residual_nav | trigger_hf_pct | trigger_refi_pct |
| --- | --- | --- | --- | --- |
| Moderate (<8yr) | 52.00 | 8,925,454.97 | 0.80 | 0.10 |
| Not Reached | 488.00 | 0.00 | 0.00 | 0.00 |

## Key Observations
1. **Liquidity Mix:** Successful redemptions rely on a specific balance between HF liquidation and property refinancing.
2. **Success Rate:** Out of 540 permutations, 52 reached the 2.0x hurdle within the model horizon.

## Top 5 GP Value Scenarios (Successful Redemption)
| Index | hf_allocation | hf_harvest_rate | backend_strategy | refi_cap | hf_liquidation_cap | routing_policy | year_hurdle_achieved | gp_residual_nav |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 395 | 0.30 | 0.00 | No Refi | 0.00 | 1.00 | More Aggressive HF Compounding | 8.00 | 10,627,017.12 |
| 475 | 0.30 | 0.25 | No Refi | 0.00 | 1.00 | Very Backend Heavy | 8.00 | 10,613,283.36 |
| 535 | 0.30 | 0.50 | No Refi | 0.00 | 1.00 | Very Backend Heavy | 8.00 | 10,400,448.63 |
| 455 | 0.30 | 0.25 | No Refi | 0.00 | 1.00 | More Aggressive HF Compounding | 8.00 | 10,201,442.08 |
| 445 | 0.30 | 0.25 | Balanced Liquidity | 0.35 | 0.85 | More Aggressive HF Compounding | 8.00 | 10,201,442.08 |

---
Note: Detailed raw data is available in `sensitivity_analysis.csv` for further pivot analysis.