# Codex Prompt: Add Oak Cliff Bottom-Up Scenarios

You are working in the existing `hybrid_econ_model` repo.

The bottom-up real estate deal model now exists. Do not add new model features unless absolutely necessary. This task is primarily an **inputs/scenario build** using the existing bottom-up framework.

## Objective

Add Oak Cliff as the first real underwriting test case.

The goal is to create bottom-up scenarios that let us answer one practical question:

```text
Can Oak Cliff, as the real estate anchor asset, help the Gamma Fund get LPs to 2.0x actual cash within the target period?
```

Focus only on Oak Cliff. Do not model Amarillo or WTAMSH yet.

## Source Assumptions

Use the `Oak Cliff UW` tab from `Blue Lion Multifamily Underwriting.xlsx`.

Key assumptions from the Oak Cliff underwriting:

```text
Asset: Oak Cliff Multifamily
Units: 136
Year built: 1974
Location: South Dallas
Purchase price: $7,250,000
Loan-to-price / LTV: 70%
Loan amount: $5,075,000
Interest rate: 7.50%
Amortization: 30 years
Annual debt service from workbook: $429,706.52
Closing costs: 2.0% of purchase price = $145,000
Renovation budget: $1,836,000
Total equity required: $4,156,000
Hold period: 5 years
Rent growth: 3.0%
Other income growth: 3.0%
Expense inflation: 3.0%
Stabilized economic vacancy: 7.0%
Management fee: 3.5% of EGI
Replacement reserves: $250/unit/year = $34,000/year
Rent premium: $110/unit/month
Normalized in-place NOI: $701,409
Normalized going-in cap rate: 9.67%
Exit cap rate in independent case: 9.25%
Year-5 exit value in independent case: ~$11,043,575
Independent levered IRR: ~17.6%
Independent equity multiple: ~2.03x
Sponsor IRR: ~42.8%
Sponsor equity multiple: 3.00x
```

Important modelling note:

The current bottom-up model does **not** support amortizing debt balances. Do **not** add amortizing debt in this patch. Use:

```yaml
amortization_type: "fixed_annual_debt_service"
annual_debt_service: 429706.52
```

Accept that debt balance will remain at the original loan amount in the model. That is conservative versus the workbook, which amortizes the loan balance down to about `$4.79m` by exit.

## Hybrid Fund Context

The fund thesis says LPs receive 100% of distributions until they receive a 2.0x equity multiple, after which their fund interest is extinguished. The Gamma Fund thesis targets a 2.0x LP equity multiple over roughly a 5-year hold.

For scenario testing, we also want to see whether 2.0x is more realistic by year 7.

## Required Changes

### 1. Update `inputs/deals.yaml`

Add a new deal:

```yaml
oak_cliff:
  enabled: true
  acquisition_year: 1
  description: "Oak Cliff Multifamily base case from Blue Lion underwriting."

  acquisition:
    asset_value: 7250000
    value_type: "purchase_price"
    purchase_price: 7250000
    new_equity_required: 4156000
    closing_costs: 145000
    initial_capex_reserve: 1836000

  capital_stack:
    assumed_debt: 5075000
    assumed_liabilities: 0
    liabilities_written_down: 0
    seller_note: 0
    preferred_equity: 0

  operations:
    current_noi: 701409
    stabilized_noi: 991777
    years_to_stabilization: 5
    annual_noi_growth_after_stabilization: 0.03
    gross_rent: null
    gross_rent_growth: 0.03
    vacancy_rate: 0.07

  debt:
    interest_rate: 0.075
    maturity_year: 5
    amortization_type: "fixed_annual_debt_service"
    annual_debt_service: 429706.52
    amortization_years: null
    dscr_minimum: 1.25
    recourse: "unknown"

  capex:
    annual_capex:
      1: 800000
      2: 600000
      3: 300000
      4: 100000
      5: 36000
    recurring_capex_pct_of_noi: 0.0

  valuation:
    method: "growth"
    exit_cap_rate: null
    annual_value_growth: 0.110946
    stabilized_value: null

  refinance:
    enabled: false
    target_years: []
    refi_ltv: 0.70
    refi_costs_pct: 0.02
    max_cash_out_pct_of_value: null
    proceeds_use: "fund_liquidity"
```

Notes:

- `annual_value_growth: 0.110946` is calibrated so that `$7.25m` grows to approximately `$11.04m` by year 5, matching the independent underwriting exit value.
- The capex schedule is an approximation of the renovation budget and reserves. It intentionally front-loads renovation spend.
- Use `current_noi` and `stabilized_noi` based on the independent underwriting. The model will interpolate between them.
- Since the model applies capex separately, make sure the result roughly resembles the workbook’s J-curve. It does not need to match exactly.

If `inputs/deals.yaml` already contains old placeholder deals, leave them in place but make sure these new Oak Cliff scenarios activate only Oak Cliff. Either disable the old placeholders or use scenario-level `deal_overrides` to set them to `enabled: false`.

### 2. Update `inputs/model_config.yaml`

Use the existing model config, but make sure bottom-up allocation can produce a sensible HF/reserve split after funding Oak Cliff.

Assume global LP capital remains:

```yaml
model:
  initial_lp_capital: 10000000
```

Oak Cliff requires `$4.156m` of year-1 equity, leaving:

```text
Remaining capital = $10.000m - $4.156m = $5.844m
```

Target day-one HF allocation is approximately `$800k`.

Therefore set:

```yaml
bottom_up_allocation:
  remaining_capital_hf_pct: 0.1369
  remaining_capital_reserve_pct: 0.8631
  allow_overallocated_deals: false
  failed_acquisition_funding_treatment: "do_not_fund"
  failed_acquisition_loss_pct: 0.0
```

This gives approximately:

```text
HF NAV:      $800k
Reserve NAV: $5.044m
```

This is intentionally conservative because Oak Cliff alone does not deploy the full $10m raise into RE.

Do not set global `real_estate.mode` to `bottom_up`. Leave default mode as:

```yaml
real_estate:
  mode: "top_down"
```

Specific Oak Cliff scenarios should enable bottom-up mode at the scenario level.

### 3. Add Oak Cliff Scenarios to `inputs/scenarios.yaml`

Add three scenarios.

#### Scenario A: `oak_cliff_base_no_refi`

Purpose:

Test Oak Cliff without relying on refi proceeds.

```yaml
oak_cliff_base_no_refi:
  description: "Oak Cliff base case using independent underwriting, no deal-level refi."
  years: 7

  real_estate_model:
    mode: "bottom_up"

  deal_overrides:
    oak_cliff:
      enabled: true
      refinance:
        enabled: false
        target_years: []
    jon_deal_1:
      enabled: false

  real_estate:
    initial_noi_yield: 0.07
    annual_noi_growth: 0.03
    annual_nav_appreciation: 0.03
    gross_rent_yield: 0.11

  hedge_fund:
    annual_returns: [0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]

  cashflow_routing:
    enabled: true
    re_cashflow:
      lp_distribution_pct: 0.60
      hf_reinvestment_pct: 0.25
      reserve_pct: 0.15
    hf_harvest:
      lp_distribution_pct: 0.60
      hf_reinvestment_pct: 0.25
      reserve_pct: 0.15
```

#### Scenario B: `oak_cliff_base_year4_refi`

Purpose:

Test Jon’s refi concept: year-3 or year-4 refi returning roughly one-third to one-half of invested equity. Use year 4.

```yaml
oak_cliff_base_year4_refi:
  description: "Oak Cliff base case with year-4 refi using independent valuation ramp."
  years: 7

  real_estate_model:
    mode: "bottom_up"

  deal_overrides:
    oak_cliff:
      enabled: true
      refinance:
        enabled: true
        target_years: [4]
        refi_ltv: 0.70
        refi_costs_pct: 0.02
        proceeds_use: "fund_liquidity"
    jon_deal_1:
      enabled: false

  real_estate:
    initial_noi_yield: 0.07
    annual_noi_growth: 0.03
    annual_nav_appreciation: 0.03
    gross_rent_yield: 0.11

  hedge_fund:
    annual_returns: [0.13, 0.13, 0.13, 0.13, 0.13, 0.13, 0.13]

  cashflow_routing:
    enabled: true
    re_cashflow:
      lp_distribution_pct: 0.60
      hf_reinvestment_pct: 0.25
      reserve_pct: 0.15
    hf_harvest:
      lp_distribution_pct: 0.60
      hf_reinvestment_pct: 0.25
      reserve_pct: 0.15
```

Expected rough check:

By year 4, Oak Cliff value under the calibrated growth assumption should be roughly:

```text
$7.25m × (1 + 11.0946%) ^ 3 ≈ $9.94m
```

At 70% LTV:

```text
max debt supported ≈ $6.96m
less existing debt: $5.075m
gross cash-out before costs ≈ $1.89m
less 2% costs ≈ $38k
estimated refi proceeds ≈ $1.85m
```

This is approximately 44% of Oak Cliff equity required (`$1.85m / $4.156m`), which is within Jon’s one-third to one-half range.

#### Scenario C: `oak_cliff_downside_no_refi`

Purpose:

Test a conservative/downside case.

```yaml
oak_cliff_downside_no_refi:
  description: "Oak Cliff downside case with slower value growth, weaker HF returns, and no refi."
  years: 7

  real_estate_model:
    mode: "bottom_up"

  deal_overrides:
    oak_cliff:
      enabled: true
      operations:
        current_noi: 650000
        stabilized_noi: 900000
        years_to_stabilization: 5
        annual_noi_growth_after_stabilization: 0.02
      capex:
        annual_capex:
          1: 900000
          2: 700000
          3: 400000
          4: 150000
          5: 50000
        recurring_capex_pct_of_noi: 0.0
      valuation:
        method: "growth"
        annual_value_growth: 0.06
      refinance:
        enabled: false
        target_years: []
    jon_deal_1:
      enabled: false

  real_estate:
    initial_noi_yield: 0.07
    annual_noi_growth: 0.02
    annual_nav_appreciation: 0.02
    gross_rent_yield: 0.11

  hedge_fund:
    annual_returns: [-0.08, -0.07, 0.00, 0.06, 0.08, 0.08, 0.08]

  cashflow_routing:
    enabled: true
    re_cashflow:
      lp_distribution_pct: 0.60
      hf_reinvestment_pct: 0.25
      reserve_pct: 0.15
    hf_harvest:
      lp_distribution_pct: 0.60
      hf_reinvestment_pct: 0.25
      reserve_pct: 0.15
```

### Important Robustness Requirement

The old placeholder deal may be called `jon_deal_1`, but do not assume that name exists. If it exists, disable it in the Oak scenarios. If it does not exist, do not create invalid overrides for unknown deals.

Implement this robustly:

- If `jon_deal_1` exists in `inputs/deals.yaml`, disable it in the scenario overrides or set it `enabled: false` globally.
- If there are other enabled placeholder deals, disable them too for the Oak Cliff scenarios.
- The Oak Cliff scenarios should include **only Oak Cliff** as active real estate.

If scenario-level overrides do not tolerate unknown deal names, avoid adding overrides for deals that are not present.

## 4. Output Review Requirements

After adding the scenarios, run:

```bash
pytest
python run_model.py
```

Then inspect the generated outputs.

Report the following for each Oak Cliff scenario:

```text
scenario
years_modelled
lp_cash_moic
lp_economic_moic
lp_cash_irr
lp_hurdle_achieved
year_hurdle_achieved
final_fund_nav
final_refinance_liability
gp_residual_nav
total_deal_refi_proceeds
total_re_cashflow_generated
total_distributed_to_lp
total_reinvested_into_hf
total_added_to_reserve
primary_flag
all_flags
```

Also inspect `outputs/deal_cashflows.csv` for Oak Cliff and report:

```text
year
asset_value
debt_balance
deal_nav_before_refi_liability
deal_nav_after_refi_liability
noi
debt_service
capex
free_cashflow_after_debt_and_capex
dscr
refi_capacity
refi_proceeds
ending_refi_liability
```

## 5. Manual Sanity Checks

Add or perform these checks manually:

### Base no-refi

Expected:

- Oak Cliff should not magically get LPs to 2.0x cash by itself.
- LP cash MOIC should be materially below 2.0x unless the backend trigger monetizes reserve/HF/RE.
- Deal-level economics should look positive, but fund-level 2x cash may still be hard because only `$4.156m` of the `$10m` fund is deployed into Oak Cliff.

### Base year-4 refi

Expected:

- Year-4 refi proceeds should be roughly `$1.8m–$1.9m`, depending on exact model output.
- Refi proceeds should increase fund liquidity and `refinance_liability`.
- Refi should improve LP cash outcome but may still not get the whole `$10m` fund to 2.0x by year 5 or 7.

### Downside

Expected:

- No refi.
- Weaker HF returns.
- Lower valuation growth.
- LP 2.0x should almost certainly not be achieved.
- This is a failure / caution case, not a target case.

## 6. Do Not Do These Things

Do not add:

- Amarillo scenarios
- WTAMSH scenarios
- tax modelling
- amortizing debt support
- Streamlit UI changes
- Monte Carlo
- monthly periods
- new waterfall mechanics
- new legal/theory documentation

This patch is only about adding Oak Cliff bottom-up scenarios and reporting the outputs.

## 7. Deliverables

When finished, report:

1. files changed;
2. exact Oak Cliff assumptions added;
3. confirmation that only Oak Cliff is active in the Oak scenarios;
4. test result;
5. run result;
6. summary table of Oak scenario outcomes;
7. whether LPs hit 2.0x cash by year 5 or year 7;
8. whether year-4 refi materially changes the result;
9. any obvious model limitations discovered.
