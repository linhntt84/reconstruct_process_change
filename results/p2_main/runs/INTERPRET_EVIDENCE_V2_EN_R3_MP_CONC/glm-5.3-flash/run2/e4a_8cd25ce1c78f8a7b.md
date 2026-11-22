### Observed differences

- In the earlier window, the elapsed time between the completion of each of the activities A03, A04, A05, A06, A07 and A08 and the completion of A09 was stable at about 1 hour (means 0.98–1.02 hours). In the later window, all six of these intervals sit at about 1.9–2.0 hours — an increase of roughly 0.9 to 1.1 hours, meaning the time from each predecessor's completion to A09's completion roughly doubled. [TWAIT001, TWAIT002, TWAIT003, TWAIT004, TWAIT005, TWAIT006]
- The shift affects the whole distribution, not only the average: medians rose from about 0.95–1.02 hours to about 1.89–2.03 hours, and the spread also grew (for example, A03→A09 median 0.95 to 2.03 hours; A08→A09 median 1.02 to 1.93 hours). [TWAIT001, TWAIT006]
- Each of the six differences is larger than in more than 999 of 1,000 random re-splits of the pooled data. [TWAIT001, TWAIT002, TWAIT003, TWAIT004, TWAIT005, TWAIT006]
- How often each pair is observed changed only modestly and in both directions (A04→A09: 40 to 30 traces; A05→A09: 35 to 43; A07→A09: 30 to 36; the rest nearly flat), and no control-flow indicator qualified (0 items against about 0.23 expected without change), so the routing around these transitions appears stable. [TWAIT001, TWAIT002, TWAIT003, TWAIT004, TWAIT005, TWAIT006]

### Inference

Support level: Supported hypothesis

The evidence supports a timing change centred on A09: in the later window, the elapsed time between the completion of each of A03, A04, A05, A06, A07, A08 and the completion of A09 is about twice as long as before, rising from roughly 1 hour to roughly 2 hours on every transition into A09. Supporting signs: the time family produced 6 qualifying items where about 0.008 would be expected if nothing had changed, a gap far beyond what a stable process typically yields; all six measurements agree in direction and magnitude (added roughly 0.9–1.1 hours each); each difference exceeds essentially all reference comparisons; and each pair rests on a moderate number of observations (29–43 per window, about 15–20 in 100 traces). [TWAIT001, TWAIT002, TWAIT003, TWAIT004, TWAIT005, TWAIT006]

Limitations: T_WAIT is the elapsed time between consecutive completion events, not pure waiting or service time, so the extra hour could accumulate before A09 starts, within A09's own handling, or in unlogged intervening steps — the evidence cannot distinguish these. It also covers only transitions ending at A09, so it cannot show whether transitions elsewhere in the process slowed as well. [TWAIT001, TWAIT002, TWAIT003, TWAIT004, TWAIT005, TWAIT006]

Other differences: the observation counts behind the pairs shifted slightly in both directions (A04→A09 in 40 vs 30 traces, A05→A09 in 35 vs 43, A07→A09 in 30 vs 36); given that no control-flow item passed screening, these look like sampling variation rather than a routing change. [TWAIT002, TWAIT003, TWAIT005]