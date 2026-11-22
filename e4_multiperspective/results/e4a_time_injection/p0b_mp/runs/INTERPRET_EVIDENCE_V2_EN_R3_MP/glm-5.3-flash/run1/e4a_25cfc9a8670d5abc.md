### Observed differences

- In the earlier window, A27, A28 and A29 each ran in every one of the 200 traces; in the later window A27 appears in about 46 in 100 traces and A28 and A29 in about 55 in 100, while A21, A23 and A24 still appear in every trace in both windows. [OCC001, OCC002, OCC003, POS002, POS003, POS004]
- The early segment changed: before, A20's outgoing transitions split between A28 (about 47 in 100) and A29 (about 53 in 100), with A21 reached three steps later; in the later window A20 is always followed directly by A21. [DIR001, LAG001]
- The late segment changed: before, A23 was always followed by A27; in the later window A23's outgoing transitions split about 46 in 100 to A27, about 30 to A28 and about 25 to A29. [DIR002]
- A27 and the pair A28/A29 became alternatives: before, all three always co-occurred; in the later window A27 never co-occurs with A28 or A29 — about 46 in 100 traces contain A27 without the pair, about 55 contain the pair without A27. [REL013, REL014, REL015]
- The order around the pair reversed: before, A28 and A29 always ran before A21 and A23; in the later window A21 and A23 always run before them. [REL005, REL006, REL008, REL009]
- Distances shifted accordingly: A20→A28/A29 grew from 1–2 steps to 4–5 steps, A28/A29→A24 shrank from 5 steps to 1–2 steps, A23→A24 grew from 2 to 2–3 steps, and A28/A29 now sit later in the trace (mean relative position about 0.43 vs about 0.55). [LAG003, LAG004, LAG006, LAG007, LAG008, POS006, POS007]
- The elapsed time between consecutive completions into A20 roughly doubled: A14→A20 from about 1.0 h to about 2.0 h mean, and A15→A20 likewise, with roughly 100 observations per segment per window. [TWAIT001, TWAIT002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the two-activity block A28–A29, which in the earlier window always executed between A20 and A21 (A20 → A28/A29 in either order → A21), now executes after A23 as an alternative to A27: in the later window about 46 in 100 traces run A23 → A27 → A24, while about 54 in 100 skip A27 and run the pair A28–A29 (in either order) between A23 and A24. A27 changed from mandatory to optional, and A28/A29 from mandatory-and-early to conditional-and-late. [DIR001, DIR002, REL005, REL006, REL008, REL009, REL013, REL014, LAG001, LAG003, LAG007, LAG008, OCC001, OCC002, OCC003]

The placement change is shown directly by the successor changes at A20 and A23, the complete order reversals between A21/A23 and the pair, and the matching lag shifts; the alternative structure is shown by the strict mutual exclusivity between A27 and the pair, whose participation levels (about 46 and 55 in 100) match the split. The pair's internal order remains unfixed in both windows, consistent with relocating the pair rather than reordering it. With 37 qualifying control-flow items against roughly 0.4 expected if nothing had changed (each item's difference exceeding about 995 of 1000 random re-splits), sampling variation cannot account for the pattern as a whole. [DIR001, DIR002, REL005, REL013, REL015, LAG001, LAG007]

A competing explanation the evidence cannot rule out is that the segment between A21 and A23 was restructured around activities not covered by this evidence (at least one unobserved activity sits between them in both windows), producing the same observable order relations. [LAG002]

Other differences: The elapsed time between consecutive completion events on the segments A14→A20 and A15→A20 roughly doubled (mean about 1.0 h to about 2.0 h; 2 time items against about 0.01 expected without change). This is a timing hypothesis in its own right; the evidence cannot show whether it is connected to the restructuring above, and it concerns elapsed time between completions, not pure waiting or service time. [TWAIT001, TWAIT002]