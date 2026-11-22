### Observed differences

- In the earlier window, A27 was executed in every trace (100 in 100) exactly once, and A26 routed almost all of its outgoing transitions to A27 (about 99 in 100), which in turn led to A28 (about 99 in 100). In the later window, A27 appears in only about 51 in 100 traces. [OCC001, DIR001, DIR002]
- Three activities that never occurred in the earlier window (0 of 200 traces) — A32, A33 and A38 — each now occur in about 49 in 100 traces, once per trace when present. [OCC002, OCC003, OCC004]
- A26's outgoing transitions are now split: about 50 in 100 still go to A27, while roughly 17 go to A33, 16 to A38 and 15 to A32. [DIR001]
- The new activities were not observed as sources earlier; now each leads to A28 and to the other new activities (for example, A38 → A28 accounts for about 43 in 100 of A38's outgoing transitions, A33 → A32 about 43 in 100, A32 → A38 about 35 in 100). [DIR003, DIR004, DIR005]
- A27 and each of A32, A33, A38 now behave as alternatives: they co-occur in at most about 1 in 200 traces, while each appears alone in roughly half of all traces. [REL006, REL007, REL008]
- The three new activities co-occur with one another in about 49 in 100 traces and appear in both orders in similar proportions (for example, A32 before A33 in about 23 in 100 traces and A33 before A32 in about 27 in 100), so they have no fixed internal order. [REL012, REL013, REL014]
- A28 still occurs in essentially every trace, but now without A27 in about 49 in 100 traces (earlier it always co-occurred with A27); each new activity precedes A28 in about 49 in 100 traces, and A26 precedes both A27 and each new activity whenever they co-occur. [REL001, REL002, REL003, REL004, REL005, REL009, REL010, REL011]
- The new activities sit around the middle of the trace by event position (medians about 0.48–0.50). [POS001, POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new alternative branch was inserted between A26 and A28, involving A27 and the previously unobserved activities A32, A33 and A38. In the earlier window every trace ran A26 → A27 → A28; in the later window about half the traces keep that path, while the other half skip A27 and route from A26 through A32, A33 and A38 — executed as a group in varying order — before continuing to A28. The routing split at A26, the drop of A27 from universal to about half of traces, the mutual exclusivity between A27 and each new activity, and A28 now occurring without A27 in about half the traces all point to this directly. [OCC001, OCC002, OCC003, OCC004, DIR001, REL005, REL006, REL007, REL008]

The placement and internal structure of the new branch are also shown relationally: A26 precedes each new activity, each new activity precedes A28, the three co-occur in about 49 in 100 traces without a fixed order among themselves, and they occupy the mid-trace region. The volume of qualifying items (26, against well under one expected by chance at these thresholds) cannot be explained by random sampling as a whole. [DIR003, DIR004, DIR005, POS001, POS002, POS003, REL001, REL002, REL003, REL004, REL009, REL010, REL011, REL012, REL013, REL014]

Limitations: the evidence cannot rule out that the two windows draw from different process variants or populations in shifting proportions rather than reflecting a change at a single point in time, and it cannot show whether the new branch existed at a very low rate before — it was simply not observed in the 200 earlier traces. [OCC002, OCC003, OCC004]

Other differences: A26 and A27 each show a few additional low-frequency outgoing edges in the later window (each about 1–2 in 100 of the source's outgoing transitions, e.g. towards A23 from A26 and A09 from A27), and A27 recurs in about 1 in 200 traces; these are minor and consistent with sampling variation. [DIR001, DIR002, OCC001]