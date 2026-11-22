### Observed differences

- In the earlier window, A19, A20 and A25 were never observed (0 of 200 traces). In the later window each participates in roughly a third of traces — A19 in about 37% (74 of 200), A25 in about 34% (68), A20 in about 29% (57) — each occurring at most once per trace. [OCC001, OCC002, OCC003]
- The three are mutually exclusive alternatives: pairs of them co-occur in at most about 0.5% of later traces, and their participations sum to almost exactly 100%, so the later window shows virtually every trace running exactly one of A19/A20/A25, whereas earlier traces contained none of them. [REL001, REL002, REL007]
- A41's successors changed: before, about 93% of its observed outgoing transitions led to A26; in the later window they lead to A19 (~34%), A25 (~31%) and A20 (~27%), with A26 at about 1%. [DIR004]
- The new activities in turn lead to A26: about 96–98% of the observed outgoing transitions of A19, A20 and A25 go to A26. [DIR001, DIR002, DIR003]
- Ordering places the new activities between A41 and A26/A31: A41 precedes each of them in essentially every trace where they occur (co-occurrence 28–37%, ≤1% interleaved), and each of them precedes both A26 and A31 (co-occurrence 28.5–37%, always in that order). [REL006, REL010, REL014, REL003, REL004, REL008, REL009, REL011, REL012]
- The step distance from A41 to A26 grew from one step (94% of cases) to two steps (90%), consistent with one activity now sitting between them. [LAG002]
- The new activities occur at a consistent early relative position (mean about 0.36 of the trace), just before A26; A26's mean position moved only slightly later (about 0.37 to 0.39) and A31's likewise (about 0.69 to 0.71), while both still occur in every trace in both windows. [POS001, POS002, POS003, POS004, POS005]
- Other: the gap between A31 and A35 shifted from mostly one step (55% of cases) to mostly two steps (62%); A19 and A25 now precede A35 in the ~15–20% of traces where they co-occur, which was not observed before. [LAG001, REL005, REL013]

Every qualified item's difference exceeds about 99.5% of random re-splits, and 28 items qualified in total. [OCC001, DIR004, LAG002, REL003]

### Inference

Support level: Supported hypothesis

In the later window, an exclusive three-way branch — one of the previously unobserved activities A19, A20 or A25 — is inserted between A41 and A26. Previously A41 led directly to A26 (about 93% of its outgoing transitions, one step apart in 94% of traces); in the later window A41 leads to exactly one of A19/A20/A25 (together about 92% of its outgoing transitions, split roughly 34%/31%/27%), which then leads on to A26, with A26 and A31 continuing to occur in every trace. [OCC001, OCC002, OCC003, DIR004, DIR001, DIR002, DIR003, LAG002, REL006, REL003, POS004]

The hypothesis is shown directly and consistently by a multi-indicator chain: appearance from zero participation, rewiring of A41's successors toward the three new activities, their successors pointing back to A26, fixed order A41 → new activity → A26/A31, and the A41-to-A26 step distance growing from one to two. The screening comparison supports this at the set level: 28 control-flow items qualified against about 0.57 expected without change, roughly fifty times the chance expectation, so sampling alone cannot explain the ensemble. Limitations: zero participation in the earlier window strictly means only "not observed", so a pre-existing extremely rare variant cannot be fully ruled out, though ~30% participation later across 200 traces makes that reading implausible; several items describe the same underlying insertion and are not independent confirmations; and the branch shares (~28–37% each) carry sampling error. [REL001, REL002, REL007, LAG002, OCC001]

Other differences: the A31-to-A35 spacing shifted toward two-step gaps (42% to 62% of cases), and A19/A25 now precede A35 in the ~15–20% of traces where they co-occur; these are not part of the main hypothesis. [LAG001, REL005, REL013]