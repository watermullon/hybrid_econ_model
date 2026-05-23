# Bottom-Up Real Estate Deal Modelling Report

## Overview

This update adds bottom-up real estate deal modelling to the existing deterministic annual hybrid fund model.

The prior model was top-down: initial LP capital was allocated into real estate, hedge fund, and reserve sleeves, then real estate was grown using scenario-level assumptions such as NOI yield, NOI growth, NAV appreciation, and gross rent yield.

That top-down mode still works and remains the default.

The new bottom-up mode allows the model to represent specific real estate transactions, including a structure where a relatively small amount of new equity controls a much larger asset base through assumed debt and other liabilities. The sample `inputs/deals.yaml` includes a placeholder transaction with:

- Gross asset value: `$23,000,000`
- New equity required: `$2,000,000`
- Assumed debt: `$16,000,000`
- Current NOI: `$1,200,000`
- Stabilized NOI: `$1,800,000`

The implementation is additive. It does not redesign the fund-level waterfall.

## Layering Principle

The model now keeps three layers cleanly separated:

```text
Deal model       = asset economics
Fund model       = cash routing, HF, reserve, retained cash, liquidity
Waterfall model  = LP/GP economics
```

The deal model does not decide LP distributions, GP residual ownership, or hurdle completion. It only produces real estate asset economics:

- Gross asset value
- Debt balance
- Assumed liabilities
- Net equity value
- NOI
- Gross rent
- Debt service
- Capex
- Free cashflow after debt service and capex
- DSCR
- Refinance capacity
- Refinance proceeds
- Deal NAV
- Entry equity cushion
- Value-to-new-equity multiple

The fund engine then uses those outputs for cash routing, reserve funding, hedge fund allocation, refinance liability, liquidity tests, and LP/GP waterfall calculations.

## Files Changed

### Core Model

- `src/model_types.py`
- `src/engine.py`
- `src/utils.py`
- `src/config_loader.py`
- `src/validation.py`

### New Bottom-Up Deal Layer

- `src/deal_types.py`
- `src/deal_model.py`
- `src/portfolio_aggregator.py`

### Outputs And Reporting

- `src/outputs.py`
- `src/reporting.py`
- `src/chatgpt_export.py`
- `src/calibration.py`

### Entry Points And Supporting Code

- `run_model.py`
- `run_calibration.py`
- `run_sensitivities.py`
- `dashboard/app.py`

### Inputs

- `inputs/model_config.yaml`
- `inputs/deals.yaml`

### Tests

- `tests/test_bottom_up_deals.py`
- `tests/test_calibration.py`
- `tests/test_economic_mechanics.py`
- `tests/test_engine_basic.py`
- `tests/test_error_handling.py`

### Generated Outputs

- `outputs/deal_cashflows.csv`
- `outputs/scenario_cashflows.csv`
- `outputs/scenario_summary.csv`
- `outputs/scenario_summary.xlsx`
- `outputs/chatgpt_model_context.md`

## Deep Merge Fix

The previous `merge_model()` helper in `src/utils.py` used shallow Pydantic updates.

That was risky for nested scenario overrides because overriding one nested field could drop sibling fields. The new implementation adds:

```python
def deep_merge_dict(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge overrides into base without mutating either input."""
```

And updates:

```python
def merge_model(base: T, overrides: dict[str, Any] | None) -> T:
    """Return a Pydantic model copy with nested overrides applied and revalidated."""
```

The new merge behavior:

- Preserves existing fields not mentioned in overrides
- Recursively merges nested dictionaries
- Does not mutate the base model
- Revalidates using `type(base).model_validate(merged)`
- Raises validation errors for invalid nested overrides

This matters for bottom-up deal overrides, where a scenario might override only `operations.current_noi` without restating the full deal.

## New Configuration Settings

`inputs/model_config.yaml` now includes:

```yaml
real_estate:
  mode: "top_down"

bottom_up_allocation:
  remaining_capital_hf_pct: 0.0
  remaining_capital_reserve_pct: 1.0
  allow_overallocated_deals: false
```

`real_estate.mode` supports:

- `top_down`
- `bottom_up`

The default remains:

```yaml
mode: "top_down"
```

That preserves existing behavior.

`bottom_up_allocation` controls what happens to LP capital that is not deployed into year-1 real estate deal equity.

For example, if initial LP capital is `$10,000,000` and year-1 deals require `$2,000,000` of new equity, then `$8,000,000` remains. With the default settings:

```yaml
remaining_capital_hf_pct: 0.0
remaining_capital_reserve_pct: 1.0
```

The remaining `$8,000,000` goes to reserve.

## New Deal Input File

Added:

```text
inputs/deals.yaml
```

It defines one or more named deals:

```yaml
deals:
  jon_deal_1:
    enabled: true
    acquisition_year: 1
    description: "Specific distressed real estate package under review. Placeholder assumptions pending underwriting."

    acquisition:
      asset_value: 23000000
      value_type: "unknown"
      purchase_price: null
      new_equity_required: 2000000
      closing_costs: 0
      initial_capex_reserve: 0

    capital_stack:
      assumed_debt: 16000000
      assumed_liabilities: 0
      liabilities_written_down: 0
      seller_note: 0
      preferred_equity: 0

    operations:
      current_noi: 1200000
      stabilized_noi: 1800000
      years_to_stabilization: 3
      annual_noi_growth_after_stabilization: 0.02
      gross_rent: null
      gross_rent_growth: 0.02
      vacancy_rate: null

    debt:
      interest_rate: 0.065
      maturity_year: 5
      amortization_type: "interest_only"
      annual_debt_service: null
      amortization_years: null
      dscr_minimum: 1.25
      recourse: "unknown"

    capex:
      annual_capex:
        1: 300000
        2: 250000
        3: 150000
      recurring_capex_pct_of_noi: 0.03

    valuation:
      method: "growth"
      exit_cap_rate: null
      annual_value_growth: 0.03
      stabilized_value: null

    refinance:
      enabled: true
      target_years: [5, 7, 10]
      refi_ltv: 0.65
      refi_costs_pct: 0.02
      max_cash_out_pct_of_value: null
      proceeds_use: "fund_liquidity"
```

## New Pydantic Deal Models

Added `src/deal_types.py`.

It defines:

- `DealAcquisition`
- `DealCapitalStack`
- `DealOperations`
- `DealDebt`
- `DealCapex`
- `DealValuation`
- `DealRefinance`
- `DealConfig`
- `DealSet`
- `DealYearResult`
- `RealEstatePortfolioYearResult`

Validation rules include:

- Asset value must be positive
- Acquisition year must be positive
- New equity required must be non-negative
- Debt and liabilities must be non-negative
- At least current NOI or stabilized NOI must be provided
- Interest-only debt requires an interest rate
- Fixed annual debt service requires annual debt service
- Cap-rate valuation requires exit cap rate
- Fixed stabilized value valuation requires stabilized value
- Capex years must be positive
- Capex amounts must be non-negative
- Refinance LTV and costs must be between valid ranges

One important compatibility decision: `DealSet` allows deals to load even if no deals are enabled. The check for at least one enabled deal happens only when a scenario actually uses `bottom_up` mode. This keeps top-down mode from being broken by an unused deal file.

## Deal-Level Calculations

Added `src/deal_model.py`.

The main function is:

```python
def run_deal_year(
    *,
    scenario_name: str,
    deal_name: str,
    deal: DealConfig,
    model_year: int,
) -> DealYearResult:
    ...
```

Supporting functions include:

- `is_deal_active`
- `relative_deal_year`
- `calculate_noi`
- `calculate_gross_rent`
- `calculate_debt_service`
- `calculate_capex`
- `calculate_asset_value`
- `calculate_refi_capacity`

### NOI

NOI is interpolated from current NOI to stabilized NOI over the configured stabilization period.

After stabilization, NOI grows by:

```yaml
annual_noi_growth_after_stabilization
```

Example with current NOI `$1.2m`, stabilized NOI `$1.8m`, and 3 years to stabilization:

```text
Year 1: $1.2m
Year 2: $1.5m
Year 3: $1.8m
Year 4: $1.8m grown by post-stabilization growth
```

### Debt Service

Supported debt methods:

- `interest_only`
- `fixed_annual_debt_service`

Amortizing debt was intentionally not implemented in this pass.

For interest-only debt:

```text
debt_service = debt_balance * interest_rate
```

For fixed annual debt service:

```text
debt_service = annual_debt_service
```

### Capex

Capex is:

```text
scheduled capex for relative deal year
+ recurring_capex_pct_of_noi * NOI
```

### Asset Value

Supported valuation methods:

- `growth`
- `cap_rate`
- `fixed_stabilized_value`

Growth valuation:

```text
asset_value = acquisition.asset_value * (1 + annual_value_growth) ^ (relative_year - 1)
```

Cap-rate valuation:

```text
asset_value = NOI / exit_cap_rate
```

Fixed stabilized value:

```text
asset_value = stabilized_value
```

### NAV

Deal NAV is:

```text
asset_value
- assumed_debt
- assumed_liabilities
- seller_note
- preferred_equity
```

### Entry Equity Cushion

Entry equity cushion is:

```text
initial asset value
- assumed debt
- assumed liabilities
- seller note
- preferred equity
- new equity required
```

For the sample `$23m / $16m / $2m` deal with no other liabilities:

```text
$23m - $16m - $2m = $5m entry equity cushion
```

If additional liabilities are added, the cushion falls accordingly.

### Refinance Capacity

Refi capacity is:

```text
max(0, asset_value * refi_ltv - debt_balance - refi costs)
```

Refi proceeds occur only in configured target years.

Refi proceeds do not reduce asset value.

## Portfolio Aggregation

Added `src/portfolio_aggregator.py`.

It provides:

```python
def apply_deal_overrides(deals: DealSet, overrides: dict[str, Any] | None) -> DealSet:
    ...

def build_re_portfolio_years(
    *,
    scenario_name: str,
    years: int,
    deals: DealSet,
    deal_overrides: dict[str, Any] | None = None,
) -> tuple[list[RealEstatePortfolioYearResult], list[DealYearResult]]:
    ...
```

Portfolio aggregation sums active deal rows into annual RE portfolio results:

- Gross asset value
- Debt balance
- Assumed liabilities
- Net equity value
- NOI
- Gross rent
- Debt service
- Capex
- Free cashflow after debt and capex
- Refi capacity
- Refi proceeds
- Refinance liability added
- Deal NAV

Portfolio DSCR is:

```text
portfolio NOI / portfolio debt service
```

If debt service is zero, DSCR is `None`.

## Engine Integration

Updated `src/engine.py`.

At scenario start, the engine now determines:

```python
real_estate_settings = merge_model(config.real_estate, scenario.real_estate_model)
real_estate_mode = real_estate_settings.mode
```

### Top-Down Mode

If `real_estate_mode == "top_down"`:

- Existing `calculate_initial_allocation()` is used
- Existing annual top-down RE calculations are used
- Deals are ignored
- Default outputs remain compatible

### Bottom-Up Mode

If `real_estate_mode == "bottom_up"`:

- Deals are required
- Scenario deal overrides are applied and revalidated
- Annual deal and portfolio rows are built
- Initial RE cash deployed is the sum of year-1 `new_equity_required`
- Initial RE NAV comes from year-1 portfolio deal NAV
- Remaining LP capital goes to HF and reserve according to `bottom_up_allocation`

Example:

```text
Initial LP capital:       $10,000,000
Year-1 deal equity:        $2,000,000
Remaining capital:         $8,000,000
```

With default bottom-up allocation:

```text
HF allocation:             $0
Reserve allocation:        $8,000,000
```

### Annual Bottom-Up Integration

For each model year:

```text
re_opening_nav = prior year RE NAV
re_noi = portfolio NOI
gross_rent = portfolio gross rent
net_re_cashflow = portfolio free cashflow after debt/capex - RE asset management fee
re_cashflow_generated = max(0, net_re_cashflow)
re_nav = portfolio deal NAV
```

If net RE cashflow is negative, the fund engine funds the deficit from:

1. Retained cash
2. Reserve

Any remaining unfunded amount is recorded as:

```text
re_cashflow_shortfall
```

This prevents negative real estate cashflow from becoming a negative LP distribution or negative HF reinvestment.

### Deal Refinance Proceeds

Deal refi proceeds:

- Increase `refinance_liability`
- Increase retained cash or reserve depending on `proceeds_use`
- Do not reduce RE NAV
- Do not directly distribute to LPs

Supported `proceeds_use` values:

- `fund_liquidity`
- `retained_cash`
- `reserve`

The LP distribution decision remains in the fund-level waterfall.

## Output Changes

Updated `src/outputs.py`.

New CSV:

```text
outputs/deal_cashflows.csv
```

New Excel sheet:

```text
Deal Cashflows
```

Scenario summary now includes bottom-up fields:

- `real_estate_mode`
- `initial_re_cash_deployed`
- `initial_re_gross_asset_value`
- `initial_re_debt_balance`
- `initial_re_assumed_liabilities`
- `initial_re_net_equity_value`
- `initial_re_entry_equity_cushion`
- `initial_re_value_to_new_equity_multiple`
- `final_re_gross_asset_value`
- `final_re_debt_balance`
- `final_re_assumed_liabilities`
- `final_re_net_equity_value`
- `final_re_dscr`
- `total_re_debt_service`
- `total_re_capex`
- `total_deal_refi_proceeds`
- `total_re_cashflow_shortfall`

Scenario cashflows now include RE portfolio fields:

- `real_estate_mode`
- `re_gross_asset_value`
- `re_debt_balance`
- `re_assumed_liabilities`
- `re_net_equity_value`
- `re_debt_service`
- `re_capex`
- `re_dscr`
- `re_refi_capacity`
- `re_refi_proceeds_from_deals`
- `re_free_cashflow_after_debt_and_capex`
- `re_cashflow_shortfall`
- `active_deal_count`

Deal cashflows include:

- Scenario
- Deal name
- Year
- Relative deal year
- Active flag
- Asset value
- Debt balance
- Assumed liabilities
- Net equity value
- NOI
- Gross rent
- Debt service
- Capex
- Free cashflow after debt and capex
- DSCR
- Refi capacity
- Refi proceeds
- Refi liability added
- Deal NAV
- Entry equity cushion
- Value-to-new-equity multiple
- New equity required
- Refinance proceeds use

## Reporting And ChatGPT Export

Updated:

- `src/reporting.py`
- `src/chatgpt_export.py`

Markdown reporting now adds a bottom-up section when a scenario uses bottom-up mode.

The ChatGPT export includes bottom-up deal rows when available, while keeping the context compact.

## Test Coverage

Added `tests/test_bottom_up_deals.py`.

Coverage includes:

- Nested deep merge preserves sibling fields
- Invalid nested override raises validation errors
- Base model is not mutated
- NAV calculation
- Entry equity cushion
- Interest-only debt service
- Fixed annual debt service
- DSCR
- Capex
- NOI interpolation
- Growth valuation
- Cap-rate valuation
- Refi capacity floors at zero
- Refi proceeds occur only in target years
- One active deal aggregation
- Future acquisition inactive before acquisition year
- Two active deals aggregate correctly
- Scenario-level deal overrides
- Top-down default run remains unchanged
- Bottom-up mode requires deals
- Bottom-up uses deal NAV and cashflow
- Negative RE cashflow does not produce negative LP distributions
- Deal refi proceeds increase refinance liability and retained cash/reserve
- LP hurdle trigger still works with bottom-up RE portfolio values
- `deal_cashflows.csv` is created
- Excel workbook includes the `Deal Cashflows` sheet

## Verification Results

Tests were run using the parent venv:

```powershell
cd C:\Users\water\HAC\github\hybrid-fund\hybrid_econ_model
..\.venv\Scripts\python.exe -m pytest
```

Result:

```text
80 passed
```

The full model was run using:

```powershell
..\.venv\Scripts\python.exe run_model.py
```

Result:

```text
Ran 8 scenarios.
Outputs written to outputs/
ChatGPT context written to outputs/chatgpt_model_context.md
```

## How To Use Top-Down Mode

Top-down mode remains the default.

Run:

```powershell
cd C:\Users\water\HAC\github\hybrid-fund\hybrid_econ_model
..\.venv\Scripts\python.exe run_model.py
```

With this config:

```yaml
real_estate:
  mode: "top_down"
```

The model uses the existing scenario-level assumptions:

```yaml
real_estate:
  initial_noi_yield: 0.075
  annual_noi_growth: 0.025
  annual_nav_appreciation: 0.04
  gross_rent_yield: 0.12
```

Deals are loaded but ignored.

## How To Use Bottom-Up Mode

The recommended way is to enable bottom-up mode for a specific scenario, not globally.

Add a scenario like this to `inputs/scenarios.yaml`:

```yaml
scenarios:
  jon_bottom_up_case:
    description: "Bottom-up underwriting case for Jon Deal 1."
    years: 10

    real_estate_model:
      mode: "bottom_up"

    real_estate:
      initial_noi_yield: 0.07
      annual_noi_growth: 0.02
      annual_nav_appreciation: 0.03
      gross_rent_yield: 0.11

    hedge_fund:
      annual_returns: [0.20, 0.10, 0.15, 0.05, 0.20, 0.12, 0.10, 0.08, 0.12, 0.10]
```

The `real_estate` block is still required by the current `Scenario` schema for compatibility. In bottom-up mode, the actual RE economics come from `inputs/deals.yaml`.

Then run:

```powershell
..\.venv\Scripts\python.exe run_model.py
```

Review:

```text
outputs/scenario_summary.csv
outputs/scenario_cashflows.csv
outputs/deal_cashflows.csv
outputs/scenario_summary.xlsx
outputs/scenario_report.md
outputs/chatgpt_model_context.md
```

## How To Override Deal Assumptions By Scenario

Use `deal_overrides` in a scenario:

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

Only the fields listed under `deal_overrides` are changed. All sibling deal assumptions are preserved through the new validated deep merge.

## How To Add Another Deal

Add another key under `deals:` in `inputs/deals.yaml`:

```yaml
deals:
  jon_deal_1:
    ...

  second_deal:
    enabled: true
    acquisition_year: 2
    description: "Second acquisition."

    acquisition:
      asset_value: 8000000
      value_type: "appraised"
      purchase_price: null
      new_equity_required: 1500000
      closing_costs: 0
      initial_capex_reserve: 0

    capital_stack:
      assumed_debt: 5000000
      assumed_liabilities: 0
      liabilities_written_down: 0
      seller_note: 0
      preferred_equity: 0

    operations:
      current_noi: 500000
      stabilized_noi: 700000
      years_to_stabilization: 3
      annual_noi_growth_after_stabilization: 0.02
      gross_rent: null
      gross_rent_growth: 0.02
      vacancy_rate: null

    debt:
      interest_rate: 0.065
      maturity_year: 5
      amortization_type: "interest_only"
      annual_debt_service: null
      amortization_years: null
      dscr_minimum: 1.25
      recourse: "unknown"

    capex:
      annual_capex:
        1: 100000
        2: 50000
      recurring_capex_pct_of_noi: 0.03

    valuation:
      method: "growth"
      exit_cap_rate: null
      annual_value_growth: 0.03
      stabilized_value: null

    refinance:
      enabled: true
      target_years: [6, 9]
      refi_ltv: 0.65
      refi_costs_pct: 0.02
      max_cash_out_pct_of_value: null
      proceeds_use: "fund_liquidity"
```

The portfolio aggregator will include the deal only from its acquisition year onward.

## How To Read The New Outputs

### `outputs/deal_cashflows.csv`

Use this file to inspect asset-level underwriting.

Most useful fields:

- `deal_name`
- `year`
- `active`
- `asset_value`
- `debt_balance`
- `assumed_liabilities`
- `noi`
- `debt_service`
- `capex`
- `free_cashflow_after_debt_and_capex`
- `dscr`
- `refi_capacity`
- `refi_proceeds`
- `deal_nav`
- `entry_equity_cushion`
- `value_to_new_equity_multiple`

### `outputs/scenario_cashflows.csv`

Use this file to inspect annual fund-level integration.

Most useful bottom-up fields:

- `real_estate_mode`
- `re_gross_asset_value`
- `re_debt_balance`
- `re_assumed_liabilities`
- `re_net_equity_value`
- `re_noi`
- `re_debt_service`
- `re_capex`
- `re_dscr`
- `re_refi_capacity`
- `re_refi_proceeds_from_deals`
- `re_free_cashflow_after_debt_and_capex`
- `re_cashflow_shortfall`
- `active_deal_count`
- `refinance_liability`
- `retained_cash`
- `reserve_closing_nav`
- `lp_distribution`
- `fund_nav`

### `outputs/scenario_summary.csv`

Use this file for scenario-level comparison.

Most useful bottom-up fields:

- `real_estate_mode`
- `initial_re_cash_deployed`
- `initial_re_gross_asset_value`
- `initial_re_debt_balance`
- `initial_re_assumed_liabilities`
- `initial_re_net_equity_value`
- `initial_re_entry_equity_cushion`
- `initial_re_value_to_new_equity_multiple`
- `final_re_gross_asset_value`
- `final_re_debt_balance`
- `final_re_assumed_liabilities`
- `final_re_net_equity_value`
- `final_re_dscr`
- `total_re_debt_service`
- `total_re_capex`
- `total_deal_refi_proceeds`
- `total_re_cashflow_shortfall`

## Known Limitations

This pass intentionally does not add:

- Tax modelling
- Monthly periods
- Database storage
- Monte Carlo
- Streamlit UI changes
- Property-level tenant schedules
- Full amortizing debt
- Complex waterfall redesign

Additional limitation:

- Future-year acquisitions become active economically in their acquisition year, but the fund engine does not yet explicitly reserve and deploy future acquisition equity in later years. Year-1 deployed equity is handled directly.

## Practical Workflow

1. Keep `real_estate.mode: "top_down"` for normal existing runs.
2. Add or edit deals in `inputs/deals.yaml`.
3. Add a scenario with:

```yaml
real_estate_model:
  mode: "bottom_up"
```

4. Optionally add `deal_overrides` for downside/base/upside underwriting cases.
5. Run:

```powershell
..\.venv\Scripts\python.exe run_model.py
```

6. Review `outputs/deal_cashflows.csv` first to validate asset economics.
7. Review `outputs/scenario_cashflows.csv` to validate fund-level routing and liquidity.
8. Review `outputs/scenario_summary.csv` for LP/GP outcome comparison.

