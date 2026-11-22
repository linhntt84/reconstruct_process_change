### Observed differences

- In the later window, activities A19, A20, and A25 appear in about 29%, 41%, and 30% of traces respectively, whereas they were absent in the earlier window. [OCC001, OCC002, OCC003]
- These new activities are mutually exclusive: in the later window, A19 and A20 never co-occur, A19 and A25 co-occur in 0.5% of traces, and A20 and A25 co-occur in 0.5% of traces; each appears alone in its traces. [REL001, REL002, REL006]
- In the later window, A27 and A28 now have outgoing transitions to A19, A20, and A25, which they did not have before. A27's transition to A28 dropped from about 97% to about 43%, and A28's transition to A29 dropped from about 98% to about 57%. [DIR004, DIR005]
- The new activities appear after A27 and A28 and before A29: in the later window, A19, A20, and A25 co-occur with A27 in 29%, 41%, and 30% of traces, respectively, and in those co-occurrences they almost always follow A27. They also co-occur with A28 and A29, with A19/A20/A25 before A29 in most of those co-occurrences. [REL003, REL007, REL010, REL005, REL009, REL012]
- The distance between A27 and A28, A27 and A29, and A28 and A29 increased: for example, A27 to A28 was at lag 1 in 97.5% of traces before and only 42.8% after, with lag 2 in 52.5% after; A28 to A29 was at lag 1 in 98% before and 56.5% after, with lag 2 in 41.3% after. [LAG001, LAG002, LAG003]
- The positions of A27 and A29 shifted slightly: A27 moved earlier (mean position from 0.481 to 0.463) and A29 later (mean from 0.552 to 0.566). [POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in the later window a new optional step, consisting of one of three alternative activities (A19, A20, or A25), is inserted between the existing activities A27/A28 and A29. In the earlier window, the process typically went A27 → A28 → A29 (with A27 to A28 in about 97% of A27's transitions and A28 to A29 in about 98% of A28's transitions). In the later window, A27 and A28 sometimes lead to A19, A20, or A25 instead of directly to A28/A29, and these new activities then lead to A29. The new activities are mutually exclusive alternatives, appearing in about 29–41% of traces, and they are placed between A27/A28 and A29, as shown by the increased lags between A27–A28, A27–A29, and A28–A29, and by the positional shifts. The evidence is strong: 28 control-flow items were flagged against an expected 0.56 by chance. A competing explanation that the new activities are simply rare variants is unlikely given the large number of consistent items, but the exact routing shares (which of A19/A20/A25 is chosen) vary and are not fully specified.

Other differences: The relative frequency of the old direct path A27→A28→A29 decreased, but it still exists in a substantial share of traces. No other structural changes are indicated.