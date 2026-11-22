### Observed differences

- Earlier, A27 ran in every case (200 of 200 traces, once per case); in the later window it runs in about 51 of 100 cases. [OCC001]
- A32, A33 and A38 were not observed at all earlier (0 of 200 traces); in the later window each runs in about 49 of 100 cases, once per case, and they always come as a group: in roughly 49 of 100 cases all three run together, and in about 51 of 100 none of them appears. [OCC002, OCC003, OCC004, REL012, REL013, REL014]
- Routing out of A26 changed sharply: earlier about 99 in 100 of A26's outgoing transitions went to A27; in the later window about 51 in 100 go to A27, with the rest split almost evenly among A33 (about 17 in 100), A38 (about 16) and A32 (about 15). [DIR001]
- The new activities sit between A26 and A28: A26 precedes each of them in about 49 of 100 cases, and each of them precedes A28 in about 49 of 100 cases. Their mutual order varies, with both orders in similar proportions for every pair, and each of the three can be the last activity before A28 (A32 leads to A28 in about 28 in 100 of its outgoing transitions, A33 about 27, A38 about 43). [REL002, REL003, REL004, REL009, REL010, REL011, REL012, REL013, REL014, DIR003, DIR004, DIR005]
- A27 and the new activities are alternatives: A27 co-occurs with A32, A33 or A38 in at most about 1 of 100 cases, and A28 now runs without A27 in about 49 of 100 cases. [REL005, REL006, REL007, REL008]
- The distance from A26 to A28 was almost always 2 positions earlier (A26 → A27 → A28); in the later window it is about 50 of 100 cases at distance 2 and about 48 of 100 at distance 4 (three activities in between), with the new activities sitting around the middle of the trace (median position about 0.5). [LAG001, POS001, POS002, POS003]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the segment between A26 and A28 was restructured: earlier, every case ran A26 → A27 → A28; in the later window about half the cases still do, while in the other half A27 does not run and three previously unobserved activities — A32, A33 and A38 — run instead as a block between A26 and A28, in varying order, with A28 still following. A26 and A28 themselves behave as before, each still appearing in every case. [OCC001, OCC002, OCC003, OCC004, DIR001, REL001, REL005, LAG001]

The placement is shown directly by relational evidence — A26 precedes each new activity and each new activity precedes A28 in about 49 of 100 cases — and A27 is mutually exclusive with all three, which rules out a move or swap of A27 and points to an inserted alternative path. The screening flagged 27 control-flow items against roughly 0.57 expected in an unchanged process, so the pattern as a whole is far beyond what random re-splits of stable traces produce. [REL002, REL003, REL004, REL009, REL010, REL011, REL006, REL007, REL008, DIR001]

The evidence cannot show what decides which path a case takes: a fixed roughly 50/50 branch at A26 and routing driven by case attributes would look identical here, and no case attributes are available; the sample also cannot establish that all six internal orders of the A32/A33/A38 block occur equally often. [DIR001, REL012, REL013, REL014]

Other differences: in the later window A27's outgoing transitions include small new shares to A09, A34 and A25 (about 1–2 in 100 of its outgoing transitions, in place of A04); these rest on only a handful of cases and may be sampling noise. [DIR002]