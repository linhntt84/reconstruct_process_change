### Observed differences

- Activity A10 was observed in about 44 in 100 traces in the earlier window (88 of 200) but in none of the 200 later traces; its mean occurrences per trace fell from 0.44 to 0. [OCC001, POS001]
- Earlier, A10 sat between A04 and A12: A04 and A10 co-occurred in about 44 in 100 traces, usually with A04 first (about 32 in 100 traces versus about 13 in 100 the other way round), and about 82 of 100 of A10's observed outgoing transitions led to A12. [REL001, REL002, DIR003]
- Later, A10 has disappeared from these relations: A04 appears without A10 in about 58 in 100 traces and A12 without A10 in about 58 in 100, with no co-occurrence of A10 with either, and A10 shows no outgoing transitions at all. [REL001, REL002, DIR003]
- A04's outgoing flow rerouted: transitions from A04 to A10, about 55 of 100 of its observed outgoing transitions earlier, vanished, while transitions from A04 to A12 rose from about 10 of 100 to about 73 of 100. [DIR002]
- A12 now follows A04 almost immediately: the A04-to-A12 distance is one step in about 75 of 100 cases (about 11 of 100 earlier), whereas distances of two or more steps, about 89 of 100 earlier, fell to about 25 of 100. [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A12 is now reached directly from A04, so that A10 is no longer executed between them: in the earlier window A10 occurred in about 44 in 100 traces, was typically reached from A04 and typically followed by A12, with the A04-to-A12 distance typically two steps; in the later window A10 is not observed at all, A04 sends about 73 of 100 of its observed outgoing transitions straight to A12, and A12 follows A04 within one step in about 75 of 100 cases. [OCC001, REL001, REL002, DIR002, DIR003, LAG001]

This hypothesis is shown directly by relational, directional and lag evidence rather than by occurrence counts alone, and it is consistent across indicators: nine control-flow items qualified against roughly 0.15 expected for an unchanged process, each difference exceeds about 199 of 200 random re-splits, and the items behind the main hypothesis rest on roughly 70 to 115 observations per window where the behaviour is present. [OCC001, DIR002, DIR003, LAG001, REL001, REL002]

Limitations: zero participation in the later window shows only that A10 was not observed there, so a very rare continued execution of A10 cannot be ruled out; moreover, most items describe the same underlying rerouting, so they are not independent confirmations of it. [OCC001, DIR002, LAG001]

Other differences: A03 and A11 also redirected their flow — A03 moved from A10 and A02 to A04 and A12 (about 50 of 100 each), and A11 moved from A02 and A10 mainly to A04 (about 78 of 100), leaving A02 without their transitions in the later window — which is consistent with the same rerouting but rests on only 5 to 10 outgoing transitions per window. [DIR001, DIR004]