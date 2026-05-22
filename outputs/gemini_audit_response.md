# Gemini Audit Response

## Findings reviewed

| Finding | Validity | Action taken |
| --- | --- | --- |
| `cap_rate_sized` allocation is inverted or mislabeled | Not a code bug against the written project prompt. The prompt explicitly says `A_HF = LP capital x initial_noi_yield`, `A_RESERVE = LP capital x reserve_allocation_pct`, and `A_RE = LP capital - A_HF - A_RESERVE`. | No formula change. Added test coverage confirming the documented formula. |
| Configured refinance proceeds create cash without an offsetting liability | Valid. Prior prompts said not to reduce RE NAV, but the model also needs a liability so fund NAV is not overstated. | Added `refinance_liability`; fund NAV, economic hurdle tests, remaining LP claim, and GP residual NAV are now net of refinance liability. |
| Hurdle trigger refi creates cash without an offsetting liability | Valid. Same issue as configured refinance events. | Trigger refi now increases `refinance_liability`; gross RE NAV remains unchanged, but fund NAV and GP residual NAV are net of the liability. |
| LP terminal NAV claim may give LP first priority on residual NAV | Mostly intended. The LP has the first economic claim until the cash hurdle is met. GP fees already paid are tracked separately as GP economics. | No change. |
| Multiple distribution buckets create interaction risk | Valid risk area. One specific issue was possible: cash yield payments could be configured not to reduce the LP cash hurdle. | Added validation: enabled LP cash yield must reduce the LP cash hurdle because the hurdle is based on actual cash received. |
| GP survivability ignores co-investment | Valid limitation, not a bug in the current metric. The metric is explicitly fee survivability. | No change. Future enhancement candidate: GP liquidity/capital-at-risk analysis. |
| Dashboard test path issue | Not valid in this repo state. `streamlit.testing.v1.AppTest.from_file("dashboard/app.py")` passes locally. | No change. |
| NOI growth compounds yield on opening NAV, creating growth on growth | Intended per original prompt: `NOI_yield_t = initial_noi_yield x (1 + annual_noi_growth)^(t-1)` and `NOI_t = RE_NAV_open_t x NOI_yield_t`. | No change. |
| Floating point tolerances too small for dollar modelling | Reasonable style point, but no observed failure. | No broad change yet. Future cleanup candidate: centralize money tolerance. |

## Tests

After fixes:

- `pytest`: 67 passed
- `python run_model.py`: completed
- `python run_calibration.py`: completed

## Important modelling note

Refinance is now represented as:

- gross RE NAV remains visible and unchanged by the refi event,
- refinance proceeds create cash for LP distribution, retained cash, reserve, or trigger funding,
- refinance proceeds also create `refinance_liability`,
- fund NAV and GP residual NAV are net of `refinance_liability`.

This keeps the model audit-friendly while avoiding double-counting refinance proceeds as free value.
