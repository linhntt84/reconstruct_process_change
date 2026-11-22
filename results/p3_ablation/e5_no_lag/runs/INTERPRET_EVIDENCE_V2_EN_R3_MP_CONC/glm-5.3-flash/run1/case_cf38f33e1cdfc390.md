### Observed differences

- The three activities A16, A17 and A18 each ran in about 75 in 100 traces in the earlier window, but in only about 25 in 100 traces in the later window; their mean occurrences per trace fell from 0.75 to about 0.25, with no repetitions in either window. [OCC001, OCC002, OCC003]
- The three activities A19, A20 and A21 each moved the opposite way, from about 25 in 100 traces earlier to about 75 in 100 in the later window. [OCC004, OCC005, OCC006]
- A15, present in every trace in both windows, redistributed its outgoing flow: earlier roughly three quarters of its outgoing transitions led to A16, A17 or A18 (about 23–27% each) and one quarter to A19, A20 or A21; in the later window roughly three quarters led to A19, A20 or A21 (about 22–29% each) and one quarter to A16, A17 or A18. [DIR001]
- The two groups stayed mutually exclusive: a pair made of one activity from {A16, A17, A18} and one from {A19, A20, A21} never occurred in the same trace in either window; only which side of each exclusive pair was filled flipped, from about 75/25 earlier to about 25/75 later. [REL009, REL014, REL018]
- The branch structure itself was stable across both windows: within the active branch the three activities co-occurred without a fixed order (both orders in similar proportions), A15 preceded the active branch's activities in about 75 in 100 traces, and A25 ran in all traced cases throughout, co-occurring with whichever branch was active. [REL007, REL022, REL001, REL004, REL012, REL024]
- Scale of the signal: 34 control-flow items qualified in screening against roughly 0.4 expected if nothing had changed, and every item's difference exceeded about 995 of 1000 random re-splits of the pooled data. [OCC001, DIR001, REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the two mutually exclusive branches following A15 were taken with reversed frequencies: in the earlier window about 75 in 100 traces ran the branch containing A16, A17 and A18 (together with the ever-present A25) and about 25 in 100 ran the branch containing A19, A20 and A21, while in the later window the A19–A21 branch ran in about 75 in 100 traces and the A16–A18 branch in about 25 in 100. [OCC001, OCC004, DIR001, REL009, REL001, REL004]

Supporting signs: all six activities shifted participation by the same large margin (about 50 in 100 traces) in opposite directions, the routing out of A15 flipped in step, and the relational evidence shows a share shift rather than a structural replacement — both branches were observed in a substantial share of traces in both windows, the groups remained mutually exclusive, the fixed position of A15 before the active branch and the unordered co-occurrence inside each branch were preserved, and A25 was unaffected. The count of qualifying items (34 against roughly 0.4 expected without change) rules out chance sampling as an explanation of the ensemble. [OCC001, DIR001, REL007, REL022, REL012]

Limitations: the evidence cannot distinguish a changed choice probability at the A15 point from a changed mix of complete trace variants that happens to use the A19–A21 branch more often, and it shows only that the shares moved, not why. [OCC001, DIR001, REL009]

Other differences: none beyond the branch-share reversal; the internal ordering within each branch (no fixed order among its three activities) and A25's constant presence were the same in both windows. [REL007, REL013, REL022, REL012, REL024]