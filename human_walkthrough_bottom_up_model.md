# Human Walkthrough: Hybrid Fund Model With Bottom-Up Real Estate Deals

## 1. What This Project Is

This project is a deterministic annual economic model for a hybrid investment fund.

It models a fund that can hold:

- Real estate assets
- A hedge fund / liquid investment sleeve
- A reserve / cash-like sleeve
- Retained cash
- Refinance proceeds and refinance liabilities

The model tracks how cash and value move through the fund over time, then tests whether LP investors receive their required cash return before GP receives residual economics.

The central LP target in the current model is a cash MOIC hurdle, for example:

```text
LPs must receive 2.0x their original capital in actual cash distributions.
```

The model distinguishes between:

- Cash paid to LPs
- Paper NAV / unrealized asset value
- Liquidity that could be generated from reserves, hedge fund liquidation, real estate refi, or partial real estate sale

That distinction matters because a deal can look valuable on paper but still fail to generate enough actual cash to pay LPs.

## 2. The Big Picture

The model now supports two real estate modes:

```text
top_down
bottom_up
```

### Top-Down Mode

Top-down mode is the original model.

It starts with LP capital and allocates percentages into:

```text
real estate
hedge fund
reserve
```

Then real estate is modelled using broad scenario assumptions:

```yaml
initial_noi_yield
annual_noi_growth
annual_nav_appreciation
gross_rent_yield
```

This is useful for abstract strategy testing.

### Bottom-Up Mode

Bottom-up mode models specific real estate deals.

Instead of saying:

```text
85% of LP capital goes into real estate
```

you can now say:

```text
This specific deal has:
- $23m gross asset value
- $16m assumed debt
- $2m new equity required
- current NOI
- stabilized NOI
- capex
- debt service
- refinance assumptions
```

The deal model calculates annual asset economics. The fund model then decides how those economics flow through the fund.

## 3. The Three Layers

The model is intentionally split into three layers.

```text
Deal model       = asset economics
Fund model       = cash routing, HF, reserve, retained cash, liquidity
Waterfall model  = LP/GP economics
```

### Deal Model

The deal model answers:

- What is the asset worth?
- What debt is attached?
- What liabilities are assumed?
- What is NOI?
- What is debt service?
- What capex is needed?
- What is free cashflow after debt and capex?
- What refinance proceeds are available?
- What is deal NAV?

The deal model does not decide whether LPs get paid.

### Fund Model

The fund model answers:

- How is LP capital initially deployed?
- How much capital remains in reserve or hedge fund?
- What happens to positive real estate cashflow?
- What happens if real estate cashflow is negative?
- Are refinance proceeds retained, reserved, or available as liquidity?
- Can the fund afford future acquisitions?

### Waterfall Model

The waterfall answers:

- How much cash have LPs received?
- Has the LP cash hurdle been met?
- Is there enough liquidity to redeem LPs?
- What residual NAV remains for GP after LPs are extinguished?

## 4. Important Files

### Inputs

```text
inputs/model_config.yaml
inputs/scenarios.yaml
inputs/deals.yaml
```

### Core Code

```text
src/model_types.py
src/deal_types.py
src/deal_model.py
src/portfolio_aggregator.py
src/engine.py
src/waterfall.py
```

### Outputs

```text
outputs/scenario_summary.csv
outputs/scenario_cashflows.csv
outputs/deal_cashflows.csv
outputs/scenario_summary.xlsx
outputs/scenario_report.md
outputs/chatgpt_model_context.md
```

## 5. How To Run The Model

From PowerShell:

```powershell
cd C:\Users\water\HAC\github\hybrid-fund\hybrid_econ_model
..\.venv\Scripts\python.exe run_model.py
```

Expected output:

```text
Ran 8 scenarios.
Outputs written to outputs/
ChatGPT context written to outputs/chatgpt_model_context.md
```

To run tests:

```powershell
..\.venv\Scripts\python.exe -m pytest
```

Current expected result:

```text
87 passed
```

## 6. How Top-Down Mode Works

Top-down mode is controlled in `inputs/model_config.yaml`:

```yaml
real_estate:
  mode: "top_down"
```

In this mode, deals are ignored.

A scenario in `inputs/scenarios.yaml` provides real estate assumptions like:

```yaml
real_estate:
  initial_noi_yield: 0.075
  annual_noi_growth: 0.025
  annual_nav_appreciation: 0.04
  gross_rent_yield: 0.12
```

The engine starts with the configured allocation:

```yaml
allocation:
  hedge_fund_allocation_pct: 0.10
  real_estate_allocation_pct: 0.85
  reserve_allocation_pct: 0.05
```

If initial LP capital is `$10m`, this means:

```text
Real estate: $8.5m
Hedge fund:  $1.0m
Reserve:     $0.5m
```

Then each year:

```text
RE NOI = opening RE NAV * NOI yield
Gross rent = opening RE NAV * gross rent yield
RE NAV grows by annual appreciation
```

## 7. How Bottom-Up Mode Works

Bottom-up mode can be enabled globally in `inputs/model_config.yaml`, but the better approach is to enable it per scenario:

```yaml
real_estate_model:
  mode: "bottom_up"
```

Bottom-up real estate assumptions come from:

```text
inputs/deals.yaml
```

The sample deal is:

```yaml
deals:
  jon_deal_1:
    enabled: true
    acquisition_year: 1

    acquisition:
      asset_value: 23000000
      new_equity_required: 2000000

    capital_stack:
      assumed_debt: 16000000
      assumed_liabilities: 0

    operations:
      current_noi: 1200000
      stabilized_noi: 1800000
      years_to_stabilization: 3

    debt:
      interest_rate: 0.065
      amortization_type: "interest_only"
```

This lets the model represent the question:

```text
Can $2m of new equity control $23m of real estate with $16m of assumed debt?
```

## 8. What A Deal Calculates

For each active deal and year, the model calculates:

```text
asset_value
debt_balance
assumed_liabilities
NOI
gross_rent
debt_service
capex
free_cashflow_after_debt_and_capex
DSCR
refi_capacity
refi_proceeds
deal_nav
entry_equity_cushion
value_to_new_equity_multiple
```

### Example: Year-1 NAV

If:

```text
Asset value:       $23m
Assumed debt:      $16m
Liabilities:       $0
Seller note:       $0
Preferred equity:  $0
```

Then:

```text
Deal NAV before refi liability = $23m - $16m = $7m
```

If the deal requires `$2m` of new equity:

```text
Value-to-new-equity multiple = $7m / $2m = 3.5x
```

That does not mean LPs have received cash. It means the model is accepting the gross asset value and debt assumptions as economic NAV.

## 9. Deal NAV Before And After Refi Liability

The model now reports both:

```text
deal_nav_before_refi_liability
deal_nav_after_refi_liability
```

This matters because refinancing creates cash but also creates liability.

Current convention:

```text
deal_nav
```

is kept as a backward-compatible alias for:

```text
deal_nav_before_refi_liability
```

For interpretation, use the explicit fields.

## 10. Refinance Logic

The model tracks refinance capacity statefully by deal.

This prevents the same asset from repeatedly cashing out against the same equity cushion in years 5, 7, and 10.

Formula:

```text
max_debt_supported = asset_value * refi_ltv
cash_out_before_refi_costs = max_debt_supported - debt_balance - prior_refi_liability
refi_costs = max(cash_out_before_refi_costs, 0) * refi_costs_pct
refi_capacity = max(0, cash_out_before_refi_costs - refi_costs)
```

If proceeds are taken:

```text
ending_refi_liability = prior_refi_liability + refi_proceeds
```

That ending liability becomes the prior liability in the next year.

Refi proceeds do not directly reduce asset value. At the fund level, they increase cash or reserve and increase refinance liability.

## 11. Future Acquisition Funding

Future acquisitions are not allowed to magically become active.

If a deal has:

```yaml
acquisition_year: 3
new_equity_required: 1500000
```

then in year 3 the fund engine checks whether the fund has enough retained cash and reserve to fund it.

Funding order:

```text
1. retained cash
2. reserve
```

Year-1 deals are special. Their equity is funded from initial LP capital and recorded as:

```text
acquisition_funding_source = initial_lp_capital
```

### If A Future Deal Is Fully Funded

The deal becomes active and starts contributing:

- asset value
- NOI
- NAV
- refi capacity
- cashflow

### If A Future Deal Is Not Fully Funded

Default behavior:

```yaml
failed_acquisition_funding_treatment: "do_not_fund"
```

That means:

- retained cash stays unchanged
- reserve stays unchanged
- deal remains inactive
- shortfall is recorded
- no asset value, NOI, NAV, refi capacity, or cashflow is counted

Alternative stress behavior:

```yaml
failed_acquisition_funding_treatment: "partial_loss"
failed_acquisition_loss_pct: 0.10
```

This can model sunk diligence costs or a lost deposit.

## 12. Scenario Overrides

You do not need to copy a full deal to test downside or upside cases.

Use `deal_overrides` in `inputs/scenarios.yaml`.

Example:

```yaml
scenarios:
  jon_downside_case:
    description: "Downside underwriting case for Jon Deal 1."
    years: 10

    real_estate_model:
      mode: "bottom_up"

    deal_overrides:
      jon_deal_1:
        operations:
          current_noi: 900000
          stabilized_noi: 1500000
        valuation:
          annual_value_growth: 0.01
        refinance:
          refi_ltv: 0.60
          target_years: [7, 10]

    real_estate:
      initial_noi_yield: 0.07
      annual_noi_growth: 0.02
      annual_nav_appreciation: 0.03
      gross_rent_yield: 0.11

    hedge_fund:
      annual_returns: [0.05, -0.05, 0.08, 0.03, 0.06, 0.04, 0.08, 0.05, 0.07, 0.04]
```

The model deep-merges the override into the base deal.

This means changing:

```yaml
operations:
  current_noi: 900000
```

does not erase other `operations` fields.

## 13. Recommended Jon/Asher Scenarios

Once real underwriting is available, create:

```text
jon_base_case
jon_downside_case
jon_upside_case
```

Use the same `jon_deal_1` deal in `inputs/deals.yaml`.

Then use scenario-level `deal_overrides` to vary:

- current NOI
- stabilized NOI
- capex
- liabilities
- refi LTV
- valuation growth
- exit cap rate
- debt service
- future acquisition assumptions if applicable

## 14. What Questions The Model Answers

The model is now designed to test:

```text
Can $2m actually control the $23m asset base?
```

```text
What liabilities, capex, or seller claims are missing?
```

```text
What is true current NOI versus stabilized NOI?
```

```text
Can refinance realistically generate LP liquidity?
```

```text
Does the LP 2.0x cash hurdle get paid from actual liquidity or only from paper NAV?
```

```text
What residual asset value remains for GP after LPs are extinguished?
```

```text
What happens if a future acquisition cannot be funded?
```

## 15. How To Read The Outputs

### Start With `deal_cashflows.csv`

Use:

```text
outputs/deal_cashflows.csv
```

This is the best file for checking asset-level economics.

Important columns:

```text
deal_name
year
active
asset_value
debt_balance
assumed_liabilities
noi
debt_service
capex
free_cashflow_after_debt_and_capex
dscr
prior_refi_liability
refi_capacity
refi_proceeds
ending_refi_liability
deal_nav_before_refi_liability
deal_nav_after_refi_liability
entry_equity_cushion
value_to_new_equity_multiple
```

Use this file to ask:

```text
Does the property-level deal make sense before fund mechanics?
```

### Then Read `scenario_cashflows.csv`

Use:

```text
outputs/scenario_cashflows.csv
```

This shows annual fund-level movement.

Important bottom-up columns:

```text
real_estate_mode
re_gross_asset_value
re_debt_balance
re_assumed_liabilities
re_noi
re_debt_service
re_capex
re_dscr
re_refi_capacity
re_refi_proceeds_from_deals
re_cashflow_shortfall
acquisition_new_deal_equity_required
acquisition_funded_from_retained_cash
acquisition_funded_from_reserve
acquisition_failed_loss
acquisition_unfunded_shortfall
retained_cash
reserve_closing_nav
refinance_liability
lp_distribution
lp_cumulative_distribution
fund_nav
event_flag
```

Use this file to ask:

```text
How does the deal affect the whole fund each year?
```

### Then Read `scenario_summary.csv`

Use:

```text
outputs/scenario_summary.csv
```

This is the best file for scenario comparison.

Important columns:

```text
scenario
real_estate_mode
lp_cash_moic
lp_economic_moic
lp_cash_irr
lp_hurdle_achieved
year_hurdle_achieved
final_fund_nav
final_refinance_liability
gp_residual_nav
total_deal_refi_proceeds
total_acquisition_unfunded_shortfall
primary_flag
all_flags
```

Use this file to ask:

```text
Which scenario works, which fails, and why?
```

## 16. Key Warnings

### Paper NAV Is Not Cash

The model can show strong economic value before LPs have received cash.

Always compare:

```text
lp_cash_moic
lp_economic_moic
```

If economic MOIC is high but cash MOIC is low, the deal may be valuable but illiquid.

### Refi Creates Liability

Refi proceeds are not free money.

They increase cash or reserve, but they also increase:

```text
refinance_liability
```

### Future Deals Must Be Funded

A future acquisition does not count unless the fund can fund the required equity.

If not, look for:

```text
ACQUISITION_FUNDING_SHORTFALL
```

in `event_flag`.

### Negative RE Cashflow Is Funded At Fund Level

If real estate cashflow is negative, the model funds the shortfall from:

```text
retained cash
reserve
```

If still unfunded, it records:

```text
re_cashflow_shortfall
```

## 17. Practical Workflow For A New Underwriting Case

1. Open `inputs/deals.yaml`.
2. Replace placeholder deal assumptions with real underwriting.
3. Open `inputs/scenarios.yaml`.
4. Add three scenarios:

```text
jon_base_case
jon_downside_case
jon_upside_case
```

5. Set each scenario to:

```yaml
real_estate_model:
  mode: "bottom_up"
```

6. Use `deal_overrides` to vary assumptions.
7. Run:

```powershell
..\.venv\Scripts\python.exe run_model.py
```

8. Review:

```text
outputs/deal_cashflows.csv
outputs/scenario_cashflows.csv
outputs/scenario_summary.csv
outputs/scenario_summary.xlsx
```

9. Ask:

```text
Is the deal good at the asset level?
Does the fund have enough liquidity?
Can LPs actually get paid 2.0x cash?
What remains for GP?
```

## 18. Current Limitations

The model still does not include:

- Tax modelling
- Monthly periods
- Tenant schedules
- Full amortizing debt
- Database storage
- Monte Carlo
- Streamlit UI updates for this bottom-up layer
- Escrow / retry queue for failed acquisitions
- Partial acquisition close mechanics

Those should only be added if real underwriting requires them.

