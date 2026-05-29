"""Generate a self-contained HTML report with all charts and summary tables."""

from __future__ import annotations

import base64
from pathlib import Path
from datetime import datetime
import pandas as pd


def _img_to_base64(path: Path) -> str:
    """Convert an image file to a base64 data URI."""
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{b64}"


def _fmt_m(value) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "—"
    v = float(value) / 1e6
    if abs(v) >= 10:
        return f"${v:.0f}M"
    return f"${v:.1f}M"


def _fmt_pct(value) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "—"
    return f"{float(value):.1%}"


def _fmt_x(value) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return "—"
    return f"{float(value):.2f}x"


GLOBAL_ASSUMPTION_DETAILS = {
    "model.initial_lp_capital": "CRITICAL. The total equity basis for all MOIC and IRR calculations.",
    "allocation.hedge_fund_allocation_pct": "CRITICAL. Determines the Day 1 'Liquid Alpha' pool used to accelerate the hurdle.",
    "allocation.real_estate_allocation_pct": "CRITICAL. The primary capital allocated to property acquisitions.",
    "waterfall.lp_hurdle_moic": "CRITICAL. The terminal target. The engine runs until this cash multiple is returned.",
    "waterfall.require_liquidity_for_lp_redemption": "HIGH. If 'Yes', the LP is only paid when the fund has actual cash available.",
    "cashflow_routing.re_cashflow.lp_distribution_pct": "HIGH. Controls how much property profit goes to the LP vs. staying in the fund.",
    "cashflow_routing.hf_harvest.lp_distribution_pct": "HIGH. Controls how much liquid profit is 'harvested' to pay down the LP hurdle.",
    "hurdle_completion_trigger.enabled": "HIGH. The automated 'exit scanner' that triggers asset sales to finish the LP payout.",
    "backend_liquidity_strategy.enabled": "HIGH. A scheduled plan to refinance properties to generate LP liquidity.",
    "real_estate.mode": "Determines if the model uses general assumptions (Top-Down) or specific properties (Bottom-Up).",
    "lp_cash_yield_policy.enabled": "If enabled, the fund prioritizes a target annual yield to the LP before other routing.",
    "liquidity.max_refinance_or_sale_capacity_pct_of_re_nav": "Limits how much cash can be pulled out of properties in a single event.",
}


def build_html_report(
    summary_csv: str | Path = "outputs/scenario_summary.csv",
    charts_dir: str | Path = "outputs/charts",
    output_path: str | Path = "outputs/report.html",
    title: str = "Hybrid Fund Model — Scenario Report",
    config: dict[str, Any] | None = None,
    scenarios: dict[str, Any] | None = None,
) -> Path:
    """Build a self-contained HTML report with all charts and tables."""

    summary_csv = Path(summary_csv)
    charts_dir = Path(charts_dir)
    output_path = Path(output_path)

    sf = pd.read_csv(summary_csv)
    sf = sf.sort_values(["lp_hurdle_achieved", "year_hurdle_achieved"],
                         ascending=[False, True]).reset_index(drop=True)

    # ── collect chart paths ──────────────────────────────────────────────
    waterfall_paths = {}
    for p in sorted(charts_dir.glob("waterfall_*.png")):
        name = p.stem.replace("waterfall_", "", 1)
        waterfall_paths[name] = p

    gp_lp_paths = {}
    for p in sorted(charts_dir.glob("gp_lp_split_*.png")):
        name = p.stem.replace("gp_lp_split_", "", 1)
        gp_lp_paths[name] = p

    timeline_path = charts_dir / "hurdle_timeline.png"
    matrix_path = charts_dir / "outcome_matrix.png"
    heatmap_path = charts_dir / "sensitivity_heatmap.png"

    # ── build HTML ──────────────────────────────────────────────────────
    parts: list[str] = []

    def h(level, text):
        return f"<h{level}>{text}</h{level}>"

    def p(text):
        return f"<p>{text}</p>"

    def img_tag(path: Path, alt: str = "", max_width: str = "100%") -> str:
        if not path.exists():
            return f"<p><em>Chart not found: {path.name}</em></p>"
        b64 = _img_to_base64(path)
        return f'<img src="{b64}" alt="{alt}" style="max-width:{max_width}; border:1px solid #ddd; border-radius:4px; margin:12px 0;">'

    def table_html(df: pd.DataFrame, columns: list[str], headers: list[str] | None = None) -> str:
        if headers is None:
            headers = columns
        rows = []
        rows.append("<thead><tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr></thead>")
        rows.append("<tbody>")
        for _, row in df.iterrows():
            cells = []
            for col in columns:
                val = row.get(col, "—")
                cells.append(f"<td>{val}</td>")
            rows.append("<tr>" + "".join(cells) + "</tr>")
        rows.append("</tbody>")
        return '<table class="data-table">' + "".join(rows) + "</table>"

    def _fmt_val(val: Any) -> str:
        if val is None or val == "": return "—"
        if isinstance(val, bool): return "Yes" if val else "No"
        if isinstance(val, list): return ", ".join([_fmt_val(v) for v in val])
        if isinstance(val, float):
            if 0 < abs(val) < 1: return f"{val:.1%}"
            return f"{val:,.2f}"
        if isinstance(val, int): return f"{val:,}"
        return str(val)

    # ── CSS ─────────────────────────────────────────────────────────────
    css = """
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 1200px; margin: 0 auto; padding: 24px;
            background: #fafafa; color: #2c3e50; line-height: 1.5;
        }
        h1 { font-size: 22px; border-bottom: 2px solid #2c3e50; padding-bottom: 8px; }
        h2 { font-size: 17px; margin-top: 36px; color: #2c3e50; border-bottom: 1px solid #bdc3c7; padding-bottom: 4px; }
        h3 { font-size: 14px; margin-top: 24px; color: #34495e; }
        .subtitle { color: #7f8c8d; font-size: 13px; margin-top: -4px; }
        .data-table {
            border-collapse: collapse; width: 100%; margin: 12px 0;
            font-size: 12px;
        }
        .data-table th {
            background: #2c3e50; color: white; padding: 6px 10px;
            text-align: left; font-weight: 600; white-space: nowrap;
        }
        .data-table td {
            padding: 5px 10px; border-bottom: 1px solid #ecf0f1;
        }
        .data-table tr:nth-child(even) td { background: #f8f9fa; }
        .data-table tr:hover td { background: #eaf2f8; }
        .achieved { color: #27ae60; font-weight: 600; }
        .failed { color: #e74c3c; font-weight: 600; }
        .section { margin-bottom: 40px; }
        .chart-container { text-align: center; margin: 16px 0; }
        .footer {
            margin-top: 48px; padding-top: 16px;
            border-top: 1px solid #bdc3c7; color: #7f8c8d;
            font-size: 11px; text-align: center;
        }
        .key-findings {
            background: #eaf2f8; border-left: 4px solid #2e86c1;
            padding: 12px 16px; margin: 16px 0; border-radius: 0 4px 4px 0;
            font-size: 13px;
        }
        .assumptions-box {
            background: #fdfefe; border: 1px solid #d5d8dc;
            padding: 10px; border-radius: 4px; font-size: 11px;
            margin: 10px 0;
        }
        .assumptions-box table { width: 100%; border-collapse: collapse; }
        .assumptions-box td { padding: 3px 8px; border-bottom: 1px solid #f2f3f4; }
        .assumptions-box td:first-child { font-weight: 600; color: #7f8c8d; width: 30%; }
    </style>
    """

    parts.append("<!DOCTYPE html><html><head><meta charset='utf-8'>")
    parts.append(f"<title>{title}</title>")
    parts.append(css)
    parts.append("</head><body>")

    # ── header ──────────────────────────────────────────────────────────
    parts.append(h(1, title))
    parts.append(p(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"))
    parts.append(p("Deterministic annual scenario model. LP hurdle achievement is based on actual cash distributions received, not NAV appreciation. Scenarios run on a 20-year diagnostic horizon; the engine stops early once the LP cash hurdle is achieved."))

    # ── global assumptions ──────────────────────────────────────────────
    if config:
        parts.append(h(2, "Global Assumptions"))
        from src.chatgpt_export import GLOBAL_ASSUMPTION_KEYS, _get_nested
        ga_rows = []
        for key, label in GLOBAL_ASSUMPTION_KEYS:
            val = _get_nested(config, key)
            detail = GLOBAL_ASSUMPTION_DETAILS.get(key, "Standard operational parameter.")
            ga_rows.append({
                "Assumption": label, 
                "Value": _fmt_val(val),
                "Context / Importance": detail
            })
        parts.append(table_html(pd.DataFrame(ga_rows), ["Assumption", "Value", "Context / Importance"]))

    # ── key findings ────────────────────────────────────────────────────
    n_total = len(sf)
    n_achieved = sf["lp_hurdle_achieved"].sum()
    n_failed = n_total - n_achieved
    avg_years = sf.loc[sf["lp_hurdle_achieved"], "year_hurdle_achieved"].mean()
    best_gp = sf.loc[sf["gp_residual_nav"].idxmax(), "scenario"] if sf["gp_residual_nav"].max() > 0 else "N/A"
    best_gp_val = _fmt_m(sf["gp_residual_nav"].max())

    parts.append('<div class="key-findings">')
    parts.append(f"<strong>Key Findings:</strong> {n_achieved} of {n_total} scenarios achieve the LP 2.0x hurdle. ")
    parts.append(f"Average time to hurdle: {avg_years:.1f} years. ")
    parts.append(f"Highest GP residual: <strong>{best_gp}</strong> ({best_gp_val}). ")
    parts.append(f"{n_failed} scenario(s) fail to reach the hurdle within 20 years.")
    parts.append("</div>")

    # ── summary table ───────────────────────────────────────────────────
    parts.append(h(2, "Scenario Summary"))

    summary_cols = [
        ("scenario", "Scenario"),
        ("years_modelled", "Years"),
        ("lp_cash_moic", "LP Cash MOIC"),
        ("lp_cash_irr", "LP Cash IRR"),
        ("year_hurdle_achieved", "Year 2x"),
        ("gp_residual_nav", "GP Residual"),
        ("gp_total_economics", "GP Total Econ"),
        ("total_trigger_cash_from_hf_liquidation", "HF Liq Used"),
        ("total_trigger_cash_from_refi", "Refi Used"),
    ]
    avail_cols = [c for c, _ in summary_cols if c in sf.columns]
    headers = [h for c, h in summary_cols if c in sf.columns]

    # Format values
    display_df = sf[avail_cols].copy()
    for col in display_df.columns:
        if col == "scenario":
            continue
        if col in ("lp_cash_irr",):
            display_df[col] = display_df[col].apply(_fmt_pct)
        elif col in ("lp_cash_moic",):
            display_df[col] = display_df[col].apply(_fmt_x)
        elif col == "year_hurdle_achieved":
            display_df[col] = display_df[col].apply(
                lambda v: f"Y{int(v)}" if pd.notna(v) and v > 0 else "—")
        elif col in ("gp_residual_nav", "gp_total_economics",
                      "total_trigger_cash_from_hf_liquidation",
                      "total_trigger_cash_from_refi"):
            display_df[col] = display_df[col].apply(_fmt_m)
        elif col == "years_modelled":
            display_df[col] = display_df[col].apply(lambda v: f"Y{int(v)}")

    parts.append(table_html(display_df, avail_cols, headers))

    # ── overview charts ─────────────────────────────────────────────────
    parts.append(h(2, "Overview Charts"))

    parts.append(h(3, "LP Hurdle Timeline"))
    parts.append(p("Green = hurdle achieved. Red hatched = not reached by year 20."))
    parts.append(f'<div class="chart-container">{img_tag(timeline_path, "Hurdle Timeline")}</div>')

    parts.append(h(3, "Outcome Matrix"))
    parts.append(f'<div class="chart-container">{img_tag(matrix_path, "Outcome Matrix")}</div>')

    if heatmap_path.exists():
        parts.append(h(3, "Sensitivity Heatmap"))
        parts.append(p("Years to 2.0x across HF allocation and harvest rate. Green = fast, red = slow, grey = not achieved."))
        parts.append(f'<div class="chart-container">{img_tag(heatmap_path, "Sensitivity Heatmap")}</div>')

    # ── tax analysis ────────────────────────────────────────────────────
    tax_summary_csv = Path(summary_csv).parent / "tax_summary.csv"
    tax_yearly_csv = Path(summary_csv).parent / "tax_yearly.csv"
    tax_comp_path = charts_dir / "after_tax_comparison.png"

    if tax_summary_csv.exists() and tax_comp_path.exists():
        parts.append(h(2, "Tax Analysis (Ideal LP — Real Estate Professional)"))
        parts.append(p("The following shows the impact of real estate depreciation and interest expense deductions on after-tax returns. "
                       "Assumes 37% federal marginal rate, 100% bonus depreciation (OBBBA 2025), 25% cost segregation, "
                       "20% land allocation, 27.5-year residential straight-line. "
                       "This is a post-processing analysis — the LP 2x hurdle and engine cash flows are unaffected."))

        # Tax comparison chart
        parts.append(h(3, "After-Tax vs Pre-Tax Comparison"))
        parts.append(f'<div class="chart-container">{img_tag(tax_comp_path, "After-Tax Comparison")}')

        # Tax summary table
        try:
            tf = pd.read_csv(tax_summary_csv)
            tf = tf.sort_values("final_after_tax_moic", ascending=False)
            tax_display = tf[["scenario", "total_depreciation", "total_interest_deductions",
                              "total_tax_savings", "final_after_tax_moic", "final_after_tax_irr"]].copy()
            tax_display["total_depreciation"] = tax_display["total_depreciation"].apply(_fmt_m)
            tax_display["total_interest_deductions"] = tax_display["total_interest_deductions"].apply(_fmt_m)
            tax_display["total_tax_savings"] = tax_display["total_tax_savings"].apply(_fmt_m)
            tax_display["final_after_tax_moic"] = tax_display["final_after_tax_moic"].apply(_fmt_x)
            tax_display["final_after_tax_irr"] = tax_display["final_after_tax_irr"].apply(_fmt_pct)
            tax_renamed = tax_display.rename(columns={
                "scenario": "Scenario",
                "total_depreciation": "Total Depreciation",
                "total_interest_deductions": "Total Interest Deductions",
                "total_tax_savings": "Total Tax Savings",
                "final_after_tax_moic": "After-Tax MOIC",
                "final_after_tax_irr": "After-Tax IRR",
            })
            parts.append(table_html(tax_renamed, list(tax_renamed.columns)))
        except Exception:
            parts.append("<p><em>Tax summary table could not be loaded.</em></p>")
        parts.append("</div>")

        # Per-scenario tax shield waterfalls
        tax_shield_paths = sorted(charts_dir.glob("tax_shield_*.png"))
        if tax_shield_paths:
            parts.append(h(3, "Tax Shield Composition by Scenario"))
            parts.append(p("Annual deductions from bonus depreciation, straight-line depreciation, and interest expense. "
                           "Green line shows cumulative tax savings over time."))
            for tsp in tax_shield_paths:
                sn = tsp.stem.replace("tax_shield_", "", 1).replace("_", " ")
                parts.append(f'<div class="chart-container">{img_tag(tsp, f"Tax Shield: {sn}")}</div>')

    # ── per-scenario detail ─────────────────────────────────────────────
    parts.append(h(2, "Scenario Detail"))

    for _, row in sf.iterrows():
        name = row["scenario"]
        achieved = row["lp_hurdle_achieved"]
        status = "achieved" if achieved else "failed"

        display_name = name.replace("_", " ")
        parts.append(f'<div class="section">')
        parts.append(h(3, f"{display_name} — <span class='{status}'>{'2.0x Achieved' if achieved else 'Not Achieved'}</span>"))

        # Key stats line
        year_str = f"Y{int(row['year_hurdle_achieved'])}" if achieved and pd.notna(row.get("year_hurdle_achieved")) else "—"
        stats_line = (
            f"Years modelled: <strong>{int(row['years_modelled'])}</strong>  │  "
            f"LP Cash MOIC: <strong>{_fmt_x(row.get('lp_cash_moic'))}</strong>  │  "
            f"LP Cash IRR: <strong>{_fmt_pct(row.get('lp_cash_irr'))}</strong>  │  "
            f"Year 2x: <strong>{year_str}</strong>  │  "
            f"GP Residual: <strong>{_fmt_m(row.get('gp_residual_nav'))}</strong>  │  "
            f"GP Total Econ: <strong>{_fmt_m(row.get('gp_total_economics'))}</strong>"
        )
        parts.append(p(stats_line))

        # Scenario assumptions box
        if scenarios and name in scenarios:
            s_data = scenarios[name]
            re = s_data.get("real_estate", {})
            hf = s_data.get("hedge_fund", {})
            
            from src.chatgpt_export import _scenario_overrides
            overrides = _scenario_overrides(s_data)
            
            parts.append('<div class="assumptions-box">')
            parts.append('<table>')
            parts.append(f'<tr><td>Description</td><td>{s_data.get("description", "—")}</td></tr>')
            parts.append(f'<tr><td>Diagnostic Horizon</td><td>{s_data.get("years", "—")} years</td></tr>')
            parts.append(f'<tr><td>Initial NOI Yield</td><td>{_fmt_val(re.get("initial_noi_yield"))}</td></tr>')
            parts.append(f'<tr><td>NOI Annual Growth</td><td>{_fmt_val(re.get("annual_noi_growth"))}</td></tr>')
            parts.append(f'<tr><td>NAV Appreciation</td><td>{_fmt_val(re.get("annual_nav_appreciation"))}</td></tr>')
            parts.append(f'<tr><td>Gross Rent Yield</td><td>{_fmt_val(re.get("gross_rent_yield"))}</td></tr>')
            parts.append(f'<tr><td>HF Annual Returns</td><td>{_fmt_val(hf.get("annual_returns"))}</td></tr>')
            if overrides:
                parts.append(f'<tr><td>Custom Overrides</td><td>{overrides}</td></tr>')
            parts.append('</table>')
            parts.append('</div>')

        # Waterfall chart — lookup by underscore key, display with spaces
        display_name = name.replace("_", " ")
        wp = waterfall_paths.get(name)
        if wp and wp.exists():
            parts.append(f'<div class="chart-container">{img_tag(wp, f"Waterfall: {display_name}")}</div>')

        # GP vs LP split chart
        glp = gp_lp_paths.get(name)
        if glp and glp.exists():
            parts.append(f'<div class="chart-container">{img_tag(glp, f"GP vs LP Split: {display_name}")}</div>')

        parts.append("</div>")

    # ── footer ──────────────────────────────────────────────────────────
    parts.append('<div class="footer">')
    parts.append(f"Hybrid Fund Economic Model — {n_total} scenarios — {datetime.now().strftime('%Y-%m-%d')}")
    parts.append("</div>")

    parts.append("</body></html>")

    # ── write ───────────────────────────────────────────────────────────
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(parts), encoding="utf-8")
    print(f"Saved: {output_path} ({output_path.stat().st_size / 1024 / 1024:.1f} MB)")
    return output_path


if __name__ == "__main__":
    build_html_report()
