### Observed differences

- Activity A03 was not observed at all in the earlier window (0 of 200 traces); in the later window it occurs exactly once in every trace (200 of 200, mean 1.0 occurrence per trace), at about position 2/9 of the trace. [OCC001, POS002]
- In the earlier window, A07 passed control on to A02 (about 33 in 100 of its outgoing transitions), A06 (about 32) and A10 (about 36); in the later window, A07 leads to A03 in essentially every case (100%). [DIR004, REL005]
- In the later window, A03 hands over to A02 (about 39 in 100), A06 (about 33) and A10 (about 29) — closely matching the successor shares A07 had before. [DIR002, DIR004]
- A03 co-occurs with A02, A06 and A10 in all later traces and always precedes each of them; earlier, A03 never co-occurred with any of them (A02 appeared without it in every trace). [REL001, REL004, REL005, REL006]
- The activities downstream of A07 each shifted later by roughly 0.06–0.09 of normalized trace position (for example A10's mean position moved from 0.37 to 0.45), and their distance from A07 grew from lags of 1–3 steps to 2–4 steps; A07's own normalized position fell slightly (0.125 to 0.111), consistent with one event inserted directly after it. [POS001, POS003, POS004, POS005, LAG005, LAG006, LAG007]
- The relative order of A02, A06 and A10 remains mixed in both windows, with only small share shifts (for example A02 before A10 in about 49 in 100 earlier traces versus 55 in 100 later ones). [REL002, REL003, REL007]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new activity, A03, was inserted into the flow immediately after A07. In the earlier window, A07 was followed directly by one of A02, A06 or A10 in roughly equal shares; in the later window, A07 always leads to A03, which then hands over to A02, A06 or A10 with similar shares, and A03 appears exactly once in every trace. [OCC001, DIR002, DIR004, REL005, REL001, REL004, REL006]

The support is direct and consistent: occurrence, direction, relation, position and lag indicators all describe the same single insertion; the participation change is deterministic (0 of 200 versus 200 of 200 traces) rather than a rare variant appearing in one window only; and the downstream position and lag shifts match exactly one added event. [OCC001, DIR004, POS002, POS005, LAG007]

An important competing explanation the evidence cannot rule out is that the two windows sample two different process variants and the window boundary coincides with a complete switch between them, rather than a modification of one flow; the evidence also cannot show why the flow changed. [OCC001, DIR004]

Other differences: small redistributions in the outgoing shares and relative order of A02, A06 and A10 (for example A06 leading to A10 in about 30 versus 37 in 100 of A06's outgoing transitions) are of a size that random re-splits of unchanged behaviour also produce and are not part of the insertion pattern. [DIR003, DIR005, REL002, REL003, REL007, LAG002]