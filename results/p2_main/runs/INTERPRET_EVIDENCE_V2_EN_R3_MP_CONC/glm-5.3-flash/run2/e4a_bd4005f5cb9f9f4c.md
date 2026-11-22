### Observed differences

- The elapsed time between consecutive completion events of A28 and A33 roughly halved. In the earlier window a typical gap was about 0.91 hours (middle half about 0.82–0.99 hours); in the later window it was about 0.46 hours (middle half about 0.42–0.50 hours), a drop of about 0.45 hours. [TWAIT001]
- The shift affects the whole distribution: median and both quartiles fell by roughly half, and the spread narrowed from about 0.13 hours to about 0.06 hours, so gaps became both shorter and more uniform. [TWAIT001]
- The consecutive A28–A33 pair was observed somewhat less often: 58 gaps in the earlier window versus 45 in the later one, roughly 29 versus 23 in 100 traces (200 traces per window). [TWAIT001]
- Screening context: no control-flow indicator qualified (0 items against about 0.28 expected by chance), while the time family produced 1 item against about 0.01 expected — about 100 times the chance expectation. [TWAIT001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in timing: in the later window, the elapsed time between consecutive completions of A28 and A33 is about half of what it was in the earlier window (median about 0.46 hours versus about 0.91 hours). The signal is direct, since TWAIT measures exactly this elapsed time, and consistent: mean, median, both quartiles and the spread all decreased together, which fits an across-the-board shortening of the gaps rather than the disappearance of only the slow cases. It rests on 58 and 45 observed gaps, and a difference of this size exceeded all but about 1 of 2,000 random re-splits of the pooled data; the time family also yielded 1 qualifying item where about 0.01 would be expected if nothing had changed, while control flow yielded none. A consistent change in these elapsed times is a hypothesis in its own right and needs no structural counterpart, and none is observed. [TWAIT001]

Limitations: TWAIT is elapsed time between consecutive completion events, so the evidence cannot show whether the reduction lies in waiting, processing or scheduling between the two events, and it covers a single activity pair; an unlucky random split of an unchanged process cannot be fully excluded, although both the screening excess and the reference comparison make it unlikely. [TWAIT001]

Other differences: the consecutive A28–A33 pair occurred in a somewhat smaller share of traces in the later window (about 23 in 100 versus about 29 in 100), a modest participation change that did not qualify as a control-flow difference. [TWAIT001]