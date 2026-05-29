# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

**Hybrid Fund Economic Model** is a deterministic annual scenario model for a hybrid fund structure with real estate, hedge fund, reserve, and a non-standard LP/GP waterfall. The model does not use Monte Carlo; it runs deterministic annual scenarios to completion or until LP hurdle completion.

**Architecture principle:** All assumptions live in YAML (human-editable). Python code contains logic, validation, calculations, and output formatting only.

## Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Model
```bash
python run_model.py
```
Outputs go to `outputs/` (CSV, Excel, Markdown, HTML, PNG charts).

### Run Calibration Suite
```bash
python run_calibration.py
```
Generates deterministic scenario variants for HF allocation, HF harvesting, LP hurdle, RE liquidity, and 20-year horizon checks without changing base scenarios.

### Run Dashboard
```bash
streamlit run dashboard/app.py
```
Interactive presentation dashboard for the pre-baked scenarios. Routing sliders are in-memory only; they don't edit YAML or overwrite outputs.

### Run Tests
```bash
pytest
```
Tests are in `tests/`. Example: `pytest tests/test_engine_basic.py`.

## Input Files (YAML)

All inputs live in `inputs/`. These are human-editable; the Python code does not modify them.

- **`model_config.yaml`**: Global assumptions, waterfall settings (LP hurdle, GP splits), fees, liquidity, distribution policy, LP cash yield policy, backend liquidity strategy, cashflow routing, GP survivability metrics, flag thresholds.
- **`scenarios.yaml`**: Named scenario assumptions. Can override any model_config setting per scenario.
- **`deals.yaml`** (optional): Individual real estate deals for bottom-up modeling. If provided and scenario uses `real_estate.mode: bottom_up`, the engine sums deal-level cash flows instead of using top-down assumptions.
- **`tax_config.yaml`** (optional): Tax analysis settings. If present, `run_model.py` auto-runs `run_tax_analysis()` and writes tax summaries.
- **`calibration_tests.yaml`**: Policy-set variants (backend-heavy compounding, balanced LP yield + compounding, aggressive LP extinguishment) and individual scenario tweaks.

## Core Architecture

The model flows through these stages:

### 1. Input Layer
`config_loader.py` loads YAML and validates using Pydantic models (`model_types.py`).

### 2. Engine Initialization
`engine.py:run_all_scenarios()` → `run_scenario()` for each scenario. Validates assumptions and initializes sleeve NAVs.

### 3. Annual Operation Loop (engine.py)
Each scenario iterates year-by-year:
1. **Acquisition Check**: Funds new RE deals from Retained Cash, then Reserve.
2. **Sleeve Operations**:
   - **Real Estate** (`portfolio_aggregator.py`, `deal_model.py`): Calculates NOI, debt service, capex. If `bottom_up`, sums all active deal cash flows.
   - **Hedge Fund** (`engine.py`): Appreciates NAV by scenario return, optionally harvests gains.
   - **Reserve** (`engine.py`): Appreciates by annual return.
3. **Cashflow Routing** (`engine.py`): Generated RE and HF cash is split between LP distributions, HF reinvestment, and Reserve by configured percentages (must sum to 100%).
4. **LP Yield Policy** (optional): Pays target annual yield to LP before other routing, sourced from RE cashflow, HF harvests, and Reserve.
5. **Refinance Events** (scenario-level and deal-level): Generates cash and creates a refinance liability, reducing Fund NAV.
6. **Hurdle Completion Trigger**: Tests whether LP 2.0x hurdle can be met by liquidating HF, using Reserve, using Retained Cash, and performing a final refinance. If liquidity ≥ remaining hurdle, scenario finishes.

### 4. Waterfall & Reporting (waterfall.py)
After all years or hurdle completion:
- `redeem_lp()`: Final LP redemption (cash hurdle or NAV hurdle).
- `pay_lp_distribution()`: Annual LP distribution mechanics.
- Waterfall logic produces GP residual NAV.
- `outputs.py` writes CSV, Excel, Markdown.
- `report_html.py` generates self-contained HTML with embedded charts.
- `charts.py`, `charts_gp_lp.py` generate PNG charts.

## Key Files by Role

### Entry Points
- `run_model.py`: Main runner. Loads inputs, runs scenarios, writes outputs, optionally builds tax analysis and charts.
- `run_calibration.py`: Runs calibration suite. Loads calibration_tests.yaml, applies variants, generates separate outputs.
- `dashboard/app.py`: Streamlit app. Reads scenario_summary.csv and scenario_cashflows.csv; allows in-memory routing adjustments.

### Core Logic
- **`engine.py`**: Annual operation loop. Defines `run_scenario()` and `run_all_scenarios()`.
- **`waterfall.py`**: LP distribution, redemption, and GP residual NAV logic. Key functions: `pay_lp_distribution()`, `redeem_lp()`, `available_liquidity()`.
- **`deal_model.py`**: Individual real estate deal cash flow model (NOI, debt service, capex, equity balance).
- **`portfolio_aggregator.py`**: Aggregates deal-level cash flows into portfolio-level RE cash flow (or merges top-down assumptions). Applies deal overrides.
- **`metrics.py`**: Calculates MOIC (cash and economic), IRRs (cash and economic).

### Data Models & Validation
- **`model_types.py`**: Pydantic models for all config/scenario/result objects (Scenario, ModelConfig, ScenarioResult, YearlyResult, etc.).
- **`deal_types.py`**: Pydantic models for deals (Deal, DealSet, RealEstatePortfolioYearResult).
- **`config_loader.py`**: YAML loading, Pydantic validation, ConfigError exception.
- **`validation.py`**: Scenario-level validation rules.

### Output & Reporting
- **`outputs.py`**: Writes CSV and Excel outputs. Formats worksheet headers and pivots summary data.
- **`reporting.py`**: Writes Markdown scenario report.
- **`report_html.py`**: Generates self-contained HTML report with embedded PNG charts as base64.
- **`chatgpt_export.py`**: Builds compact Markdown context for ChatGPT review.
- **`charts.py`**, **`charts_gp_lp.py`**: Generate Plotly/PNG charts for NAV, distributions, GP/LP splits.

### Auxiliary Modules
- **`tax.py`**: Post-processing module for tax analysis. Separate from core engine.
- **`utils.py`**: Utilities (merge_model, value_for_year, etc.).

## Key Concepts

### Waterfall & MOIC
- **LP Cash MOIC**: Based only on actual LP cash distributions received.
- **LP Economic MOIC**: May include LP's remaining NAV claim when the 2.0x hurdle has not been redeemed.
- **Hurdle Amount**: `initial_lp_capital × lp_hurdle_moic` (typically 2.0x).
- **Liquidity Constraint**: Flag raised if available liquidity < remaining LP hurdle at the terminal year.
- **GP Residual NAV**: NAV remaining to the GP after all LP distributions and waterfall logic.

### Scenario Horizon
- Default horizon is 20 years (diagnostic).
- Model stops early once LP cash hurdle is achieved (`year_hurdle_achieved`).
- Use `years_modelled`, `year_hurdle_achieved`, `years_until_lp_2x_cash_return` to check actual duration.

### Refinance & Liabilities
- Refinance events (scenario-level and deal-level) generate cash to Retained Cash or Reserve.
- A refinance liability is created; Fund NAV is net of that liability.
- GP residual NAV and economic hurdle tests are also net of refinance liabilities.

### Cashflow Routing (Phase 2)
- Generated RE cashflow and HF gains are routed to LP distributions, HF reinvestment, and Reserve by configured percentages.
- Percentages must sum to 100%.
- Routing is yaml-editable per scenario; can be adjusted via dashboard sliders (in-memory only).

### Backend Liquidity Strategy
- Models low-interim-distribution structure: RE cashflow mostly reinvested into HF during hold period.
- Scheduled "backend years" apply refinance-led liquidity assumptions plus reserve/HF support to test LP hurdle completion.
- Outside backend years, the ordinary hurdle trigger can still evaluate.

### LP Yield Policy (Phase 2)
- Optional fixed annual yield paid to LP before other routing.
- Sourced from RE cashflow, HF harvests, and Reserve (in priority order).
- Must reduce LP hurdle (`lp_cash_yield_policy.reduce_lp_hurdle = true`).

### Hurdle Completion Trigger
- Terminal logic: tests whether LP 2.0x target can be met by liquidating HF, using Reserve, Retained Cash, and optional final refinance.
- If total available liquidity ≥ remaining hurdle, scenario finishes.
- Can retry after unsuccessful year if eligibility conditions are met.
- Configuration keys: `hurdle_completion_trigger` in model_config.yaml.

## Testing

Tests are in `tests/`. Coverage includes:
- Engine mechanics (annual operation loop, sleeve operations).
- Waterfall logic (LP distribution, GP residual NAV).
- Cashflow routing, LP yield policy, refinance events.
- Bottom-up deal modeling.
- Calibration runs.
- Error handling.
- Tax analysis.

Example test runs:
```bash
pytest tests/test_engine_basic.py
pytest tests/test_waterfall.py -v
pytest tests/test_bottom_up_deals.py
```

## Common Development Tasks

### Adding a New Model Assumption
1. Add the assumption to the appropriate Pydantic model in `model_types.py` (or `deal_types.py`).
2. Update YAML schema comments in `model_config.yaml` or `scenarios.yaml`.
3. In `engine.py:run_scenario()`, merge the assumption from config/scenario (using `merge_model()`).
4. Use the assumption in the calculation logic (e.g., `engine.py`, `waterfall.py`, `deal_model.py`).
5. Add tests in `tests/`.

### Modifying Sleeve Logic
- **Real Estate**: Edit `deal_model.py` (individual deal) or `portfolio_aggregator.py` (portfolio aggregation).
- **Hedge Fund**: Edit `engine.py:run_scenario()` (appreciation, harvesting).
- **Reserve**: Edit `engine.py:run_scenario()` (appreciation).

### Changing Waterfall or Distribution Logic
- Edit `waterfall.py:pay_lp_distribution()`, `waterfall.py:redeem_lp()`, or related functions.
- Update tests in `tests/test_waterfall.py`.

### Adding New Outputs
- Add columns to `outputs.py:write_outputs()` (CSV/Excel).
- Add sections to `reporting.py:write_markdown_report()` (Markdown).
- Embed new data in `report_html.py` or charts (PNG).

### Debugging a Scenario
- Inspect YAML inputs in `inputs/scenarios.yaml`.
- Add print statements or pdb breakpoints in `engine.py:run_scenario()`.
- Check outputs: `outputs/scenario_summary.csv`, `outputs/scenario_cashflows.csv`.
- Run dashboard to visualize: `streamlit run dashboard/app.py`.

## Known Limitations

- No Monte Carlo. Model is deterministic.
- No frontend or database. YAML and file-based.
- No monthly periods. Annual only.
- No property-level debt amortization (aggregate debt schedules only).
- No bottom-up tax modeling (Phase 2 adds tax analysis, but post-processing only, not integrated into core engine).

## Output Files

Standard outputs from `run_model.py`:
- `scenario_summary.csv`: Scenario-level summary (MOIC, IRR, hurdle status, flags, etc.).
- `scenario_summary.xlsx`: Excel version with formatted sheets.
- `scenario_cashflows.csv`: Year-by-year cashflow detail (distributions, NAVs, sleeve operations).
- `scenario_flags.csv`: Flags raised per scenario (e.g., liquidity constraint, debt covenant breach).
- `scenario_report.md`: Markdown report with narrative observations and data tables.
- `chatgpt_model_context.md`: Compact Markdown for ChatGPT review (YAML assumptions, key outputs, flags).
- `report.html`: Self-contained HTML report with all charts embedded.
- `charts/`: PNG charts (NAV evolution, distribution timing, GP/LP splits).
- `deal_cashflows.csv` (if bottom-up): Deal-level cash flows.

Optional outputs (if tax_config.yaml exists):
- `tax_summary.csv`, `tax_yearly.csv`: Tax analysis results.
- (Merged into Excel if `output_excel_sheet: true`.)

Optional calibration outputs from `run_calibration.py`:
- `calibration_summary.csv`, `calibration_summary.xlsx`: Calibration variant results.
- `calibration_cashflows.csv`, `calibration_flags.csv`: Calibration detail.
- `calibration_report.md`: Calibration narrative.
