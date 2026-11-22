### Observed differences

- In the earlier window, A21, A22 and A23 each ran exactly once in every trace (participation 100 in 100 cases, one occurrence per case); in the later window they survive in only about 1 in 200 traces. [OCC004, OCC005, OCC006]
- A14, A15 and A16 were not observed at all in the earlier window; in the later window they run in about 30, 33 and 37 in 100 traces respectively, and never together — their shares cover essentially all later traces, so each later case contains exactly one of the three. [OCC001, OCC002, OCC003, REL001, REL002, REL010]
- A39's successors changed wholesale: earlier its outgoing transitions led to A23, A22 and A21 in roughly equal thirds (about 35, 31 and 35 in 100); later they lead to A16, A15 and A14 in roughly equal thirds (about 37, 33 and 30 in 100). [DIR007]
- The new activities sit exactly where the old block was: A39 precedes each of A14, A15 and A16 in every trace in which they appear, and each of them is always followed by A24, its only observed successor. [REL007, REL015, REL022, DIR001, DIR002, DIR003, REL006, REL014, REL021]
- The gap from A39 to A24 shrank from always 4 event positions earlier to 2 positions in about 995 in 1000 later traces, and A24's mean position moved slightly earlier (about 0.43 to 0.39 of the trace length). [LAG010, POS007]
- Earlier, A21, A22 and A23 ran together in every case without a fixed order among themselves (for example, A21 before A22 in about 52 in 100 traces and A22 before A21 in about 48); that whole block is gone in the later window. [REL025, REL026, REL031]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the segment between A39 and A24 was restructured by replacement: the block of three activities A21, A22 and A23, which every case previously executed in varying order, was removed, and a single per-case choice among three new activities — A14, A15 or A16 — now runs in its place, each followed by A24. The participation changes are near-complete rather than marginal (100 in 100 down to about 1 in 200, and 0 up to 30–37 in 100); A39's successor profile flipped from the old trio to the new one with full support in both windows (200 traces each); the new activities are mutually exclusive and embedded between A39 and A24; and the A39-to-A24 distance collapsed from 4 to 2 positions, as expected when three activities are replaced by one. With 71 qualifying items against roughly 0.64 expected if nothing had changed, chance sampling cannot account for the overall pattern. [OCC004, OCC005, OCC006, OCC001, OCC002, OCC003, DIR007, REL001, REL002, REL010, REL006, REL014, REL021, LAG010]

Limitations: the evidence shows that the new activities occupy the old block's position, but it cannot show that they perform the same function — the codes are anonymous, so a relabelling or a functionally different step inserted at the same spot cannot be excluded. The few items describing A21, A22 or A23 behaviour in the later window rest on a single trace and carry almost no weight. [DIR004, DIR005, DIR006, LAG001, POS004]

Other differences:
- A41 ran in about 59 in 100 traces earlier and about 69 in 100 later; earlier it always accompanied the A21/A22/A23 block, whereas later it co-occurs with the chosen A14/A15/A16 activity in nearly all of its appearances. [REL030, REL035, REL039, REL009, REL017, REL024]
- The ordering between the choice activity and A40 loosened: earlier A23 preceded A40 in about 63 in 100 traces (interleaved in the rest); later the chosen activity precedes A40 in only about 14–22 in 100 traces, with the remainder interleaved, while A40's participation and approximate position are essentially unchanged. [REL038, REL008, REL016, REL023, POS009]