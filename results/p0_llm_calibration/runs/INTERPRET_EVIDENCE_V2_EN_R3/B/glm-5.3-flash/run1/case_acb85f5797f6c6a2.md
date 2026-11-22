### Observed differences

- The order between two groups of activities flipped completely. In the earlier window, A30, A31, A36 and A37 each ran before A21 and before A22 in all 200 traces; in the later window, A21 and A22 each ran before all four of them in all 200 traces, while all six activities still occur together in every trace in both windows. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008]
- Successors around this group were rewired. In the earlier window, A20 passed to A30, A31, A36 or A37 in roughly equal shares (about 25 in 100 each), and A21 always passed to A25; in the later window, A20 always passes to A22, and A21 passes to A30, A31, A36 or A37 (about 19–30 in 100 each). [DIR001, DIR002]
- The group's exit changed: in the earlier window, each of A30, A31, A36 and A37 passed to A22 in about a quarter of its outgoing transitions (24–26 in 100), besides passing to the other group members; in the later window, that exit goes to A25 instead (about 22–27 in 100). [DIR003, DIR004, DIR005, DIR006]
- Positions shifted accordingly: A21 moved from about 62% to about 51% through the trace and A22 from about 48% to about 37% (both earlier), while A30, A31, A36 and A37 moved from about 41% to about 58% (later). [POS001, POS002, POS003, POS004, POS005, POS006]
- Step distances match: A22 followed A20 five steps later in the earlier window but immediately in the later window, and A25 followed A21 immediately in the earlier window but five steps later in the later window. [LAG001, LAG002]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that two segments of the process exchanged their order. In the earlier window the sequence ran A20, then the group A30/A31/A36/A37 (in a varying internal order), then A22, then A21, then A25; in the later window it runs A20, A22, A21, then the group, then A25 — the four-activity group now executes after A21 instead of between A20 and A22, with A20 and A25 keeping their places at the ends. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, LAG001, LAG002]

- The order flips are direct relational evidence: all eight activity pairs change from 100% one order to 100% the other while co-occurrence stays at 100%. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008]
- The successor changes agree point by point: A20 now exits to A22, A21 now enters the group, and the group now exits to A25. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006]
- The distance changes (five steps to one, and one to five) are exactly what moving a four-activity group across the A22–A21 pair predicts, and every position shift agrees in direction. [LAG001, LAG002, POS001, POS002, POS003, POS004, POS005, POS006]
- Participation is unchanged — each involved activity occurs in every trace in both windows — so this is a reordering, not activities becoming optional, added or removed. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008]
- The pattern as a whole is far beyond chance: 20 items qualified against about 0.44 expected without a change, each with empirical strength of about 0.995 on 200 traces per window. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, POS001, POS002, POS003, POS004, POS005, POS006, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, LAG001, LAG002]

An important competing explanation the evidence cannot rule out: it cannot tell whether the four-activity group moved later past A22 and A21, or whether A22 and A21 moved earlier past the group — both produce the same observations. Also, only the outgoing transitions of six activities were profiled, so connections outside the observed edges (for example before A20 or after A25) could bound the change slightly differently. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, LAG001, LAG002]

Other differences: small shifts in transition shares within the group — for example, A31 to A30 fell from about 29 to 19 in 100 while A31 to A37 rose from about 19 to 30 in 100 — which are too small to separate from sampling variation. [DIR003, DIR004, DIR005, DIR006]