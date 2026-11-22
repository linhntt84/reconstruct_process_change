### Observed differences

- In the later window, A19 and A20 are almost never executed: A19 appears in about 0.5 in 100 traces (1 of 200) versus about 45 in 100 before, and A20 in about 0.5 in 100 (1 of 200) versus about 55 in 100 before. [OCC001, OCC002]
- Before, each trace contained either A19 or A20 — never both — so they acted as mutually exclusive alternatives; in the later window, about 99 in 100 traces contain neither of them. [REL001]
- Routing into these activities collapsed: before, about 23 in 100 of A26's outgoing transitions went to A19 and about 27 in 100 to A20 (about 45 in 100 to A27); in the later window, about 97 in 100 go to A27. [DIR003]
- Routing out of them collapsed as well: before, A27's outgoing transitions went to A28 (about 51 in 100), A20 (about 27 in 100) and A19 (about 21 in 100); in the later window, about 97 in 100 go to A28. [DIR004]
- A19 and A20 no longer co-occur with A26, A27 or A28: pairs that co-occurred in roughly 45–55 in 100 traces before now appear together in about 0.5 in 100, with A26, A27 and A28 appearing without them in about 99.5 in 100 traces. [REL002, REL003, REL004, REL005, REL006, REL007]
- Distances between the remaining activities shortened by about one event position: A26 to A27 is now 1 step apart in about 99 in 100 cases (mostly 2 before), A26 to A28 is 2 steps apart in about 96 in 100 (3 before in about 93 in 100), and A27 to A28 is 1 step apart in about 98 in 100 (previously split between 1 and 2). [LAG005, LAG006, LAG007]
- The after-window profiles of A19's and A20's own outgoing transitions and positions rest on a single trace each, so details such as A19 routing only to A32 carry little weight. [DIR001, DIR002, POS001, POS002, LAG001, LAG002, LAG003, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the alternative steps A19 and A20 — previously executed in roughly half of the cases around the A26–A27–A28 sequence — are now skipped in almost all executions, leaving A26 followed directly by A27 and A27 directly by A28 as the near-exclusive route. [OCC001, OCC002, DIR003, DIR004, REL001]

The signs are direct and consistent: the participation collapse is backed by 91 and 109 traces before versus 1 after; the successor profiles of A26 and A27, each backed by about 200 outgoing transitions per window, concentrate almost exclusively on A27 and A28; and the relation and lag items, each backed by all 200 traces in both windows, show co-occurrence with A19 and A20 vanishing while inter-event distances shorten by about one step, consistent with an intermediate activity no longer being executed. Eighteen qualifying items against roughly 0.5 expected if nothing had changed also makes chance as a whole implausible. [DIR003, DIR004, REL002, REL003, REL004, REL005, REL006, REL007, LAG005, LAG006, LAG007]

Limitations remain: the later window still shows A19 and A20 once in 200 traces each, so a branch removed entirely cannot be distinguished from one now taken with very low probability, and a shift in case mix toward traces that never enter this branch is behaviourally indistinguishable from a structural edit. Many items also describe the same underlying trace behaviour, so they are not independent confirmations. Sampling differences in variant frequencies can make a variant dominate one window, but a drop from about half of all traces to 1 in 200, at these support sizes, is difficult to attribute to sampling alone. [OCC001, OCC002, REL001, DIR001, DIR002]