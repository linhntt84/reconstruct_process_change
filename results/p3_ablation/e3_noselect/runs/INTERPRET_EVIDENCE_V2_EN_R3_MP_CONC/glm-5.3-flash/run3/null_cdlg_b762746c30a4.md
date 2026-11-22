### Observed differences

- In the later window, A01 is executed in more traces: about 52 in 100 traces versus about 46 in 100 before (105 vs 92 of 200 traces). Its outgoing behaviour is essentially unchanged, still leading to A07 in about 95 in 100 of its outgoing transitions. [OCC001, DIR001]
- A10 and A11, which always occur together (identical support counts in both windows), are executed in fewer traces: about 48 in 100 versus about 54 in 100 before (95 vs 108 of 200 traces). [OCC008, OCC009]
- After A05, the flow is redirected: A01 receives about 49% of A05's outgoing transitions versus about 39% before, while A10 drops from about 25% to 21% and A11 from about 26% to 23%; the small flows to A03 and A04 (about 3 in 100) shrink to under 1 in 100. [DIR002]
- A06 is executed in fewer traces: about 9–10 in 100 versus about 15 in 100 before (19 vs 29 of 200 traces), matching a drop in A07's outgoing flow to A06 from about 14% to about 10%. [OCC005, DIR003]
- A02 appears in more traces: about 9 in 100 versus about 4–5 in 100 before (18 vs 9 of 200 traces), mirrored by A07's outgoing flow to A02 rising from about 4.5% to 9%; this rests on few traces. [OCC002, DIR003]
- Participation of A03, A04, A08 and A09 changes only slightly (within about 3 percentage points, empirical strengths 0.0–0.43), and the internal balance of the A10/A11 loop shifts only weakly (for example A10 to A11 from about 43% to 47% of A10's outgoing transitions). [OCC003, OCC004, OCC006, OCC007, DIR004, DIR005]

### Inference

Support level: Weak hypothesis

The evidence suggests a redistribution of flow between existing paths: in the later window, traces pass through A01 more often (about 52 in 100 traces vs 46) and through A10 and A11 less often (about 48 in 100 vs 54), with A05 sending about 10 percentage points more of its outgoing transitions to A01 and correspondingly less to A10/A11. Supporting signs: the participation changes align with the observed rerouting at A05's outgoing transitions; every activity involved is observed in a substantial share of traces in both windows, no activity or edge appears or disappears, and no repetition occurs in either window, which fits a shift in how often existing alternatives are taken rather than activities being added, removed or bypassed. [OCC001, OCC008, OCC009, DIR002]

What is missing: the evidence provides no screening baseline, so it cannot be shown that this number of qualifying items exceeds what an unchanged process typically produces; the empirical strengths are moderate (about 0.78–0.85, meaning roughly 15–22 in 100 random re-splits show equally large differences), and the A10/A11 items describe one shared behaviour rather than two independent confirmations. An important competing explanation that cannot be ruled out is ordinary sampling variation between the two 200-trace windows. [OCC001, OCC002, DIR002]

Other differences: A06 is executed less often (about 9–10 in 100 traces vs about 15) and A02 more often (about 9 in 100 vs 4–5, on only 18 vs 9 traces), with matching shifts in A07's outgoing transitions; these participation changes are not part of the main hypothesis. [OCC005, OCC002, DIR003]