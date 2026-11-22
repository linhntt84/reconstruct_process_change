### Observed differences

- In the earlier window, activities A25, A26, A31, A32 and A33 each occurred on average about 3.6 times per trace and were repeated (more than one occurrence) in about 70% of traces; in the later window they each occur about once per trace and repeat in about 1% of traces, while still appearing in every trace. [OCC001, OCC002, OCC003, OCC004, OCC005]
- The successor of A33 changed: in the earlier window about 72% of its outgoing transitions went to A25 and 28% to A20; in the later window about 98% go to A20 and 2% to A25. [DIR001]
- For pairs among these activities, the share of traces where the two activities are interleaved or repeated dropped from about 70% to about 1%. In the later window, pairs such as A25–A26, A25–A31, A25–A32, A25–A33, A26–A33, A31–A33 and A32–A33 appear in a fixed order (A before B) in about 99% of traces, whereas pairs like A26–A31, A26–A32 and A31–A32 appear in both orders about half the time each, but never interleaved. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010]
- The distance between these activities within a trace shortened: for example, the lag between A26 and A31 was previously spread over 1 to 5 steps, and in the later window about 63% of occurrences are 1 step apart and 32% are 2 steps apart; similar shifts appear for A26–A32, A31–A32, A32–A26 and A31–A26. [LAG001, LAG002, LAG004, LAG005, LAG007, LAG008]
- The relative positions of A25, A26, A31, A32 and A33 within traces became much more concentrated: the standard deviation of their relative position dropped from about 0.15 to about 0.06, and the upper quartile moved earlier. [POS001, POS002, POS003, POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process changed from a loop that repeated a block of activities (A25, A26, A31, A32, A33) to a single execution of that block, with A33 now routing to A20 instead of back to A25. The drop in repetition, the change in A33's successor, the loss of interleaving, the shortened lags and the reduced position spread all point to the same underlying change. A competing explanation that the activities were simply removed or added is ruled out because participation remains 100% in both windows; the change is in how often and in what order they are executed. The evidence cannot rule out that the loop was replaced by a different mechanism that still produces a single pass, but the direct successor change from A33 to A20 strongly supports the loop removal.

Other differences: The order between some pairs (e.g., A26–A31) is now mixed (both orders about half) rather than interleaved, which is consistent with the loss of repetition. [REL005, REL006, REL008]