### Observed differences

- A27 was executed exactly once in every trace in the earlier window (participation 100%); in the later window it appears in only about 51 in 100 traces, still once per trace when present [OCC001].
- A32, A33 and A38 were not observed at all in the earlier window; in the later window each appears once per trace in roughly 49–50 in 100 traces (98–99 traces out of 200 each) [OCC002, OCC003, OCC004].
- The routing out of A26 changed sharply: before, about 99 in 100 of its outgoing transitions went to A27; after, only about 50 in 100 go to A27, while about 17 in 100 go to A33, 16 to A38 and 15 to A32 [DIR001].
- The three new activities form an interconnected block that exits to A28: A32 leads to A38 (about 35 in 100), A33 (34) or A28 (28); A33 leads to A32 (43), A38 (31) or A28 (27); A38 leads to A28 (43), A33 (30) or A32 (27) [DIR003, DIR004, DIR005].
- The new activities occur around the midpoint of the trace (median position about 0.5) [POS001, POS002, POS003].
- The distance from A26 to A28 grew: before, A28 followed within 2 steps of A26 in about 98 in 100 cases; after, this holds in only about 50 in 100, while in about 48 in 100 the gap is 4 steps [LAG001].
- A27's own outgoing behaviour is essentially unchanged, still leading to A28 in about 96 in 100 of its transitions (about 99.5 in 100 before) [DIR002].

### Inference

Support level: Supported hypothesis

In about half of the later-window executions, a block of three activities — A32, A33 and A38, following one another in varying order — appears between A26 and A28, and A27, which was previously always executed between them, is skipped in those cases; in the remaining half, the original A26 → A27 → A28 path runs as before. The insertion is shown directly: A26 now sends about half of its transitions to the new activities instead of A27, the new activities chain among themselves and exit to A28, and the A26–A28 distance grows from 2 steps to 4 steps in about 48 in 100 cases — exactly what inserting three activities between them would produce. Participation and position agree: A27 drops from every trace to about half, each new activity appears in about half of the traces at the mid-trace position where A27 used to run. With 13 qualifying items against roughly 0.5 expected for an unchanged process, and 98–99 supporting traces behind each new activity, chance sampling or a one-window rare variant cannot account for the pattern as a whole [DIR001, DIR003, DIR004, DIR005, LAG001, OCC001, OCC002, OCC003, OCC004, POS001, POS002, POS003].

Limitations: the indicators are aggregate, so the evidence cannot show directly that A27 is skipped in precisely the traces that run the new block — the roughly 50/50 split at A26 together with A27's 51% participation make this the coherent reading, but a one-to-one correspondence is not observed. The internal structure of the block also remains imprecise, since A32, A33 and A38 follow one another in both directions. A competing explanation the evidence cannot fully exclude is that these paths existed before at a very low rate (unobserved in 200 traces) and merely became frequent, rather than being entirely new; the behavioural difference between the windows is substantial either way [DIR001, OCC001, DIR003, DIR004, DIR005].

Other differences: only marginal changes accompany this pattern — a few new edges at the 1–2 in 100 level (A26→A23, A32→A06 and A32→A25, A38→A02) and a slight dilution of A27's outgoing profile towards A09, A34 and A25, none of them individually large [DIR001, DIR002, DIR003, DIR005].