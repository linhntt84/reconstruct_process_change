### Observed differences

- In the earlier window, virtually every case ran the fixed spine A26 → A27 → A28: about 98.5 in 100 of A26's outgoing transitions went to A27, about 99.5 in 100 of A27's went to A28, A26 preceded A27 in 99.5 in 100 traces, and A28 followed A26 within 2 steps in about 98 in 100 traces. [DIR001, DIR002, REL001, REL005, LAG001]
- In the later window this spine survives in only about half of the cases: A27 appears in roughly 103 of 200 traces, A26 and A27 co-occur in 51 in 100 traces, and A28 now appears without A27 in 49 in 100 traces. [DIR002, REL001, REL005]
- Three activities not observed at all in the earlier window — A32, A33 and A38 — each appear in about 49 in 100 later traces, around the middle of the trace (mean event position about 0.49 of the trace). [POS001, POS002, POS003]
- These three sit between A26 and A28: A26 precedes each of them in about 49 in 100 traces, each precedes A28 in about 49 in 100 traces, and A26's outgoing transitions are now split roughly evenly between A27 (about 50 in 100) and the three new activities (A33 about 17, A38 about 16, A32 about 15 in 100). [REL002, REL003, REL004, REL009, REL010, REL011, DIR001]
- The three new activities co-occur in about 49 in 100 traces and appear in both orders in similar shares (each direction roughly 22–27 in 100), so they run in no fixed order among themselves; each has outgoing transitions to the other two and to A28. [REL012, REL013, REL014, DIR003, DIR004, DIR005]
- A27 and the new block are mutually exclusive: A27 co-occurs with A32, A33 or A38 in at most about 0.5 in 100 traces. [REL006, REL007, REL008]
- The positional gap from A26 to A28 doubled in about half of the later traces: distance 2 steps in about 50 in 100 (unchanged path) versus 4 steps in about 48 in 100 (three activities in between); before, distance 2 held in about 98 in 100 traces. [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, about half of the cases no longer execute A27 between A26 and A28 and instead insert a newly observed block of three activities — A32, A33 and A38 — between A26 and A28, executed in no fixed internal order, while the other half keep the original A26 → A27 → A28 path. [REL001, REL005, REL006, REL007, REL008, REL002, REL003, REL004, REL009, REL010, REL011, REL012, REL013, REL014, DIR001, DIR002]

The placement is shown directly by relational and successor evidence: A26 precedes each new activity and each new activity precedes A28 in about 49 in 100 traces, A26 now leads to the three in roughly half of its outgoing transitions, and the three lead back to A28; the doubling of the A26–A28 distance from 2 to 4 steps in about 48 in 100 traces matches exactly the insertion of three activities; A27's presence drops from about 99.5 in 100 traces to about half, and it never co-occurs with the new block. The volume of qualifying items (23 control-flow items against roughly 0.35 expected by chance for 71 tested units) is far above what an unchanged process typically produces. [DIR001, DIR002, DIR003, DIR004, DIR005, REL009, REL010, REL011, LAG001, screening]

Limitations: zero participation in the earlier window means A32, A33 and A38 were not observed there, not proven absent, so a rare pre-existing occurrence that missed the 200 earlier traces cannot be fully excluded; and the mixed internal order means no single fixed sequence within the block can be asserted. [POS001, POS002, POS003, REL012, REL013, REL014]

Other differences: a few new edges appear at very low frequency (about 0.5–2 in 100 of the relevant outgoing transitions), such as A26→A23, A32→A06/A25, A38→A02 and A27→A09/A34/A25; they are too rare to characterise further. [DIR001, DIR002, DIR003, DIR005]