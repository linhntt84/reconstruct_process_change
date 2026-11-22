### Observed differences

- In the earlier window, activity A22 occurred in every trace (100%); in the later window it occurred in about 56.5% of traces. [OCC001]
- Activities A27, A28, A33, A34 and A35 were absent in the earlier window; in the later window each occurred in about 43.5% of traces. [OCC002, OCC003, OCC004, OCC005, OCC006]
- In the earlier window, A21 always led to A22; in the later window, A21 led to A22 in about 56.5% of traces and to A27, A28, A33, A34 or A35 in the remaining traces. [DIR001]
- In the later window, the five activities A27, A28, A33, A34 and A35 co-occurred in about 43.5% of traces, and within those traces they appeared in both orders (no fixed sequence). [REL018–REL027]
- In the earlier window, A22 always preceded A23; in the later window, when A22 was present it still preceded A23, but in about 43.5% of traces A23 occurred without A22. [REL007]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control flow: in the later window, the previously mandatory activity A22 is sometimes skipped, and instead a block of five activities (A27, A28, A33, A34, A35) is executed between A21 and A23. This is directly shown by the drop in A22 participation, the appearance of the five activities, the change in A21's outgoing edges, and the relational evidence that the five activities co-occur and precede A23. The five activities appear together in about 43.5% of traces and have no fixed order among themselves, suggesting they form a parallel or unordered subprocess. A competing explanation that cannot be fully ruled out is that the five activities are actually a single repeated pattern rather than independent activities, but the evidence consistently points to a replacement of A22 by this block. Other differences: A21's position shifted slightly earlier (mean from 0.492 to 0.460), which is minor and likely a consequence of the new path. [OCC001, OCC002–OCC006, DIR001, REL001, REL007, REL013–REL027, POS001]