### Observed differences

- In the earlier window, every trace followed one backbone: A38, then A14, then A15, then either A20 together with A21 (about 50 in 100 traces) or A22 (about 50 in 100), and finally A23. A38's only observed successor was A14, and A23 always lay 4–5 steps after A38. [DIR001, LAG001, REL001, REL005, REL012, REL013, REL016]
- In the later window, about 52 in 100 traces still run this full path, but in about 48 in 100 traces A38 is followed directly by A23, only one step apart, so that A14, A15 and the A20/A21/A22 branch are all skipped; such direct A38→A23 transitions were not observed at all in the earlier window. [DIR001, LAG001, REL005, REL006, REL011]
- Participation fell accordingly: A14 and A15 from all traces (100%) to about 52 in 100, A20 and A21 from about 50 to about 29 in 100, and A22 from about 50 to about 24 in 100; none of them disappeared. [OCC001, OCC002, OCC003, OCC004, OCC005]
- The internal branch structure is unchanged: A20 and A21 still occur together, remain mutually exclusive with A22, and still precede A23 when they run. [REL012, REL013, REL014, REL016]
- Positions shifted only slightly: A38's mean relative position moved from about 0.30 to about 0.32 and A23's from about 0.44 to about 0.41, consistent with the segment between them being shortened rather than either activity being relocated. [POS001, POS002]
- Timing also differs: among traces that still execute A14, the elapsed time from A38 to A14 rose from about 2.0 to about 3.0 hours; the elapsed time from A28 to A34 fell from about 0.9 to about 0.45 hours (47 vs 63 observations), and from A35 to A34 from about 0.20 to about 0.08 hours. [TWAIT001, TWAIT002, TWAIT003]

### Inference

Support level: Supported hypothesis

Main hypothesis: in the later window, roughly half of the cases take a shortcut in which A38 leads directly to A23, bypassing A14, A15 and the A20/A21/A22 branch, which previously always executed between them. These five activities became skippable in about 48 in 100 cases rather than removed: they still run, with their previous mutual order, in the remaining traces. The change is shown directly by A38's successor profile (100% to A14 before, versus about 52% to A14 and 48% to A23 after), by the A38→A23 distance collapsing from always 4–5 steps to one step in about 48% of traces, and by A23 and A38 now occurring without A14 in about 48 in 100 traces, which never happened before. [DIR001, LAG001, REL005, REL006, REL011, OCC001, OCC002]

The screening comparison supports this reading: the control-flow family produced 29 qualifying items against roughly 0.45 expected for an unchanged process, and the time family 3 against roughly 0.01, with every item's difference exceeding about 995 in 1000 random re-splits. The many REL items largely restate this single bypass behaviour rather than constituting independent confirmations. [DIR001, LAG001, REL005, TWAIT003]

A competing explanation the evidence cannot fully rule out: the direct A38→A23 edge was simply not observed in the earlier window, and an empty profile does not prove absence, so a very rare pre-existing shortcut that grew in frequency cannot be excluded. The evidence also cannot indicate why cases take the shortcut. [DIR001, LAG001]

Other differences: Timing changed on transitions outside the bypass structure. Among the cases that still run A14, the elapsed time from A38 to A14 increased by about 1 hour (its observation count fell from 200 to 105, mirroring A14's participation), while the elapsed times from A28 to A34 and from A35 to A34 roughly halved; no structural change was flagged for A28, A34 or A35. [TWAIT001, TWAIT002, TWAIT003, OCC001]