### Observed differences

- In the earlier window, activities A14, A15, A20, A21, and A22 each appeared in about 17–25% of traces (A14 21.5%, A15 18%, A20 16.5%, A21 24.5%, A22 19.5%). In the later window, none of these activities appear at all. [OCC001–OCC005]
- In the earlier window, each of these five activities had all its outgoing transitions go to A23. In the later window, they have no outgoing transitions. [DIR001–DIR005]
- In the earlier window, A38 had outgoing transitions to these five activities (shares between 16.5% and 24.5%). In the later window, A38's only outgoing transition is to A23. [DIR006]
- The lag between A38 and A23 changed from 2 steps to 1 step, so A23 now directly follows A38. [LAG001]
- In the earlier window, A14, A15, A20, A21, and A22 co-occurred with A23 and with A38 (e.g., A14–A23 co-occurrence 21.5%, A21–A23 24.5%, A14–A38 21.5%, A21–A38 24.5%). In the later window, these co-occurrences disappear; A23 and A38 appear alone. [REL005, REL006, REL020, REL021]
- A41 and A42 previously co-occurred with these five activities (e.g., A14–A41 co-occurrence 12%, A21–A41 12.5%). In the later window, they no longer co-occur with them; A41 and A42 appear alone in 67% of traces. [REL008, REL009, REL013, REL014, REL017, REL018, REL023–REL026]
- The elapsed time between A16 and A28, A17 and A28, A18 and A28, and A19 and A28 increased from about 1 hour to about 2 hours (means: A16–A28 from 1.01 to 2.10 hours; A17–A28 from 1.03 to 2.07; A18–A28 from 1.05 to 2.08; A19–A28 from 1.04 to 2.09). [TWAIT001–TWAIT004]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in which activities A14, A15, A20, A21, and A22 are no longer executed, and A38 now connects directly to A23 instead of going through those activities. This is directly shown by the disappearance of these activities, the change in A38's outgoing transitions, the shift in the A38–A23 lag from 2 to 1, and the loss of co-occurrences between these activities and A23, A38, A41, and A42. The number of control-flow items (44) far exceeds the 0.54 expected by chance, and the time items (4) far exceed the 0.01 expected, so the overall evidence is not a chance artifact.

Other differences: The elapsed time between A16–A19 and A28 increased from about 1 hour to about 2 hours. This is a separate timing change, not directly tied to the structural change.

A competing explanation that cannot be fully ruled out is that the five activities were moved to a different part of the process not captured by the observed windows, but the DIR and REL evidence strongly indicate their absence. The timing change could also be due to unrelated factors, but it is consistent and large.