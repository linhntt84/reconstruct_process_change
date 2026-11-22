### Observed differences

- In the earlier window, activity A06 occurred in every trace (mean 1.0 per trace, 100% participation); in the later window it occurred in no trace (0% participation). [OCC001]
- In the earlier window, A03 had outgoing transitions to A06 in 106 of 200 traces; in the later window A03 had no outgoing transitions, and its position became fixed at the end of the trace (mean normalized position 1.0, standard deviation 0). [DIR001, POS001]
- In the earlier window, A06 had outgoing transitions to A03 in 94 of 200 traces; in the later window A06 is absent. [DIR003]
- A04's outgoing transitions: earlier, about 52% to A02, 26% to A03, and 23% to A06; later, about 50% to A03 and 50% to A02, with no A06. [DIR002]
- A03 and A06 co-occurred in all traces earlier, with mixed order (A03 before A06 in 53%, A06 before A03 in 47%); later, A03 occurs alone. [REL001]
- A04 and A06 co-occurred in all traces earlier, with A04 before A06 in 44% and interleaved/repeated in 56%; later, A04 occurs alone. [REL002]
- The lag between A04 and A03: earlier, A04 was directly followed by A03 in 53% of traces and with one activity in between in 47%; later, A04 is always directly followed by A03 (lag 1 in 100%). [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that activity A06 was removed from the process. In the earlier window, A06 was executed in every trace, often between A04 and A03; in the later window, A06 no longer occurs, A04's outgoing transitions no longer include A06, and A04 is always directly followed by A03, which is always the final activity. The change is directly shown by the disappearance of A06 (OCC001, POS003), the loss of A06 from A04's outgoing transitions (DIR002), the loss of A06 from A03's outgoing transitions (DIR001), and the change in A04–A03 lag from sometimes having an intervening activity to always being consecutive (LAG001). The evidence is consistent across all control-flow indicators. A competing explanation that cannot be fully ruled out is that A06 was renamed or merged with another activity, but within the observed activity set it is absent.

Other differences: A04's position shifted later (mean normalized position from 0.59 to 0.65) and A03's position became fixed at the end; these are consistent with the removal of A06 and not treated as separate changes.