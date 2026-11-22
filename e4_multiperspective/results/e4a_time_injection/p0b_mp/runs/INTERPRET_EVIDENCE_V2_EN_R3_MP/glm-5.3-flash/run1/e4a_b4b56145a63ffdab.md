### Observed differences

- In the earlier window, the elapsed time between consecutive completions of A14 and A20 was about 1.0 hour on average (median about 0.98 hours, middle half roughly 0.88–1.09 hours). In the later window it was about 2.0 hours (median about 1.96 hours, middle half roughly 1.78–2.16 hours) — roughly a doubling, with the whole distribution shifted rather than only a tail. This rests on 94 intervals per window, about 47 in 100 traces. [TWAIT001]
- The pair A15 → A20 shows the same pattern: median elapsed time rose from about 0.97 hours before to about 1.99 hours after, also roughly doubled, on 106 intervals per window, about 53 in 100 traces. [TWAIT002]
- Both timing differences are far outside what random re-splits of the pooled traces produce: each observed shift was larger than in about 1999 of 2000 reference comparisons. [TWAIT001, TWAIT002]
- No control-flow difference qualified: 0 of 52 tested units, where about 0.26 items would be expected by chance in an unchanged process. [screening]

### Inference

Support level: Supported hypothesis

The evidence supports a timing change as a possibility: in the later window, the elapsed time between the completion of A14 and A20, and between A15 and A20, roughly doubled from about 1 hour to about 2 hours per interval. The signs are direct and consistent: both intervals shifted by about 1 hour in the same direction, the entire distribution moved (all quartiles and the spread increased together), and the time family produced 2 qualifying items where only about 0.009 were expected without change — many times the chance expectation. A consistent change in these completion-to-completion times is a timing hypothesis in its own right and needs no structural counterpart; accordingly, control-flow screening found nothing (0 of 52 units against about 0.26 expected), so the shift appears isolated from any structural change. [TWAIT001, TWAIT002, screening]

Limitations: both intervals end at A20, so the two items may describe one underlying delay around A20 rather than two independent changes. TWAIT measures elapsed time between consecutive completion events, so the extra hour cannot be attributed to waiting, processing or scheduling components. An important competing explanation the evidence cannot rule out is that the delay is specific to these two activity pairs for reasons confined to this sample, rather than part of a broader timing shift. [TWAIT001, TWAIT002]

Other differences: none observed — control-flow screening produced no qualifying items at the configured thresholds. [screening]