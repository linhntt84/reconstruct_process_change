### Observed differences

- Three activities appear only in the later window: in the earlier window, A19, A20 and A25 were not observed in any of the 200 traces, while in the later window A19 occurs in about 37 in 100 traces (74 of 200), A25 in about 34 (68 of 200) and A20 in about 29 (57 of 200), each at roughly one third of the trace's event positions (mean relative position about 0.36). [DIR001, DIR002, DIR003, POS001, POS002, POS003]
- The three are mutually exclusive alternatives in the later window: A19 and A20 never share a trace, A20 and A25 never do, and A19 and A25 share about 1 in 200 traces; combining their shares, about 99 in 100 later traces contain exactly one of them, whereas earlier traces contained none of the three. [REL001, REL002, REL007]
- A41 no longer leads directly to A26: earlier, A41 (present in all 200 traces) sent about 93 in 100 of its outgoing transitions to A26; in the later window only about 1 in 100 go to A26, while about 34 in 100 go to A19, about 31 to A25 and about 27 to A20. [DIR004, REL006]
- The new activities lead back into the main flow: each sends about 96–98 in 100 of its outgoing transitions to A26, and the distance from A41 to A26 moved from one step (about 93 in 100 cases earlier) to two steps (about 90 in 100 later). [DIR001, DIR002, DIR003, LAG002]
- Ordering is fixed: whenever a new activity co-occurs with A26 or A31 (about 28–37 in 100 traces), it always comes before them, and A41 always comes before the new activity. [REL003, REL004, REL006, REL008, REL009, REL010, REL011, REL012, REL014]
- Minor shifts: A26 and A31 still occur in every trace in both windows; their mean relative positions moved slightly later (A26 about 0.374 to 0.393; A31 about 0.693 to 0.708). [POS004, POS005]
- A separate small difference: the distance from A31 to A35 shifted from mostly one step (about 55 in 100 cases) to mostly two steps (about 62 in 100), and A35's participation slipped from about 54 in 100 earlier traces to about 48 in 100 later ones. [LAG001, REL005, REL013]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, the route from A41 to A26 runs through a new intermediate step: A41, which previously led almost directly to A26, now leads to one of three mutually exclusive activities — A19 (about 37 in 100 traces), A25 (about 34) or A20 (about 29) — each of which leads on to A26, so that A26 is reached two steps after A41 instead of immediately, with about 99 in 100 later traces containing exactly one of the three. [DIR001, DIR002, DIR003, DIR004, LAG002, REL001, REL002, REL003, REL006, REL007, REL008, REL010, REL011, REL014]

Supporting signs: 25 control-flow items qualified where about 0.35 would be expected if nothing had changed, so chance cannot account for the set as a whole; the structural claim rests on direct relational and directional evidence (redirection of A41's outgoing transitions, the A41-to-A26 gap moving from one to two steps, and the new activities' fixed position between A41 and A26), not on position shifts alone; and the three activities were entirely absent from 200 earlier traces, which rules out sampling fluctuation or a rare variant as the explanation. [DIR004, LAG002, REL003, REL006, POS001]

Limitations: the evidence does not show what determines which of the three alternatives is taken in a given trace, and it cannot rule out that the new activities also have predecessors other than A41; the slight later shift of A26's and A31's positions is consistent with the extra step but too small to be informative on its own. [DIR001, DIR002, DIR003, POS004, POS005]

Other differences: the A31-to-A35 distance moved from mostly one step to mostly two steps, and A35's participation decreased modestly (about 54 in 100 earlier traces to about 48 in 100); these differences are small and not accounted for by the main hypothesis. [LAG001, REL005, REL013]