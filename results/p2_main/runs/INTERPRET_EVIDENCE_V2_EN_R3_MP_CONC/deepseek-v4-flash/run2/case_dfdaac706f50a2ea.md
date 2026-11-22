### Observed differences

- In the earlier window, activities A27, A36, A37 and A42 appeared in every trace (participation 1.0, mean occurrences ~1.0). In the later window, each appears in about half the traces (participation 0.47–0.535, mean occurrences ~0.5). [OCC001, OCC002, OCC003, OCC004]
- A25's outgoing transitions changed: before it went to A42, A36 and A37 (about 0.34, 0.34 and 0.31); after it goes to A28 in about 98% of cases. [DIR001]
- A26's outgoing transitions changed: before it went to A27 in about 98% of cases; after it goes to A27 in about 53% and to A37, A42 and A36 in about 16%, 17% and 14% respectively. [DIR002]
- A36, A37 and A42 now often lead to A31 (about 0.28–0.36 of their outgoing transitions), whereas before they led mainly to A28 and to each other. [DIR003, DIR004, DIR005]
- Co-occurrence of A25 with A27, A36, A37 and A42 dropped from 1.0 to about 0.5, with A25 occurring alone in about half the traces. [REL001, REL002, REL003, REL004]
- Co-occurrence of A26 with A27 dropped from 1.0 to 0.535; with A36, A37 and A42 it dropped from 1.0 to about 0.47, and the order reversed (before A36/A37/A42 preceded A26, after A26 precedes them). [REL005, REL006, REL007, REL008]
- A27 and A36, A37, A42 now almost never co-occur (co-occurrence ~0.01), whereas before they co-occurred in all traces. [REL011, REL012, REL013]
- A28 now immediately follows A25 (lag 1 in about 98% of cases, vs lag 4 before). [LAG001]
- A26 and A31 are now often 4 steps apart (lag 4 in about 46% of cases, vs lag 2 before). [LAG005]

### Inference

Support level: Supported hypothesis

The process changed from a single flow that always included A27, A36, A37 and A42 to a process with two alternative branches: one branch includes A27 (and A28), the other includes A36, A37 and A42 (and A28). A25 now always leads to A28, whereas before it led to A36/A37/A42. A26 now leads to A27 in about half the cases and to A36/A37/A42 in the other half. The activities A27, A36, A37 and A42 became optional/alternative, each appearing in about half the traces. This is supported by the large drop in participation and co-occurrence for these activities, the shift in A25's and A26's outgoing transitions, and the near-disappearance of co-occurrence between A27 and the trio. The evidence is control-flow only; no time or resource indicators are present. Some LAG items have very low support in the later window (e.g., A25–A36, A25–A37, A25–A42), but the main pattern is corroborated by many OCC, DIR and REL items.

Other differences: A31 now appears as a successor of A36, A37 and A42, and the order between A26 and A36/A37/A42 reversed. These are consistent with the branch split described above. A competing explanation that cannot be fully ruled out is a change in case mix, but the routing changes (A25→A28, A26→A27 vs trio) are direct and consistent.