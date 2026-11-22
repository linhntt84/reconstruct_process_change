### Observed differences

- Both A15 and A16 occur in every trace in both windows, but in the later window they repeat more often: for each activity, mean occurrences per trace rose from about 1.45 to about 1.8, and the share of traces in which the activity occurs more than once rose from about 30 in 100 to about 44 in 100. [OCC001, OCC002]
- In the later window, A16 hands over to A15 more often: about 44 in 100 of A16's outgoing transitions led to A15, up from about 30 in 100 (roughly 160 transitions vs roughly 90), while transitions to A42 fell from about 37 in 100 to about 26 in 100 (about 105 transitions before vs about 95 after, roughly stable in absolute terms). A16's total outgoing transitions grew from 291 to 361, in line with its higher repetition. [DIR001, OCC002]
- The direct hand-over from A15 to A16 became less common: the ordered pair occurs within five steps in essentially all traces in both windows, but the share of pairs at distance 1 fell from about 43 in 100 to about 28 in 100, with pairs at separations of 2–5 steps slightly more common. [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that, in the later window, A15 and A16 are executed with more repetitions per case and with looser adjacency: both activities still run in every case, but each repeats in about 44 in 100 cases (previously about 30), A16 continues to A15 more often (about 30% to about 44% of its transitions) and to A42 relatively less often (about 37% to about 26%), and A15 is directly followed by A16 in only about 28 in 100 of their observed pairs, down from about 43. Four control-flow items qualified against roughly 0.5 expected if nothing had changed — many times the chance expectation — and each difference exceeds about 995 of 1000 random re-splits of the pooled data, so sampling variation alone is an unlikely explanation for the pattern as a whole. [OCC001, OCC002, DIR001, LAG001]

Limitations: all four items concern the same two activities and likely reflect one underlying difference rather than independent confirmations. The evidence cannot show which activities now separate A15 and A16, and because DIR shares are taken over A16's outgoing transitions, the falling A42 share does not show that the route to A42 is used less often overall (its absolute count stayed roughly similar). Since repetitions per trace changed, this should not be read as a pure shift of frequencies between unchanged paths. [DIR001, LAG001]

Other differences: A16 shows a few marginal successors in the later window (A14, A10, A26, each below about 1% of its transitions) that were not observed before, and several equally marginal ones (about 0.3% each) that disappeared; at this size these are consistent with sampling noise. [DIR001]