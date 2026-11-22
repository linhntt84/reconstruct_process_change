### Observed differences

- In the earlier window, A26, A27 and A28 each ran in every trace (200 of 200); in the later window they appear in only about 1 in 100 traces (1–2 of 200). [OCC004, OCC005, OCC006]
- A19, A20 and A21 were not observed before (A21 in a single trace); in the later window each runs in about 31–37 in 100 traces, once per trace where present, at roughly a third of the trace length. [OCC001, OCC002, OCC003, POS001, POS002, POS003]
- The three new activities behave as exclusive alternatives: each pair co-occurs in at most about 1 in 100 later traces, and their shares sum to nearly every trace, so exactly one of them runs in almost each case. Before, A26, A27 and A28 co-occurred in every trace, in varying internal order. [REL013, REL014, REL020, REL031, REL032, REL035]
- A44's successors changed completely: before, about 33 in 100 of its outgoing transitions went to A26, 28 to A27 and 32 to A28; in the later window about 27 go to A19, 30 to A20 and 36 to A21 (about 200 outgoing transitions in each window). [DIR007, REL019, REL025, REL030]
- The new activities lead almost exclusively to A29 (about 97 in 100 of their outgoing transitions); before, the old trio fed A29 in every trace, each of A26/A27/A28 sending roughly 28–37 in 100 of its transitions to one of the other two and a similar share to A29. [DIR001, DIR002, DIR003, DIR004, DIR005, DIR006, REL033, REL036, REL038]
- A11 and A12, which previously ran before A26/A27/A28 in about 45–47 in 100 traces, now precede A19/A20/A21 in about 16–20 in 100 traces each; their own participation rose slightly (about 47 in 100 traces before, about 56 in 100 later). [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the segment between A44 and A29 was restructured: the mandatory trio A26, A27, A28 — executed together in every earlier trace, entered from A44 (and often from A11/A12), with no fixed order among them and always followed by A29 — was replaced by three mutually exclusive alternatives, A19, A20 and A21, of which exactly one now runs in almost every later trace (about 31–37 in 100 each), again after A44 and before A29. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, DIR001, DIR002, DIR003, DIR007, REL013, REL018, REL019, REL024, REL025, REL029, REL030, REL031]

The change is shown directly: participation counts show the three old activities disappearing and the three new ones appearing; the redirection is visible in A44's outgoing profile and the new edges into A29; and the relational profiles agree (A44 and A11/A12 before the chosen activity, which precedes A29). The screening produced 60 qualifying control-flow items where only about 0.7 would be expected without a change, so chance cannot account for the pattern as a whole. [OCC004, DIR007, REL018, REL019, REL024, REL025, REL029, REL030]

A competing explanation the evidence cannot rule out is that the two windows sampled different case populations or pre-existing variants, since the old behaviour is essentially absent later and the new one essentially absent earlier; additionally, the later routing out of A26/A27/A28 rests on only 1–2 observations and cannot be characterised. [OCC004, OCC005, OCC006, DIR004, DIR005, DIR006]

Other differences: A29 now sits slightly earlier in the trace (mean position about 0.43 before, 0.40 later) and A44 slightly later (about 0.31 before, 0.33 later), both still present in every trace; these small shifts are consistent with the replacement above but do not independently confirm it. [POS007, POS008]