# Hybrid Fund Economic Model Runbook and Input Guide

This document explains how to run the model, what input files are required, how each input is formatted, and how to switch between the original top-down real estate model and the newer bottom-up deal model.

It is written for someone fresh to the project.

## 1. What The Model Does

The model is a deterministic annual economic model for a hybrid fund. It projects:

- real estate NAV, NOI, fees, refinance proceeds, debt, liabilities, and cashflow;
- hedge fund NAV, gains, harvests, and reinvestment;
- reserve account balances;
- retained cash;
- LP distributions and LP hurdle completion;
- GP fees and residual economics;
- liquidity constraints and warning flags.

The model has three clean layers:

- **Deal model:** asset economics only, including asset value, debt, NOI, capex, refinance capacity, and deal NAV.
- **Fund model:** cash routing, hedge fund, reserve, retained cash, acquisition funding, refinance proceeds, and fund NAV.
- **Waterfall model:** LP/GP economics, hurdle tests, LP distributions, and GP residual value.

The deal model does not decide LP distributions or GP ownership. Those decisions stay at the fund and waterfall layers.

## 2. Folder Layout

Run the model from:

```powershell
C:\Users\water\HAC\github\hybrid-fund\hybrid_econ_model
```

Important files:

```text
inputs/model_config.yaml     Global model, allocation, waterfall, routing, liquidity, fees, and reporting assumptions.
inputs/scenarios.yaml        Named scenario assumptions and scenario-level overrides.
inputs/deals.yaml            Optional bottom-up real estate deal assumptions.
run_model.py                 Main model runner.
run_calibration.py           Calibration/sensitivity runner.
build_chatgpt_context.py     Rebuilds compact context from existing inputs and outputs.
outputs/                     Generated CSV, Excel, Markdown, and ChatGPT review files.
src/                         Model code.
tests/                       Automated tests.
```

## 3. Prerequisites

Use the existing virtual environment in the parent folder:

```powershell
C:\Users\water\HAC\github\hybrid-fund\.venv
```

From the model folder, the Python executable is:

```powershell
..\.venv\Scripts\python.exe
```

If dependencies ever need to be installed or refreshed:

```powershell
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 4. Quick Start

From `C:\Users\water\HAC\github\hybrid-fund\hybrid_econ_model`:

```powershell
..\.venv\Scripts\python.exe run_model.py
```

Expected terminal output:

```text
Ran N scenarios.
Outputs written to outputs/
ChatGPT context written to outputs/chatgpt_model_context.md
```

The default configuration currently uses:

```yaml
real_estate:
  mode: "top_down"
```

That means the default run uses the original top-down real estate assumptions in `inputs/scenarios.yaml`. The bottom-up `inputs/deals.yaml` file may exist, but it is not used unless a scenario or config switches real estate mode to `bottom_up`.

## 5. Outputs

The main run writes these files to `outputs/`:

```text
scenario_summary.csv          One row per scenario with high-level economics and summary metrics.
scenario_cashflows.csv        One row per scenario year with fund-level annual cashflows and NAV.
deal_cashflows.csv            One row per deal per year for bottom-up real estate deal outputs.
scenario_flags.csv            Warning flags and interpretation notes.
scenario_summary.xlsx         Excel workbook containing Summary, Cashflows, Deal Cashflows, Flags, Assumptions, and Scenario Notes.
scenario_report.md            Human-readable Markdown report.
chatgpt_model_context.md      Compact package for uploading to ChatGPT or another reviewer.
```

`deal_cashflows.csv` is created even if the current run is top-down. In a pure top-down run it may contain only headers.

## 6. Required Input Files

The model loader expects this folder:

```text
inputs/
```

Required:

```text
inputs/model_config.yaml
inputs/scenarios.yaml
```

Optional unless bottom-up mode is used:

```text
inputs/deals.yaml
```

If any YAML is invalid, missing required fields, or fails validation, the model exits with a clear error message.

## 7. YAML Format Rules

Use ordinary YAML mappings and lists.

Numbers can be entered as integers or decimals:

```yaml
initial_lp_capital: 10000000
annual_noi_growth: 0.025
```

Percentages are entered as decimals, not whole percentages:

```yaml
0.10   # 10%
0.65   # 65%
1.0    # 100%
```

Use `null` for unknown optional values:

```yaml
purchase_price: null
gross_rent: null
```

Lists use bracket style or block style:

```yaml
annual_returns: [0.30, 0.15, -0.05]
```

or:

```yaml
target_years:
  - 5
  - 7
  - 10
```

## 8. Global Config: `inputs/model_config.yaml`

`model_config.yaml` contains the default assumptions used by every scenario. Scenarios can override selected nested settings without copying the whole config.

### `model`

```yaml
model:
  currency: "USD"
  periods_per_year: 1
  max_years: 15
  initial_lp_capital: 10000000
  gp_co_investment: 0
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `currency` | Yes | String | Reporting currency label. |
| `periods_per_year` | Yes | Integer, must be `1` | The model currently supports annual periods only. |
| `max_years` | Yes | Positive integer | Maximum allowed scenario length. |
| `initial_lp_capital` | Yes | Positive number | Initial LP capital committed/deployed into the model. |
| `gp_co_investment` | Yes | Non-negative number | Optional GP co-investment for GP IRR/multiple reporting. |

### `allocation`

```yaml
allocation:
  method: "fixed"
  hedge_fund_allocation_pct: 0.10
  real_estate_allocation_pct: 0.85
  reserve_allocation_pct: 0.05
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `method` | Yes | `"fixed"` or `"cap_rate_sized"` | Initial allocation method. The default model uses fixed percentages. |
| `hedge_fund_allocation_pct` | Yes | Decimal >= 0 | Percent of initial LP capital allocated to hedge fund in top-down mode. |
| `real_estate_allocation_pct` | Yes | Decimal >= 0 | Percent of initial LP capital allocated to real estate in top-down mode. |
| `reserve_allocation_pct` | Yes | Decimal >= 0 | Percent of initial LP capital allocated to reserve in top-down mode. |

If `method` is `"fixed"`, the three percentages must sum to `1.0`.

### `real_estate`

```yaml
real_estate:
  mode: "top_down"
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `mode` | Yes | `"top_down"` or `"bottom_up"` | Selects real estate modelling mode. |

Use `"top_down"` to preserve the original model behavior.

Use `"bottom_up"` to make real estate come from individual deals in `inputs/deals.yaml`.

### `bottom_up_allocation`

Used only when real estate mode is bottom-up.

```yaml
bottom_up_allocation:
  remaining_capital_hf_pct: 0.0
  remaining_capital_reserve_pct: 1.0
  allow_overallocated_deals: false
  failed_acquisition_funding_treatment: "do_not_fund"
  failed_acquisition_loss_pct: 0.0
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `remaining_capital_hf_pct` | Yes | Decimal from 0 to 1 | Share of LP capital not used for initial deal equity that goes to hedge fund. |
| `remaining_capital_reserve_pct` | Yes | Decimal from 0 to 1 | Share of LP capital not used for initial deal equity that goes to reserve. |
| `allow_overallocated_deals` | Yes | Boolean | If false, year-1 deal equity cannot exceed initial LP capital. |
| `failed_acquisition_funding_treatment` | Yes | `"do_not_fund"` or `"partial_loss"` | What happens if a future-year acquisition cannot be fully funded. |
| `failed_acquisition_loss_pct` | Yes | Decimal from 0 to 1 | If `partial_loss`, percent of attempted unavailable funding treated as sunk loss. |

`remaining_capital_hf_pct + remaining_capital_reserve_pct` must equal `1.0`.

Default behavior for failed future acquisitions is conservative and realistic:

- if the fund cannot fully fund the deal, the model does not consume partial cash;
- the deal remains inactive;
- the unfunded shortfall is recorded.

### `waterfall`

```yaml
waterfall:
  lp_hurdle_moic: 2.0
  lp_receives_100_percent_until_hurdle: true
  gp_receives_residual_after_lp_hurdle: true
  include_unrealized_nav_in_hurdle_test: true
  require_liquidity_for_lp_redemption: true
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `lp_hurdle_moic` | Yes | Positive decimal | LP cash multiple target, for example `2.0` means 2x LP capital. |
| `lp_receives_100_percent_until_hurdle` | Yes | Boolean | If true, LP receives distributions until the hurdle is complete. |
| `gp_receives_residual_after_lp_hurdle` | Yes | Boolean | If true, GP can receive residual NAV after LP hurdle completion. |
| `include_unrealized_nav_in_hurdle_test` | Yes | Boolean | If true, economic hurdle tests can include unrealized NAV. |
| `require_liquidity_for_lp_redemption` | Yes | Boolean | If true, LP cash redemption requires actual liquidity, not just paper NAV. |

### `liquidity`

```yaml
liquidity:
  hf_liquidation_allowed: true
  hf_liquidation_capacity_pct_per_year: 1.0
  reserve_liquidation_capacity_pct_per_year: 1.0
  real_estate_liquidation_capacity_pct_per_year: 0.0
  max_refinance_or_sale_capacity_pct_of_re_nav: 0.25
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `hf_liquidation_allowed` | Yes | Boolean | Whether hedge fund NAV can be liquidated for hurdle completion. |
| `hf_liquidation_capacity_pct_per_year` | Yes | Decimal from 0 to 1 | Max annual share of HF NAV that can be liquidated. |
| `reserve_liquidation_capacity_pct_per_year` | Yes | Decimal from 0 to 1 | Max annual share of reserve NAV available for liquidity tests. |
| `real_estate_liquidation_capacity_pct_per_year` | Yes | Decimal from 0 to 1 | Max annual share of RE NAV sale capacity. Usually `0.0` unless partial sale is allowed. |
| `max_refinance_or_sale_capacity_pct_of_re_nav` | Yes | Decimal from 0 to 1 | General refinance/sale capacity limit used by liquidity logic. |

### `fees`

```yaml
fees:
  real_estate_asset_management_fee:
    enabled: true
    rate: 0.03
    basis: "gross_rent"
  hedge_fund_fees:
    model_as_net_returns: true
    management_fee_rate: 0.0
    performance_fee_rate: 0.0
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `real_estate_asset_management_fee.enabled` | Yes | Boolean | Turns RE asset management fees on/off. |
| `real_estate_asset_management_fee.rate` | Yes | Decimal >= 0 | Annual fee rate. |
| `real_estate_asset_management_fee.basis` | Yes | `"gross_rent"`, `"noi"`, or `"re_nav"` | Base used for RE asset management fee. |
| `hedge_fund_fees.model_as_net_returns` | Yes | Boolean | If true, HF returns are already net of fees. |
| `hedge_fund_fees.management_fee_rate` | Yes | Decimal >= 0 | HF management fee rate if not using net returns. |
| `hedge_fund_fees.performance_fee_rate` | Yes | Decimal >= 0 | HF performance fee rate if not using net returns. |

Important convention: if the RE fee basis is `re_nav`, the basis follows the model's current RE NAV convention. In bottom-up mode, review whether this should be gross of or net of refinance liability for the fund economics you want to show.

### `distribution_policy`

```yaml
distribution_policy:
  distribute_re_cashflow_annually: true
  distribute_hf_realized_gains_annually: false
  hf_positive_return_harvest_rate: 0.0
  retain_cash_until_hurdle_redemption: false
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `distribute_re_cashflow_annually` | Yes | Boolean | Whether positive RE cashflow is routed annually. |
| `distribute_hf_realized_gains_annually` | Yes | Boolean | Whether harvested HF gains are routed annually. |
| `hf_positive_return_harvest_rate` | Yes | Decimal from 0 to 1 | Percent of positive HF gain harvested each year. |
| `retain_cash_until_hurdle_redemption` | Yes | Boolean | If true, keeps cash retained until hurdle redemption logic uses it. |

### `cashflow_routing`

```yaml
cashflow_routing:
  re_cashflow:
    lp_distribution_pct: 0.10
    hf_reinvestment_pct: 0.75
    reserve_pct: 0.15
  hf_harvest:
    lp_distribution_pct: 0.10
    hf_reinvestment_pct: 0.80
    reserve_pct: 0.10
```

Fields under both `re_cashflow` and `hf_harvest`:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `lp_distribution_pct` | Yes | Decimal from 0 to 1 | Share routed to LP cash distributions. |
| `hf_reinvestment_pct` | Yes | Decimal from 0 to 1 | Share routed into the hedge fund sleeve. |
| `reserve_pct` | Yes | Decimal from 0 to 1 | Share routed into reserve. |

Each route must sum to `1.0`.

### `lp_cash_yield_policy`

```yaml
lp_cash_yield_policy:
  enabled: false
  target_annual_yield_on_unreturned_capital: 0.0
  source_priority:
    - net_re_cashflow
    - hf_harvest
    - retained_cash
    - reserve
  reduce_lp_hurdle: true
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `enabled` | Yes | Boolean | Enables target annual LP cash yield policy. |
| `target_annual_yield_on_unreturned_capital` | Yes | Decimal >= 0 | Target annual cash yield on unrecovered LP capital. |
| `source_priority` | Yes | Non-empty list | Funding order for LP yield payments. |
| `reduce_lp_hurdle` | Yes | Boolean, must be true when enabled | LP cash yield payments reduce the LP cash hurdle. |

Allowed `source_priority` values:

```text
net_re_cashflow
hf_harvest
retained_cash
reserve
```

### `reserve`

```yaml
reserve:
  annual_return: 0.0
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `annual_return` | Yes | Decimal | Annual reserve return. For example `0.03` means 3%. |

Reserve returns compound inside the reserve sleeve.

### `reporting`

```yaml
reporting:
  output_excel: true
  output_csv: true
  output_markdown: true
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `output_excel` | Yes | Boolean | Writes `scenario_summary.xlsx`. |
| `output_csv` | Yes | Boolean | Writes CSV files. |
| `output_markdown` | Yes | Boolean | Writes `scenario_report.md`. |

### `flag_thresholds`

Controls warning flags and interpretation labels.

```yaml
flag_thresholds:
  fast_gp_dynasty_max_year: 4
  fast_gp_dynasty_residual_multiple: 0.5
  slow_time_horizon_year: 8
  gp_survivability_first_years: 5
  gp_survivability_fee_threshold: 250000
  hf_major_drawdown_pct: 0.50
  re_nav_impairment_pct: 0.20
  lp_good_irr_threshold: 0.12
  lp_good_irr_gp_residual_multiple: 1.0
  long_zero_distribution_years: 3
```

These settings do not change model economics. They change how results are flagged and summarized.

### `gp_survivability`

```yaml
gp_survivability:
  first_n_years: 5
  minimum_cumulative_fees: 500000
  minimum_average_annual_fees: 100000
```

Controls summary metrics for whether GP fees are sufficient during the early years.

### `hurdle_completion_trigger`

```yaml
hurdle_completion_trigger:
  enabled: true
  trigger_when_economic_hurdle_passed: true
  minimum_lp_cash_moic_before_trigger: 0.1
  max_hf_liquidation_pct: 0.75
  max_refi_pct_of_re_nav: 0.25
  allow_retained_cash_use: true
  allow_reserve_use: true
  allow_hf_liquidation: true
  allow_refi: true
  allow_partial_re_sale: false
  max_partial_re_sale_pct_of_re_nav: 0.0
  execute_only_if_lp_fully_redeemed: true
```

This is the active trigger that tries to complete the LP hurdle using available liquidity sources once the configured trigger tests are met. If the trigger is eligible but cannot fully fund the LP hurdle in one year, it can retry in later years when liquidity or NAV capacity has grown.

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `enabled` | Yes | Boolean | Turns trigger logic on/off. |
| `trigger_when_economic_hurdle_passed` | Yes | Boolean | Trigger can activate when economic MOIC passes the hurdle. |
| `minimum_lp_cash_moic_before_trigger` | Yes | Decimal >= 0 | Minimum cash MOIC before the trigger can attempt completion. |
| `max_hf_liquidation_pct` | Yes | Decimal from 0 to 1 | Max HF liquidation for trigger. |
| `max_refi_pct_of_re_nav` | Yes | Decimal from 0 to 1 | Max refinance proceeds as share of RE NAV for trigger. |
| `allow_retained_cash_use` | Yes | Boolean | Allows retained cash to fund trigger. |
| `allow_reserve_use` | Yes | Boolean | Allows reserve to fund trigger. |
| `allow_hf_liquidation` | Yes | Boolean | Allows HF liquidation to fund trigger. |
| `allow_refi` | Yes | Boolean | Allows refinance proceeds to fund trigger. |
| `allow_partial_re_sale` | Yes | Boolean | Allows partial RE sale if enabled. |
| `max_partial_re_sale_pct_of_re_nav` | Yes | Decimal from 0 to 1 | Max partial RE sale capacity. |
| `execute_only_if_lp_fully_redeemed` | Yes | Boolean | If true, trigger executes only when it can fully complete LP hurdle. |

### `backend_liquidity_strategy`

```yaml
backend_liquidity_strategy:
  enabled: true
  target_years: [5, 7, 10]
  refi_first: true
  max_refi_pct_of_re_nav: 0.35
  max_hf_liquidation_pct: 0.50
  use_retained_cash: true
  use_reserve: true
  execute_only_if_lp_hurdle_completed: true
```

Models a scheduled backend liquidity strategy, commonly refi-led, in selected years.

Backend target years do not disable the ordinary hurdle trigger outside those years. Instead:

- in backend target years, the trigger uses backend-specific caps and source order, such as `refi_first`, `max_refi_pct_of_re_nav`, and `max_hf_liquidation_pct`;
- outside backend target years, the ordinary hurdle trigger can still evaluate and retry using the standard `hurdle_completion_trigger` caps.

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `enabled` | Yes | Boolean | Turns backend liquidity strategy on/off. |
| `target_years` | Yes if enabled | List of positive integers | Years in which backend liquidity is attempted. |
| `refi_first` | Yes | Boolean | Whether refi is attempted before other liquidity sources. |
| `max_refi_pct_of_re_nav` | Yes | Decimal from 0 to 1 | Max refi capacity as share of RE NAV. |
| `max_hf_liquidation_pct` | Yes | Decimal from 0 to 1 | Max HF liquidation capacity. |
| `use_retained_cash` | Yes | Boolean | Allows retained cash. |
| `use_reserve` | Yes | Boolean | Allows reserve. |
| `execute_only_if_lp_hurdle_completed` | Yes | Boolean | If true, executes only when it completes the LP hurdle. |

## 9. Scenarios: `inputs/scenarios.yaml`

`scenarios.yaml` contains a top-level `scenarios:` mapping. Each scenario is one named model run.

Example:

```yaml
scenarios:
  base_hit_everyone_happy:
    description: "Moderate real estate and hedge fund performance baseline."
    years: 8
    real_estate:
      initial_noi_yield: 0.075
      annual_noi_growth: 0.025
      annual_nav_appreciation: 0.04
      gross_rent_yield: 0.12
    hedge_fund:
      annual_returns: [0.30, 0.15, 0.35, 0.12, 0.24, 0.08, 0.40, 0.06]
```

Required scenario fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `description` | Yes | String | Human-readable scenario description. |
| `years` | Yes | Positive integer | Number of annual periods to model. Must be <= `model.max_years`. |
| `real_estate` | Yes | Mapping | Top-down real estate assumptions. Still required by schema even when bottom-up mode is used. |
| `hedge_fund.annual_returns` | Yes | List of decimals | Annual HF returns. Must contain at least `years` values. |

### Scenario `real_estate` Fields

These fields drive real estate economics in top-down mode.

```yaml
real_estate:
  initial_noi_yield: 0.075
  annual_noi_growth: 0.025
  annual_nav_appreciation: 0.04
  gross_rent_yield: 0.12
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `initial_noi_yield` | Yes | Decimal | Year-1 NOI as a share of opening RE NAV. |
| `annual_noi_growth` | Yes | Decimal | Annual growth rate for NOI. |
| `annual_nav_appreciation` | Yes | Decimal or list of decimals | Annual RE NAV growth. A list allows year-specific rates. |
| `gross_rent_yield` | Yes | Decimal or list of decimals | Gross rent as a share of RE NAV. A list allows year-specific rates. |

In bottom-up mode, actual RE economics come from `inputs/deals.yaml`, but this mapping is still required for compatibility with the current scenario schema.

### Scenario `hedge_fund` Fields

```yaml
hedge_fund:
  annual_returns: [0.30, 0.15, 0.35]
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `annual_returns` | Yes | List of decimals | Annual returns for the HF sleeve. Must have one value for each model year. |

### Scenario-Level Overrides

Scenarios can override selected config sections. Overrides are deep-merged and revalidated, so you only need to specify the fields you want to change.

Allowed override sections include:

```yaml
liquidity:
distribution_policy:
cashflow_routing:
lp_cash_yield_policy:
backend_liquidity_strategy:
allocation:
reserve:
real_estate_model:
deal_overrides:
refinance_events:
```

Example override:

```yaml
scenarios:
  liquidity_trap:
    description: "High NAV growth but low refinance capacity."
    years: 10
    liquidity:
      max_refinance_or_sale_capacity_pct_of_re_nav: 0.05
    real_estate:
      initial_noi_yield: 0.07
      annual_noi_growth: 0.03
      annual_nav_appreciation: 0.07
      gross_rent_yield: 0.11
    hedge_fund:
      annual_returns: [0.10, 0.38, 0.22, 0.05, 0.25, 0.05, 0.34, 0.04, 0.34, 0.04]
```

### Scenario Refinance Events

Manual refinance events can be added at scenario level:

```yaml
refinance_events:
  - year: 5
    pct_of_re_nav: 0.20
    use_of_proceeds: "retained_cash"
    description: "Manual year-5 refinance."
```

Fields:

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `year` | Yes | Positive integer <= scenario `years` | Event year. |
| `pct_of_re_nav` | Yes | Decimal >= 0 | Refinance proceeds as share of RE NAV. |
| `use_of_proceeds` | Yes | `"lp_distribution"`, `"retained_cash"`, or `"reserve"` | Where proceeds go. |
| `description` | No | String | Human-readable note. |

Bottom-up deal-level refinance events are defined inside `inputs/deals.yaml`. Scenario-level refinance events are separate.

## 10. Top-Down Real Estate Mode

Top-down mode is the original model mode.

The default top-down scenarios use a 20-year diagnostic horizon. The engine still stops a scenario early once the LP cash hurdle is achieved, so a 20-year scenario does not imply a 20-year hold if the LP reaches 2.0x earlier.

Use this in `inputs/model_config.yaml`:

```yaml
real_estate:
  mode: "top_down"
```

In top-down mode:

- initial LP capital is allocated by `allocation`;
- real estate starts as a single sleeve;
- NOI is calculated from `initial_noi_yield` and `annual_noi_growth`;
- gross rent is calculated from `gross_rent_yield`;
- NAV grows by `annual_nav_appreciation`;
- the deal file is not required.

To run:

```powershell
..\.venv\Scripts\python.exe run_model.py
```

Use top-down mode when you want high-level fund sensitivity testing without detailed property/deal assumptions.

## 11. Bottom-Up Real Estate Mode

Bottom-up mode models real estate from one or more named deals.

You can turn it on globally:

```yaml
real_estate:
  mode: "bottom_up"
```

Or for one scenario only:

```yaml
scenarios:
  jon_base_case:
    description: "Bottom-up Jon deal base case."
    years: 10
    real_estate_model:
      mode: "bottom_up"
    real_estate:
      initial_noi_yield: 0.075
      annual_noi_growth: 0.025
      annual_nav_appreciation: 0.04
      gross_rent_yield: 0.12
    hedge_fund:
      annual_returns: [0.15, 0.12, 0.10, 0.08, 0.08, 0.10, 0.12, 0.08, 0.06, 0.06]
```

When bottom-up mode is active:

- `inputs/deals.yaml` is required;
- at least one enabled deal is required;
- year-1 deals are funded from initial LP capital;
- remaining initial LP capital is allocated between HF and reserve using `bottom_up_allocation`;
- future-year acquisitions must be fully funded from retained cash first, then reserve;
- unfunded future acquisitions remain economically inactive;
- deal refinance proceeds add liquidity according to each deal's `refinance.proceeds_use`;
- refinance proceeds create refinance liability and do not reduce gross asset value directly;
- LP distributions still happen only through fund/waterfall logic.

## 12. Deals: `inputs/deals.yaml`

`deals.yaml` contains a top-level `deals:` mapping. Each key is a deal name.

Example:

```yaml
deals:
  jon_deal_1:
    enabled: true
    acquisition_year: 1
    description: "Specific distressed real estate package under review."

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

### Deal Root Fields

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `enabled` | Yes | Boolean | If false, deal is ignored. |
| `acquisition_year` | Yes | Positive integer | Model year in which the fund must acquire/fund the deal. |
| `description` | No | String | Human-readable deal note. |

### `acquisition`

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `asset_value` | Yes | Positive number | Starting gross asset value controlled by the deal. |
| `value_type` | Yes | `"unknown"`, `"current"`, `"appraised"`, `"stabilized"`, `"replacement"`, or `"purchase_price"` | Describes what the asset value represents. |
| `purchase_price` | No | Non-negative number or `null` | Purchase price if separately known. |
| `new_equity_required` | Yes | Non-negative number | Cash equity the fund must contribute to close the deal. |
| `closing_costs` | Yes | Non-negative number | Closing costs if modelled separately. |
| `initial_capex_reserve` | Yes | Non-negative number | Initial capex reserve if modelled separately. |

### `capital_stack`

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `assumed_debt` | Yes | Non-negative number | Debt assumed or placed on the asset at acquisition. |
| `assumed_liabilities` | Yes | Non-negative number | Other liabilities assumed. |
| `liabilities_written_down` | Yes | Non-negative number | Liabilities written down or forgiven. Informational for underwriting. |
| `seller_note` | Yes | Non-negative number | Seller note amount. |
| `preferred_equity` | Yes | Non-negative number | Preferred equity senior to common equity. |

### `operations`

At least one of `current_noi` or `stabilized_noi` must be provided.

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `current_noi` | Conditionally | Number or `null` | Current annual NOI. |
| `stabilized_noi` | Conditionally | Number or `null` | Stabilized annual NOI. |
| `years_to_stabilization` | Yes | Integer >= 0 | Years over which NOI moves from current to stabilized. |
| `annual_noi_growth_after_stabilization` | Yes | Decimal | NOI growth after stabilization. |
| `gross_rent` | No | Non-negative number or `null` | Annual gross rent. If unavailable, gross rent is `0`. |
| `gross_rent_growth` | Yes | Decimal | Annual gross rent growth. |
| `vacancy_rate` | No | Decimal from 0 to 1 or `null` | Informational vacancy assumption. |

NOI is interpolated from current NOI to stabilized NOI, then grown after stabilization.

### `debt`

Supported amortization types:

```text
interest_only
fixed_annual_debt_service
```

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `interest_rate` | Required for `interest_only` | Decimal >= 0 or `null` | Annual interest rate. |
| `maturity_year` | No | Positive integer or `null` | Debt maturity year. |
| `amortization_type` | Yes | `"interest_only"` or `"fixed_annual_debt_service"` | Debt service calculation method. |
| `annual_debt_service` | Required for `fixed_annual_debt_service` | Non-negative number or `null` | Fixed annual debt service. |
| `amortization_years` | No | Positive integer or `null` | Informational only in this pass. |
| `dscr_minimum` | No | Decimal >= 0 or `null` | Informational DSCR threshold. |
| `recourse` | No | String | Recourse note, for example `"unknown"`, `"non-recourse"`, or `"recourse"`. |

Full amortizing debt is not currently modelled. Use fixed annual debt service if you need a simple amortization proxy.

### `capex`

```yaml
capex:
  annual_capex:
    1: 300000
    2: 250000
    3: 150000
  recurring_capex_pct_of_noi: 0.03
```

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `annual_capex` | Yes | Mapping of positive integer year to non-negative amount | One-time capex by relative deal year. |
| `recurring_capex_pct_of_noi` | Yes | Decimal >= 0 | Annual recurring capex as a share of NOI. |

The keys under `annual_capex` are relative deal years, not fund model years. A deal acquired in fund year 3 has relative year 1 in fund year 3.

### `valuation`

Supported methods:

```text
growth
cap_rate
fixed_stabilized_value
```

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `method` | Yes | `"growth"`, `"cap_rate"`, or `"fixed_stabilized_value"` | Asset value method. |
| `exit_cap_rate` | Required for `cap_rate` | Positive decimal or `null` | Cap-rate denominator for value = NOI / cap rate. |
| `annual_value_growth` | Yes | Decimal | Annual growth from initial asset value when using `growth`. |
| `stabilized_value` | Required for `fixed_stabilized_value` | Non-negative number or `null` | Fixed stabilized asset value. |

### `refinance`

```yaml
refinance:
  enabled: true
  target_years: [5, 7, 10]
  refi_ltv: 0.65
  refi_costs_pct: 0.02
  max_cash_out_pct_of_value: null
  proceeds_use: "fund_liquidity"
```

| Field | Required | Format | Meaning |
| --- | --- | --- | --- |
| `enabled` | Yes | Boolean | Enables deal-level refi tests. |
| `target_years` | Yes | List of positive integers | Relative deal years when refi proceeds can be generated. |
| `refi_ltv` | Yes | Decimal from 0 to 1 | Maximum debt supported as percent of asset value. |
| `refi_costs_pct` | Yes | Decimal from 0 to 1 | Refi costs as percent of positive cash-out capacity. |
| `max_cash_out_pct_of_value` | No | Decimal from 0 to 1 or `null` | Optional cap on cash-out as percent of asset value. |
| `proceeds_use` | Yes | `"fund_liquidity"`, `"retained_cash"`, or `"reserve"` | Where proceeds go at fund level. |

Stateful refinance convention:

```text
max_debt_supported = asset_value * refi_ltv
cash_out_before_costs = max_debt_supported - original_debt_balance - prior_refi_liability
refi_costs = max(cash_out_before_costs, 0) * refi_costs_pct
refi_capacity = max(0, cash_out_before_costs - refi_costs)
ending_refi_liability = prior_refi_liability + refi_proceeds
```

This prevents repeated refi years from double-counting the same borrowing capacity.

## 13. Deal-Level Output Meanings

`outputs/deal_cashflows.csv` contains deal-level rows.

Important columns:

| Column | Meaning |
| --- | --- |
| `active` | Whether the deal is economically active in that year. Future unfunded deals remain inactive. |
| `relative_year` | Deal year after acquisition. Year 1 is acquisition year. |
| `asset_value` | Gross asset value. |
| `debt_balance` | Original assumed debt balance. |
| `prior_refi_liability` | Cumulative refi liability before current-year refi. |
| `ending_refi_liability` | Cumulative refi liability after current-year refi. |
| `deal_nav_before_refi_liability` | Asset value less original debt, assumed liabilities, seller note, and preferred equity. |
| `deal_nav_after_refi_liability` | Deal NAV after subtracting cumulative refi liability. |
| `deal_nav` | Alias for the model's current deal NAV convention. Use the explicit before/after columns for interpretation. |
| `entry_equity_cushion` | Asset value less capital stack and new equity required at entry. |
| `value_to_new_equity_multiple` | Deal NAV divided by new equity required. |
| `refi_capacity` | Available incremental refi capacity after prior refi liability and refi costs. |
| `refi_proceeds` | Actual proceeds generated in configured target years. |

## 14. How To Model The $2m Equity / $23m Asset / $16m Debt Deal

Use `inputs/deals.yaml`.

The current placeholder already describes this structure:

```yaml
acquisition:
  asset_value: 23000000
  new_equity_required: 2000000

capital_stack:
  assumed_debt: 16000000
```

This means:

- the fund contributes $2m of new equity;
- the deal controls $23m of gross real estate asset value;
- the asset carries $16m of assumed debt;
- any other assumed liabilities, seller notes, preferred equity, or write-downs are entered separately.

To run it in a scenario, add or edit a scenario with:

```yaml
real_estate_model:
  mode: "bottom_up"
```

Then run:

```powershell
..\.venv\Scripts\python.exe run_model.py
```

Review:

```text
outputs/deal_cashflows.csv
outputs/scenario_cashflows.csv
outputs/scenario_summary.csv
outputs/scenario_summary.xlsx
```

## 15. Creating Base, Downside, And Upside Bottom-Up Cases

The cleanest pattern is:

1. Keep the base deal assumptions in `inputs/deals.yaml`.
2. Add three scenarios to `inputs/scenarios.yaml`.
3. Use `deal_overrides` for downside/upside changes.

Example:

```yaml
scenarios:
  jon_base_case:
    description: "Jon deal base case using bottom-up real estate."
    years: 10
    real_estate_model:
      mode: "bottom_up"
    real_estate:
      initial_noi_yield: 0.075
      annual_noi_growth: 0.025
      annual_nav_appreciation: 0.04
      gross_rent_yield: 0.12
    hedge_fund:
      annual_returns: [0.15, 0.12, 0.10, 0.08, 0.08, 0.10, 0.12, 0.08, 0.06, 0.06]

  jon_downside_case:
    description: "Jon deal downside case with lower NOI and higher capex."
    years: 10
    real_estate_model:
      mode: "bottom_up"
    deal_overrides:
      jon_deal_1:
        operations:
          current_noi: 900000
          stabilized_noi: 1400000
        capex:
          annual_capex:
            1: 600000
            2: 400000
            3: 250000
    real_estate:
      initial_noi_yield: 0.075
      annual_noi_growth: 0.025
      annual_nav_appreciation: 0.04
      gross_rent_yield: 0.12
    hedge_fund:
      annual_returns: [0.05, -0.10, 0.08, 0.04, 0.05, 0.07, 0.08, 0.05, 0.04, 0.04]

  jon_upside_case:
    description: "Jon deal upside case with stronger NOI and value growth."
    years: 10
    real_estate_model:
      mode: "bottom_up"
    deal_overrides:
      jon_deal_1:
        operations:
          current_noi: 1300000
          stabilized_noi: 2100000
        valuation:
          annual_value_growth: 0.05
    real_estate:
      initial_noi_yield: 0.075
      annual_noi_growth: 0.025
      annual_nav_appreciation: 0.04
      gross_rent_yield: 0.12
    hedge_fund:
      annual_returns: [0.25, 0.20, 0.18, 0.12, 0.12, 0.15, 0.15, 0.10, 0.08, 0.08]
```

Why the top-down `real_estate` block is still present: the schema currently requires it for every scenario. In bottom-up mode, the deal file drives real estate economics.

## 16. Future-Year Acquisitions

A deal with:

```yaml
acquisition_year: 3
```

does not contribute economics in years 1 or 2.

In year 3:

1. the fund checks `new_equity_required`;
2. it tries to fund from retained cash first;
3. it then tries to fund from reserve;
4. if fully funded, the deal becomes active;
5. if not fully funded, the deal remains inactive and a shortfall is recorded.

Relevant output columns in `scenario_cashflows.csv`:

```text
acquisition_new_deal_equity_required
acquisition_funded_from_initial_lp_capital
acquisition_funded_from_retained_cash
acquisition_funded_from_reserve
acquisition_failed_loss
acquisition_unfunded_shortfall
acquisition_funding_source
```

## 17. Running Tests

From the model folder:

```powershell
..\.venv\Scripts\python.exe -m pytest
```

Use tests after changing code or assumptions that affect validation. For documentation-only changes, tests are usually not required.

## 18. Rebuilding Only The ChatGPT Context

If outputs already exist and you only want to rebuild the compact review package:

```powershell
..\.venv\Scripts\python.exe build_chatgpt_context.py
```

This writes:

```text
outputs/chatgpt_model_context.md
```

## 19. Calibration Runs

Calibration variants live in:

```text
inputs/calibration_tests.yaml
```

Run:

```powershell
..\.venv\Scripts\python.exe run_calibration.py
```

Calibration outputs are written to:

```text
outputs/calibration_summary.csv
outputs/calibration_summary.xlsx
outputs/calibration_cashflows.csv
outputs/calibration_flags.csv
outputs/calibration_report.md
```

## 20. Common Validation Errors

### Fixed allocation percentages must sum to 1.0

Cause:

```yaml
allocation:
  method: "fixed"
  hedge_fund_allocation_pct: 0.10
  real_estate_allocation_pct: 0.80
  reserve_allocation_pct: 0.05
```

These sum to `0.95`, not `1.0`.

Fix:

```yaml
reserve_allocation_pct: 0.10
```

### Scenario requires more hedge fund returns

Cause:

```yaml
years: 10
hedge_fund:
  annual_returns: [0.10, 0.08, 0.06]
```

Fix: provide at least 10 annual returns.

### Bottom-up mode requires deals

Cause:

```yaml
real_estate:
  mode: "bottom_up"
```

but `inputs/deals.yaml` is missing or contains no enabled deals.

Fix: add `inputs/deals.yaml` with at least one enabled deal.

### Interest-only debt requires interest rate

Cause:

```yaml
debt:
  amortization_type: "interest_only"
  interest_rate: null
```

Fix:

```yaml
interest_rate: 0.065
```

### Cap-rate valuation requires exit cap rate

Cause:

```yaml
valuation:
  method: "cap_rate"
  exit_cap_rate: null
```

Fix:

```yaml
exit_cap_rate: 0.075
```

### Cashflow routing percentages must sum to 1.0

Cause:

```yaml
re_cashflow:
  lp_distribution_pct: 0.10
  hf_reinvestment_pct: 0.75
  reserve_pct: 0.10
```

These sum to `0.95`.

Fix one field so the route sums to `1.0`.

## 21. Practical Review Checklist

After running a bottom-up case, check these files in this order:

1. `outputs/deal_cashflows.csv`
   - Is each deal active in the expected years?
   - Does NOI stabilize as expected?
   - Are debt service, capex, DSCR, and refi proceeds plausible?
   - Are refi liabilities accumulating correctly?

2. `outputs/scenario_cashflows.csv`
   - Is acquisition funding coming from the expected source?
   - Are negative RE cashflows funded by retained cash/reserve rather than creating negative distributions?
   - Are refi proceeds going to retained cash or reserve as configured?
   - Is fund NAV net of refinance liability?

3. `outputs/scenario_summary.csv`
   - Does LP cash MOIC reach the hurdle?
   - Is the hurdle reached through actual liquidity or only through paper NAV?
   - What residual NAV remains for GP?
   - Are there acquisition shortfalls, refi limitations, or cashflow shortfalls?

4. `outputs/scenario_flags.csv`
   - Review any warning flags before relying on the case.

## 22. Known Limitations

The model intentionally does not include:

- monthly periods;
- tax modelling;
- tenant-level property schedules;
- full amortizing debt schedules;
- Monte Carlo simulation;
- database persistence;
- Streamlit/UI changes;
- complex waterfall redesign.

Debt support is currently annual and simplified. If actual underwriting requires monthly lease-up, tenant rollover, amortization schedules, tax, or property-level financing covenants, those should be added as a separate modelling phase.
