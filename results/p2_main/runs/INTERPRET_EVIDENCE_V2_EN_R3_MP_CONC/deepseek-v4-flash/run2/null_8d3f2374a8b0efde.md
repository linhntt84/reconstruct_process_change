### Observed differences

- In the later window, after activity A22, the next activity is more often A21 (about 58% of outgoing transitions vs 18% before) and less often A25 (about 13% vs 53% before); the share to A23 stays about the same (29% in both windows). [DIR001]
- The gap between A22 and A25 increased: in the later window, A22 and A25 occur within one step in about 13% of cases (vs 53% before), while gaps of 2–3 steps rise from about 47% to about 87%. [LAG001]
- Activity A22 is observed in fewer traces in the later window (31 out of 200 vs 49 out of 200). [DIR001, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports a change in the control-flow routing from activity A22: in the later window, A25 is less often the immediate successor of A22, A21 more often takes that role, and when A25 is still reached, it tends to occur after more intermediate steps. This is directly shown by the shift in A22's outgoing transition distribution and by the increased lag between A22 and A25. The number of qualifying items (2) is well above the 0.29 expected by chance for the control-flow family, so the overall pattern is unlikely to be a sampling artefact. A limitation is that both items describe the same underlying behaviour (A22's relation to A25), so they are not independent confirmations, and the number of traces containing A22 is moderate (49 before, 31 after), giving some uncertainty in the exact shares.

Other differences: none.