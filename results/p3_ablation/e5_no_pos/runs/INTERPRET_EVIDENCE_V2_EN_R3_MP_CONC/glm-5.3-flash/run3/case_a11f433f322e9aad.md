### Observed differences

- In the earlier window, A27 ran in every case (200 of 200 traces, once per case) and A32, A33 and A38 never appeared; in the later window, A27 runs in about 51 in 100 cases and each of A32, A33 and A38 runs in about 49 in 100 cases, once per case. [OCC001, OCC002, OCC003, OCC004]
- Routing after A26 changed: earlier, about 99 in 100 of A26's outgoing transitions went to A27; in the later window, about 50 in 100 go to A27, with the rest split almost evenly among A33 (about 17 in 100), A38 (about 16 in 100) and A32 (about 15 in 100). [DIR001]
- A27 and the three new activities are now strict alternatives: in the later window, A27 co-occurs with A32, A33 or A38 in at most about 1 in 200 cases, while A26 appears with A27 in about half of the cases and with each of A32, A33 and A38 in about half, essentially always before them. [REL001, REL002, REL003, REL004, REL006, REL007, REL008]
- In the later window, the three new activities typically run together: each pair of them co-occurs in about 49 in 100 cases and appears in both orders in similar shares (for example, A32 before A33 in about 23 in 100 and A33 before A32 in about 27 in 100), so there is no fixed order among them. [REL012, REL013, REL014]
- A28 still occurs in essentially every case in both windows, but in the later window each of A32, A33 and A38 precedes A28 in about 49 in 100 cases, whereas earlier A28 was always reached via A27. [REL005, REL009, REL010, REL011]
- A28's distance from A26 shifted: earlier it followed two steps after A26 in about 98 in 100 cases; in the later window it is two steps after in about half of the cases and four steps after in about 48 in 100, consistent with three activities now sitting between them. [LAG001]
- When A27 does run in the later window, it still leads almost always to A28 (about 96 in 100 of its outgoing transitions). [DIR002]

### Inference

Support level: Supported hypothesis

The control-flow screening flagged 24 items where about 0.54 would be expected if nothing had changed, so the volume of flagged behaviour is far beyond what an unchanged process typically produces. [OCC001, OCC002, OCC003, OCC004, DIR001, DIR002, DIR003, DIR004, DIR005, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012, REL013, REL014, LAG001]

The evidence supports the possibility that in the later window about half of the cases skip A27 between A26 and A28 and instead run A32, A33 and A38 — all three, in no fixed order among themselves — between A26 and A28, while the remaining cases still follow the earlier A26 → A27 → A28 sequence; A26 and A28 themselves still open and close essentially every case. The signs are direct and mutually consistent: participation flipped from A27 to the trio [OCC001, OCC002, OCC003, OCC004]; A26 now routes to either A27 or one of the new activities [DIR001]; the trio is mutually exclusive with A27, co-occurs internally in both orders, and precedes A28 [REL001, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012, REL013, REL014]; and A28's positional lag from A26 moved from two steps to two or four steps in equal shares [LAG001].

The evidence cannot distinguish whether A32, A33 and A38 run sequentially in varying orders or largely in parallel, since each pair appears in both orders with similar shares; nor can it rule out that the later window blends two case populations (old and new behaviour) rather than one behaviour shared by all cases. [REL012, REL013, REL014]

Other differences: a few rare new transitions appear in the later window — from A27 to A09, A34 and A25, and from the new activities to A06, A25 and A02 — each at about 1–2 in 100 of the source's observed outgoing transitions, too rare to characterise further. [DIR002, DIR003, DIR004, DIR005]