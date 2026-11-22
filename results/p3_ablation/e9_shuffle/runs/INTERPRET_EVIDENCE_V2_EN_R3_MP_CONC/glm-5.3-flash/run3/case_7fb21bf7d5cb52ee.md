### Observed differences

- In the earlier window, the activities A31, A22, A20, A23, A24, A26, A25 and A32 ran as one fixed chain: A31 was followed by A22 in about 99 in 100 of its observed outgoing transitions, A22 by A20 (about 99 in 100), A20 by A23 (about 99 in 100), A23 by A24 (about 99 in 100), A24 by A26 (about 99 in 100), A26 by A25 (about 98 in 100) and A25 by A32 (about 88 in 100). [DIR010, DIR005, DIR004, DIR006, DIR007, DIR009, DIR008]

- In the later window this fixed order is largely gone. A24 now precedes A23 in about 84 in 100 traces (before, A23 preceded A24 in about 98 in 100); A24 precedes A20 in about 73 in 100 (before about 1 in 100); A26 precedes A23 in about 67 in 100 (before about 3 in 100). A20/A26, A23/A25 and A22/A24 now occur in both orders in roughly equal shares, where previously the first activity of each pair almost always came first. [REL020, REL015, REL022, REL017, REL021, REL018]

- Distances between consecutive activities spread out: A22 to A26 was exactly 4 steps apart in essentially every case and now ranges over 1–4 steps; A24 to A25 was always 2 steps and now ranges over 2–5; A22 to A23 was always 2 steps and now ranges over 2–5. [LAG013, LAG017, LAG010]

- Routing around this block changed as well: in the later window A23 leads directly to A32 in about 47 in 100 of its outgoing transitions (about 1 in 200 before), skipping A24, A26 and A25; A31 goes to A24 in about 46 in 100, an edge not observed earlier, while A31 → A22 falls from about 99 to 52 in 100; and back-edges appear, with A24 returning to A22 in about 23 in 100 of its outgoing transitions and A25 and A26 returning to A20/A22/A23 in roughly 10–20 in 100 of theirs. [DIR006, LAG016, DIR010, DIR007, DIR008, DIR009]

- Event positions shift accordingly: A23, A20 and A22 now occur later in the trace (mean relative position up by about 0.04–0.06), while A24, A25 and A26 occur earlier (down by about 0.02–0.05). [POS005, POS003, POS004, POS006, POS007, POS008]

- A10 behaves differently: it appears in about 70 in 100 traces in the later window versus about 19 in 100 before (mean occurrences per trace 0.78 vs 0.21); its occurrences now cluster early in the trace (median relative position about 0.15 vs 0.34, previously highly variable), and about 85 in 100 of its outgoing transitions go to A15, where before they were spread over A46, A16, A48 and A21. A14 now leads to A10 in about 66 in 100 of its outgoing transitions while its direct edge to A15 drops from about 86 to 33 in 100, and the A14→A15 distance shifts from mostly 1 step to mostly 2 steps. [OCC003, POS001, DIR002, DIR003, LAG002, LAG001, LAG003]

- A08 and A04 are executed in fewer traces: A08 in about 4 in 100 (before about 20 in 100) and A04 in about 10 in 100 (before about 21 in 100); A08's remaining outgoing transitions (8 observations) are too few to characterise. [OCC002, OCC001, DIR001]

- Smaller consolidations: A45 → A46 and A47 → A48 become near-always transitions (about 98 in 100 of outgoing transitions each, up from about 78 and 86 in 100). [DIR011, DIR012]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the ordering constraints around the block A31, A22, A20, A23, A24, A26, A25 changed: a chain executed in one fixed sequence in the earlier window (A31 → A22 → A20 → A23 → A24 → A26 → A25, ending at A32) is in the later window executed in a flexible order — A24 typically before A23 and A20, A26 before A23, several pairs with no fixed order, gaps varying over 1–5 steps, a new direct exit from A23 to A32 that bypasses A24, A26 and A25, and a new entry from A31 to A24. The change is shown directly by the order reversals, the successor redistributions and the gap spreads, and the position shifts point the same way; with 77 qualifying items against about 1 expected if nothing had changed, chance sampling cannot account for the pattern as a whole. [REL020, REL015, REL022, REL017, DIR006, DIR010, DIR007, LAG013, LAG016, POS005, POS006]

Limitations: the evidence cannot distinguish a genuinely reordered single pass from repeated re-entry into the block (back-edges such as A24 → A22 and A26 → A20 are consistent with rework), nor whether the mixed orders reflect one flexible behaviour or a mixture of two fixed variants; edge sets are inferred from observed outgoing transitions only. [DIR007, DIR008, DIR009]

Other differences: A10 appears to have been inserted between A14 and A15 — in the later window A14 leads to A10 in about two thirds of its outgoing transitions, A10 leads to A15 in about 85 in 100, and A10's participation rises from about 19 to 70 in 100 traces, whereas before it was rare and variably placed; A08 and A04 are executed in far fewer traces (about 4 and 10 in 100, from about 20 and 21); and the A45 → A46 and A47 → A48 transitions became near-obligatory. [DIR003, DIR002, OCC003, POS001, OCC002, OCC001, DIR011, DIR012]