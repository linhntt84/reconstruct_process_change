### Observed differences

- The elapsed time from the completion of A15 to the next completion, A16, shortened: the median was about 6 minutes in the earlier window (39 occurrences) versus about 2 minutes in the later window (42 occurrences), with the mean falling from about 0.11 to about 0.04 hours. [TWAIT001]
- The same pattern for A19 → A16: mean about 7 minutes before (39 occurrences) versus about 3 minutes after (46 occurrences); median about 7 versus about 2 minutes. [TWAIT002]
- The largest shift is A28 → A16: mean about 48 minutes before versus about 24 minutes after — roughly halved (median about 49 versus about 26 minutes). [TWAIT003]
- All three differences point the same way and are unusually large: a difference of this size or larger appeared in only about 1 in 2,000 random re-splits of the pooled traces for each item. Each transition pair occurs in roughly 15–25 out of 100 traces in both windows, so the estimates rest on moderate sample sizes. [TWAIT001, TWAIT002, TWAIT003]
- No control-flow difference qualified: 0 of 55 tested units, in line with the roughly 0.27 items expected by chance, so no structural or ordering change was detected at the configured thresholds. [screening]

### Inference

Support level: Supported hypothesis

The evidence supports a timing change: in the later window, A16 completes sooner after the completion of its predecessors A15, A19 and A28 than in the earlier window. The short gaps (about 6–7 minutes after A15 or A19) shrank to about 2–3 minutes, and the long gap after A28 (about 48 minutes) was roughly halved. All three transitions into A16 show the same direction, each difference exceeds virtually all random re-splits, and the time family produced 3 qualifying items against roughly 0.014 expected without change — many times the chance expectation — while control flow produced none. [TWAIT001, TWAIT002, TWAIT003, screening]

Limitations: T_WAIT measures elapsed time between consecutive completion events, so the evidence cannot distinguish whether A16 started earlier, was executed faster, or whether idle time between the predecessor's completion and A16 shrank. Because all three pairs share A16, the change may be local to A16 rather than process-wide, and each pair covers only about one in five traces, leaving the rest of the process unobserved for timing. [TWAIT001, TWAIT002, TWAIT003]

Other differences: the A28 → A16 pair occurred in fewer traces in the later window (about 16 in 100 versus about 20 in 100), a small participation change that did not qualify as a control-flow difference. [TWAIT003, screening]