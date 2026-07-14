"""Chart module for hybrid fund scenario visualization.

Produces three chart types:
  1. Dual Waterfall  — per-scenario annual sources/uses + LP accumulation
                       (+ deal metrics panel for bottom-up scenarios)
  2. LP Hurdle Timeline — one-row-per-scenario overview
  3. Scenario Outcome Matrix — tabular heatmap of key outcomes
  4. Sensitivity Heatmap — 2D parameter grid showing years-to-2x
"""

from __future__ import annotations

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from pathlib import Path


# ── colour palette ──────────────────────────────────────────────────────────
# Value creation (sources)
C_APPRECIATION = "#4A90D9"
C_HF_RETURN    = "#7B68EE"
C_REFI         = "#48C9B0"
C_RE_SALE      = "#1ABC9C"

# Cash uses (routing)
C_DISTRIBUTED  = "#58D68D"
C_REINVESTED   = "#F0B27A"
C_RESERVE      = "#AEB6BF"

# LP / GP
C_LP_CUM       = "#2E86C1"
C_HURDLE       = "#E74C3C"
C_GP_RES       = "#F39C12"
C_FUND_NAV     = "#2C3E50"

# Trigger
C_TRIG_BG      = "#FADBD8"
C_TRIG_FG      = "#E74C3C"

# Deal metrics
C_ASSET_VAL    = "#2980B9"
C_DEBT         = "#C0392B"
C_DSRC         = "#8E44AD"
C_DEAL_NAV     = "#16A085"
C_REFI_DEAL    = "#27AE60"

# Grid
C_GRID         = "#D5D8DC"


# ── helpers ─────────────────────────────────────────────────────────────────
def _fmt_m(value: float) -> str:
    v = value / 1e6
    if abs(v) >= 10:
        return f"${v:.0f}M"
    return f"${v:.1f}M"


def _dollar_formatter():
    return mticker.FuncFormatter(lambda x, _: _fmt_m(x))


def _legend_patches(handles_labels: list[tuple[str, str]]) -> list[mpatches.Patch]:
    return [mpatches.Patch(color=c, label=l) for l, c in handles_labels]


def _save_fig(fig, save_path: Path, artists=None):
    save_path.parent.mkdir(parents=True, exist_ok=True)
    kwargs = dict(dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    if artists:
        kwargs["bbox_extra_artists"] = artists
    fig.savefig(save_path, **kwargs)
    print(f"Saved: {save_path}")


# ── 1. DUAL WATERFALL ──────────────────────────────────────────────────────
def build_dual_waterfall(
    df: pd.DataFrame,
    scenario_name: str,
    deal_df: pd.DataFrame | None = None,
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    df = df.sort_values("year").reset_index(drop=True)
    years = df["year"].values
    n = len(years)
    mode = df["real_estate_mode"].iloc[0] if "real_estate_mode" in df.columns else "top_down"
    is_bottom_up = mode == "bottom_up" and deal_df is not None and len(deal_df) > 0

    hurdle = df["lp_remaining_hurdle"].iloc[0] + df["lp_cumulative_distribution"].iloc[0]
    hurdle_m = hurdle / 1e6

    # Per-year components
    re_apprec  = df["re_opening_nav"].values * df["re_appreciation_rate"].values
    hf_gross   = df["hf_opening_nav"].values * df["hf_return"].values
    refi       = df["refinance_proceeds"].values
    re_sale    = df["re_nav_sold_for_hurdle"].values
    reinvested = df["total_cash_reinvested"].values
    distributed = df["lp_distribution"].values
    reserved   = df["total_cash_reserved"].values
    total_sources = re_apprec + hf_gross + refi + re_sale
    net = total_sources - (reinvested + distributed + reserved)

    trigger_mask = df["hurdle_trigger_executed"] == True
    trigger_years = df.loc[trigger_mask, "year"].values
    has_trigger = len(trigger_years) > 0
    lp_achieved = has_trigger

    # ── figure layout ────────────────────────────────────────────────────
    if is_bottom_up:
        fig = plt.figure(figsize=(17, 15))
        gs = fig.add_gridspec(3, 1, height_ratios=[1.0, 1.0, 0.8], hspace=0.40,
                               top=0.94, bottom=0.14, left=0.07, right=0.93)
        ax1 = fig.add_subplot(gs[0])
        ax2 = fig.add_subplot(gs[1])
        ax3 = fig.add_subplot(gs[2])
    else:
        fig = plt.figure(figsize=(17, 12))
        gs = fig.add_gridspec(2, 1, height_ratios=[1.1, 1], hspace=0.38,
                               top=0.94, bottom=0.14, left=0.07, right=0.93)
        ax1 = fig.add_subplot(gs[0])
        ax2 = fig.add_subplot(gs[1])
        ax3 = None

    fig.patch.set_facecolor("#FAFAFA")
    mode_label = "Bottom-Up" if mode == "bottom_up" else "Top-Down"
    fig.suptitle(f"{scenario_name}", fontsize=15, fontweight="bold",
                 color="#2C3E50", y=0.98)
    fig.text(0.5, 0.955, f"{mode_label}  •  {n} years modelled",
             ha="center", fontsize=9, color="#7F8C8D", style="italic")

    for ax in (ax1, ax2):
        ax.set_facecolor("#F8F9FA")
        ax.grid(axis="y", color=C_GRID, linewidth=0.5, linestyle="--")

    bw = 0.6
    x = np.arange(n)

    # ── TOP PANEL: Sources & Uses ─────────────────────────────────────────
    ax1.set_title("Annual Sources & Uses", fontsize=12, fontweight="bold",
                   color="#2C3E50", pad=10)

    ax1.bar(x, re_apprec / 1e6, bw, color=C_APPRECIATION, alpha=0.9, label="RE Appreciation")
    ax1.bar(x, hf_gross / 1e6, bw, bottom=re_apprec / 1e6,
            color=C_HF_RETURN, alpha=0.9, label="HF Gross Return")
    bottom_src = (re_apprec + hf_gross) / 1e6
    ax1.bar(x, refi / 1e6, bw, bottom=bottom_src,
            color=C_REFI, alpha=0.9, label="Refinance Proceeds")
    if re_sale.sum() > 0:
        bottom_src2 = bottom_src + refi / 1e6
        ax1.bar(x, re_sale / 1e6, bw, bottom=bottom_src2,
                color=C_RE_SALE, alpha=0.9, label="RE Sale Proceeds")

    ax1.bar(x, -distributed / 1e6, bw, color=C_DISTRIBUTED, alpha=0.85, label="LP Distribution")
    ax1.bar(x, -reinvested / 1e6, bw, bottom=-distributed / 1e6,
            color=C_REINVESTED, alpha=0.85, label="HF Reinvestment")
    ax1.bar(x, -reserved / 1e6, bw, bottom=-(distributed + reinvested) / 1e6,
            color=C_RESERVE, alpha=0.85, label="Reserve Addition")

    ax1.plot(x, net / 1e6, "o-", color=C_FUND_NAV, linewidth=2,
             markersize=5, label="Net Sources − Uses", zorder=5)
    ax1.axhline(0, color="#2C3E50", linewidth=0.8)

    if has_trigger:
        ty = trigger_years[0]
        idx = int(np.where(years == ty)[0][0])
        ax1.axvspan(idx - 0.45, idx + 0.45, alpha=0.18, color=C_TRIG_BG, zorder=0)
        # Place trigger label to the right if room, otherwise to the left
        x_label = idx + 1.5 if idx < n - 3 else idx - 1.5
        y_label = 0.0  # at zero line, clear of title
        ax1.annotate(
            f"TRIGGER Y{int(ty)}",
            xy=(idx, 0), xytext=(x_label, y_label),
            fontsize=8.5, fontweight="bold", color=C_TRIG_FG,
            ha="left" if idx < n - 3 else "right", va="center",
            arrowprops=dict(arrowstyle="->", color=C_TRIG_FG, lw=1.2),
            bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
                      edgecolor=C_TRIG_FG, alpha=0.95), zorder=10,
        )

    ax1.set_xticks(x)
    ax1.set_xticklabels([])  # remove top x-labels; bottom panel has them
    ax1.set_ylabel("Value ($M)")
    ax1.yaxis.set_major_formatter(_dollar_formatter())

    legend_items = [
        ("RE Appreciation", C_APPRECIATION), ("HF Gross Return", C_HF_RETURN),
        ("Refinance Proceeds", C_REFI), ("LP Distribution", C_DISTRIBUTED),
        ("HF Reinvestment", C_REINVESTED), ("Reserve Addition", C_RESERVE),
        ("Net Sources − Uses", C_FUND_NAV),
    ]
    ax1.legend(handles=_legend_patches(legend_items), loc="upper center",
               fontsize=7.5, framealpha=0.95, ncol=7, handlelength=1.0,
               columnspacing=0.7, bbox_to_anchor=(0.5, -0.06), borderaxespad=0.)

    # ── BOTTOM PANEL: LP Cash Accumulation ────────────────────────────────
    ax2.set_title(
        f"LP Cash Accumulation  —  Hurdle: {_fmt_m(hurdle)} / 2.0x",
        fontsize=12, fontweight="bold", color="#2C3E50", pad=10,
    )

    lp_cum = df["lp_cumulative_distribution"].values / 1e6
    annual_dist = df["lp_distribution"].values / 1e6

    ax2.fill_between(x, 0, lp_cum, alpha=0.12, color=C_LP_CUM)
    ax2.plot(x, lp_cum, "o-", color=C_LP_CUM, linewidth=2.5,
             markersize=6, zorder=5, label="Cumulative LP Distribution")
    ax2.bar(x, annual_dist, bw * 0.65, color=C_DISTRIBUTED, alpha=0.65,
            label="Annual LP Distribution", zorder=4)
    ax2.axhline(hurdle_m, color=C_HURDLE, linewidth=2, linestyle="--",
                zorder=6, label=f"Hurdle: {_fmt_m(hurdle)} / 2.0x")

    for i in range(n):
        if lp_cum[i] < hurdle_m:
            ax2.plot([x[i], x[i]], [lp_cum[i], hurdle_m],
                     color=C_HURDLE, linewidth=1.2, linestyle=":", alpha=0.35, zorder=3)

    # GP residual NAV (twin axis)
    gp_res = df["gp_residual_nav"].values / 1e6
    ax2_twin = ax2.twinx()
    ax2_twin.plot(x, gp_res, "s--", color=C_GP_RES, linewidth=1.5,
                  markersize=5, alpha=0.8, label="GP Residual NAV", zorder=5)
    ax2_twin.set_ylabel("GP Residual NAV ($M)", color=C_GP_RES, fontsize=9)
    ax2_twin.yaxis.set_major_formatter(_dollar_formatter())
    ax2_twin.tick_params(axis="y", labelcolor=C_GP_RES, labelsize=8)

    if has_trigger:
        ty = trigger_years[0]
        idx = int(np.where(years == ty)[0][0])
        ax2.axvspan(idx - 0.45, idx + 0.45, alpha=0.18, color=C_TRIG_BG, zorder=0)
        row = df[df["year"] == ty].iloc[0]
        sources = []
        if row["trigger_cash_from_hf_liquidation"] > 0:
            sources.append(f"HF Liq: {_fmt_m(row['trigger_cash_from_hf_liquidation'])}")
        if row["trigger_cash_from_refi"] > 0:
            sources.append(f"Refi: {_fmt_m(row['trigger_cash_from_refi'])}")
        if row["trigger_cash_from_retained_cash"] > 0:
            sources.append(f"Cash: {_fmt_m(row['trigger_cash_from_retained_cash'])}")
        if row["trigger_cash_from_reserve"] > 0:
            sources.append(f"Reserve: {_fmt_m(row['trigger_cash_from_reserve'])}")
        if row["trigger_cash_from_re_sale"] > 0:
            sources.append(f"RE Sale: {_fmt_m(row['trigger_cash_from_re_sale'])}")
        src_text = "\n".join(sources) if sources else f"Trigger Fires (Y{int(ty)})"
        # Place annotation: to the right if room, to the left if near end
        if idx < n - 3:
            x_text = idx + 1.8
            ha_text = "left"
        else:
            x_text = idx - 1.8
            ha_text = "right"
        y_text = lp_cum[min(idx, len(lp_cum) - 1)] + (hurdle_m * 0.15)
        ax2.annotate(src_text, xy=(idx, lp_cum[idx]), xytext=(x_text, y_text),
                     fontsize=7.5, fontweight="bold", color=C_TRIG_FG,
                     ha=ha_text, va="bottom",
                     arrowprops=dict(arrowstyle="->", color=C_TRIG_FG, lw=1.2),
                     bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                               edgecolor=C_TRIG_FG, alpha=0.95), zorder=10)

    if not lp_achieved:
        ax2.text(n - 0.5, hurdle_m * 0.5, "Hurdle not reached\nby year 20",
                 ha="right", va="center", fontsize=9, fontweight="bold",
                 color=C_HURDLE, alpha=0.7,
                 bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                           edgecolor=C_HURDLE, alpha=0.5))

    ax2.set_xticks(x)
    if is_bottom_up:
        ax2.set_xticklabels([])
    else:
        ax2.set_xticklabels([f"Y{int(y)}" for y in years], fontsize=7.5, rotation=45)
    ax2.set_ylabel("LP Distribution ($M)")
    ax2.yaxis.set_major_formatter(_dollar_formatter())

    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2_twin.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2,
               loc="upper center", fontsize=8, framealpha=0.95, ncol=4,
               bbox_to_anchor=(0.5, -0.14), borderaxespad=0.)

    # ── DEAL METRICS PANEL (bottom-up only) ───────────────────────────────
    if is_bottom_up and ax3 is not None:
        ax3.set_facecolor("#F8F9FA")
        ax3.grid(axis="y", color=C_GRID, linewidth=0.5, linestyle="--")
        ax3.set_title("Deal-Level Metrics — jon_deal_1", fontsize=12,
                       fontweight="bold", color="#2C3E50", pad=10)

        ddf = deal_df.sort_values("year").reset_index(drop=True)
        deal_years = ddf["year"].values
        dn = len(deal_years)
        dx = np.arange(dn)

        # Asset value + debt (bars)
        ax3.bar(dx - 0.15, ddf["asset_value"].values / 1e6, 0.25,
                color=C_ASSET_VAL, alpha=0.85, label="Gross Asset Value")
        ax3.bar(dx + 0.15, ddf["debt_balance"].values / 1e6, 0.25,
                color=C_DEBT, alpha=0.85, label="Debt Balance")

        # Deal NAV (line)
        ax3.plot(dx, ddf["deal_nav"].values / 1e6, "o-", color=C_DEAL_NAV,
                 linewidth=2, markersize=5, label="Deal NAV (Net Equity)", zorder=5)

        # Refi proceeds (line)
        refi_deal = ddf["refi_proceeds"].values / 1e6
        if refi_deal.sum() > 0:
            ax3.plot(dx, refi_deal, "s--", color=C_REFI_DEAL, linewidth=1.5,
                     markersize=5, alpha=0.8, label="Refi Proceeds", zorder=5)

        ax3.set_ylabel("Value ($M)")
        ax3.yaxis.set_major_formatter(_dollar_formatter())

        # DSCR on twin axis
        ax3_twin = ax3.twinx()
        dscr = ddf["dscr"].values
        ax3_twin.plot(dx, dscr, "D--", color=C_DSRC, linewidth=1.2,
                      markersize=4, alpha=0.7, label="DSCR", zorder=4)
        ax3_twin.axhline(1.0, color=C_DSRC, linewidth=0.8, linestyle=":", alpha=0.5)
        ax3_twin.set_ylabel("DSCR", color=C_DSRC, fontsize=9)
        ax3_twin.tick_params(axis="y", labelcolor=C_DSRC, labelsize=8)
        ax3_twin.set_ylim(0, max(2.5, dscr.max() * 1.2))

        # Trigger year highlight
        if has_trigger:
            ty = trigger_years[0]
            if ty in deal_years:
                tidx = int(np.where(deal_years == ty)[0][0])
                ax3.axvspan(tidx - 0.45, tidx + 0.45, alpha=0.18,
                            color=C_TRIG_BG, zorder=0)

        ax3.set_xticks(dx)
        ax3.set_xticklabels([f"Y{int(y)}" for y in deal_years],
                             fontsize=7.5, rotation=45)

        # Combined legend
        lines3, labels3 = ax3.get_legend_handles_labels()
        lines3t, labels3t = ax3_twin.get_legend_handles_labels()
        ax3.legend(lines3 + lines3t, labels3 + labels3t,
                   loc="upper center", fontsize=7.5, framealpha=0.95, ncol=4,
                   bbox_to_anchor=(0.5, -0.14), borderaxespad=0.)

    # ── footer ────────────────────────────────────────────────────────────
    final_nav = df["fund_nav"].iloc[-1]
    gp_total = df["gp_residual_nav"].iloc[-1] + df["gp_cumulative_fees"].iloc[-1]
    footer = (
        f"Hurdle Achieved: {'Yes' if lp_achieved else 'No'}  │  "
        f"Years: {n}  │  "
        f"Final Fund NAV: {_fmt_m(final_nav)}  │  "
        f"Total RE Cashflow: {_fmt_m(df['re_cashflow_generated'].sum())}  │  "
        f"Total HF Harvest: {_fmt_m(df['hf_harvest_generated'].sum())}  │  "
        f"GP Total Economics: {_fmt_m(gp_total)}"
    )
    fig.text(0.5, 0.02, footer, ha="center", fontsize=8, color="#555555",
             style="italic")

    if save_path:
        save_path = Path(save_path)
        artists = [ax1.get_legend(), ax2.get_legend()]
        if ax3 is not None:
            artists.append(ax3.get_legend())
        _save_fig(fig, save_path, artists=artists)

    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig


# ── 2. LP HURDLE TIMELINE ──────────────────────────────────────────────────
def build_hurdle_timeline(
    summary_df: pd.DataFrame,
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    summary_df = summary_df.copy()
    summary_df["achievement_year"] = summary_df.apply(
        lambda r: r["year_hurdle_achieved"] if r["lp_hurdle_achieved"] else None, axis=1)
    summary_df["failed"] = ~summary_df["lp_hurdle_achieved"]
    summary_df["sort_key"] = summary_df["achievement_year"].fillna(99)
    summary_df = summary_df.sort_values(["failed", "sort_key"]).reset_index(drop=True)

    n = len(summary_df)
    fig, ax = plt.subplots(figsize=(14, max(5, n * 0.7 + 2)))
    fig.patch.set_facecolor("#FAFAFA")
    ax.set_facecolor("#F8F9FA")
    ax.set_title("LP 2.0x Hurdle Timeline — All Scenarios",
                 fontsize=14, fontweight="bold", color="#2C3E50", pad=14)

    bar_height = 0.5
    y_positions = np.arange(n)

    for i, row in summary_df.iterrows():
        y = y_positions[i]
        achieved = not row["failed"]
        year = row["achievement_year"]
        if achieved:
            ax.barh(y, year, height=bar_height, color=C_DISTRIBUTED, alpha=0.85,
                    edgecolor="white", linewidth=0.5)
            ax.text(year + 0.2, y, f"Y{int(year)}",
                    va="center", fontsize=9, fontweight="bold", color="#2C3E50")
        else:
            ax.barh(y, 20, height=bar_height, color=C_HURDLE, alpha=0.35,
                    edgecolor=C_HURDLE, linewidth=0.8, hatch="//")
            ax.text(10, y, "Not reached by Y20",
                    va="center", ha="center", fontsize=8.5, fontweight="bold", color=C_HURDLE)
        gp = row.get("gp_residual_nav", 0)
        if achieved and gp > 0:
            ax.text(20.5, y, f"GP: {_fmt_m(gp)}",
                    va="center", fontsize=7.5, color=C_GP_RES, fontweight="500")

    ax.set_yticks(y_positions)
    ax.set_yticklabels(summary_df["scenario"].values, fontsize=9)
    ax.set_xlabel("Year", fontsize=10)
    ax.set_xlim(0, 26)
    ax.axvline(20, color="#2C3E50", linewidth=1, linestyle=":", alpha=0.5)
    ax.text(20, n - 0.3, "Y20", ha="center", fontsize=8, color="#7F8C8D")

    legend_items = [
        mpatches.Patch(color=C_DISTRIBUTED, alpha=0.85, label="Hurdle achieved"),
        mpatches.Patch(color=C_HURDLE, alpha=0.35, hatch="//", label="Not reached by Y20"),
    ]
    ax.legend(handles=legend_items, loc="lower right", fontsize=9, framealpha=0.95)
    ax.grid(axis="x", color=C_GRID, linewidth=0.5, linestyle="--")
    ax.invert_yaxis()
    plt.tight_layout()

    if save_path:
        _save_fig(fig, Path(save_path))
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig


# ── 3. SCENARIO OUTCOME MATRIX ──────────────────────────────────────────────
def build_outcome_matrix(
    summary_df: pd.DataFrame,
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    summary_df = summary_df.copy()
    col_map = {
        "scenario": "Scenario", "years_modelled": "Years",
        "lp_cash_moic": "LP Cash MOIC", "lp_cash_irr": "LP Cash IRR",
        "year_hurdle_achieved": "Year 2x", "gp_residual_nav": "GP Residual",
        "gp_total_economics": "GP Total Econ",
        "total_trigger_cash_from_hf_liquidation": "HF Liq Used",
        "total_trigger_cash_from_refi": "Refi Used",
    }
    available = [c for c in col_map if c in summary_df.columns]
    df = summary_df[available].rename(columns=col_map).fillna("—")

    n_rows = len(df)
    n_cols = len(df.columns)

    fig, ax = plt.subplots(figsize=(16, max(4, n_rows * 0.6 + 2)))
    fig.patch.set_facecolor("#FAFAFA")
    ax.axis("off")
    ax.set_title("Scenario Outcome Matrix", fontsize=14, fontweight="bold",
                 color="#2C3E50", pad=14)

    def fmt_val(col, val):
        if val == "—":
            return "—"
        if col == "Scenario":
            return str(val)
        if col == "Years":
            return str(int(val)) if isinstance(val, (int, float)) else str(val)
        if col == "Year 2x":
            return f"Y{int(val)}" if isinstance(val, (int, float)) and val > 0 else "—"
        if col == "LP Cash MOIC":
            return f"{val:.2f}x" if isinstance(val, (int, float)) else str(val)
        if col == "LP Cash IRR":
            return f"{val:.1%}" if isinstance(val, (int, float)) else str(val)
        if col in ("GP Residual", "GP Total Econ", "HF Liq Used", "Refi Used"):
            return _fmt_m(val) if isinstance(val, (int, float)) else str(val)
        return str(val)

    cell_text = [[fmt_val(col, df.iloc[r][col]) for col in df.columns]
                 for r in range(n_rows)]

    cell_colors = []
    for r in range(n_rows):
        row_colors = []
        for c, col in enumerate(df.columns):
            val = df.iloc[r][col]
            if col == "Scenario":
                row_colors.append("#F8F9FA")
            elif col == "Year 2x":
                if isinstance(val, (int, float)) and val > 0:
                    intensity = max(0, 1 - val / 20)
                    row_colors.append((*matplotlib.colors.to_rgb(C_DISTRIBUTED),
                                       0.15 + 0.3 * (1 - intensity)))
                else:
                    row_colors.append((*matplotlib.colors.to_rgb(C_HURDLE), 0.15))
            elif col == "LP Cash MOIC":
                if isinstance(val, (int, float)):
                    if val >= 2.0:
                        row_colors.append((*matplotlib.colors.to_rgb(C_DISTRIBUTED), 0.25))
                    elif val >= 1.0:
                        row_colors.append((*matplotlib.colors.to_rgb(C_REINVESTED), 0.2))
                    else:
                        row_colors.append((*matplotlib.colors.to_rgb(C_HURDLE), 0.15))
                else:
                    row_colors.append("#FFFFFF")
            elif col in ("GP Residual", "GP Total Econ"):
                if isinstance(val, (int, float)) and val > 0:
                    row_colors.append((*matplotlib.colors.to_rgb(C_GP_RES), 0.15))
                else:
                    row_colors.append("#FFFFFF")
            else:
                row_colors.append("#FFFFFF")
        cell_colors.append(row_colors)

    table = ax.table(cellText=cell_text, colLabels=df.columns,
                     cellColours=cell_colors, loc="center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1, 1.4)

    for c in range(n_cols):
        table[0, c].set_facecolor("#2C3E50")
        table[0, c].set_text_props(color="white", fontweight="bold", fontsize=9)

    plt.tight_layout()
    if save_path:
        _save_fig(fig, Path(save_path))
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig


# ── 4. SENSITIVITY HEATMAP ─────────────────────────────────────────────────
def build_sensitivity_heatmap(
    sens_df: pd.DataFrame,
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    """
    2D heatmap: x = HF allocation, y = HF harvest rate,
    color = years to 2x (or grey if not achieved).
    One facet per backend_strategy × routing_policy combination.
    """
    df = sens_df.copy()

    # Convert to numeric
    df["year_hurdle_achieved"] = pd.to_numeric(df["year_hurdle_achieved"], errors="coerce")
    df["hf_allocation"] = pd.to_numeric(df["hf_allocation"], errors="coerce")
    df["hf_harvest_rate"] = pd.to_numeric(df["hf_harvest_rate"], errors="coerce")

    # Use trigger_threshold = 0.0 (most permissive) for the main view
    base_threshold = 0.0
    dff = df[df["trigger_threshold"] == base_threshold].copy()

    if len(dff) == 0:
        dff = df.copy()

    # Get unique facets
    strategies = sorted(dff["backend_strategy"].unique())
    routings = sorted(dff["routing_policy"].unique())

    n_strat = len(strategies)
    n_route = len(routings)

    fig, axes = plt.subplots(n_strat, n_route,
                              figsize=(5 * n_route + 2, 4 * n_strat + 1),
                              squeeze=False)
    fig.patch.set_facecolor("#FAFAFA")
    fig.suptitle(
        f"Sensitivity: Years to LP 2.0x Hurdle  (trigger_threshold={base_threshold}x)",
        fontsize=14, fontweight="bold", color="#2C3E50", y=0.98,
    )

    hf_allocs = sorted(dff["hf_allocation"].unique())
    hf_harvests = sorted(dff["hf_harvest_rate"].unique())

    # Custom colormap: green (fast) → yellow → red (slow) → grey (never)
    from matplotlib.colors import LinearSegmentedColormap
    cmap_colors = ["#27AE60", "#F1C40F", "#E67E22", "#E74C3C", "#BDC3C7"]
    cmap = LinearSegmentedColormap.from_list("hurdle", cmap_colors, N=256)

    vmin, vmax = 5, 20

    for si, strat in enumerate(strategies):
        for ri, route in enumerate(routings):
            ax = axes[si][ri]
            ax.set_facecolor("#F8F9FA")

            sub = dff[(dff["backend_strategy"] == strat) &
                       (dff["routing_policy"] == route)]

            if len(sub) == 0:
                ax.set_visible(False)
                continue

            # Pivot: rows = harvest rate, cols = HF allocation
            pivot = sub.pivot_table(
                values="year_hurdle_achieved",
                index="hf_harvest_rate",
                columns="hf_allocation",
                aggfunc="min",  # best case across refi/hf liq caps
            )

            # Mask NaN (not achieved) → show as grey
            masked = np.ma.array(pivot.values, mask=np.isnan(pivot.values))

            im = ax.imshow(masked, cmap=cmap, vmin=vmin, vmax=vmax,
                           aspect="auto", origin="lower")

            # Labels
            ax.set_xticks(range(len(pivot.columns)))
            ax.set_xticklabels([f"{x:.0%}" for x in pivot.columns], fontsize=7.5)
            ax.set_yticks(range(len(pivot.index)))
            ax.set_yticklabels([f"{y:.0%}" for y in pivot.index], fontsize=7.5)

            # Cell annotations
            for i in range(len(pivot.index)):
                for j in range(len(pivot.columns)):
                    val = pivot.values[i, j]
                    if np.isnan(val):
                        text = "—"
                        color = "#7F8C8D"
                    else:
                        text = f"{int(val)}"
                        color = "#2C3E50"
                    ax.text(j, i, text, ha="center", va="center",
                            fontsize=7.5, fontweight="bold", color=color)

            ax.set_title(f"{strat} / {route}", fontsize=9, fontweight="bold",
                         color="#2C3E50", pad=6)

            if ri == 0:
                ax.set_ylabel("HF Harvest Rate", fontsize=8)
            if si == n_strat - 1:
                ax.set_xlabel("HF Allocation", fontsize=8)

    # Colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin, vmax))
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax)
    cbar.set_label("Years to 2.0x", fontsize=9)
    cbar.set_ticks([5, 10, 15, 20])
    cbar.set_ticklabels(["5", "10", "15", "20+"])

    plt.tight_layout(rect=[0, 0, 0.9, 0.96])

    if save_path:
        _save_fig(fig, Path(save_path))
    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig


# ── batch runner ────────────────────────────────────────────────────────────
def build_all_charts(
    csv_path: str | Path = "outputs/scenario_cashflows.csv",
    summary_csv_path: str | Path = "outputs/scenario_summary.csv",
    deal_csv_path: str | Path = "outputs/deal_cashflows.csv",
    sens_csv_path: str | Path = "outputs/sensitivity_analysis.csv",
    tax_summary_csv: str | Path = "outputs/tax_summary.csv",
    tax_yearly_csv: str | Path = "outputs/tax_yearly.csv",
    output_dir: str | Path = "outputs/charts",
    scenarios: list[str] | None = None,
) -> dict[str, list[Path]]:
    csv_path = Path(csv_path)
    summary_csv_path = Path(summary_csv_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cf = pd.read_csv(csv_path)
    sf = pd.read_csv(summary_csv_path)

    deal_cf = None
    if Path(deal_csv_path).exists():
        deal_cf = pd.read_csv(deal_csv_path)

    all_scenarios = cf["scenario"].unique()
    if scenarios:
        missing = set(scenarios) - set(all_scenarios)
        if missing:
            print(f"Warning: scenarios not found: {missing}")
        to_run = [s for s in scenarios if s in all_scenarios]
    else:
        to_run = list(all_scenarios)

    waterfalls: list[Path] = []
    for name in to_run:
        sdf = cf[cf["scenario"] == name]
        ddf = deal_cf[deal_cf["scenario"] == name] if deal_cf is not None else None
        safe = name.replace(" ", "_").replace("/", "_")
        p = output_dir / f"waterfall_{safe}.png"
        build_dual_waterfall(sdf, name, deal_df=ddf, save_path=p)
        waterfalls.append(p)

    timeline_path = output_dir / "hurdle_timeline.png"
    build_hurdle_timeline(sf, save_path=timeline_path)

    matrix_path = output_dir / "outcome_matrix.png"
    build_outcome_matrix(sf, save_path=matrix_path)

    sens_path = output_dir / "sensitivity_heatmap.png"
    if Path(sens_csv_path).exists():
        sens_df = pd.read_csv(sens_csv_path)
        build_sensitivity_heatmap(sens_df, save_path=sens_path)
        print(f"\nBuilt {len(waterfalls)} waterfalls + timeline + matrix + heatmap in {output_dir}/")
    else:
        print(f"\nBuilt {len(waterfalls)} waterfalls + timeline + matrix in {output_dir}/")
        print(f"(No sensitivity data at {sens_csv_path})")

    # --- Tax charts ---
    tax_charts: list[Path] = []
    if Path(tax_summary_csv).exists() and Path(tax_yearly_csv).exists():
        at_path = output_dir / "after_tax_comparison.png"
        result = build_after_tax_comparison(
            tax_summary_csv, summary_csv_path, save_path=at_path,
        )
        if result:
            tax_charts.append(result)

        # Per-scenario tax shield waterfall (only for bottom-up scenarios with deals)
        if deal_cf is not None:
            for name in to_run:
                safe = name.replace(" ", "_").replace("/", "_")
                tw_path = output_dir / f"tax_shield_{safe}.png"
                result = build_tax_waterfall(tax_yearly_csv, name, save_path=tw_path)
                if result:
                    tax_charts.append(result)

        if tax_charts:
            print(f"Built {len(tax_charts)} tax charts in {output_dir}/")

    return {"waterfalls": waterfalls, "timeline": [timeline_path],
            "matrix": [matrix_path], "tax": tax_charts}


# ── After-Tax Comparison Chart ──────────────────────────────────────────────

def build_after_tax_comparison(
    tax_summary_csv: str | Path,
    summary_csv: str | Path,
    save_path: str | Path | None = None,
    title: str = "After-Tax vs Pre-Tax Returns (Ideal LP)",
) -> Path | None:
    """Bar chart comparing pre-tax MOIC, after-tax MOIC, and tax savings by scenario."""
    try:
        tf = pd.read_csv(tax_summary_csv)
        sf = pd.read_csv(summary_csv)
    except Exception as e:
        print(f"Could not read tax CSVs: {e}")
        return None

    if tf.empty:
        print("Tax summary is empty — skipping after-tax chart.")
        return None

    # Merge with summary to get pre-tax MOIC
    merged = tf.merge(sf[["scenario", "lp_cash_moic", "lp_irr"]], on="scenario", how="left")
    merged = merged.sort_values("final_after_tax_moic", ascending=True)

    scenarios = merged["scenario"].tolist()
    n = len(scenarios)
    y_pos = np.arange(n)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, max(6, n * 0.5 + 2)))

    # Left panel: MOIC comparison
    bar_h = 0.35
    pre_tax = merged["lp_cash_moic"].fillna(0).values
    after_tax = merged["final_after_tax_moic"].fillna(0).values

    ax1.barh(y_pos - bar_h / 2, pre_tax, bar_h, label="Pre-Tax Cash MOIC", color=C_LP_CUM, alpha=0.8)
    ax1.barh(y_pos + bar_h / 2, after_tax, bar_h, label="After-Tax MOIC (Ideal LP)", color="#27AE60", alpha=0.8)

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(scenarios, fontsize=9)
    ax1.set_xlabel("Equity Multiple (MOIC)")
    ax1.set_title("Pre-Tax vs After-Tax MOIC")
    ax1.axvline(x=2.0, color=C_HURDLE, linestyle="--", alpha=0.7, label="2x Hurdle")
    ax1.legend(loc="lower right", fontsize=8)
    ax1.xaxis.set_major_formatter(mticker.FormatStrFormatter("%.1fx"))

    # Add value labels
    for i, (pt, at) in enumerate(zip(pre_tax, after_tax)):
        ax1.text(pt + 0.02, i - bar_h / 2, f"{pt:.2f}x", va="center", fontsize=7, color="#2C3E50")
        ax1.text(at + 0.02, i + bar_h / 2, f"{at:.2f}x", va="center", fontsize=7, color="#27AE60")

    # Right panel: Tax savings
    tax_savings = merged["total_tax_savings"].fillna(0).values / 1e6
    colors = ["#27AE60" if s > 0 else "#E74C3C" for s in tax_savings]

    ax2.barh(y_pos, tax_savings, bar_h * 1.5, color=colors, alpha=0.8)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(scenarios, fontsize=9)
    ax2.set_xlabel("Total Tax Savings ($M)")
    ax2.set_title("Lifetime Tax Savings (Depreciation + Interest Shield)")
    ax2.xaxis.set_major_formatter(mticker.FormatStrFormatter("$%.1fM"))

    for i, s in enumerate(tax_savings):
        ax2.text(s + 0.05, i, f"${s:.1f}M", va="center", fontsize=7, color="#2C3E50")

    fig.suptitle(title, fontsize=13, fontweight="bold", y=1.01)
    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        return Path(save_path)
    plt.close(fig)
    return None


def build_tax_waterfall(
    tax_yearly_csv: str | Path,
    scenario_name: str,
    save_path: str | Path | None = None,
) -> Path | None:
    """Stacked bar chart showing annual tax shield composition for one scenario."""
    try:
        df = pd.read_csv(tax_yearly_csv)
    except Exception:
        return None

    sdf = df[df["scenario"] == scenario_name]
    if sdf.empty:
        return None

    years = sdf["year"].values
    bonus = sdf["bonus_depreciation"].fillna(0).values / 1e6
    sl = sdf["straight_line_depreciation"].fillna(0).values / 1e6
    interest = sdf["interest_deduction"].fillna(0).values / 1e6

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(years, bonus, label="Bonus Depreciation", color="#E67E22", alpha=0.85)
    ax.bar(years, sl, bottom=bonus, label="Straight-Line Depreciation", color="#3498DB", alpha=0.85)
    ax.bar(years, interest, bottom=bonus + sl, label="Interest Deduction", color="#8E44AD", alpha=0.85)

    ax.set_xlabel("Year")
    ax.set_ylabel("Annual Tax Deductions ($M)")
    ax.set_title(f"Tax Shield Composition — {scenario_name}")
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("$%.1fM"))
    ax.legend(loc="upper right", fontsize=9)

    # Add cumulative tax savings line on secondary axis
    cum_savings = sdf["cumulative_tax_savings"].fillna(0).values / 1e6
    ax2 = ax.twinx()
    ax2.plot(years, cum_savings, color="#27AE60", linewidth=2, marker="o", markersize=4, label="Cumulative Tax Savings")
    ax2.set_ylabel("Cumulative Tax Savings ($M)", color="#27AE60")
    ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter("$%.1fM"))
    ax2.tick_params(axis="y", labelcolor="#27AE60")

    # Combine legends
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=8)

    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        return Path(save_path)
    plt.close(fig)
    return None


if __name__ == "__main__":
    build_all_charts()
