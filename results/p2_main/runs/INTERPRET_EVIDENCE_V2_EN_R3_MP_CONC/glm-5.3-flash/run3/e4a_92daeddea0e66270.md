### Observed differences

- In the later window, the elapsed time between consecutive completions of A38 and A41 is roughly half of what it was earlier: the median fell from about 1.0 hour (middle half roughly 0.9–1.1 hours) to about 0.5 hours (middle half roughly 0.45–0.54 hours), a drop of about 0.54 hours, and the spread narrowed (standard deviation about 0.15 → 0.08 hours). The pair itself occurred at almost the same rate, in about 100 of 200 traces before and about 104 of 200 after. [TWAIT001]
- The same pattern appears for A40 and A41: the median elapsed time fell from about 1.0 hour to about 0.5 hours (a drop of about 0.50 hours), while the pair occurred in about 100 of 200 traces before and about 96 of 200 after. [TWAIT002]
- Both timing differences are larger than those produced by all but about 1 of 2,000 random re-splits of the pooled data (empirical strength about 0.9995 each), so they are highly unusual for an unchanged process. [TWAIT001, TWAIT002]
- Screening qualified only these two timing items: the time family produced 2 items where about 0.008 would be expected by chance, while the control-flow family produced none among 63 units tested (about 0.31 expected), so no structural difference was detected at the configured thresholds. [TWAIT001, TWAIT002]

### Inference

Support level: Supported hypothesis

The evidence supports a timing change centred on A41: in the later window, the elapsed time from the completion of A38 to the next completion of A41, and from the completion of A40 to the next completion of A41, is about half of what it was in the earlier window — roughly 0.5 hours instead of about 1 hour — while the frequency with which these pairs occur is essentially unchanged (about 100 of 200 traces per window for each pair). [TWAIT001, TWAIT002]

Supporting signs: the two items agree in direction and magnitude, each rests on about 100 pair observations per window, each difference exceeds essentially all random re-splits, and the time family produced 2 qualifying items against a chance expectation of about 0.008 — far more than an unchanged process would typically yield. No control-flow item qualified, so the change presents as purely temporal rather than structural. [TWAIT001, TWAIT002]

Limitations: both items share A41, so they may reflect one underlying change rather than two independent confirmations; T_WAIT measures elapsed time between consecutive completion events, so the evidence cannot show whether the reduction lies in waiting, processing, or how completions are spaced; and a structural shift too small to pass the control-flow thresholds cannot be fully ruled out. [TWAIT001, TWAIT002]