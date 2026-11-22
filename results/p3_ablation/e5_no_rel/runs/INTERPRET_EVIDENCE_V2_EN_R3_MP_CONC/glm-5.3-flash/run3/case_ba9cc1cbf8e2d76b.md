### Observed differences

- Three activities — A19, A20 and A25 — do not appear in any of the 200 earlier traces. In the later window they are substantial participants: A19 occurs in about 29 in 100 traces, A20 in about 41 in 100 and A25 in about 30 in 100, essentially never more than once per trace. [OCC001, OCC002, OCC003]
- The established chain around them changes its routing. Earlier, A27 passed almost exclusively to A28 (about 97 in 100 of its outgoing transitions) and A28 almost exclusively to A29 (about 98 in 100). In the later window, A27 sends about 52 in 100 of its outgoing transitions to A19, A20 or A25 while A28 still receives about 43 in 100, and A28 sends about 41 in 100 to one of the new activities while A29 still receives about 57 in 100. [DIR004, DIR005]
- The new activities feed back into the chain: each sends roughly half of its outgoing transitions to A28 and roughly half to A29 (for example A20: about 56 in 100 to A28, about 43 in 100 to A29). [DIR001, DIR002, DIR003]
- Distances between the established activities, measured in event positions, grew: A27→A28 was one event apart in about 98 in 100 cases earlier and is now two apart in about 52 in 100; A28→A29 moved from one apart (about 98 in 100) to two apart in about 41 in 100; A27→A29 shifted from two apart (about 96 in 100) to three apart in about 92 in 100. [LAG001, LAG002, LAG003]
- The new activities sit near the middle of the trace (median relative position about 0.52), between A27, whose median position shifted slightly earlier (about 0.48 to 0.46), and A29, which shifted slightly later (about 0.56 to 0.57). [POS001, POS002, POS003, POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in the later window, A19, A20 and A25 execute as optional single steps inserted into the existing A27 → A28 → A29 sequence — sometimes between A27 and A28, sometimes between A28 and A29 — each appearing in roughly 30 to 40 in 100 traces, whereas none of them was observed in the earlier window. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, DIR005, LAG001, LAG002, LAG003]

Supporting signs:
- The routing change is direct: A27 and A28 now hand over to the new activities in about half and about four in ten of their outgoing transitions respectively, while the original direct edges A27→A28 and A28→A29 persist, so the new steps coexist with the old path rather than replacing it. [DIR004, DIR005]
- The pairwise distances widened by roughly one event exactly where the new activities connect, and the new activities' own successors are A28 and A29 in roughly equal shares, matching the two insertion points. [LAG001, LAG002, LAG003, DIR001, DIR002, DIR003]
- The mid-trace positions of the new activities, between A27 and A29, are consistent with this placement. [POS001, POS002, POS003]
- The volume of qualifying evidence far exceeds what an unchanged process produces: 16 control-flow items qualified where about 0.5 would be expected by chance across the 101 tested units. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, DIR005, POS001, POS002, POS003, POS004, POS005, LAG001, LAG002, LAG003]

Limitations: zero participation in the earlier window means only that A19, A20 and A25 were not observed then; the evidence cannot rule out that they existed as very rare options whose execution rose sharply rather than being newly added. The indicators also overlap heavily — occurrence, routing, position and distance describe largely the same trace behaviour — so their agreement is not independent confirmation. [OCC001, OCC002, OCC003, DIR004, DIR005, LAG001, LAG002, LAG003]