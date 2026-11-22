### Observed differences

- In the earlier window, A01, A03, A05 and A06 never appear (0 of 200 traces each), while A04 and A07 appear in every trace; A04 is followed directly by A07, which is the final event of the trace (mean relative position 1.0, one step after A04, itself at about 0.5). [OCC001, OCC002, OCC003, OCC004, DIR002, LAG001, POS003, POS006]
- In the later window, A01, A03, A05 and A06 each occur exactly once in every trace (200 of 200, no repetitions), and A04's outgoing flow now goes entirely to A03 instead of A07. [OCC001, OCC002, OCC003, OCC004, DIR002]
- The later window shows a fixed chain of new consecutive edges — A03→A05, A05→A06, A06→A07 and A07→A01 — each the only observed outgoing transition of its source; A07, which ended traces before, now continues to A01. [DIR001, DIR003, DIR004, DIR005]
- Pairwise ordering in the later window matches one strict sequence: A04 precedes A03, A05 and A06; A03 precedes A05, A06 and A07; A05 precedes A06, A07 and A01; A06 precedes A07; and A07 precedes A01, each in all 200 traces. Before, these pairs were either never co-observed or only one of the two activities appeared. [REL001, REL002, REL004, REL005, REL006, REL007, REL008, REL010, REL011, REL012, REL013, REL014]
- The distance from A04 to A07 grows from one step to four steps, and relative positions shift accordingly: A04 moves earlier (about 0.17 from 0.5), A07 is no longer last (about 0.83 from 1.0), and A01 is now the final event (1.0). [LAG001, POS001, POS003, POS006]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that three previously unobserved activities — A03, A05 and A06 — now run as a fixed sequential block between A04 and A07, and that a further new activity, A01, runs after A07 at the end of every case. In the earlier window, traces went directly from A04 to A07, which ended the case; in the later window, every trace runs the chain A04 → A03 → A05 → A06 → A07 → A01, with each new activity executed exactly once. [OCC001, OCC002, OCC003, OCC004, DIR001, DIR002, DIR003, DIR004, DIR005, LAG001, REL006, REL007, REL012, REL014, REL005]

The screening produced 30 qualifying items against an expectation of about 0.15 without change (all control-flow), a volume chance cannot explain; every item's difference exceeds about 99.5% of random re-splits, and the items converge on one coherent structure — the successor change at A04, the lag growth from one to four steps, and the shift from 0 to 200 of 200 traces for each new activity show the new sequence directly rather than indirectly. [DIR002, LAG001, OCC001, OCC002, OCC003, OCC004]

Limitations: the evidence contains only control-flow items, so nothing can be said about timing or resource allocation; zero participation in the earlier window strictly means only that A01, A03, A05 and A06 were not observed there; and the comparison cannot rule out that the two windows draw from different process variants or populations rather than one modified process, even though the behavioural difference itself is consistent across all items. [OCC001, OCC002, OCC003, OCC004]