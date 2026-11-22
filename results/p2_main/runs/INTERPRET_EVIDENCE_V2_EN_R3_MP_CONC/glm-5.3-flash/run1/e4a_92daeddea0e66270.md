### Observed differences

- In the earlier window, the elapsed time between the completions of A38 and A41 was about 1.0 hours on average (median about 1.03 hours, middle half roughly 0.93–1.13 hours); in the later window it is about 0.50 hours (median about 0.49, middle half roughly 0.45–0.54). The interval is cut roughly in half and is observed in about 100 of 200 traces in each window. [TWAIT001]
- The pair A40–A41 shows the same shift: about 1.0 hours on average before (median about 1.01) versus about 0.51 hours after (median about 0.52), again roughly halved, with about 100 intervals per window. [TWAIT002]
- In both pairs the intervals also became more uniform: the standard deviation fell from about 0.15 hours to about 0.08 hours. [TWAIT001, TWAIT002]
- Both differences are larger than in about 1,999 of 2,000 random re-splits of the pooled data, so they are very unusual for an unchanged process. [TWAIT001, TWAIT002]
- How often these intervals occur is essentially unchanged: 100 versus 104 intervals for A38–A41 and 100 versus 96 for A40–A41 across 200 traces per window. [TWAIT001, TWAIT002]
- Screening produced no control-flow items (0 among 63 units, against about 0.31 expected by chance) but 2 time items against about 0.008 expected, so the time differences far exceed what an unchanged process typically yields. [screening]

### Inference

Support level: Supported hypothesis

The evidence supports a timing change centred on A41: in the later window, the elapsed time from the completion of A38 — and likewise from A40 — to the subsequent completion of A41 is about half an hour instead of about one hour. Both intervals show the same roughly 0.5-hour reduction with about 100 observations per window each, both differences exceed essentially all random re-splits, and the time family yielded 2 items where about 0.008 were expected without change; the absence of control-flow items (0 versus about 0.31 expected) is consistent with a timing change that has no structural counterpart. [TWAIT001, TWAIT002, screening]

Limitations: TWAIT measures elapsed time between consecutive completion events, not pure waiting or service time, and an interval measure cannot show which endpoint moved — the reduction could reflect A41 being completed sooner after its predecessors or a change in when A38/A40 complete relative to A41. The two items also share A41, so they likely describe one underlying difference rather than two independent confirmations. [TWAIT001, TWAIT002]