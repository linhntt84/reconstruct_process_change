### Observed differences

- Before, the six activities A28, A30, A31, A32, A33 and A34 each appeared exactly once in every trace (200 of 200). In the later window, A28, A30 and A31 each appear in about 47 in 100 traces, and A32, A33 and A34 in about 56 in 100 traces; none of them repeats within a trace in either window. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006]

- In the later window these six activities split into two nearly mutually exclusive groups: a trace contains either A28/A30/A31 or A32/A33/A34. Pairs within a group still co-occur whenever one of them occurs (about 47 or 56 in 100 traces), while cross-group pairs such as A28 with A32 co-occur in only about 2 in 100 traces. Before, every pair among the six co-occurred in all traces. Every later trace still contains at least one of the two groups. [REL013, REL015, REL018, REL025]

- The embedding order is preserved: A25 still precedes A28/A30/A31 and A32/A33/A34 whenever they occur, and these still precede A26. The ordering inside each group remains mixed in both windows (for example, A28 precedes A30 in roughly half of their co-occurrences before and after). [REL001, REL004, REL007, REL010, REL013, REL025]

- Routing at the boundaries changed: before, the observed outgoing transitions of A25 went only to A28, A30 and A31 (shares roughly 0.34, 0.37, 0.30); in the later window they spread over all six group activities (roughly 0.15–0.20 each). A28, A30 and A31 now transition directly to A26 in about 26–35 in 100 of their outgoing transitions, which was not observed before. [DIR001, DIR002, DIR003, DIR004]

- Distances and positions shifted accordingly: the gap from A25 to A32/A33/A34, and from A28/A30/A31 to A26, was always 4–5 steps before and is mostly 1–3 steps in the later window. A28/A30/A31 now sit at relatively later positions (mean about 0.68 to 0.74 of the trace) and A32/A33/A34 at relatively earlier positions (about 0.77 to 0.74). A25 and A26 still appear in every trace in both windows. [LAG001, LAG002, LAG003, LAG004, LAG008, LAG011, POS001, POS002, POS003, POS006]

- Caveat on support: the lag items for cross-group pairs in the later window rest on only about 4 observations each and are weak; the lag items used above rest on roughly 90–150 observations per window. [LAG005, LAG009, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that in the later window traces typically execute only one of two activity blocks between A25 and A26 — either A28/A30/A31 (about 47 in 100 traces) or A32/A33/A34 (about 56 in 100) — whereas before, both blocks ran in sequence in every trace (A25, then A28/A30/A31 in varying order, then A32/A33/A34 in varying order, then A26). About 2 in 100 later traces still contain both blocks. [OCC001, OCC004, REL013, REL015, REL025, DIR001]

The support is direct and consistent: the participation drop is large (from 200 of 200 traces to about 93 or 111 of 200) and affects all six activities in the same structured way, which rules out a rare variant appearing in one window; the relational items show the near-mutual exclusivity of the two groups and the preserved A25-before and before-A26 order; the routing items show A25 branching into either group and A28/A30/A31 now exiting to A26; and the gap distributions shrink from 4–5 steps to 1–3 steps, exactly as expected if one block is skipped. The number of qualifying items (58) is far above the roughly 0.63 expected if nothing had changed, and every item's difference is larger than in about 995 of 1,000 random re-splits of the pooled traces. [REL015, DIR001, DIR002, LAG001, LAG004]

Limitations: the indicator families largely describe the same traces, so they are not independent confirmations of one another. The evidence also cannot distinguish a modification of the process from a shift in the mix of two pre-existing variants (for example, different cases already following different paths), since the one-block behaviour is absent from all 200 before-traces and present in nearly all after-traces; and the cross-group lag items rest on only about 4 later-window observations each. [REL015, LAG005]