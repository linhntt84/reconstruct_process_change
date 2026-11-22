### Observed differences

- In the earlier window, A19 appeared in about 45 in 100 traces and A20 in about 55 in 100; in the later window, each appears in only about 1 in 200 traces. [OCC001, OCC002]
- In the earlier window, A19 and A20 were strict alternatives: every trace contained exactly one of the two (A19 alone in about 45 in 100 traces, A20 alone in about 55 in 100) and they never occurred together; in the later window, about 99 in 100 traces contain neither of them. [REL001]
- Routing consolidated around the missing activities. In the earlier window, about 45 in 100 of A26's outgoing transitions went to A27, about 27 to A20 and about 23 to A19; in the later window, about 97 in 100 go to A27. [DIR003]
- Likewise, in the earlier window about 51 in 100 of A27's outgoing transitions went to A28, about 27 to A20 and about 21 to A19; in the later window, about 97 in 100 go to A28. [DIR004]
- The remaining steps also sit closer together: A26 is followed by A27 after one step in about 99 in 100 later cases (earlier about 45 in 100, mostly after two steps); A26 reaches A28 after two steps in about 96 in 100 later cases (earlier about 93 in 100 after three steps); A27 reaches A28 after one step in about 98 in 100 later cases (earlier split roughly evenly between one and two steps). [LAG005, LAG006, LAG007]
- The later-window profiles of A19's and A20's own outgoing transitions and positions rest on a single observed case each and carry little weight. [DIR001, DIR002, POS001, POS002, LAG001, LAG002, LAG003, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, the alternative branches containing A19 and A20 are essentially no longer executed and the flow runs through A27 instead: earlier, every trace took exactly one of the two branches (about 45 in 100 via A19, about 55 in 100 via A20, never both), whereas in the later window about 99 in 100 traces contain neither activity, A26 leads to A27 in about 97 in 100 transitions and A27 leads to A28 in about 97 in 100, with the A26→A27→A28 steps now consecutive. [OCC001, OCC002, REL001, DIR003, DIR004, LAG005, LAG006, LAG007]

Supporting signs: 22 evidence items qualified, against about 0.5 expected by chance in an unchanged process; the participation drop rests on about 200 traces per window; and the rerouting at A26 and A27 and the lag changes each rest on about 200 observations in both windows and point in the same direction. Several items describe the same underlying behaviour (the disappearance of A19 and of A20), so they are not independent confirmations, but the participation, routing and positional evidence complement one another. [OCC001, OCC002, DIR003, DIR004, LAG005, LAG006, LAG007]

An important competing explanation remains: the later window still shows A19 and A20 once each, so the evidence cannot distinguish between the branches having been removed and their now being chosen only very rarely; the finding is therefore a shift in how often existing paths are taken, not evidence that activities were moved or reordered. [OCC001, OCC002]

Other differences: none beyond the above; the remaining items reflect the same disappearance of A19 and A20 and are based on single later-window observations. [DIR001, DIR002, POS001, POS002, LAG001, LAG002, LAG003, LAG004]