# Stage 1 Dashboard

Run from the project root:

```powershell
streamlit run dashboard/app.py
```

The dashboard reads:

- `outputs/scenario_cashflows.csv`
- `outputs/scenario_summary.csv`
- `inputs/model_config.yaml`
- `inputs/scenarios.yaml`

If the summary CSV is missing, it falls back to the `Summary` tab in `outputs/scenario_summary.xlsx`.

The app uses the project-level `.streamlit/config.toml` to force a light theme so Streamlit chrome and Plotly charts use a consistent presentation style.

## Column Assumptions

The app uses existing model output columns only. It does not run the model or fabricate new scenario data.

Explicit columns used from `scenario_summary.csv`:

- `scenario`
- `description`
- `lp_initial_capital`
- `lp_cash_distributions`
- `lp_cash_moic`
- `lp_economic_moic`
- `lp_cash_irr`
- `lp_economic_irr`
- `lp_hurdle_amount`
- `lp_hurdle_achieved`
- `year_hurdle_achieved`
- `liquidity_constrained`
- `gp_total_economics`
- `gp_total_economics_pct_initial_lp_capital`
- `gp_residual_nav`
- `final_fund_nav`
- `all_flags`

Explicit columns used from `scenario_cashflows.csv`:

- `scenario`
- `year`
- `lp_distribution`
- `lp_cumulative_distribution`
- `lp_remaining_hurdle`
- `fund_nav`
- `net_re_cashflow`
- `hf_harvest`
- `refinance_proceeds`
- `re_asset_mgmt_fee`
- `re_closing_nav`
- `hf_closing_nav`
- `reserve_closing_nav`
- `retained_cash`
- `event_flag`

## Fallbacks and Inferences

- LP economic value over time is calculated as cumulative LP cash distributions plus the lesser of fund NAV and remaining LP hurdle.
- Reserve drawdown is inferred as `reserve_opening_nav - reserve_closing_nav`, clipped at zero, because the model does not currently emit an explicit reserve drawdown column.
- If a required column is missing, the affected chart is skipped or simplified and a note is shown in the dashboard.
- Scenario display names are presentation labels mapped in `SCENARIO_DISPLAY_NAMES`; they do not change model identifiers.
- Selected-scenario assumptions are displayed from YAML in a collapsible section. They are read-only and do not re-run the model.

## Scope

This is a presentation dashboard for the eight pre-baked scenarios. The routing sliders rerun those same scenarios in memory only, using temporary routing assumptions. They do not edit YAML or overwrite CSV/Excel outputs.

The sidebar also includes a custom scenario form. Pressing **Run custom scenario** creates a temporary in-memory scenario and adds it to the selector as `Custom dashboard scenario`. This custom scenario is not saved to YAML and is not written to the model output files.
