"""GP vs LP split chart — stacked area showing fund ownership over time."""

from __future__ import annotations

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from pathlib import Path


def build_gp_lp_split(
    df: pd.DataFrame,
    scenario_name: str,
    save_path: str | Path | None = None,
    show: bool = False,
) -> plt.Figure:
    """
    Stacked area chart showing how the total fund value is divided between
    LP cash received, LP remaining hurdle, GP fees, and GP residual NAV.
    """
    df = df.sort_values("year").reset_index(drop=True)
    years = df["year"].values
    n = len(years)
    x = np.arange(n)

    # Components (all in $M)
    lp_cash = df["lp_cumulative_distribution"].values / 1e6
    lp_claim = df["lp_remaining_hurdle"].values / 1e6
    gp_fees = df["gp_cumulative_fees"].values / 1e6
    gp_resid = df["gp_residual_nav"].values / 1e6

    # Total fund value = sum of all components
    total = lp_cash + lp_claim + gp_fees + gp_resid

    # Trigger info
    trigger_mask = df["hurdle_trigger_executed"] == True
    trigger_years = df.loc[trigger_mask, "year"].values
    has_trigger = len(trigger_years) > 0

    # ── figure ───────────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor("#FAFAFA")
    ax.set_facecolor("#F8F9FA")

    fig.suptitle(f"{scenario_name} — GP vs LP Split",
                 fontsize=14, fontweight="bold", color="#2C3E50")

    # Stacked area
    colors = ["#58D68D", "#AED6F1", "#F0B27A", "#E74C3C"]
    labels = ["LP Cash Received", "LP Remaining Hurdle", "GP Cumulative Fees", "GP Residual NAV"]

    ax.stackplot(x, lp_cash, lp_claim, gp_fees, gp_resid,
                 labels=labels, colors=colors, alpha=0.85)

    # Total fund value line
    ax.plot(x, total, "k-", linewidth=1.5, alpha=0.5, label="Total Fund Value")
    ax.plot(x, total, "ko", markersize=3, alpha=0.5)

    # Trigger year vertical line
    if has_trigger:
        ty = trigger_years[0]
        idx = int(np.where(years == ty)[0][0])
        ax.axvline(idx, color="#E74C3C", linewidth=2, linestyle="--", alpha=0.8,
                   label=f"Trigger Year (Y{int(ty)})")

        # Annotate the split at trigger
        y_pos = total[idx]
        ax.annotate(
            f"Trigger Y{int(ty)}\nLP: ${lp_cash[idx] + lp_claim[idx]:.1f}M\nGP: ${gp_fees[idx] + gp_resid[idx]:.1f}M",
            xy=(idx, y_pos),
            xytext=(idx + 1.5, y_pos * 0.85),
            fontsize=8, fontweight="bold", color="#2C3E50",
            ha="left", va="center",
            arrowprops=dict(arrowstyle="->", color="#2C3E50", lw=1),
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor="#BDC3C7", alpha=0.95),
        )

    # Labels
    ax.set_xticks(x[::max(1, n // 10)])  # show ~10 ticks
    ax.set_xticklabels([f"Y{int(years[i])}" for i in range(0, n, max(1, n // 10))],
                        fontsize=8, rotation=45)
    ax.set_ylabel("Value ($M)")
    ax.yaxis.set_major_formatter(
        mticker.FuncFormatter(lambda v, _: f"${v:.0f}M" if v >= 1 else f"${v:.1f}M"))
    ax.grid(axis="y", color="#D5D8DC", linewidth=0.5, linestyle="--")

    # Legend
    legend_handles = [
        mpatches.Patch(color=colors[0], alpha=0.85, label=labels[0]),
        mpatches.Patch(color=colors[1], alpha=0.85, label=labels[1]),
        mpatches.Patch(color=colors[2], alpha=0.85, label=labels[2]),
        mpatches.Patch(color=colors[3], alpha=0.85, label=labels[3]),
    ]
    if has_trigger:
        from matplotlib.lines import Line2D
        legend_handles.append(
            Line2D([0], [0], color="#E74C3C", linewidth=2, linestyle="--", label=f"Trigger Year"))
    ax.legend(handles=legend_handles, loc="center left", fontsize=8,
              framealpha=0.95, bbox_to_anchor=(1.01, 0.5))

    # Footer
    final_total = total[-1]
    final_gp = (gp_fees[-1] + gp_resid[-1]) / final_total * 100 if final_total > 0 else 0
    final_lp_cash = lp_cash[-1] / final_total * 100 if final_total > 0 else 0
    final_lp_claim = lp_claim[-1] / final_total * 100 if final_total > 0 else 0

    footer = (
        f"Final split — LP Cash: {final_lp_cash:.0f}%  │  "
        f"LP Hurdle Remaining: {final_lp_claim:.0f}%  │  "
        f"GP Total: {final_gp:.0f}%  │  "
        f"Total Fund: ${final_total:.1f}M"
    )
    fig.text(0.5, 0.01, footer, ha="center", fontsize=8, color="#555555", style="italic")

    plt.tight_layout(rect=[0, 0.04, 0.82, 0.96])

    if save_path:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(save_path, dpi=150, bbox_inches="tight",
                     facecolor=fig.get_facecolor())
        print(f"Saved: {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)
    return fig


def build_all_splits(
    csv_path: str | Path = "outputs/scenario_cashflows.csv",
    output_dir: str | Path = "outputs/charts",
    scenarios: list[str] | None = None,
) -> list[Path]:
    csv_path = Path(csv_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path)
    all_scenarios = df["scenario"].unique()

    if scenarios:
        to_run = [s for s in scenarios if s in all_scenarios]
    else:
        to_run = list(all_scenarios)

    saved: list[Path] = []
    for name in to_run:
        sdf = df[df["scenario"] == name]
        safe = name.replace(" ", "_").replace("/", "_")
        p = output_dir / f"gp_lp_split_{safe}.png"
        build_gp_lp_split(sdf, name, save_path=p)
        saved.append(p)

    print(f"\nBuilt {len(saved)} GP vs LP split charts in {output_dir}/")
    return saved


if __name__ == "__main__":
    build_all_splits()
