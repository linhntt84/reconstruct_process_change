### Observed differences

- A08 participation dropped from 74% of traces to 23.5%, and its mean occurrences per trace fell from 0.775 to 0.24. [OCC003]
- A02, A04, A10 and A17 increased participation: A02 from 5.5% to 20.5%, A04 from 4% to 17%, A10 from 8% to 24%, A17 from 20% to 33%. [OCC001, OCC002, OCC004, OCC005]
- A08 moved later in the trace (mean normalized position from 0.24 to 0.45), while A19, A20, A25, A26 and A27 moved earlier (means from about 0.61 to about 0.33). [POS001, POS002, POS003, POS004, POS005, POS006]
- A19, A20, A25, A26 and A27 previously sent most outgoing transitions to A30/A34; in the later window they send 92–97% of transitions to A28. [DIR004, DIR005, DIR006, DIR007, DIR008]
- A47 previously sent 96.5% of transitions to A28; in the later window it sends about 15–22% each to A26, A27, A25, A20 and A19. [DIR011]
- A08 used to precede A28, A29, A30, A34 and A47 in about 70% of traces; in the later window that share drops to about 14–15% and the reverse order appears. [REL010, REL011, REL012, REL013, REL014]
- A19, A20, A25, A26 and A27 used to follow A28 (e.g., A20–A28: A28 before A20 in 20% of traces); in the later window they precede A28 (A20 before A28 in 20%). [REL016, REL017, REL018, REL019, REL020, REL021, REL023, REL024]
- Lag distances changed: A08–A16 became less adjacent (lag 1 from 98% to 56%), A08–A28 distance increased (lag 4 from 95% to lag 5 65%), and A47–A28 distance increased (lag 1 from 96.5% to lag 2 84%). [LAG001, LAG003, LAG027]

### Inference

Support level: Supported hypothesis

The evidence supports a reordering of the process: a group of activities (A19, A20, A25, A26, A27) that previously occurred after A28 and then led to A30/A34 now occur before A28 and lead to A28. A08, which used to be a frequent early activity preceding A28 and several others, became much less frequent and moved later in the trace. A47, which used to lead to A28, now leads to that same group of activities. This is supported by consistent successor changes (DIR), order reversals (REL), position shifts (POS) and lag-distance changes (LAG). The screening shows 74 control-flow items against 0.93 expected by chance, so the overall difference is far beyond sampling noise.

Other differences: A02, A04, A10 and A17 increased their participation, which is not part of the main reordering hypothesis.

A competing explanation that cannot be fully ruled out is that the observed changes reflect a shift between two distinct process variants rather than a single reordering, but the coherent pattern across multiple indicators makes that less likely.