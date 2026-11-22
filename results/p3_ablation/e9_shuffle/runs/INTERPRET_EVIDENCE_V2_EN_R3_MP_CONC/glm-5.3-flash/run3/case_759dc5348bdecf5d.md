### Observed differences

- In the earlier window, A03 appeared in about 57 of 200 traces (roughly 1.2 occurrences per trace) and A11 in about 39 of 200; in the later window, neither activity was observed at all (0 of 200 traces). [OCC001, OCC002]
- All outgoing transitions of the two disappeared activities are gone: A03 previously led mostly to A11 (about 44%), A19 (about 28%) and A12 (about 22%), and A11 led almost always to A03 (about 97%); in the later window no outgoing transitions of either are observed. [DIR001, DIR003]
- A06's routing changed: before, about 86% of its outgoing transitions went to A03 and about 7% to A11; in the later window, about 58% go to A19 and about 37% to A12, with no transition to A03 or A11 observed. [DIR002]
- A19 and A12 now follow A06 much sooner: within five steps, A06→A19 at lag 1 rose from about 2% to about 24% of cases, and A06→A12 at lags 1–2 rose from about 18% to about 40%. [LAG003, LAG002]
- A12 and A19 each now occur in fewer traces (about 43 of 200 versus about 57 of 200) and at earlier positions (mean position about 0.33 to 0.23 for A12, and about 0.32 to 0.22 for A19). [POS003, POS004]
- Co-occurrence with A03 collapsed: A03 previously co-occurred with A06, A12 and A19 in about 29% of traces (mostly interleaved or repeated); in the later window co-occurrence is zero, A12 and A19 appear without A03 in about 21% of traces, and A03 and A11 never share a trace. [REL001, REL002, REL003, REL004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the part of the process running through A03 and A11 is no longer executed: in the earlier window A06 typically led to A03, which continued to A11, A19 or A12, whereas in the later window A03 and A11 are entirely unobserved and A06 proceeds directly to A19 and A12, which now follow it almost immediately and appear earlier in the traces. This is shown directly by the successor change at A06 and the complete disappearance of A03 and A11 across occurrence, position, direction and relation indicators, and it is consistent across all 18 qualifying items — far more than the roughly 0.22 expected by chance for 44 tested units. [DIR002, OCC001, OCC002, LAG003, LAG002, POS003, POS004]

A limitation: zero participation only means A03 and A11 were not observed in the later 200 traces, so the evidence cannot distinguish their removal from them becoming unreachable or extremely rare, nor fully rule out that the rerouting originates at A06 rather than at A03 itself. [OCC001, OCC002, DIR002]

Other differences: self-repetitions now occur at shorter distances — A12→A12 and A19→A19 previously clustered at lags 4–5 and now cluster at lags 3–4, and A06→A06 moved from lag 5 to lag 4 — though these rest on modest support (about 20 observations per window each). [LAG001, LAG004, LAG005]