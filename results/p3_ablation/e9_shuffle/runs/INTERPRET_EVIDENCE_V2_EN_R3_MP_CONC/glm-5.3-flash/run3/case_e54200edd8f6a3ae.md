### Observed differences

- Activity A03 was not executed at all in the earlier window (0 of 200 traces); in the later window it appears in every trace, exactly once per trace, always at the same early relative position (mean 0.22 of the trace length, no variation). [OCC001, POS002]
- Earlier, the outgoing transitions of A07 split roughly evenly between A02 (about 33 in 100), A06 (about 32 in 100) and A10 (about 36 in 100); in the later window, A07 is followed by A03 in essentially all observed transitions. [DIR002]
- In the later window, A03's outgoing transitions go to A02 (about 39 in 100), A06 (about 33 in 100) and A10 (about 29 in 100); no outgoing transitions from A03 could be observed earlier because A03 did not occur. [DIR001]
- The distance from A07 to each of A02, A06 and A10 grew by about one step: earlier the pairs occurred 1–3 positions apart (roughly a third of cases at each distance), later 2–4 positions apart. [LAG001, LAG002, LAG003]
- Earlier, A03 never co-occurred with A02, A06 or A10 (each of the three appeared without it in 100 in 100 traces); later, all three always co-occur with A03, with A03 before A02, A03 before A06 and A03 before A10, while A07 comes before A03. [REL001, REL002, REL003, REL004]
- The relative positions of A02, A06 and A10 each moved slightly later (mean from about 0.37–0.38 to about 0.44–0.45 of the trace), while A07 moved slightly earlier (0.125 to 0.111), consistent with every trace gaining one event. [POS001, POS003, POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A03 was added as a mandatory step between A07 and the block of A02, A06 and A10. Earlier, traces ran from A07 directly into one of A02, A06 or A10 in roughly equal shares, and A03 was never executed; later, every trace runs A07 into A03, and A03 hands over to A02, A06 or A10 in broadly similar proportions, with the distance from A07 to each of the three longer by about one step and their positions shifted slightly later. This is shown directly by the successor change at A07 and the new outgoing edges of A03, and it is consistent across the relation, lag, position and occurrence indicators; 15 items qualified against roughly 0.12 expected by chance in the control-flow family, far beyond what an unchanged process typically produces. [OCC001, DIR001, DIR002, REL001, REL002, REL003, REL004, LAG001, LAG002, LAG003, POS002]

Limitations: zero participation in the earlier window means only that A03 was not observed then, not that it was absent from the process model, and the evidence cannot rule out changes outside the tested units. The evidence also cannot exclude that the modest shift in successor shares is sampling variation. [OCC001, DIR001, DIR002]

Other differences: the shares of the three successors moved somewhat (A02 from about 33 to about 39 in 100, A10 from about 36 to about 29 in 100, A06 roughly unchanged), which is not required by the insertion itself and may be noise. [DIR001, DIR002]