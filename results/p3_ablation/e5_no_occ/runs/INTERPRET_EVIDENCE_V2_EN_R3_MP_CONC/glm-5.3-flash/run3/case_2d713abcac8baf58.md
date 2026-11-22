### Observed differences

- In the earlier window, A19, A20 and A21 each ran in roughly 30–36 in 100 traces (70, 60 and 72 of 200) and behaved as alternatives: each pair co-occurred in at most about 1 in 100 traces, so nearly every trace contained exactly one of the three. In the later window all three nearly disappear — A19 in 2 of 200 traces, A20 and A21 in 1 of 200 each — and no pair of them co-occurs. [POS001, POS002, POS003, REL001, REL002, REL008]
- A26, A27 and A28 show the mirror image: none appeared in the earlier window, while in the later window each appears in all 200 traces, around position 0.37–0.38 of the trace. [POS004, POS005, POS006]
- A44, present in essentially every trace in both windows, changed its routing: earlier, about 85 in 100 of its outgoing transitions went to A19 (about 30 in 100), A21 (about 30) or A20 (about 25); later, about 85 in 100 go to A26 (about 31), A27 (about 27) or A28 (about 26). [DIR007]
- In the later window the three new activities run together in every trace with no fixed order between them (for example A26 precedes A27 in about 51 in 100 traces and follows it in about 49), and each of them precedes A29 in about 98–99 in 100 traces. Earlier, A29 always ran without them. [REL019, REL020, REL023, REL021, REL024, REL026]
- Earlier, the single chosen activity led on to A29 (about 95–99 in 100 of its outgoing transitions), and A19, A20 or A21 preceded A29 in about 35, 30 and 35 in 100 traces respectively; later, about 99 in 100 traces contain A29 with none of the three before it. [DIR001, DIR002, DIR003, REL006, REL012, REL017]
- The distance from A44 to A29 grew from mostly 2 steps (about 84 in 100 cases) to mostly 4 steps (about 82 in 100), and A29's mean position moved slightly later (about 0.40 to 0.44 of the trace). [LAG001, POS007]

### Inference

Support level: Supported hypothesis

The segment between A44 and A29 was restructured from a one-of-three choice into a fixed group. In the earlier window, A44 was followed by exactly one of the alternatives A19, A20 or A21, which then led to A29. In the later window, A19, A20 and A21 are no longer observed, and A44 is instead followed by A26, A27 and A28, which all execute in every trace in no fixed order among themselves and each precede A29, lengthening the A44-to-A29 path from about 2 to about 4 steps. [DIR007, REL019, REL021, REL022, LAG001]

The support is direct and consistent: relational evidence places A44 before each of A26/A27/A28 (about 99 in 100) and each of them before A29 (about 98–99 in 100); participation swings from 60–72 in 200 traces to 1–2 in 200 for the old activities and from 0 to 200 in 200 for the new ones; and 42 control-flow items qualified in screening against fewer than 1 expected without change, with every item larger than about 995 of 1000 random re-splits. Since the old activities are (nearly) absent later and the new ones absent earlier, this is a replacement of one path segment by another, not a shift in how often existing paths are taken. [REL022, REL025, REL027, POS001, POS004, DIR007]

Other differences: the rare later traces that still contain A19, A20 or A21 show different successors (A10/A09 after A19, A45 after A20, A34 after A21), but these profiles rest on only 1–2 traces each. [DIR001, DIR002, DIR003]

Limitations: the evidence cannot show whether A19, A20 and A21 still execute in a very small share of cases or have disappeared entirely, since zero participation only means non-observation, and whether the new trio always runs exactly once per trace is only mostly established (about 1–2 in 100 traces show repetition). Most items also describe the same underlying trace behaviour, so their agreement is not independent confirmation. [POS001, DIR004, REL019]