from __future__ import annotations

import itertools
from pathlib import Path
from typing import Any

import pandas as pd
from src.config_loader import load_inputs
from src.engine import run_scenario, result_dicts
from src.model_types import CashflowRoute, CashflowRoutingSettings


def main() -> None:
    root = Path(__file__).resolve().parent
    try:
        config, scenarios = load_inputs(root / "inputs")
    except Exception as exc:
        print(f"Failed to load inputs: {exc}")
        return

    # Base scenario for sensitivity
    base_scenario_name = "base_hit_everyone_happy"
    if base_scenario_name not in scenarios.scenarios:
        print(f"Base scenario {base_scenario_name} not found.")
        return
    base_scenario = scenarios.scenarios[base_scenario_name]

    # Sensitivity Grid
    hf_allocations = [0.10, 0.20, 0.30]
    hf_harvest_rates = [0.0, 0.25, 0.50]
    # RE Routing Policies (LP / HF / Reserve)
    routing_policies = [
        {"name": "Current", "re": [0.20, 0.50, 0.30], "hf": [0.20, 0.70, 0.10]},
        {"name": "More Aggressive HF Compounding", "re": [0.10, 0.75, 0.15], "hf": [0.10, 0.80, 0.10]},
        {"name": "Very Backend Heavy", "re": [0.00, 0.80, 0.20], "hf": [0.00, 0.90, 0.10]},
    ]

    backend_strategies = [
        {"name": "Refi Led", "refi_cap": 0.40, "hf_liq_cap": 0.85, "refi_first": True},
        {"name": "Balanced Liquidity", "refi_cap": 0.35, "hf_liq_cap": 0.85, "refi_first": True},
        {"name": "HF Led", "refi_cap": 0.15, "hf_liq_cap": 1.00, "refi_first": False},
        {"name": "No Refi", "refi_cap": 0.00, "hf_liq_cap": 1.00, "refi_first": False},
    ]
    
    trigger_thresholds = [0.0, 0.10, 0.50, 1.0, 1.25]

    results_data = []
    
    # Generate permutations
    grid = list(itertools.product(
        hf_allocations,
        hf_harvest_rates,
        routing_policies,
        backend_strategies,
        trigger_thresholds
    ))
    
    total_runs = len(grid)
    print(f"Starting sensitivity analysis: {total_runs} permutations...")

    for i, (hf_alloc, harvest, routing, backend_strategy, threshold) in enumerate(grid):
        if (i + 1) % 50 == 0:
            print(f"Processing run {i + 1}/{total_runs}...")
            
        # 1. Modify Config
        variant_config = config.model_copy(deep=True)
        
        # Adjust allocation
        variant_config.allocation.hedge_fund_allocation_pct = hf_alloc
        variant_config.allocation.reserve_allocation_pct = 0.05
        variant_config.allocation.real_estate_allocation_pct = 1.0 - hf_alloc - 0.05
        
        # Adjust trigger settings
        variant_config.hurdle_completion_trigger.minimum_lp_cash_moic_before_trigger = threshold
        variant_config.hurdle_completion_trigger.max_refi_pct_of_re_nav = backend_strategy["refi_cap"]
        variant_config.hurdle_completion_trigger.max_hf_liquidation_pct = backend_strategy["hf_liq_cap"]
        variant_config.backend_liquidity_strategy.enabled = True
        variant_config.backend_liquidity_strategy.target_years = [5, 7, 8, 10]
        variant_config.backend_liquidity_strategy.refi_first = backend_strategy["refi_first"]
        variant_config.backend_liquidity_strategy.max_refi_pct_of_re_nav = backend_strategy["refi_cap"]
        variant_config.backend_liquidity_strategy.max_hf_liquidation_pct = backend_strategy["hf_liq_cap"]
        variant_config.backend_liquidity_strategy.use_reserve = True
        
        # Adjust distribution/harvest policy
        variant_config.distribution_policy.hf_positive_return_harvest_rate = harvest
        
        # Adjust routing
        variant_config.cashflow_routing = CashflowRoutingSettings(
            enabled=True,
            re_cashflow=CashflowRoute(
                lp_distribution_pct=routing["re"][0],
                hf_reinvestment_pct=routing["re"][1],
                reserve_pct=routing["re"][2]
            ),
            hf_harvest=CashflowRoute(
                lp_distribution_pct=routing["hf"][0],
                hf_reinvestment_pct=routing["hf"][1],
                reserve_pct=routing["hf"][2]
            )
        )

        # 2. Run Scenario
        variant_label = (
            f"hf{hf_alloc:.0%}_harv{harvest:.0%}_{backend_strategy['name'].replace(' ', '')}_"
            f"{routing['name'].replace(' ', '')}_thr{threshold:.2f}x"
        )
        
        try:
            res = run_scenario(variant_label, base_scenario, variant_config)
            
            # 3. Collect Data
            summary = res.summary
            
            # Calculate funding split if trigger executed
            total_trigger = 0.0
            hf_pct = 0.0
            refi_pct = 0.0
            
            if summary.get("hurdle_trigger_executed"):
                total_trigger = (
                    summary.get("total_trigger_cash_from_hf_liquidation", 0.0) +
                    summary.get("total_trigger_cash_from_refi", 0.0) +
                    summary.get("total_trigger_cash_from_re_sale", 0.0) +
                    summary.get("total_trigger_cash_from_retained_cash", 0.0) +
                    summary.get("total_trigger_cash_from_reserve", 0.0)
                )
                if total_trigger > 0:
                    hf_pct = summary.get("total_trigger_cash_from_hf_liquidation", 0.0) / total_trigger
                    refi_pct = summary.get("total_trigger_cash_from_refi", 0.0) / total_trigger

            results_data.append({
                "hf_allocation": hf_alloc,
                "hf_harvest_rate": harvest,
                "backend_strategy": backend_strategy["name"],
                "refi_cap": backend_strategy["refi_cap"],
                "hf_liquidation_cap": backend_strategy["hf_liq_cap"],
                "routing_policy": routing["name"],
                "trigger_threshold": threshold,
                "lp_cash_moic": summary["lp_cash_moic"],
                "lp_hurdle_achieved": summary["lp_hurdle_achieved"],
                "year_hurdle_achieved": summary["year_hurdle_achieved"],
                "gp_residual_nav": summary["gp_residual_nav"],
                "total_gp_economics": summary["gp_total_economics"],
                "trigger_executed": summary.get("hurdle_trigger_executed", False),
                "trigger_hf_pct": hf_pct,
                "trigger_refi_pct": refi_pct,
                "final_fund_nav": summary["final_fund_nav"]
            })
        except Exception as exc:
            print(f"Error in variant {variant_label}: {exc}")

    # 4. Save and Report
    df = pd.DataFrame(results_data)
    output_dir = root / "outputs"
    output_dir.mkdir(exist_ok=True)
    
    df.to_csv(output_dir / "sensitivity_analysis.csv", index=False)
    print(f"Raw data saved to {output_dir}/sensitivity_analysis.csv")
    
    generate_asher_report(df, output_dir / "asher_summary.md")


def df_to_markdown_simple(df: pd.DataFrame) -> str:
    """Manual markdown table generator to avoid 'tabulate' dependency."""
    if df.empty:
        return ""
    
    # Header
    cols = list(df.columns)
    if df.index.name:
        header = [df.index.name] + cols
    else:
        header = ["Index"] + cols
        
    lines = ["| " + " | ".join(str(h) for h in header) + " |"]
    lines.append("| " + " | ".join(["---"] * len(header)) + " |")
    
    # Rows
    for idx, row in df.iterrows():
        formatted_row = [str(idx)] + [str(v) if not isinstance(v, float) else f"{v:,.2f}" for v in row]
        lines.append("| " + " | ".join(formatted_row) + " |")
    
    return "\n".join(lines)


def generate_asher_report(df: pd.DataFrame, path: Path) -> None:
    # Bucketing
    def get_bucket(row):
        if not row["lp_hurdle_achieved"]:
            return "Not Reached"
        yr = row["year_hurdle_achieved"]
        if yr <= 5: return "Target (<5yr)"
        if yr <= 8: return "Moderate (<8yr)"
        if yr <= 10: return "Slow (<10yr)"
        return "Lagging (>10yr)"

    df["redemption_bucket"] = df.apply(get_bucket, axis=1)
    
    # Aggregating
    summary = df.groupby("redemption_bucket").agg({
        "lp_cash_moic": "count",
        "gp_residual_nav": "mean",
        "trigger_hf_pct": "mean",
        "trigger_refi_pct": "mean"
    }).rename(columns={"lp_cash_moic": "count"})
    summary.index.name = "Timing Bucket"
    
    report = [
        "# Sensitivity Analysis - Executive Summary for Asher",
        "",
        "This report evaluates the impact of liquidity engineering strategies on the fund structure.",
        "",
        "## Outcomes by Redemption Timing",
        df_to_markdown_simple(summary),
        "",
        "## Key Observations",
        "1. **Liquidity Mix:** Successful redemptions rely on a specific balance between HF liquidation and property refinancing.",
        f"2. **Success Rate:** Out of {len(df)} permutations, {len(df[df['lp_hurdle_achieved']])} reached the 2.0x hurdle within the model horizon.",
        "",
        "## Top 5 GP Value Scenarios (Successful Redemption)",
        df_to_markdown_simple(df[df["lp_hurdle_achieved"]].sort_values("gp_residual_nav", ascending=False).head(5)[[
            "hf_allocation",
            "hf_harvest_rate",
            "backend_strategy",
            "refi_cap",
            "hf_liquidation_cap",
            "routing_policy",
            "year_hurdle_achieved",
            "gp_residual_nav",
        ]]),
        "",
        "---",
        "Note: Detailed raw data is available in `sensitivity_analysis.csv` for further pivot analysis."
    ]
    
    with open(path, "w") as f:
        f.write("\n".join(report))
    print(f"Executive summary saved to {path}")


if __name__ == "__main__":
    main()
