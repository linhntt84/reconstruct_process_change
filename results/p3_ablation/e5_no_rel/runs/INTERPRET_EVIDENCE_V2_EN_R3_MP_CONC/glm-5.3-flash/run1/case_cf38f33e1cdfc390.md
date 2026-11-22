### Observed differences

- Three activities lost participation: A16, A17 and A18 each appeared in about 75 in 100 traces in the earlier window (150 of 200 traces) but in only about 25 in 100 in the later window (49 of 200); in both windows each occurs at most once per trace. [OCC001, OCC002, OCC003]
- Three activities gained participation: A19, A20 and A21 each appeared in about 25 in 100 traces earlier (50 of 200) and in about 75 in 100 later (151 of 200), likewise never repeating within a trace. [OCC004, OCC005, OCC006]
- The routing out of A15 flipped: earlier, its outgoing transitions went mainly to A16 (about 27 in 100), A18 (about 26) and A17 (about 23), rarely to A19, A21 and A20 (about 14, 8 and 4 in 100); in the later window they go mainly to A21 (about 29), A19 (about 25) and A20 (about 22), rarely to A16, A17 and A18 (about 9, 9 and 8 in 100). [DIR001]
- Where A20 follows A15, it now does so sooner: within one or two steps in about 66 in 100 cases, up from about 48 in 100, while a three-step distance fell from about 52 to about 34 in 100. [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the choice between two alternative routes out of A15 flipped: in the earlier window the alternative leading to A16, A17 and A18 was taken in about 75 in 100 cases and the alternative leading to A19, A20 and A21 in about 25 in 100, while in the later window these shares reversed. The redistribution is shown directly in A15's outgoing transitions and matches the participation movements of all six activities; every activity involved is well observed in both windows, none repeats, and A15 still leads to all six, so this is a shift in how often existing paths are taken rather than activities or paths being added, removed or bypassed. Screening qualified 8 control-flow items where fewer than one would be expected without a change, and each item's difference exceeds about 199 of 200 random re-splits, so sampling variation alone cannot account for the set. [DIR001, OCC001, OCC002, OCC003, OCC004, OCC005, OCC006]

What the evidence cannot rule out: there are no relation items, so it remains unknown whether the two groups of three are mutually exclusive branches or can occur together in one trace, and in what order; the constant total of roughly three of the six activities per trace also fits a changed selection among the six activities rather than two fixed branches flipping. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006]

Other differences: in traces containing both A15 and A20, A20 now follows A15 within one or two steps in about 66 in 100 cases instead of about 48; this is consistent with the more frequent direct A15→A20 transition, but as a step-distance measure it could also reflect reordering within the route and does not by itself show that A20 was moved. [LAG001]