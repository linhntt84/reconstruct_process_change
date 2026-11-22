### Observed differences

- In the earlier window, activities A19, A20 and A25 never occur (0 of 200 traces). In the later window, A19 occurs in about 37 in 100 traces, A25 in about 34, and A20 in about 29. The three almost never share a trace (about 1 in 200 exceptions), so together they cover essentially every later trace, one alternative per trace. [OCC001, OCC002, OCC003, REL001, REL002, REL007]

- Routing out of A41 changed fundamentally. Earlier, about 93 in 100 of A41's observed outgoing transitions went directly to A26; in the later window, about 34 in 100 go to A19, about 31 to A25, about 27 to A20, and only about 1 in 100 still goes directly to A26. [DIR004]

- Each of the three activities leads almost exclusively to A26 (about 96–98 in 100 of their observed outgoing transitions). [DIR001, DIR002, DIR003]

- The distance from A41 to A26 shifted from one step (about 94 in 100 cases earlier) to two steps (about 90 in 100 later, with about 9 in 100 at three steps). [LAG002]

- Whenever one of the three occurs, it co-occurs with A41 and A26 in a fixed order: A41 first, the new activity second, A26 after it (for example, A19 and A26 co-occur with A19 first in 37 in 100 traces, and A41 precedes A19 in the same share). The new activities sit at about 36% of the trace length, just before A26's mean position of about 39%. [REL003, REL004, REL006, REL008, REL009, REL010, REL011, REL012, REL014, POS001, POS002, POS003, POS004]

- A26 and A31 appear in every trace in both windows and moved only slightly later (mean relative position up about 0.02). [POS004, POS005]

- The distance from A31 to A35 grew: A35 followed A31 immediately in about 55 in 100 cases earlier versus about 37 later, while a two-step gap rose from about 42 to about 62 in 100. [LAG001]

### Inference

Support level: Supported hypothesis

In the later window, a step is executed between A41 and A26 that was not executed in the earlier window: after A41, exactly one of three mutually exclusive activities — A19, A20 or A25 — runs, and it is followed by A26, whereas earlier A41 led directly to A26 with no activity in between. The hypothesis is supported directly and consistently: A41's outgoing transitions moved from A26 onto exactly these three activities, each of which leads back to A26; the A41–A26 distance moved from one to two positions; and the co-occurrence, ordering and position evidence consistently places the new activity between A41 and A26 in every trace where it occurs. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, LAG002, REL001, REL003, REL006, REL011]

The screening context supports this reading: 28 control-flow items qualified against roughly 0.57 expected if nothing had changed, so chance sampling cannot account for the pattern as a whole, and the behaviour affects essentially all later traces rather than a rare variant. The main limitation is that zero participation in the earlier window only shows A19, A20 and A25 were not executed then; the evidence cannot distinguish a newly added step from an existing path that simply went untaken in the earlier sample, and the exact split between the three alternatives (about 37/29/34) could differ under repeated sampling. [OCC001, OCC002, OCC003]

Other differences:
- The distance from A31 to A35 grew from mostly one step to mostly two steps, suggesting further work may now sit between A31 and A35, though the evidence does not identify which activity. [LAG001]
- A26 and A31 occur slightly later within traces, consistent with the additional earlier work but not diagnostic on their own. [POS004, POS005]