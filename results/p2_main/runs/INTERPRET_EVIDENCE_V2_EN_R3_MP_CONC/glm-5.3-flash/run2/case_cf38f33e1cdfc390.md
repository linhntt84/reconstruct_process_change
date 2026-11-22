### Observed differences

- The choice between two alternative paths out of A15 reversed. In the earlier window, A15's outgoing flow went to A16, A17 or A18 in about 75 in 100 cases (outgoing shares roughly 27, 23 and 26 in 100) and to A19, A20 or A21 in about 25 in 100 (roughly 14, 4 and 8); in the later window, about 75 in 100 go to A19, A20 or A21 (roughly 25, 22 and 29) and only about 25 in 100 to A16, A17 or A18 (roughly 9, 9 and 8). [DIR001]
- Participation flipped accordingly: A16, A17 and A18 each ran in 150 of 200 traces before but in only 49 of 200 after, while A19, A20 and A21 each rose from 50 of 200 to 151 of 200. Each of the six activities still occurs at most once per trace in both windows. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006]
- The two groups remain mutually exclusive alternatives in both windows: for pairs spanning the groups (e.g. A16 with A19) co-occurrence is zero throughout, and the share of traces where only one side runs moves from about 75 in 100 favouring A16's group to about 75 in 100 favouring A19's group. [REL009, REL014, REL018]
- The internal structure of each group is unchanged: A16, A17 and A18 ran together in about 75 in 100 traces before, in both orders between them, and rarely afterwards (neither present in about 75 in 100); A19, A20 and A21 went from about 25 to about 75 in 100 running together, again in both orders. [REL007, REL013, REL022, REL025]
- A25 runs in every trace in both windows but switches company: its co-occurrence with A16, A17 or A18 fell from about 75 to about 25 in 100, while with A19, A20 or A21 it rose from about 25 to about 75 in 100, with no fixed order relative to the active group in either window. [REL012, REL021, REL024, REL027]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that two existing alternative paths after A15 were taken with different frequencies in the later window: the path on which A16, A17 and A18 run together (alongside A25, which executes in every case) dropped from about 75 in 100 traces to about 25 in 100, while the alternative on which A19, A20 and A21 run together rose from about 25 to about 75 in 100. [OCC001, OCC004, DIR001, REL009, REL022]

The reversal appears directly and consistently in three views of the same behaviour — participation counts, A15's outgoing routing shares, and the co-occurrence and order relations of every involved pair. Both paths and all six activities are observed in substantial shares in both windows, the groups stay mutually exclusive, the internal mixed order and the at-most-one occurrence per trace are unchanged, and no activity is bypassed — exactly the situation in which a shift between existing path frequencies is the reading the data supports. With 35 qualifying control-flow items against roughly 0.53 expected by chance for the 106 tested units, sampling variation cannot account for the pattern as a whole. [DIR001, REL007, REL022, REL025]

One competing explanation cannot be ruled out: because both blocks hang as alternatives off the same activity A15 and have no fixed internal order, the evidence cannot distinguish a change in the branch-choice frequencies from the two blocks exchanging their roles in the process — both would leave the same traces. [DIR001, REL009]

Other differences: the positional gap between A15 and A20 shortened slightly — a gap of 3 event positions in about 52 in 100 observed pairs before versus about 34 in 100 after, with gaps of 1–2 positions becoming more common; this is based on event positions, not clock time. [LAG001]