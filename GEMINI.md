# Hybrid Fund Economic Model - Project Context

Annual deterministic scenario engine for a hybrid fund structure (Real Estate + Hedge Fund + Reserve) with a non-standard LP/GP waterfall.

## Project Overview

The model projects fund economics over a 15-20 year horizon. It handles initial capital allocation, annual operations (NOI, HF gains), cashflow routing (to LP, HF reinvestment, or Reserve), and a specific LP hurdle completion trigger (2.0x MOIC target).

### Architecture
- **Deal Layer (`src/deal_model.py`):** Models individual real estate assets, debt, capex, and refinance events.
- **Fund Layer (`src/engine.py`):** Manages cash routing, acquisition funding, and sleeve-level NAV.
- **Waterfall Layer (`src/waterfall.py`):** Logic for LP distributions, GP fees, and GP residual economics.
- **Tax Layer (`src/tax.py`):** Post-processing for depreciation (bonus + straight-line) and taxable income analysis.
- **Reporting (`src/reporting.py`, `src/report_html.py`, `src/charts.py`):** Generates Markdown, HTML, Excel, and PNG outputs.

### Key Technologies
- **Python 3.10+**
- **Data:** `pandas`, `numpy`, `numpy-financial`
- **Validation:** `pydantic`, `pyyaml`
- **Visualization:** `streamlit`, `plotly`
- **Excel:** `openpyxl`
- **Testing:** `pytest`

## Building and Running

### Setup
Ensure dependencies are installed:
```powershell
pip install -r requirements.txt
```

### Core Commands
- **Run Standard Model:**
  ```powershell
  python run_model.py
  ```
  Processes scenarios in `inputs/scenarios.yaml` and writes to `outputs/`.

- **Run Calibration/Sensitivities:**
  ```powershell
  python run_calibration.py
  ```
  Runs variants defined in `inputs/calibration_tests.yaml`.

- **Launch Dashboard:**
  ```powershell
  streamlit run dashboard/app.py
  ```
  Interactive visualization of scenario results.

- **Rebuild ChatGPT Context:**
  ```powershell
  python build_chatgpt_context.py
  ```
  Updates `outputs/chatgpt_model_context.md` for external review.

- **Run Tests:**
  ```powershell
  pytest
  ```

## Development Conventions

### Inputs & Validation
- **YAML Driven:** All model assumptions live in `inputs/*.yaml`. Never hardcode scenario parameters in the engine.
- **Pydantic Models:** Use models in `src/model_types.py` and `src/deal_types.py` for all input validation and type safety.

### Logic & Modules
- **Deterministic:** The model is annual and deterministic. No stochastic/Monte Carlo logic in the core engine.
- **Targeted Edits:** When modifying the engine, ensure `src/engine.py` remains the central orchestrator and logic is delegated to specialized modules (e.g., `waterfall.py`, `tax.py`).
- **Debugging:** Keep debugging logs informative but concise.

### Output Standard
- Results are always written to `outputs/`.
- Ensure new metrics are added to both `scenario_summary.csv` and the Excel export in `src/outputs.py`.

## Directory Map
- `src/`: Core logic and model implementation.
- `inputs/`: YAML configuration files.
- `outputs/`: Generated results and charts.
- `dashboard/`: Streamlit visualization app.
- `tests/`: Comprehensive test suite.
- `ECONOMIC_MODEL_SPEC.md`: Authoritative design specification.
- `MODEL_RUNBOOK_AND_INPUTS.md`: Detailed guide for running and configuring the model.
