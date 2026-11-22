### Observed differences

- Three activities that were entirely absent from the earlier window — A19, A20 and A25 — appear in the later window in about 29, 41 and 30 in 100 traces respectively (58, 82 and 61 of 200 traces). Each occurs at most once per trace, two of them practically never share a trace, and one of the three runs in about 99 in 100 later traces. [OCC001, OCC002, OCC003, REL001, REL002, REL006]

- In the earlier window, flow passed directly from A27 to A28 (about 97 in 100 of A27's outgoing transitions) and from A28 to A29 (about 98 in 100). In the later window, only about 43 in 100 of A27's outgoing transitions go to A28, while about 52 in 100 go to one of the new activities (A20 about 22, A25 about 16, A19 about 14); A28 now sends about 41 in 100 of its outgoing transitions to the new activities, with about 57 in 100 still going to A29. [DIR004, DIR005]

- Each new activity leads on to A28 in roughly half of its outgoing transitions and to A29 in most of the rest (A19 about 47 vs 53 in 100; A20 about 56 vs 43; A25 about 54 vs 41). [DIR001, DIR002, DIR003]

- The new activities sit mid-trace (mean position about 0.52) and are placed between A27 and A29: A27 precedes them in essentially every co-occurrence and they precede A29 in essentially every co-occurrence, while their order against A28 is mixed (for example, A19 before A28 in about 15 in 100 traces and after it in about 14). [REL003, REL005, REL007, REL009, REL010, REL012, REL004, REL008, REL011, POS001, POS002, POS003]

- The segment stretches by one event: A28 follows A27 two positions later in about 52 in 100 later cases (earlier immediately in about 97 in 100), A29 follows A27 three positions later in about 92 in 100 (earlier two, about 96 in 100), and A29 follows A28 two positions later in about 41 in 100 (earlier immediately, about 98 in 100). A27's mean position shifts slightly earlier (about 0.48 to 0.46) and A29's slightly later (about 0.55 to 0.57). [LAG001, LAG002, LAG003, POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new step was inserted into the existing A27 → A28 → A29 sequence in the later window. The step executes as one of three mutually exclusive activities — A19, A20 or A25 — and is placed either between A27 and A28 or between A28 and A29: A27 now routes to one of the three in about half of its outgoing transitions (previously almost exclusively to A28), each of the three continues on to A28 or A29, A27 essentially always precedes and A29 essentially always follows it, and A28 and A29 are each pushed one position later in the sequence. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, DIR005, REL003, REL005, REL007, REL009, REL010, REL012, LAG001, LAG002, LAG003]

The screening context supports treating these differences as more than sampling noise: 28 control-flow items qualified against fewer than 1 expected by chance for the 113 tested units, and every item's difference exceeded 199 of 200 random re-splits. The change is shown directly and consistently rather than through one unusual indicator: participation rises from 0 of 200 traces to 58–82 of 200 per activity, new direct successions appear on both sides of the inserted step, the ordering constraints hold in every co-occurrence, and the lag distributions of A28 and A29 shift by exactly one position. [OCC001, OCC002, OCC003, DIR004, DIR005, LAG001, LAG002, LAG003]

An important competing explanation remains: the evidence cannot distinguish one inserted step with three variants from three separate new steps that routing keeps mutually exclusive, and it cannot rule out further changes in units that did not reach the screening thresholds. Positions are event positions, so no claim about clock-time duration is made. [REL001, REL002, REL006]

Other differences: a small share of the new activities' outgoing transitions go to other targets (A20 to A18, and A25 to A27, A32 and A44, each about 1–2 in 100). [DIR002, DIR003]