from __future__ import annotations

from pathlib import Path

from src.chatgpt_export import build_chatgpt_context
from src.config_loader import ConfigError, load_inputs
from src.engine import run_all_scenarios
from src.outputs import write_outputs
from src.reporting import write_markdown_report


def main() -> None:
    root = Path(__file__).resolve().parent
    try:
        config, scenarios, deals = load_inputs(root / "inputs")
        results = run_all_scenarios(config, scenarios.scenarios, deals)
        frames = write_outputs(results=results, config=config, scenarios=scenarios, output_dir=root / "outputs")
        if config.reporting.output_markdown:
            write_markdown_report(results, frames["summary"], root / "outputs" / "scenario_report.md")
        build_chatgpt_context(root)
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


if __name__ == "__main__":
    main()
