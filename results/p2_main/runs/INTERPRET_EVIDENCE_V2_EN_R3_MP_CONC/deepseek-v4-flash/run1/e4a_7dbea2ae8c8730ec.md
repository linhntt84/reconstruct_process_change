### Observed differences

- In the earlier window, activities A14, A15, A20, A21, and A22 each appeared in 16–25% of traces (A14 21.5%, A15 18%, A20 16.5%, A21 24.5%, A22 19.5%) and never co-occurred with each other; together they covered all traces. In the later window, none of them appears in any trace. [OCC001–OCC005, REL001–REL004, REL010–REL012, REL015–REL016, REL019]
- In the earlier window, A38 always led to one of these five activities, and each of them led to A23. In the later window, A38 leads directly to A23 in all traces, and the five activities have no outgoing transitions. [DIR001–DIR006]
- The distance between A38 and A23 shrank from two steps to one step: in the earlier window A23 always occurred two positions after A38; in the later window it occurs immediately after. [LAG001]
- The position of A23 shifted slightly earlier in the trace (mean from about 0.40 to 0.38 of trace length). [POS006]
- For four activity pairs (A16–A28, A17–A28, A18–A28, A19–A28), the mean elapsed time between completions increased from about 1.0–1.05 hours to about 2.07–2.10 hours, roughly doubling. [TWAIT001–TWAIT004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the process changed by removing a set of alternative activities (A14, A15, A20, A21, A22) that used to be executed between A38 and A23; in the later window A38 leads directly to A23. This is directly shown by the disappearance of these activities, the change in A38's outgoing transitions from those five activities to A23, and the reduction in the A38–A23 lag from two steps to one. The number of control-flow items (44) far exceeds the 0.54 expected by chance, and the items are consistent across occurrence, direction, position, and lag indicators.

Other differences: The elapsed time between completions of A16/A17/A18/A19 and A28 roughly doubled (from about 1 hour to about 2 hours). This timing change is separate from the structural change and does not involve the removed activities.

A competing explanation that cannot be fully ruled out is that the five activities were not removed but became extremely rare; however, their combined coverage was 100% of traces before and 0% after, making a sampling artifact unlikely.