### Observed differences

- In the later window, activities A19, A20, and A25 appear in about 29%, 41%, and 31% of traces respectively, while they were completely absent in the earlier window. [OCC001, OCC002, OCC003]
- In the later window, these new activities have outgoing transitions to A28 and A29 (and a few others); in the earlier window they had no outgoing transitions. [DIR001, DIR002, DIR003]
- The routing from A27 changed: earlier about 97% of its outgoing transitions went to A28; later only about 43% go to A28, with about 22% to A20, 16% to A25, and 14% to A19. [DIR004]
- The routing from A28 changed: earlier about 98% went to A29; later about 57% go to A29, with about 16% to A20, 13% to A19, and 12% to A25. [DIR005]
- The new activities are alternatives: A19 and A20 never co-occur, A19 and A25 co-occur in about 0.5% of traces, and A20 and A25 in about 0.5%. [REL001, REL002, REL006]
- The new activities are placed between A27/A28 and A29: e.g., A19 occurs after A27 in 29% of traces, after A28 in 29% (with mixed order), and before A29 in 29% of traces; similar patterns hold for A20 and A25. [REL003, REL004, REL005, REL007–REL012]
- The distance between A27 and A28 increased: earlier A27→A28 had lag 1 in 97.5% of traces; later lag 1 in 42.8% and lag 2 in 52.5%. [LAG001]
- The distance between A28 and A29 increased: earlier lag 1 in 98%; later lag 1 in 56.5% and lag 2 in 41.3%. [LAG003]
- The distance between A27 and A29 increased: earlier lag 2 in 95.5%; later lag 3 in 92.0%. [LAG002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a new step was inserted into the existing A27→A28→A29 path: after A27 and A28, one of the new activities A19, A20, or A25 is executed before A29. These activities were absent before, appear in a substantial share of traces, are mutually exclusive, and are positioned between A27/A28 and A29, as shown by the increased lags between the original activities. The screening count (28 items vs 0.56 expected by chance) makes it very unlikely that this is a random fluctuation.

Other differences: A27 occurs slightly earlier and A29 slightly later in the trace, consistent with the insertion. [POS004, POS005]

A competing explanation that cannot be fully ruled out is that the new activities are not strictly inserted but represent a parallel branch that happens to be ordered before A29; however, the mutual exclusivity and the consistent ordering evidence make the insertion interpretation more direct.