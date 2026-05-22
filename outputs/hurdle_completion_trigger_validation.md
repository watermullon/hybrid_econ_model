# Hurdle Completion Trigger Validation

## Purpose

The hurdle completion trigger models an active GP decision to monetize permitted sources when the LP cash hurdle can be fully completed in the current year.

The LP hurdle remains based on actual cash distributions received. NAV appreciation alone does not extinguish LP interests.

## Trigger Logic

At the end of each year, after normal annual cash routing and configured refinance events, the model:

1. Calculates the remaining LP cash hurdle.
2. Checks whether the economic hurdle has passed, if required.
3. Checks whether current LP cash MOIC is at or above the configured trigger threshold.
4. Tests available trigger funding in this order:
   - retained cash
   - reserve
   - HF liquidation
   - RE refinance proceeds
   - partial RE sale, only if enabled
5. Executes only if the configured sources can fully extinguish the LP.

## Caveats

Refinance proceeds do not reduce gross RE NAV in this version. They now create an explicit refinance liability, and fund NAV / GP residual NAV are calculated net of that liability. This prevents refinance proceeds from creating economic value without an offset.

The model still does not yet model new debt service, leverage covenants, interest-rate terms, or lender constraints.

Partial RE sale is disabled by default. If enabled later, RE NAV is reduced by the sale amount.

The trigger is separate from the passive liquidity test. The passive test asks whether theoretical liquidity exists. The trigger asks whether the GP actively uses configured sources to finish the LP buyout now.

## Backend Liquidity Strategy

The model now includes `backend_liquidity_strategy` to reflect Asher's intended profile:

- low interim LP distributions
- RE rent/cashflow primarily reinvested into the HF sleeve
- scheduled backend liquidity test years
- refinance-first funding order when `refi_first` is enabled
- HF liquidation and reserve release as supporting liquidity sources

When enabled, the active hurdle completion trigger only attempts execution in configured target years, and it uses the backend strategy's refi and HF liquidation caps instead of the generic trigger caps.
