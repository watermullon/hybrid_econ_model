from __future__ import annotations

from pathlib import Path

from src.chatgpt_export import build_chatgpt_context
from src.config_loader import ConfigError, load_inputs, load_yaml
from src.engine import run_all_scenarios
from src.outputs import write_outputs
from src.reporting import write_markdown_report
from src.report_html import build_html_report
from src.tax import TaxConfig, run_tax_analysis, write_tax_outputs


def main() -> None:
    root = Path(__file__).resolve().parent
    try:
        config, scenarios, deals = load_inputs(root / "inputs")
        results = run_all_scenarios(config, scenarios.scenarios, deals)
        frames = write_outputs(results=results, config=config, scenarios=scenarios, output_dir=root / "outputs")
        if config.reporting.output_markdown:
            write_markdown_report(results, frames["summary"], root / "outputs" / "scenario_report.md")
        build_chatgpt_context(root)

        # --- Tax analysis (separate post-processing module) ---
        tax_config_path = root / "inputs" / "tax_config.yaml"
        if tax_config_path.exists():
            tax_config = TaxConfig.from_yaml(tax_config_path)
            deal_dict = deals.model_dump() if deals else None
            tax_results = run_tax_analysis(
                results=results,
                deals=deal_dict,
                tax_config=tax_config,
                initial_lp_capital=config.model.initial_lp_capital,
            )
            tax_frames = write_tax_outputs(tax_results, root / "outputs", tax_config)
            # Merge tax summary into Excel if Excel output is enabled
            if tax_config.output_excel_sheet and config.reporting.output_excel:
                import pandas as pd
                from src.outputs import format_worksheet
                excel_path = root / "outputs" / "scenario_summary.xlsx"
                if excel_path.exists():
                    with pd.ExcelWriter(excel_path, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                        tax_frames["tax_summary"].to_excel(writer, sheet_name="Tax Summary", index=False)
                        tax_frames["tax_yearly"].to_excel(writer, sheet_name="Tax Yearly", index=False)
                        format_worksheet(writer.sheets["Tax Summary"])
                        format_worksheet(writer.sheets["Tax Yearly"])

        # --- HTML Report (self-contained, all charts embedded as base64) ---
        build_html_report(
            summary_csv=root / "outputs" / "scenario_summary.csv",
            charts_dir=root / "outputs" / "charts",
            output_path=root / "outputs" / "report.html",
        )

    except PermissionError as exc:
        raise SystemExit(
            "Model failed: could not write one or more output files. "
            "If an output workbook or CSV is open, close it and run python run_model.py again."
        ) from exc
    except (ConfigError, ValueError) as exc:
        raise SystemExit(f"Model failed: {exc}") from exc

    print(f"Ran {len(results)} scenarios.")
    print("Outputs written to outputs/")
    print("ChatGPT context written to outputs/chatgpt_model_context.md")
