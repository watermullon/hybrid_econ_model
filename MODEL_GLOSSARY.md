# Hybrid Fund Model: Plain-English Glossary

This document explains the parameters and assumptions used in the Hybrid Fund Economic Model. It is designed to help anyone understand the model's inputs and logic without needing to read the code.

---

## ️ Core Abbreviations & Concepts

- **LP (Limited Partner):** The investor who provides the majority of the capital.
- **GP (General Partner):** The manager who runs the fund.
- **NAV (Net Asset Value):** The current value of an investment after subtracting liabilities (like debt).
- **MOIC (Multiple of Invested Capital):** A performance metric showing how many times the initial investment has been returned (e.g., 2.0x MOIC means you got double your money back).
- **IRR (Internal Rate of Return):** The annual rate of growth an investment is expected to generate.
- **NOI (Net Operating Income):** For real estate, this is total income minus operating expenses (but before paying debt or taxes).
- **LTV (Loan-to-Value):** The ratio of a loan to the value of an asset (e.g., a $70 loan on a $100 building is 70% LTV).
- **Sleeve:** A specific "bucket" or sub-portfolio within the fund (e.g., the "Hedge Fund sleeve").
- **Hurdle:** A target return that must be met for the LP before the GP gets a larger share of the profits.

---

## ️ Global Model Settings (`model_config.yaml`)

These settings apply to every scenario by default.

### Fund Basics (`model`)
- **Initial LP Capital:** The total amount of money the LP puts into the fund at the start.
- **GP Co-Investment:** Any money the GP puts in alongside the LP (used for reporting total fund size).
- **Max Years:** The longest the model is allowed to run before stopping.

### Initial Allocation (`allocation`)
- **Method:** How the initial capital is split. Usually "fixed" percentages.
- **Real Estate / Hedge Fund / Reserve %:** What portion of the LP's money goes into each bucket on Day 1.

### The Waterfall (`waterfall`)
- **LP Hurdle MOIC:** The target cash return for the LP. For this project, the target is **2.0x** (returning double the LP's initial capital).
- **Include Unrealized NAV in Hurdle Test:** If true, the model checks if the LP *could* reach the hurdle if the fund sold everything today (on paper), even if it hasn't actually paid out the cash yet.
- **Require Liquidity for LP Redemption:** If true, the LP is only "paid out" when the fund actually has the cash available (from operations or selling assets).

### Fees (`fees`)
- **RE Asset Management Fee:** A fee paid to the GP for managing the properties.
 - **Rate:** The percentage fee (e.g., 3%).
 - **Basis:** What the fee is calculated on (usually Gross Rent or NOI).
- **Hedge Fund Fees:** Fees for the liquid portfolio. Often modeled as "net returns," meaning the returns you enter already have fees taken out.

### Cashflow Routing (`cashflow_routing`)
*This is the "traffic control" for the fund's cash.*
- **LP Distribution %:** What percent of generated cash goes straight to the LP's pocket.
- **HF Reinvestment %:** What percent of cash is put back into the Hedge Fund to grow.
- **Reserve %:** What percent of cash is set aside in a rainy-day fund.

---

## Real Estate Parameters (`deals.yaml` or `scenarios.yaml`)

Real estate can be modeled "Top-Down" (general assumptions) or "Bottom-Up" (specific properties).

### Property Economics
- **Initial NOI Yield:** The starting annual profit as a percentage of the property's value.
- **Annual NOI Growth:** How much the property's profit grows each year (e.g., from rent increases).
- **NAV Appreciation:** How much the property's market value grows each year.
- **Gross Rent Yield:** Total rent collected as a percentage of the property's value.

### Debt & Financing (`debt`)
- **Interest Rate:** The annual cost of the loan.
- **Amortization Type:** 
 - **Interest Only:** You only pay the interest each year; the loan balance stays the same.
 - **Fixed Debt Service:** You pay a flat dollar amount each year that covers both interest and some principal.
- **DSCR (Debt Service Coverage Ratio):** A safety check. It's the property's profit (NOI) divided by the debt payment. A ratio of 1.25x means you have 25% more profit than you need to pay the loan.

### Refinancing (`refinance`)
- **Refi LTV:** When the property is refinanced, how much of the new value can we borrow (e.g., 70%).
- **Proceeds Use:** Where the "cash out" money from a refinance goes (usually used to pay the LP or put into the Reserve).

---

## Hedge Fund Parameters

- **Annual Returns:** A list of the expected performance for the liquid portfolio each year (e.g., 15%, -5%, 20%).
- **Harvest Rate:** What percent of *gains* are pulled out of the Hedge Fund each year to be used elsewhere (like paying the LP).

---

## Risk & Success Flags (`flag_thresholds`)

The model automatically "flags" results to highlight risks or exceptional outcomes.
- **HF Major Drawdown:** Triggers if the Hedge Fund loses more than a certain percentage in one year.
- **RE NAV Impairment:** Triggers if the property value drops significantly.
- **Slow Time Horizon:** Triggers if it takes longer than expected (e.g., 8 years) to pay the LP.
- **Fast GP Dynasty:** Triggers if the GP hits a massive payday very early.

---

## Liquidity Triggers

- **Hurdle Completion Trigger:** A specialized logic that "scans" the fund's assets. If it sees that the fund has enough combined cash (from the Reserve, Hedge Fund, and Refinancing) to finish paying the LP their 2.0x, it will automatically "trigger" those events to end the scenario.
- **Backend Liquidity Strategy:** A scheduled plan to refinance properties in specific years (e.g., years 5, 7, and 10) to generate the cash needed to pay the LP.
