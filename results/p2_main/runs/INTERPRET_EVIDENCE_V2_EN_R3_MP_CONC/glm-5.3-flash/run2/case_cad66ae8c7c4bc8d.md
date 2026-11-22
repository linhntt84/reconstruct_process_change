### Observed differences

- **A five-activity alternative block disappeared from execution.** In the earlier window, A19, A20, A25, A26 and A27 were each executed in roughly 17–25 in 100 traces (33–49 of 200 traces each) and essentially never together — exactly one of the five per case; in the later window each appears in at most about 1 in 100 traces (0–2 of 200). [OCC005, OCC006, OCC007, OCC008, OCC009, REL019, REL033]

- **A43 now bypasses this block.** Earlier, about 97 in 100 of A43's observed outgoing transitions went to one of the five (A26 about 24, A19 about 21, A27 about 19, A20 about 17, A25 about 16); in the later window about 86 in 100 go straight to A28. Accordingly, the A43→A28 distance fell from two steps (about 97 of 100 cases) to one step (about 86 of 100), and A15→A28 from five steps (about 99 of 100) to four (about 76 of 100). [DIR011, DIR006, DIR007, DIR008, DIR009, DIR010, LAG007, LAG005]

- **A10, between A48 and A49, is mostly skipped.** A10 ran in about 72 of 100 traces earlier (mean position about 0.93 of the trace, near the end) versus about 15 of 100 in the later window, where its few remaining executions sit at more varied positions. Earlier, A48 led to A10 in about 69 of 100 outgoing transitions and to A49 in about 29; in the later window A48 leads directly to A49 in about 85 of 100 and to A10 in about 2, and the A48→A49 distance fell from two steps (about 71 of 100) to one (about 86 of 100). [OCC004, POS001, DIR013, LAG015, LAG014]

- **Relations confirm both losses.** A10 co-occurred with A14, A15, A28, A43, A44, A48 or A49 in about 72 of 100 traces earlier versus about 14–15 later, those partners now running without A10 in about 86 of 100; pairs of block activities that earlier appeared one at a time (one of the pair present in about 35–45 of 100 traces, almost never both) now show neither activity in about 98–100 of 100 traces. [REL001, REL002, REL008, REL009, REL010, REL013, REL014, REL019, REL020, REL021, REL022, REL029, REL030, REL031, REL033, REL034, REL036]

- **Three activities became more frequent.** A02, A04 and A06 rose from about 4–5 in 100 traces each to about 17–21 in 100; their outgoing-transition mix also changed, but the earlier profiles rest on only 7–10 observations each. [OCC001, OCC002, OCC003, DIR001, DIR002]

- **Minor shifts.** A46 led to A47 in about 99 of 100 outgoing transitions earlier versus about 85 later, with small new edges; A14's position spread widened (standard deviation about 0.02 to 0.08); A43 and A48 sit about 0.02 of a trace later. [DIR012, POS002, POS008, POS009]

### Inference

Support level: Supported hypothesis

In the later window, two segments of the process were largely skipped. First, the block of five alternatives A19, A20, A25, A26 and A27 that followed A43 — earlier executed as exactly one-of-five per case — was bypassed: A43 now connects directly to A28 in about 86 of 100 cases, while the five activities are no longer observed (0–2 of 200 traces each). Second, A10, which earlier sat between A48 and A49 in about 72 of 100 cases, is now executed in only about 15 of 100, with A48 flowing directly to A49 in about 85 of 100. [DIR011, LAG007, OCC005, OCC006, OCC007, OCC008, OCC009, OCC004, DIR013, LAG015]

The support is direct and consistent: the rerouting is visible in the outgoing transitions of A43 and A48 with essentially full support in both windows (about 200 traces each), the step distances from A43 to A28 and from A48 to A49 each shrank from two to one, and the occurrence, relation and lag indicators all agree; with 89 qualifying control-flow items against roughly 1 expected for an unchanged process, this pattern as a whole cannot be explained by random re-splits of the two windows. [DIR011, DIR013, LAG007, LAG015, REL008, REL014]

Limitations: zero participation only means an activity was not observed, so the evidence cannot distinguish a fully removed segment from one that is now only rarely chosen — A20, A26 and A27 still appear in 1–2 later traces, and the behaviour of that rare remainder (for example A26→A36 and A27→A11) rests on a single observation each. [DIR009, DIR010, OCC006, OCC008, OCC009]

Other differences: A02, A04 and A06 are executed more often (about 4–5 in 100 traces earlier to about 17–21 later), but the evidence does not show where they now fit into the flow, so they are not part of the main hypothesis; smaller shifts include A46's edge to A47 dropping from about 99 to about 85 in 100 outgoing transitions and a slightly wider position spread for A14. [OCC001, OCC002, OCC003, DIR012, POS002]