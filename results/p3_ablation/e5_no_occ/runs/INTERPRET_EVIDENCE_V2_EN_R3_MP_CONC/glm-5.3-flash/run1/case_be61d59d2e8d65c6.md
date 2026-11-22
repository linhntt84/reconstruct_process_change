### Observed differences

- The activities A19, A20 and A25 were each present in roughly 29–40% of cases in the earlier window (about 57–81 of 200 traces) but appear in only about 1 in 200 cases in the later window. [POS001, POS002, POS003]
- In the earlier window these three acted as alternatives on the way from A27 to A29: A19 and A20 hardly ever ran in the same trace (co-occurrence about 0.5%), A27 passed to A19, A20 or A25 in about 44% of its transitions (against about 52% directly to A28), each of the three led on to A28 or A29, and each appeared both before and after A28 in different cases. [REL001, DIR002, DIR003, DIR004, DIR005, REL004, REL011]
- In the later window, A27 leads almost always straight to A28 (about 98% of its outgoing transitions, up from about 52%) and A28 almost always straight to A29 (about 97%, up from about 43%); A19, A20 and A25 are no longer reached from either activity. [DIR005, DIR006]
- The successions tightened accordingly: A28 follows A27 after a single step in about 99% of cases (about 52% before), A29 follows A28 immediately in about 96% (about 43% before), and A29 is reached from A27 in two steps (about 96%) instead of three (about 90% before); these are event-step distances, not clock times. [LAG001, LAG004, LAG002]
- Co-occurrence between each of A19, A20, A25 and the A27/A28/A29 chain collapsed from roughly 29–41% of cases to about 0.5%, with the chain activities now running alone in essentially every trace. [REL003, REL005, REL007, REL009, REL010, REL012]
- Average event positions shifted only slightly (A27 from 0.46 to 0.48 of trace length, A29 from 0.57 to 0.55), consistent with the shorter middle section; such a shift alone would not show a move. [POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the alternative group A19, A20 and A25, which previously ran between A27 and A29 in roughly 29–40% of cases, is no longer executed in the later window: each of the three drops to about 1 in 200 cases, while A27 is followed directly by A28 and A28 directly by A29 in nearly every trace, so the flow reaches A29 without passing through the former alternative activities. [POS001, POS002, POS003, REL001, DIR005, DIR006]

The change is shown directly and consistently: the outgoing transitions of A27 and A28 lost the targets A19, A20 and A25 and became near-deterministic, the immediate successions A27→A28 and A28→A29 emerged, and co-occurrence between the three activities and the chain vanished; each item's difference exceeds about 99.5% of random re-splits, and the 27 qualifying items (all control-flow) far exceed the roughly 0.35 expected by chance for the 70 tested units, so the set of differences as a whole is not what an unchanged process typically produces. [DIR005, DIR006, LAG001, LAG002, LAG004, REL003, REL010, REL012]

Limitations: with only the two window samples, the evidence cannot distinguish whether the group was removed altogether or still executes in a small share of cases (about 1 in 200 traces still contain one of the three), and it cannot rule out that the later window over-represents a case type that never enters this branch, so the branch might persist for other cases rather than being gone. [POS001, POS002, POS003]

Other differences: the routing out of A10 was redistributed — earlier its transitions went mostly to A15 (about 20%), A47 (about 17%), A16 (about 17%) and A45 (about 14%), while in the later window they spread over roughly twenty targets, led by A26 (about 17%) and A45 (about 15%), with A41 (about 9%) newly prominent and A15 and A47 reduced to about 6% each; this is separate from the change involving A19, A20, A25, A27, A28 and A29. [DIR001]