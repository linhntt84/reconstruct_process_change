### Observed differences

- Screening qualified four time items where about 0.01 would be expected if nothing had changed, while the control-flow family produced no items against an expectation of about 0.27 [screening].
- In the earlier window, the elapsed time between consecutive completion events from each of A16, A17, A18 and A19 to A25 centred on about one hour (medians roughly 1.02–1.03 hours); in the later window it centred on about half an hour (medians roughly 0.48–0.53 hours), a reduction of about 0.5 hours — roughly half — on every one of the four pairs [TWAIT001, TWAIT002, TWAIT003, TWAIT004].
- These elapsed times also became more uniform, with standard deviations falling from about 0.14–0.17 hours to about 0.05–0.08 hours [TWAIT001, TWAIT002, TWAIT003, TWAIT004].
- Each of the four differences is larger than in about 1,999 of 2,000 random re-splits of the pooled traces [TWAIT001, TWAIT002, TWAIT003, TWAIT004].
- Each ordered pair was observed in a substantial minority of traces in both windows — for example A16→A25 in about 20 of 100 traces before versus about 27 after, and A19→A25 in about 31 before versus about 18 after — so the timing comparison rests on roughly 18–32 in 100 traces per window [TWAIT001, TWAIT002, TWAIT003, TWAIT004].

### Inference

Support level: Supported hypothesis

The evidence supports a change in timing: in the later window, the elapsed time between consecutive completion events on the transitions from A16, A17, A18 and A19 into A25 was about half of what it was in the earlier window (about 0.5 hours versus about 1.0 hour on average). This hypothesis is measured directly by the T_WAIT indicator, and it is consistent: all four pairs show the same direction and a nearly identical magnitude (about −0.5 hours), each based on 35–64 observations per window and each larger than in about 1,999 of 2,000 random re-splits [TWAIT001, TWAIT002, TWAIT003, TWAIT004]. The time family produced four qualifying items where about 0.01 were expected without change, so the pattern as a whole is unlikely to be a sampling artefact, and a consistent change in these inter-completion times is a timing hypothesis in its own right that needs no structural counterpart — accordingly, no control-flow items qualified [screening].

Limitations: T_WAIT is the elapsed time between consecutive completions, not pure waiting or service time, so the evidence cannot show whether the reduction originates in A25's completion behaviour, in the predecessors A16–A19, or in how completions are spaced; because all four pairs share A25, the four items may also reflect one underlying change rather than four independent ones [TWAIT001, TWAIT002, TWAIT003, TWAIT004].

Other differences: the number of traces in which each pair was observed shifted modestly and in mixed directions (A16→A25 up from 41 to 53 and A18→A25 up from 46 to 64, but A19→A25 down from 61 to 35 and A17→A25 down from 52 to 48, out of 200 traces per window); the evidence does not show a consistent participation change, and these shifts are not part of the timing hypothesis [TWAIT001, TWAIT002, TWAIT003, TWAIT004].