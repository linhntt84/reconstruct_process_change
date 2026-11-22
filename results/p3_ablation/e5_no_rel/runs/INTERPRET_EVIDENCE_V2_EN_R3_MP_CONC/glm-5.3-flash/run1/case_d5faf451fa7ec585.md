### Observed differences

- In the earlier window, A14, A15 and A20 formed an optional mid-process step: A14 ran in about 32 of 100 traces, A15 in about 28 and A20 in about 40 — shares that sum to all traces, so each earlier case contained exactly one of the three, around the middle of the case (mean relative position about 0.51–0.52). In the later window, none of the three appears in any of the 200 traces. [OCC001, OCC002, OCC003, POS001, POS002, POS003]
- Before, A22 passed to A23 in about 55 of 100 of its outgoing transitions and to A20, A14 or A15 in the remaining ~45; in the later window, A22 passes to A23 after every occurrence. [DIR004]
- Before, A23 passed to A24 in about 45 of 100 of its outgoing transitions and to A14, A15 or A20 in the remaining ~55; in the later window, A23 always passes to A24. [DIR005]
- Before, A23 immediately followed A22 in about 55 of 100 traces (one step later otherwise), and A24 immediately followed A23 in about 45 of 100 traces (one step later otherwise); A24 always sat exactly three positions after A22, i.e. with exactly one intermediate activity besides A23. In the later window, A23 always immediately follows A22, A24 always immediately follows A23, and A24 always sits two positions after A22. [LAG001, LAG002, LAG003]
- The ever-present activities shifted slightly: A22's mean relative position moved from about 0.46 to about 0.47 and A24's from about 0.57 to about 0.55, consistent with one mid-trace event disappearing from every case. [POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the optional step formed by A14, A15 and A20 was dropped from the case flow. In the earlier window, every case executed exactly one of these three activities between A22 and A24 — inserted before A23 in about 45 of 100 cases and after A23 in about 55 — whereas in the later window none of the three is observed, A22 connects directly to A23 and A23 directly to A24, and the A22-to-A24 span shortens from three positions to two, so the sequence A22 → A23 → A24 now runs without any intermediate step. [OCC001, OCC002, OCC003, DIR004, DIR005, LAG001, LAG002, LAG003]

Chance is an unlikely explanation for this pattern as a whole: sixteen control-flow items qualified against roughly 0.33 expected for an unchanged process (66 units tested), and every item exceeds the difference seen in about 995 of 1000 random re-splits. The rerouting is shown directly by successor and distance evidence rather than inferred from participation alone, and the occurrence, direction, position and lag items consistently describe this one difference, including the small position shifts of A22 and A24. [DIR004, DIR005, LAG001, LAG002, LAG003, POS004, POS005]

Limitations: zero participation strictly means only that A14, A15 and A20 were not observed in the later window; the evidence cannot distinguish a genuine removal from these activities simply never being triggered in this sample, and it cannot show whether the dropped step was replaced by behaviour outside the tested units. [OCC001, OCC002, OCC003]