### Observed differences

- Both windows contain the same two alternative blocks after A15, but their frequencies are flipped. Before, each of A16, A17 and A18 ran in about 75 in 100 traces while each of A19, A20 and A21 ran in about 25 in 100; in the later window, A16–A18 each appear in only about 25 in 100 traces, while A19–A21 each appear in about 76 in 100. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006]
- The two blocks remain strict alternatives in both windows: an activity from A16–A18 and one from A19–A21 never occur in the same trace (co-occurrence 0.0 before and after). Within each block, the three activities still run together whenever the block runs, and their internal order stays mixed (no fixed order) in both windows. [REL009, REL014, REL018, REL007, REL013, REL022, REL025]
- A15's outgoing transitions redistributed accordingly: before, about 23–27% of its observed outgoing transitions went to each of A16, A17 and A18, and only about 4–14% to each of A19, A20 and A21; in the later window, about 22–29% go to each of A19–A21 and only about 8–9% to each of A16–A18. [DIR001]
- A15 still precedes whichever block executes: before, A15 came before A16/A17/A18 in about 75 in 100 traces (never the reverse); in the later window, A15 comes before A19/A20/A21 in about 76 in 100 traces (never the reverse). [REL001, REL002, REL003, REL004, REL005, REL006]
- A25 occurs in every trace in both windows and accompanies whichever block runs: before it co-occurred with A16–A18 in about 75 in 100 traces, in the later window it co-occurs with A19–A21 in about 76 in 100. [REL012, REL024, REL027]
- A minor positional difference: the number of events between A15 and A20 shifted slightly toward shorter gaps (a distance of 3 positions fell from about half to about a third of cases, distances of 1–2 grew). [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the choice between two existing alternative paths after A15 flipped in frequency: the block A16–A17–A18, executed together with A25, was taken in about 75 in 100 traces before and about 25 in 100 in the later window, while the block A19–A20–A21, also with A25, rose from about 25 to about 76 in 100 traces. All activities keep their roles — both blocks remain conditional and mutually exclusive, A15 still precedes the chosen block, A25 remains in every trace, and the unordered internal order within each block is unchanged — so only the shares between the alternatives moved, which is the condition under which a path-frequency shift can be inferred. [OCC001, OCC004, DIR001, REL009, REL022, REL012, REL024]

The screening context supports this reading: 35 control-flow items qualified against roughly 0.5 expected if nothing had changed, far too many to attribute to sampling, and the participation, routing and relational indicators all describe the same flip of matching size (about 50 in 100 traces moved from one branch to the other). [OCC001, DIR001, REL009]

A competing explanation the evidence cannot rule out is that the mix of cases entering the process shifted (for example, case types that favour one branch became more common) rather than the routing decision at A15 itself; the evidence shows where the frequency moved, not what drives the choice. [DIR001, REL004, REL001]

Other differences: only the slight shortening of the positional gap between A15 and A20 [LAG001], which is consistent with the branch shift and introduces no separate behaviour.