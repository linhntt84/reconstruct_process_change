### Observed differences

- In the earlier window, A10 was executed in about 44 in 100 traces (88 of 200); in the later window, A10 does not appear in a single trace, and it has no observed outgoing transitions, whereas before, about 82 in 100 of those transitions led to A12 [OCC001, POS001, DIR003].
- In the earlier window, A04 sent about 55 in 100 of its outgoing transitions to A10 and only about 10 in 100 to A12; in the later window, none go to A10 and about 73 in 100 go directly to A12 [DIR002].
- In the earlier window, A04 and A10 occurred together in about 44 in 100 traces (A04 first in about 32, A10 first in about 13), and A10 and A12 occurred together in about 44 in 100 traces, always with A10 first; in the later window, neither pair co-occurs at all, and A04 appears without A10, and A12 appears without A10, in about 58 in 100 traces each [REL001, REL002].
- When A04 is followed by A12, the gap shrank: in the earlier window about 56 in 100 such pairs were two steps apart and about 11 in 100 were adjacent; in the later window, about 75 in 100 are adjacent [LAG001].
- A03 and A11, which previously led mostly to A10 and A02, now lead to A04 and A12; this rests on only about 5–10 observed outgoing transitions per window [DIR001, DIR004].

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the intermediate step A10 between A04 and A12 was dropped from execution: traces that previously ran A04 → A10 → A12 now proceed from A04 directly to A12. A10 was executed in about 44 in 100 traces before and in none afterwards; A04's outgoing flow shifted from A10 (about 55 in 100) to A12 (about 73 in 100); both neighbours now occur without A10 in about 58 in 100 traces; and A12 immediately follows A04 in about 75 in 100 observed pairs, against about 11 in 100 before. Nine control-flow items qualified where only about 0.15 would be expected without a change, and every item describes this same difference, so sampling variation cannot account for the pattern as a whole [OCC001, DIR002, DIR003, POS001, REL001, REL002, LAG001].

An important competing explanation remains: zero participation shows only that A10 was not observed in the later sample, so the evidence cannot distinguish the removal of A10 from its replacement by a different, unobserved activity code [OCC001, POS001].

Other differences: A03 and A11 now lead mainly to A04 and A12 instead of A10 and A02; with only about 5–10 observed outgoing transitions per window, this rerouting is weakly supported [DIR001, DIR004].