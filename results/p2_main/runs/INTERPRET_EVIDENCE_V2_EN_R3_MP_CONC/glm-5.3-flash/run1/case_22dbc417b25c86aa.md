### Observed differences

- Activity A06 was executed exactly once in every before-window trace (200 of 200) but is not observed at all in the later window (0 of 200). [OCC001, POS003]
- Before, A05 was followed by A06 in all observed cases; in the later window, A05 is followed directly by A01 in all observed cases. [DIR001]
- A06's outgoing transition to A01, present in all before-window cases, is no longer observed in the later window. [DIR002]
- The distance from A05 to A01 changed from two steps in every before-window case (with A06 in between) to one step — immediate succession — in every later-window case. [LAG001]
- Before, A01 and A05 each co-occurred with A06 in every trace (A06 before A01, and A05 before A06, respectively); in the later window, both activities occur in every trace but never together with A06. [REL001, REL002]
- Event positions shifted slightly: A01's mean position moved from 0.5 to 0.4 and A05's from about 0.17 to 0.2, consistent with each trace containing one event fewer. [POS001, POS002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the A06 step between A05 and A01 was dropped from the flow: in the earlier window every case ran A05 → A06 → A01, while in the later window A05 leads directly to A01 and A06 is not executed in any case. This is shown directly by the successor change at A05, the disappearance of A06 and of its edge to A01, the A05–A01 distance shrinking from two steps to one, and the co-occurrence of A01 and A05 with A06 falling from every case to none. All nine qualifying control-flow items — far more than the roughly 0.04 expected if nothing had changed — describe this one underlying difference, and each difference is larger than in about 99.5 in 100 random re-splits of the pooled data. [OCC001, DIR001, DIR002, LAG001, REL001, REL002]

Limitations: zero participation only shows that A06 was not observed in the later window, so a permanent removal cannot be distinguished from A06 becoming conditional and simply not triggering in this sample; the evidence also covers only the fragment around A05, A06 and A01. The small position shifts of A01 (mean 0.5 to 0.4) and A05 (about 0.17 to 0.2) are consistent with the same shortening of traces rather than a separate change. [POS001, POS002]