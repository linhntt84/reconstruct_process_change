### Observed differences

- In the earlier window, ten activities — A33, A34, A35, A37, A38, A39, A40, A41, A42 and A43 — each ran exactly once in every trace (participation 100 in 100, about 1.0 occurrences per trace, virtually no repetition). In the later window, each of them appears in only about 46–56 in 100 traces, still once when present and essentially never repeated. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, OCC007, OCC008, OCC009, OCC010]

- The ten activities now behave as two five-activity groups that exclude each other. Within the first group (A33, A34, A35, A37, A38), any two co-occur in about 46 in 100 later traces and are jointly absent in about 52–54 in 100; within the second group (A39–A43), they co-occur in about 55 in 100 and are jointly absent in about 44–46 in 100. Earlier, every such pair co-occurred in 100 in 100 traces. [REL021, REL030, REL038, REL045, REL056, REL057, REL065]

- Pairs across the two groups changed from always executed together to almost never: for example, A33 co-occurred with each of A39–A43 in 100 in 100 earlier traces (first-group activity first in about 97–100 in 100), but in only about 1–3 in 100 later traces, with A33 alone in about 45 in 100 and the second-group activity alone in about 53 in 100. The same collapse holds for A34, A35, A37 and A38 against A39–A43. [REL025, REL026, REL033, REL040, REL046, REL051]

- The frame around the block is unchanged: A30 and A31 still occur in every trace, A30 still precedes each block activity and each block activity still precedes A31 whenever they run together (reverse order in at most about 1 in 100 traces). What changed is that A30 and A31 now co-occur with each block activity in only about 46–56 in 100 traces instead of all of them. [REL001, REL006, REL011, REL016, REL020]

- Successor profiles agree: A30's outgoing transitions, previously concentrated on A33–A38 (about 17–23% each), now spread over both groups (about 7–13% each); A33, A34 and A38 now lead directly to A31 in about 21–25% of their observed outgoing transitions, which was not observed earlier. [DIR001, DIR002, DIR003, DIR004]

- Relative event positions shifted consistently with a shorter block: A30's mean position moved from about 0.55 to about 0.64 of the trace, the first-group activities from about 0.62 to about 0.72, and the second-group activities slightly earlier, from about 0.75–0.76 to about 0.71–0.72; these are event-order positions, not clock times. [POS001, POS002, POS003, POS004, POS005, POS006, POS007, POS008, POS009, POS010]

- Closeness within five steps changed accordingly: pairs spanning both groups (for example A34–A40, A37–A43) were within five steps in roughly 109–125 earlier traces but only 1–3 later traces, while A30/A31-to-group pairs that were previously farther apart are now within five steps in about 88–106 traces; several of these profiles rest on only 1–3 observations in one window, so they are weak corroboration. [LAG001, LAG002, LAG004, LAG006, LAG013, LAG018]

### Inference

Support level: Supported hypothesis

In the later window, the fixed ten-activity block between A30 and A31 behaves as an exclusive choice between two five-activity paths: about 45 in 100 traces execute only A33, A34, A35, A37 and A38, about 53 in 100 execute only A39, A40, A41, A42 and A43, and only about 2 in 100 still contain both groups, whereas earlier every trace executed the first group followed by the second between A30 and A31. A30 still opens and A31 still closes whichever path runs, and within each group the activities keep their earlier mixed, unfixed order. [REL001, REL011, REL021, REL025, REL040, REL056, OCC001, OCC006]

The hypothesis rests on direct relational evidence: cross-group pairs fell from universal co-occurrence to about 1–3 in 100, while within-group pairs are now jointly present or jointly absent; participation of all ten activities halved in step with no new repetition; the order relations to A30 and A31 are intact; and successor profiles show A30 feeding both groups while A33, A34 and A38 hand over directly to A31. With 112 qualifying control-flow items against about 1.28 expected for an unchanged process, the pattern as a whole is far beyond what random re-splits produce. [REL021, REL025, REL056, OCC001, OCC010, DIR001, DIR002, screening]

What the evidence cannot show is what decides which of the two paths runs in a given case, or whether the roughly 2 in 100 traces containing both groups are a retained rare path rather than sampling noise; the LAG corroboration is weak because several of its profiles rest on 1–3 observations, and the position shifts reflect event order rather than elapsed time. [REL025, LAG006, LAG008, POS001]