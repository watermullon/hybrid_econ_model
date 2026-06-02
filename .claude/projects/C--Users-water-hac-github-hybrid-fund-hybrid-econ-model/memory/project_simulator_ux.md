---
name: project-simulator-ux
description: UX action items for the scenario walkthrough simulator in the Streamlit dashboard
metadata:
  type: project
---

Hide the cashflow routing sliders (and LP hurdle trigger controls) from the left sidebar when the user is in "simulation mode" (walking through a scenario year by year). This frees up sidebar white space to surface key assumptions inline — e.g. the $1M entry equity cushion, the 60/25/15 routing split, the HF starting balance — so a non-modeller can see the "why" behind each year's numbers without needing to open the assumptions expander.

**Why:** The routing sliders are useful for what-if exploration but are noise during a walkthrough. A first-time viewer needs context, not controls.

**How to apply:** Add a toggle or mode selector (e.g. "Explore" vs "Walk through") that collapses the routing/trigger sidebar and replaces it with a read-only assumptions panel showing the most relevant inputs for the selected scenario.

## Action item 3: Separate "The Deal" (gross asset) from "The Fund NAV" (net equity)

Two distinct display blocks. Block 1 shows the capital stack — property value minus debt minus liabilities = fund equity. Appreciation percentages only appear here at gross level. Block 2 is the pie chart showing fund NAV split across RE equity, HF, reserve — all the same type of number, no leverage effects baked in silently. Reading order: pie first (simple), drill into Block 1 for RE detail.

## Action item 13: Fix contradiction in events area — two systems writing conflicting messages

Year 9 shows both "Event: Hurdle Completion Trigger Executed" AND "No significant events recorded this year" in the same area. Two separate event-writing systems not coordinated. The fallback "no events" message must not render if a real event flag is present. This is a bug that destroys credibility.

## Action item 12: Move event flag display to render under "Events & Flags" title (right side)

"Events & Flags" title is bottom right but the event flag content renders bottom left under the cashflow routing chart. Label and content must be co-located. Move event flag rendering to the right panel under its own title.

## Action item 11: NAV bridge must split HF return from HF liquidation

In any year where HF is liquidated (trigger or otherwise), the bridge currently shows one net line e.g. "HF Net Growth −$9.0M (13.0%)" — a negative number with a positive percentage that makes no sense. Must be two lines: "HF return (13%): +$X" and "HF liquidated for LP redemption: −$X". Same applies to reserve: when reserve is drawn for the trigger the line must say "Reserve used for LP redemption" not "Reserve Interest/Alloc".

## Action item 10: Hurdle trigger failure must show the liquidity working

When the trigger is attempted but insufficient, the event banner must show: what the LP needs, what each source can contribute (HF liquidation, retained cash, reserve, refi capacity), total available, and the shortfall. Currently shows only a label. This is the most important moment in the scenario and needs full numerical context. Also show "will retry next year" so the reader understands this is not a terminal failure.

## Action item 9: Retained cash invisible in NAV bridge

The $1.55M sitting in retained cash (from Year 4 refi) doesn't appear in the NAV bridge narrative. It shows in the pie chart but the bridge doesn't explain where it came from or why it's held. Needs a line in the bridge and a note that it's being held deliberately as dry powder.

## Action item 8: HF growth conflates return and reinvestment

The HF "+$1.4M (13%)" label includes both the 13% return on opening balance AND the reinvestment from RE cashflow routing. The percentage and dollar amount don't reconcile. Split into two lines: "13% return: +$1.14M" and "RE cashflow reinvested: +$231K" so a non-modeller can verify both numbers independently.

## Action item 7: "Reserve Interest/Alloc" label is misleading

The reserve earns 0% interest. The positive reserve movement is purely the 15% routing allocation from RE cashflow, not interest. Label should be "Reserve allocation (from cashflow routing)" or similar.

## Action item 6: Event notification banner when structural events fire

When a refinance, hurdle trigger attempt, or other structural event occurs, surface a highlighted event banner for that year — not just a flag code. Should explain what fired and why. For refi: show property value, LTV capacity, existing debt, net proceeds, and that it was a configured target year (not an automatic threshold). Distinguishing "scheduled" vs "threshold-triggered" events matters for a non-modeller.

## Action item 5: Pie chart label cutoff

When four slices are present (RE, HF, reserve, retained cash), the reserve label gets cut off. Fix by increasing chart height or reducing label font size dynamically based on slice count.

## Action item 4: Add dollar labels to cashflow routing chart bars

The routing chart shows proportions but no numbers. A non-modeller can see the split visually but can't read the actual amounts (e.g. $201K to LP, $84K to HF, $50K to reserve). Add data labels directly on the bars.

## Action item 2: Year-by-year drill-down detail block (right panel)

In walkthrough mode, add a collapsible detail block beneath each year's summary row showing the breakdown behind each number. Top row = summary (what a non-modeller reads first). Expand to see the components. Example for RE: NOI, debt service, capex → net. Example for HF: opening NAV, return, closing NAV, harvest status. Example for reserve: opening, drawdown/addition, closing. This is right-panel content (read, not set).
