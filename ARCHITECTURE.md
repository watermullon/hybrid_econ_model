# Hybrid Fund Model Architecture

The following diagram represents the core architecture and data flow of the Hybrid Fund Economic Model.

```mermaid
graph TD
    subgraph "1. INPUT LAYER (YAML)"
        CONFIG[model_config.yaml]
        SCENARIOS[scenarios.yaml]
        DEALS[deals.yaml]
    end

    subgraph "2. ENGINE INITIALIZATION"
        LOADER[Config Loader & Pydantic Validation]
        ENGINE[Scenario Engine]
        CONFIG --> LOADER
        SCENARIOS --> LOADER
        DEALS --> LOADER
        LOADER --> ENGINE
    end

    subgraph "3. ANNUAL OPERATION LOOP (src/engine.py)"
        RE_SLEEVE["Real Estate Sleeve<br/>(Top-Down or Bottom-Up)"]
        HF_SLEEVE["Hedge Fund Sleeve<br/>(Annual Returns)"]
        RS_SLEEVE["Reserve Sleeve<br/>(Interest)"]
        
        ENGINE -->|Iterate Year| RE_SLEEVE
        ENGINE -->|Iterate Year| HF_SLEEVE
        ENGINE -->|Iterate Year| RS_SLEEVE
        
        RE_SLEEVE -->|Net Cashflow| ROUTER
        HF_SLEEVE -->|Harvested Gains| ROUTER
        
        subgraph "CASHFLOW ROUTING & PAYMENTS"
            ROUTER{Cashflow Routing Logic}
            ROUTER -->|LP Dist| LP_CASH[LP Distributions]
            ROUTER -->|Reinvest| HF_NAV_ADD[+ HF NAV]
            ROUTER -->|Save| RS_NAV_ADD[+ Reserve NAV]
            
            LP_YIELD[LP Cash Yield Policy]
            ROUTER -.-> LP_YIELD
            LP_YIELD -->|Yield Paid| LP_CASH
        end
        
        subgraph "LIQUIDITY & HURDLE TRIGGERS"
            REFI[Refinance Events]
            TRIGGER{Hurdle Completion Trigger}
            
            REFI -->|Proceeds| RETAINED[Retained Cash]
            REFI -->|Liability| FUND_NAV
            
            RE_SLEEVE -.-> REFI
            RETAINED --> TRIGGER
            HF_SLEEVE --> TRIGGER
            RS_SLEEVE --> TRIGGER
            
            TRIGGER -->|Execute| LP_REDEMPTION[Final LP Redemption]
        end
    end

    subgraph "4. WATERFALL & REPORTING"
        LP_REDEMPTION --> WATERFALL[Waterfall Logic]
        WATERFALL -->|Residual| GP_ECON[GP Residual NAV]
        
        WATERFALL --> OUTPUTS[CSV, Excel, Markdown]
        WATERFALL --> CHARTS[PNG Charts]
        WATERFALL --> DASHBOARD[Streamlit App]
    end

    %% Styles
    style ENGINE fill:#f9f,stroke:#333,stroke-width:2px
    style ROUTER fill:#bbf,stroke:#333,stroke-width:2px
    style TRIGGER fill:#f96,stroke:#333,stroke-width:2px
    style WATERFALL fill:#dfd,stroke:#333,stroke-width:2px
```

### Key Logic Verification (How the Engine works):
1.  **Acquisition First:** At the start of each year, the model checks for new acquisitions. It tries to fund them using *Retained Cash* first, then the *Reserve*.
2.  **Sleeve Operations:**
    *   **Real Estate:** Calculates NOI, Debt Service, and Capex. If `bottom_up`, it sums all active individual deals.
    *   **Hedge Fund:** Appreciates by the scenario return and then "harvests" gains if configured.
    *   **Reserve:** Appreciates by its annual return.
3.  **Cashflow Routing:** Generated cash from RE and HF is split between the LP, reinvestment into the HF, and the Reserve based on configured percentages (must sum to 100%).
4.  **LP Yield Policy:** If enabled, the model attempts to pay a target annual yield to the LP *before* other routing, sourced from RE cashflow, HF harvests, and the Reserve.
5.  **Refinance:** Both scenario-level and deal-level refis generate cash (usually to Retained Cash or Reserve) and increase a "Refinance Liability" which reduces the overall Fund NAV.
6.  **Hurdle Trigger:** This is the terminal logic. It calculates if the LP's 2.0x target can be met by liquidating the HF, using the Reserve, using Retained Cash, and performing a final refinance. If the total liquidity ≥ remaining hurdle, the scenario finishes.
