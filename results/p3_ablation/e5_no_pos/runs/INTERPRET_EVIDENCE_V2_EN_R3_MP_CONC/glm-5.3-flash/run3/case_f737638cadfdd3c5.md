### Observed differences

- Three activities that were not observed at all in the earlier window (0 of 200 traces) occur regularly in the later window: A19 in about 37 of 100 traces (74 of 200), A25 in about 34 of 100 (68 of 200) and A20 in about 29 of 100 (57 of 200). Each occurs at most once per trace, and their shares sum to almost exactly one occurrence per trace. [OCC001, OCC002, OCC003]
- The three new activities behave as mutually exclusive alternatives: pairs of them practically never occur in the same trace (co-occurrence in at most about 0.5 of 100 traces), whereas in the earlier window neither activity of each pair was ever seen. [REL001, REL002, REL007]
- Each new activity leads almost always directly to A26: about 96 of 100 observed outgoing transitions of A19 go to A26, about 98 of 100 for A20 and about 97 of 100 for A25; in the earlier window these activities had no observed outgoing transitions. [DIR001, DIR002, DIR003]
- A41's routing changed: before, about 93 of 100 of A41's outgoing transitions went directly to A26; in the later window only about 1 of 100 does, while about 34 go to A19, about 31 to A25 and about 27 to A20 — roughly 92 of 100 combined towards the three new activities. [DIR004]
- The distance from A41 to A26 grew accordingly: before, A26 followed A41 within one event position in about 93 of 100 cases; in the later window about 90 of 100 cases show a distance of two positions. [LAG002]
- A26, A31 and A41 still occur in essentially every trace in both windows, and each new activity precedes A26, A31 and (when present) A35 in exactly the share of traces in which it occurs — so practically every occurrence of the new activities sits between A41 and A26. [REL003, REL004, REL006, REL008, REL009, REL010, REL011, REL012, REL005, REL013]
- Separately, the spacing from A31 to A35 shifted from mostly one position (about 55 of 100 cases) to mostly two positions (about 62 of 100), and A35 appears in somewhat fewer traces (about 53 of 100 before versus about 48 of 100 after). [LAG001, REL005, REL013]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that in the later window a new mutually exclusive choice stage sits between A41 and A26: A41, which previously led almost always directly to A26, now leads to exactly one of three previously unobserved activities — A19 (about 37 of 100 traces), A25 (about 34) or A20 (about 29) — and each of these then leads almost always on to A26. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, LAG002]

The support is direct and consistent: 23 evidence items qualified against roughly 0.53 expected if nothing had changed, so the volume alone cannot be explained by an unchanged process; and the occurrence, direction, relation and lag indicators all describe the same picture — zero earlier participation, an exclusive one-of-three co-occurrence pattern, near-exclusive edges to A26, the rerouting of A41, and the one-step-to-two-step distance increase between A41 and A26. [REL001, REL002, REL007, REL003, REL006, DIR004, LAG002]

Limitations: the evidence cannot rule out that A19, A20 and A25 already existed earlier but were never exercised in the 200 sampled traces; what is directly established is their routing role between A41 and A26 in the later window, not that the activities are newly created. The evidence covers control flow only, so the content of the inserted stage cannot be characterised further.

Other differences: the distance from A31 to A35 moved from mostly one position to mostly two, suggesting that in a subset of later traces an additional activity now lies between A31 and A35; the evidence does not identify which activity this would be, since all three new activities lie before A31. The slight decrease in A35's participation (about 53 to about 48 of 100 traces) is small enough to be sampling variation. [LAG001, REL004, REL005, REL013]