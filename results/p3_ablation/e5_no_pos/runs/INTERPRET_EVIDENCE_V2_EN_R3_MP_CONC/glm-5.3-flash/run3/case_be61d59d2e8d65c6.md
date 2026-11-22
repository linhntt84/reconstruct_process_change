### Observed differences

- Earlier, A19, A20 and A25 were regular but optional visitors: A19 ran in about 33 of 100 traces, A20 in about 29 and A25 in about 40 (65, 57 and 81 of 200 traces). In the later window each appears in only about 1 of 200 traces. [OCC001, OCC002, OCC003]
- The routing around them concentrated onto a direct chain. Earlier, about 52 of A27's outgoing transitions in 100 went to A28, with A25 (about 20), A19 (about 13) and A20 (about 10) taking most of the rest; in the later window about 97.5 of 100 go to A28. Earlier, about 43 of A28's outgoing transitions in 100 went to A29, with A25, A19 and A20 taking most of the remainder; in the later window about 97 of 100 go to A29. [DIR005, DIR006]
- The block's ties to the rest of the process vanished. Earlier, A19, A20 and A25 each co-occurred with A27, A28 or A29 in roughly 29–41 of 100 traces, always after A27 and before A29, but in both orders relative to A28; in the later window about 99.5 of 100 traces contain A27, A28 and A29 without any of the three, and pairs within the block are hardly seen in either window (about 99 of 100 traces contain neither member). [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009, REL010, REL011, REL012]
- Positions tightened accordingly: A27 is immediately followed by A28 in about 99 of 100 cases (earlier about 52, with about 45 at distance 2); A28 is immediately followed by A29 in about 96 of 100 (earlier about 43, with about 52 at distance 2); the A27-to-A29 distance moved from mostly 3 steps to mostly 2. [LAG001, LAG002, LAG004]
- Separately, A10's successor mix was redistributed: earlier its transitions led mostly to A15 (about 20 in 100), A47 and A16 (about 17 each) and A45 (about 14); in the later window they lead mostly to A26 (about 17), A45 (about 15), A16 and A41 (about 9 each), with A15 and A47 receding to about 6 and many small new edges appearing. [DIR001]

### Inference

Support level: Supported hypothesis

In the later window the optional block of activities A19, A20 and A25, which earlier was executed in roughly three to four of ten traces between A27 and A29, is no longer observed in practice: the flow that previously passed through one of these three activities now runs directly A27 → A28 → A29 in nearly every trace. [OCC001, OCC002, OCC003, DIR005, DIR006, REL003, REL005, REL012, LAG001, LAG002, LAG004]

The screening context supports this reading: 25 control-flow items qualified against roughly 0.5 expected for an unchanged process, so the pattern as a whole is not what random re-splits produce, and the participation collapse is large (65, 57 and 81 traces earlier versus 1 each later) while the routing, co-occurrence and distance indicators all describe the same underlying difference rather than isolated rare variants. [DIR005, DIR006, REL003, REL009, LAG001, LAG002, LAG004]

The evidence cannot distinguish a complete removal of A19, A20 and A25 from these activities still occurring in fewer than about 1 of 200 traces, which this sample could not detect; the changed successor profiles of the single remaining A19, A20 and A25 traces (toward A38, A37 and A31) rest on one observation each and do not characterise any new behaviour. [OCC001, OCC002, OCC003, DIR002, DIR003, DIR004]

Other differences: A10's outgoing transitions were redistributed (A15 and A47 receding, A26 and A41 gaining share); the evidence does not show whether this is connected to the disappearance of the A19/A20/A25 block. [DIR001]