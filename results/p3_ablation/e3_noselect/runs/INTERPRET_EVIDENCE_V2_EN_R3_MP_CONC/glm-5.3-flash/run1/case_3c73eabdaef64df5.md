### Observed differences

- In the earlier window, every trace is short and uniform: it contains only two activities, A04 followed immediately by A07; A04's only observed outgoing transition goes to A07, and A07 sits at the last position of all 200 traces. [DIR002, POS003, POS006, LAG001]
- In the later window, every trace contains six activities in a single fixed order: A04 → A03 → A05 → A06 → A07 → A01. A04 now leads to A03 in 100% of observed transitions instead of A07, and A03→A05, A05→A06, A06→A07 and A07→A01 are each the only observed successor of their source. [DIR001, DIR002, DIR003, DIR004, DIR005]
- A01, A03, A05 and A06 appear in 0 of the 200 earlier traces but in 200 of 200 later traces, exactly once per case. [OCC001, OCC002, OCC003, OCC004]
- A04 and A07 still run in every trace in both windows, but their positions shift: A04 moves from mid-trace (mean relative position about 0.5) to the first position (about 0.17), A07 from the last position (1.0) to second-to-last (about 0.83), the new activities fill the intermediate positions, and A01 takes the final position. These are event positions, not clock times. [POS001, POS002, POS003, POS004, POS005, POS006]
- The distance from A04 to A07 grows from one step (directly consecutive in 200 of 200 earlier traces) to four steps (200 of 200 later traces). [LAG001]
- Every activity pair among the six changes from "never in the same trace" or "only one of the two present" to co-occurring in 200 of 200 later traces, each in one fixed order that matches the chain above. [REL001, REL005, REL006, REL009, REL010, REL014]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a block of steps was added to the flow: cases that previously ran from A04 directly to A07 now pass through A03, A05 and A06 between them, and a further new step, A01, now closes every case after A07. A01, A03, A05 and A06 were not executed in any of the 200 earlier traces and are executed exactly once per case in the later window. [OCC001, OCC002, OCC003, OCC004, DIR001, DIR002, DIR003, DIR004, DIR005, LAG001]

The support is direct and consistent: the successor of A04 flips from A07 to A03 in 100% of observed transitions, the four new edges are deterministic, all activity pairs move to full co-occurrence in one fixed order, and the A04-to-A07 lag grows from one to four steps — a single six-step chain explains all 30 evidence items, each with the maximum empirical strength (its difference exceeds all 200 random re-splits). With four activities absent from 200 earlier traces yet present in all 200 later traces, chance sampling of a rare variant is not a plausible explanation. [OCC001, OCC002, OCC003, OCC004, DIR001, DIR002, DIR003, DIR004, DIR005, POS001, POS002, POS003, POS004, POS005, POS006, REL001, REL005, REL006, REL009, REL010, REL014, LAG001]

Limitation: the evidence describes executed behaviour only, so it cannot distinguish genuinely inserted steps from a previously optional path that was simply never taken before, nor rule out that the later window samples an exclusively different case variant; positions and lags are event positions, not clock times, so no timing claim is made. [OCC001, OCC002, OCC003, OCC004, POS003, POS006, LAG001]