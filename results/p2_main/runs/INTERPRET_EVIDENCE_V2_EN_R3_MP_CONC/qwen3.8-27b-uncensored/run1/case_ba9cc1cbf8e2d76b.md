

### Observed differences

- In the earlier window, A19, A20, and A25 are not observed, while in the later window A19 appears in about 29 in 100 traces, A20 in about 41 in 100, and A25 in about 30 in 100. [OCC001, OCC002, OCC003]
- The three activities are almost never observed together in the later window, with co-occurrence at most about 1 in 200, and their individual participations sum to about 100 in 100, so nearly all later traces contain one of them. [OCC001, OCC002, OCC003, REL001, REL002, REL006]
- In the later window, A19, A20, and A25 occur around the middle of traces, with medians about 0.52, q25 about 0.48, and q75 about 0.54 to 0.56. [POS001, POS002, POS003]
- A27 precedes the new activities in almost all co-occurring later traces: A27 is before A19 in all about 29 in 100 co-occurring traces, before A20 in about 40 in 100, and before A25 in about 29 in 100. [REL003, REL007, REL010]
- The new activities precede A29 in almost all co-occurring later traces: A19 is before A29 in about 29 in 100, A20 is before A29 in about 40 in 100, and A25 is before A29 in about 30 in 100. [REL005, REL009, REL012]
- Their order with A28 is mixed in the later window, with both orders in similar proportions, for example A20 before A28 in about 23 in 100 traces and A28 before A20 in about 18 in 100 traces. [REL004, REL008, REL011]
- Among outgoing transitions from A27, A28 was about 97 in 100 in the earlier window but about 43 in 100 in the later window, while A20, A25, and A19 appear in about 22, 16, and 14 in 100 of later outgoing transitions. [DIR004]
- Among outgoing transitions from A28, A29 was about 98 in 100 in the earlier window but about 57 in 100 in the later window, while A20, A19, and A25 appear in about 16, 13, and 12 in 100 of later outgoing transitions. [DIR005]
- The new activities mainly lead to A28 or A29 in the later window, with A28 receiving about 53 to 56 in 100 of their outgoing transitions and A29 about 41 to 47 in 100. [DIR001, DIR002, DIR003]
- The lag from A27 to A28 was immediate in about 98 in 100 earlier observations but is immediate in about 43 in 100 and two steps in about 53 in 100 later. [LAG001]
- The lag from A27 to A29 was two steps in about 96 in 100 earlier observations but is three steps in about 92 in 100 later. [LAG002]
- The lag from A28 to A29 was immediate in about 98 in 100 earlier observations but is immediate in about 57 in 100 and two steps in about 41 in 100 later. [LAG003]
- A27 and A29 remain in all traces in both windows, with A27's median event position moving slightly earlier from about 0.48 to about 0.46 and A29's median event position moving slightly later from about 0.56 to about 0.57. [POS004, POS005]

### Inference

Support level: Supported hypothesis

- The evidence supports the possibility that, in the later window, a new alternative step is executed in almost all traces: one of A19, A20, or A25 occurs after A27 and before A29, in a region around A28 where its order with A28 is not fixed. [OCC001, OCC002, OCC003, REL003, REL005, REL004, REL007, REL008, REL010, REL011, REL012]
- The pattern is not a single unusual item: 28 control-flow items qualify, while about 1 in 2 would be expected without change. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, DIR005, POS001, POS002, POS003, POS004, POS005, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012, LAG001, LAG002, LAG003]
- The supporting signs are the absence of these activities in the earlier window, their appearance in about 29, 41, and 30 in 100 later traces, their near mutual exclusivity, the increased lags between A27, A28, and A29, and the slight outward shift of A27 and A29 positions. [OCC001, OCC002, OCC003, REL001, REL002, REL006, LAG001, LAG002, LAG003, POS004, POS005]
- The outgoing-transition changes are consistent with insertion rather than replacement, because A27 and A28 now lead to the new activities while the new activities mainly lead to A28 or A29, and A27 and A29 remain in all traces. [DIR001, DIR002, DIR003, DIR004, DIR005, POS004, POS005]
- A limitation is that the evidence is control-flow only and cannot distinguish whether A19, A20, and A25 are three separate new activities or alternative variants of one new step, nor can it fix their exact order relative to A28. [REL004, REL008, REL011, POS001, POS002, POS003]
- An important competing explanation that remains possible is that the later window contains a newly sampled variant of the process, although the consistent participation, relational, and lag changes make a simple sampling fluctuation less likely. [OCC001, OCC002, OCC003, REL003, REL005, LAG001, LAG002, LAG003]