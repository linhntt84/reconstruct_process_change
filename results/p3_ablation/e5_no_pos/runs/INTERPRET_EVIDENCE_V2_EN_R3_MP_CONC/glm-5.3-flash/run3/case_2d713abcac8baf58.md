### Observed differences

- In the earlier window, A19, A20 and A21 each ran in about a third of cases (70, 60 and 72 of 200 traces) but almost never together, so nearly every case contained exactly one of the three; in the later window each appears in only 1–2 of 200 traces. [OCC001, OCC002, OCC003, REL001, REL002, REL008]
- A26, A27 and A28 were absent from the earlier window (0 of 200 traces) and now occur exactly once in virtually every case (200 of 200 traces each, with only 1–2 traces showing a repeat). [OCC004, OCC005, OCC006]
- The branching activity A44, present in all traces in both windows, now routes to the new activities: before, about 85% of its observed outgoing transitions went to A19 (31%), A21 (30%) and A20 (25%); after, about 85% go to A26 (31%), A27 (27%) and A28 (26%). [DIR007]
- A26, A27 and A28 now co-occur in 100% of traces, and for each pair both execution orders appear in roughly equal shares (about 50/50), so they run as an unordered group; each of them follows A44 in about 99% of traces and precedes A29 in about 98–99%. [REL019, REL020, REL023, REL022, REL025, REL027, REL021, REL024, REL026]
- The positional distance from A44 to A29 grew: before, A29 followed A44 at a distance of 2 event positions in about 84% of cases (16% at distance 3); after, it follows at distance 4 in about 82% (18% at distance 5), consistent with three activities now sitting between them instead of one. [LAG001]
- A29 itself is stable, present in essentially all traces in both windows; its earlier co-occurrence with A19, A20 and A21 (in 35%, 30% and 36% of traces, always after them) dropped to about 1%. [REL006, REL012, REL017, REL007, REL013, REL018]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the step between A44 and A29 was replaced: in the earlier window each case contained exactly one of the alternatives A19, A20 or A21 after A44 before reaching A29, whereas in the later window A19, A20 and A21 have nearly disappeared and A26, A27 and A28 each run once per case, in no fixed order among themselves, between A44 and A29. This is a replacement of one path segment by another — a formerly single alternative step giving way to a mandatory group of three — not a shift of shares between unchanged alternatives. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, DIR007, REL019, REL020, REL023, LAG001]

The change is shown directly and consistently: participation collapsed for A19/A20/A21 and rose from zero to universal for A26/A27/A28, A44's successor profile switched as a whole, relational evidence places the new activities between A44 and A29, and the A44→A29 distance grew from about 2 to about 4 positions, matching one activity being replaced by three. Overall, 41 evidence items qualified against fewer than 1 expected by chance for an unchanged process, so the set as a whole is not a chance artefact. [DIR007, LAG001, REL021, REL022]

A competing explanation the evidence cannot rule out is that both behaviours already existed and only their frequencies shifted between the two sampled windows, since the windows are finite samples; the evidence also cannot show why the replacement happened. [OCC004, OCC001]

Other differences: the later successor profiles observed for A19, A20 and A21 rest on only 1–2 traces each and are unreliable. [DIR001, DIR002, DIR003] A44 and the new activities also show a handful of additional weak outgoing edges, each about 0.5–1% of transitions, and 1–2 traces repeat one of A26/A27/A28. [DIR004, DIR005, DIR006, OCC004, OCC005, OCC006]