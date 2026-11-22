### Observed differences

- In the later window, activity A04 appears in about 24% of traces instead of about 73%, and its mean occurrences per trace drop from 0.79 to 0.27. [OCC002, POS001]
- Activity A02 appears in about 26% of traces instead of about 7%; A06 and A10 also increase (from about 8% to 17% and from about 5% to 16% respectively). [OCC001, OCC003, OCC004]
- The successor of A14 shifts from A04 (about 69% of outgoing transitions) to A15 (about 80%). [DIR003]
- The successors of A19, A20, A25 and A26 shift from A27 (about 93–97%) to A29 and A33 (together about 85–95%). [DIR005, DIR006, DIR007, DIR008]
- The successor of A28 shifts from A29 (98.5%) to a mix of A25, A26, A19 and A20 (about 48%). [DIR009]
- The successor of A29 shifts from A33 (96.5%) to a mix of A26, A20, A19 and A25 (about 50%). [DIR010]
- The successor of A46 shifts from A19/A25/A20/A26 to A27 (82%). [DIR011]
- A19, A20, A25 and A26 used to occur before A27/A28 (A_before_B about 0.20–0.29) and now occur after them (B_before_A about 0.21–0.27). [REL016, REL017, REL018, REL019, REL020, REL021, REL022, REL023]
- A04's cooccurrence with A14, A15, A27, A28, A29, A33 and A46 drops from about 73% to about 24%, and A04-before-them drops from about 0.63–0.65 to about 0.12–0.15. [REL003, REL004, REL009, REL010, REL011, REL012, REL013]
- The mean position of A19, A20, A25 and A26 shifts later, from about 0.32–0.35 to about 0.58–0.61 of the trace; A04 also shifts later (mean from 0.20 to 0.35). [POS003, POS004, POS005, POS006, POS001]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in which activity A04 is executed much less often, and a block of activities (A19, A20, A25, A26) that previously occurred before A27/A28 now occurs after them. The successor of A14 also changes from A04 to A15. These signs are consistent across participation, routing, order and position indicators. The main limitation is that the two windows are finite samples, so some rare variants could differ by chance, but the number and consistency of the items make a chance explanation unlikely. [OCC002, DIR003, DIR005, DIR006, DIR007, DIR008, REL016, REL017, REL018, REL019, REL020, REL021, REL022, REL023, POS003, POS004, POS005, POS006]