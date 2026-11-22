### Observed differences

- In the later window, activity A10 no longer occurs: its mean occurrences per trace dropped from 0.44 to 0, and its trace participation from 44% to 0% [OCC001, POS001].
- The outgoing transitions of A04 changed: before, about 55% went to A10 and 10% to A12; after, about 73% go to A12 and none to A10 [DIR002].
- A10's outgoing transitions (mostly to A12, 82%) disappeared because A10 is absent [DIR003].
- A03 and A11 now route to A04 and A12 instead of A10 and A02: A03 before went to A10 (60%) and A02 (40%), after to A04 (50%) and A12 (50%) [DIR001]; A11 before to A10 (40%) and A02 (60%), after to A04 (78%) and A12 (22%) [DIR004]. (Note small support for these two.)
- A04 and A10 no longer co-occur: before they co-occurred in 44% of traces, with A04 before A10 in 31.5% and A10 before A04 in 12.5%; after, A04 appears alone in 57.5% of traces and they never co-occur [REL001].
- Similarly, A10 and A12 no longer co-occur: before they co-occurred in 44% (always A10 before A12); after, A12 appears alone in 57.5% and they never co-occur [REL002].
- The distance between A04 and A12 shrank: before, the lag between them was 2 steps in 56% of cases and 1 step in 11%; after, it is 1 step in 75% and 2 steps in 19% [LAG001].

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that activity A10 was removed from the process, and the control flow now routes through A04 and A12 instead. Specifically, A04 now leads to A12, and A03 and A11 now lead to A04/A12 instead of A10/A02. The disappearance of A10 is directly shown by its zero participation and occurrence in the later window [OCC001, POS001, DIR003], and the new path is evidenced by A04's shift to A12 [DIR002] and the closer lag between A04 and A12 [LAG001]. The co-occurrence changes confirm that A10 no longer appears with A04 or A12 [REL001, REL002].

Other differences: The routing changes for A03 and A11 are based on small samples (5–10 traces) and are less reliable, but they are consistent with the main shift.

A competing explanation that cannot be fully ruled out is that A10 still exists but was not observed in the 200-trace sample; however, its complete absence from all indicators, combined with the coherent rerouting, makes this unlikely.