### Observed differences

- In the later window, four activities — A14, A15, A20 and A21 — are executed far less often: each appears in roughly 4–8 in 100 traces, down from roughly 24–28 in 100 before (for example, A15 appears in 55 of 200 traces before and 9 after; A21 in 50 before and 9 after). Each of these differences is larger than in about 199 of 200 random re-splits of the pooled data. [OCC001, OCC002, OCC003, OCC004]

- In the earlier window these four activities never co-occurred in one trace, and their participation shares sum to about 100 in 100 traces, so each earlier trace contained exactly one of them; accordingly, the distance from A23 to A25 was always 3 steps. In the later window they still never co-occur but together appear in only about 22 in 100 traces. [REL001, REL002, REL003, LAG002, OCC001, OCC002, OCC003, OCC004]

- In the later window, routing out of A23 concentrated on a single successor: transitions from A23 to A24 rose from about 48 in 100 observed outgoing transitions to 91 in 100, while transitions to A14, A15, A20 and A21 fell to about 4 in 100 or fewer each (from about 10–15 in 100 each). [DIR001]

- Routing out of A24 shows the same concentration on A25: about 87 in 100 after versus about 53 in 100 before, with transitions to the four activities dropping to about 4 in 100 or fewer each. [DIR002]

- The chain A23 → A24 → A25 therefore runs almost always without insertions in the later window: A24 immediately follows A23 in about 91 in 100 cases (about 48 before), A25 immediately follows A24 in about 87 in 100 (about 53 before), and the distance from A23 to A25 is now 2 steps in about 78 in 100 cases (previously always 3). The few remaining insertions sit mostly between A24 and A25. [LAG001, LAG002, LAG003, DIR001, DIR002]

- Pairwise relations mirror this: A15 co-occurred with A23, A24 and A25 in about 28 in 100 traces before versus about 4–5 in 100 after (with A15 before A25 in all earlier co-occurrences), A21 co-occurred with A25 in about 25 in 100 before versus about 4–5 in 100 after, and traces containing neither A14 nor A15 rose from about 49 in 100 to about 90 in 100. [REL004, REL005, REL006, REL007, REL008, REL009, REL001]

- The few remaining A15 occurrences sit slightly earlier within the trace (mean relative position about 0.48 versus 0.52), but this rests on only 9 traces. [POS001]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the process changed so that the insertion of one of the activities A14, A15, A20 or A21 — previously placed between A23 and A24 in about 52 in 100 traces, or between A24 and A25 in about 48 in 100 — is now skipped in most executions, leaving A23 → A24 → A25 as a near-always direct sequence with insertions remaining in only about 22 in 100 traces. [DIR001, DIR002, LAG001, LAG002, LAG003, OCC001, OCC002, OCC003, OCC004]

The support is direct and consistent rather than a mere frequency restatement: the successor profiles of A23 and A24 collapsed onto single targets, and the step distances A23→A24, A24→A25 and A23→A25 all shortened in exactly the way expected if one inserted activity per affected trace disappeared, while the earlier-window structure (exactly one of the four activities per trace, never two, always 3 steps from A23 to A25) is internally coherent with this reading. [DIR001, DIR002, LAG001, LAG002, LAG003, REL001, REL002, REL003]

Limitations: the residual participation rests on only 9–16 traces per activity, so the remaining insertion rate is uncertain; the occurrence, relation and position items describe the same underlying trace behaviour and are not independent confirmations of one another; and because the windows are finite samples, differences in variant frequencies alone can produce one-sided appearances — although a coordinated five-fold drop across four activities together with the routing and distance shifts is difficult to explain by sampling variation alone. The evidence cannot show whether the insertion step was removed from the process or merely became rare. [OCC001, OCC002, OCC003, OCC004, POS001]