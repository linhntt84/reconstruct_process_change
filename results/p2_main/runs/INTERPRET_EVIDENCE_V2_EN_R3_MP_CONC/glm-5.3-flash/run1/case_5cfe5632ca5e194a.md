### Observed differences

- Five activities — A14, A15, A20, A21 and A22 — disappeared from the traces. In the earlier window each ran in a minority of cases (A21 in about 25 of 100 traces, A14 about 22, A22 about 20, A15 about 18, A20 about 17), always exactly once per trace; in the later window none of the five appears in any of the 200 traces. [OCC001, OCC002, OCC003, OCC004, OCC005]
- In the earlier window these five behaved as mutually exclusive alternatives: no trace contained two of them together, and in roughly 54–66 of 100 traces none of them ran. In the later window every trace contains none of them. [REL001, REL002, REL003, REL004, REL007, REL008, REL009, REL010, REL011, REL012]
- In the earlier window, A38's observed outgoing transitions were split entirely across these five activities (about 25% to A21, 22% to A14, 20% to A22, 18% to A15, 17% to A20); in the later window A38 leads only to A23. [DIR006]
- In the earlier window, each of the five activities was always followed by A23 (its only observed outgoing edge), and A38 always preceded it; in the later window A23 occurs alone in every trace. [DIR001, DIR002, DIR003, DIR004, DIR005, REL005, REL006, REL013, REL014]
- The distance from A38 to A23 shortened from two event positions (one activity in between) in all 200 earlier traces to one position (immediate succession) in all 200 later traces. [LAG001]
- A23 itself ran in every trace in both windows, at a slightly earlier mean relative position afterwards (about 0.40 vs 0.38 of the trace). [POS006]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the block of five alternative activities (A14, A15, A20, A21, A22) that previously sat between A38 and A23 is no longer executed: in the earlier window A38 passed each case on to exactly one of the five alternatives, which in turn always led to A23, whereas in the later window A38 leads directly to A23 and none of the five is observed. [DIR006, LAG001, OCC001, OCC002, OCC003, OCC004, OCC005, REL005, REL006, REL013, REL014]

The hypothesis rests on direct and mutually consistent signs: the successor profile of A38 moved completely from the five activities to A23, the A38-to-A23 distance fell from two positions to one in every trace, the five activities fell from about 17–25 in 100 traces to zero observed occurrences, and their pairwise relations confirm they were alternatives executed between A38 and A23. The volume of flagged items (32, against roughly 0.42 expected for an unchanged process) cannot be explained by random re-sampling of the two windows. [DIR006, LAG001, OCC001, OCC002, OCC003, OCC004, OCC005, REL001, REL002, REL003, REL004, REL007, REL008, REL009, REL010, REL011, REL012, REL005, REL006, REL013, REL014]

A competing explanation the evidence cannot rule out is that the five activities still execute at a rate too low to appear in 200 traces rather than having been removed entirely; zero participation only means they were not observed. Within the observed traces, however, A38 never routes to them any more. [OCC001, OCC002, OCC003, OCC004, OCC005, DIR006]

Other differences: none beyond the slight advance of A23's mean position, which is consistent with the same change. [POS006]