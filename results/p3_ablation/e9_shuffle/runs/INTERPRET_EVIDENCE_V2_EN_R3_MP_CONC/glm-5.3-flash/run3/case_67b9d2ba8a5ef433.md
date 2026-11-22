### Observed differences

- Activity A01 was not observed at all in the earlier window (0 of 200 traces) but occurs in every trace of the later window (200 of 200), exactly once per trace, always at the same relative position, about 0.83 of the trace length [OCC001, POS001].
- In the earlier window, A07's observed outgoing transitions split about 52 in 100 to A03 and 48 in 100 to A05, while A05's split about 52 in 100 to A07 and 48 in 100 to A03; A03 was reached from A05 and A07 within 1–2 steps, so the pair A05/A07 ran in either order and was followed directly by A03 [DIR003, DIR002, LAG001, LAG002].
- In the later window, A01 sits between that pair and A03: about 53 in 100 of A07's outgoing transitions now go to A01 (about 47 still to A05), about 47 in 100 of A05's go to A01 (about 53 to A07), and all of A01's observed outgoing transitions go to A03 [DIR003, DIR002, DIR001].
- Before, A01 never co-occurred with A03, A05 or A07 (each pair appeared as the other activity alone in 100 of 100 traces); after, A01 co-occurs with each of them in all traces, always after A05 and A07 and before A03 [REL001, REL002, REL003].
- The step distance from A05 and A07 to A03 grew by one step: A05 reached A03 within 1 step in about 48 of 100 cases before versus within 2–3 steps after, and A07 within 1–2 steps before versus 2–3 steps after [LAG001, LAG002].
- A05 and A07 now occur slightly earlier in the trace (mean relative position about 0.70 for both before, versus about 0.58 and 0.59 after) [POS002, POS003].

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that, in the later window, a new step A01 was placed between the A05/A07 pair and A03: traces that previously moved from A05 and A07 (in either order) directly to A03 now execute A01 once, after both of them and before A03. The signs are direct and mutually consistent — A01 went from unobserved to occurring once in every trace at a fixed position, it always follows A05 and A07 and precedes A03, about half of the outgoing transitions of A05 and A07 that previously led to A03 now lead to A01, the distance from A05/A07 to A03 increased by exactly one step, and the slightly earlier positions of A05 and A07 fit an event added after them [OCC001, POS001, POS002, POS003, REL001, REL002, REL003, DIR001, DIR002, DIR003, LAG001, LAG002].

Twelve control-flow items qualified against roughly 0.06 expected by chance in an unchanged process, far more than random splitting would typically produce, and each difference was larger than in about 995 of 1000 random re-splits; however, many items describe the same underlying insertion, so they are not independent confirmations [OCC001, POS001, POS002, POS003, REL001, REL002, REL003, DIR001, DIR002, DIR003, LAG001, LAG002].

Limitations: the picture covers only these four activities, so A01's placement relative to unobserved parts of the process is unknown, and the position evidence reflects event order rather than clock time [POS001, DIR001]. An important competing explanation the evidence cannot rule out is that A01 already existed but was too rare to appear in the earlier 200 traces and then became frequent, rather than being genuinely new — zero participation only means it was not observed in that sample [OCC001, POS001].

Other differences: none — every qualified item fits the same insertion of A01 described above [OCC001, POS001, POS002, POS003, REL001, REL002, REL003, DIR001, DIR002, DIR003, LAG001, LAG002].