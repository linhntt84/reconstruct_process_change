### Observed differences

- Two activities are no longer observed in the later window: A01 and A02 each ran in about 50 in 100 traces before (99 of 200) and in none of the 200 later traces; A01's outgoing branches to A07, A10, A08 and A12, and A02's link to A14, are no longer observed. [OCC001, OCC002, DIR001, DIR002, POS001, POS002, REL001]

- The A06–A13 cycle largely stopped. Earlier, A06 appeared about twice per trace in about half of all traces, was followed by A13 in about 51 in 100 of its outgoing edges and by A02 in about 49 in 100, and A13 led back to A06 in about 99 in 100 cases. In the later window A06 occurs about once per trace in about 36 in 100 traces (repetition in about 11 in 100 traces, down from about 39), and both A06 and A13 now lead exclusively to A14. [OCC006, OCC013, DIR004, DIR010, LAG014, LAG041]

- A14 changed role: earlier it was always followed by A01; in the later window it is followed by A08 in about 56 in 100 cases, A07 in about 35, A12 in about 4 and the new A09 in about 4 — essentially the branch set A01 used to have. [DIR011, DIR002, DIR001]

- A09 appears only in the later window (about 24 in 100 traces, none before), sitting between A07/A12 and A11: A07 now sends about 48 in 100 of its outgoing edges to A09, and A09 leads to A11 in about 46 in 100 and to A12 in about 44 in 100 cases. [OCC009, DIR005, DIR007, POS007, REL052]

- A08's route to A05 was re-routed through A10: earlier A08 was always directly followed by A05 (one step); now A08 is always followed by A10, which then precedes A05 (two steps). Participation of both activities roughly doubled — A08 from about 24 to 50 in 100 traces, A10 from about 26 to 50. [DIR006, REL059, LAG023, OCC008, OCC010, REL036, REL038]

- A04's exit split: earlier almost all of its outgoing edges went to A06 (about 99 in 100); in the later window about 60 in 100 go to A06 and about 39 in 100 directly to A13, with the A04→A13 pair now adjacent where it previously sat two or more steps apart. [DIR003, LAG001, LAG006]

- Cross-segment distances shortened consistently with this reconnection, e.g. A04→A14 from three-plus steps to two, A13→A08 and A13→A07 from five-plus steps to two, A14→A08 from two steps to one, and A11→A13 from two steps to one. [LAG007, LAG038, LAG037, LAG043, LAG029]

- Largely unchanged: A03, A04 and A05 still run in about half of the traces with A04 preceding A05, and A07, A11 and A12 keep a participation of about 23 in 100 traces. [OCC003, OCC004, OCC005, REL024, OCC007, OCC011, OCC012]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the flow around the former A02 → A14 → A01 chain was reorganised: in the later window A01 and A02 are no longer observed, A06 and A13 — which previously cycled with each other and exited via A02 — now both lead directly into A14, A14 took over the branching that A01 previously performed (to A07, A08, A12 and the newly observed A09), A08 reaches A05 via A10 instead of directly, and A04 additionally feeds A13 directly. [OCC001, OCC002, OCC009, DIR003, DIR004, DIR010, DIR011, DIR006, LAG023]

The rewiring is shown directly by successor profiles, by participation dropping to zero (A01, A02) or rising from zero (A09), and by relation and lag evidence that matches the new wiring step for step — for example the A08→A05 distance lengthened by exactly one step while A08→A10 appeared, A14→A08 shortened from two steps to one, and A13→A08 shortened from five-plus steps to two. This coherence across occurrence, successor, relation and lag views makes sampling noise or a single rare variant an unlikely explanation for the pattern as a whole. [DIR006, DIR007, LAG007, LAG029, LAG038, LAG043, REL059, OCC006]

Limitations: "not observed" is not proof of removal — A01 and A02 could still occur at rates that 200 traces per window would not reveal — and the evidence cannot rule out that the two windows draw on different process variants (for example, a variant containing A01/A02 that stopped appearing) rather than a single modified flow. [OCC001, OCC002]

Other differences: several surviving activities now occur slightly earlier within traces by event order (for example A08's mean position moved from about 0.91 to 0.72 of the trace, A14's from about 0.55 to 0.45); these shifts follow from the re-routing above rather than indicating an independent change. [POS004, POS006, POS008, POS011, POS012]