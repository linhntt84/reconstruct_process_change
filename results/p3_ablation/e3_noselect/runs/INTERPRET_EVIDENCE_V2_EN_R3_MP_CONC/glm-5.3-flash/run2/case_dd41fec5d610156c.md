### Observed differences

- **Entry and hub activity replaced.** In the earlier window, every trace contained A03 (about 2 occurrences per trace) and A05 as the second event, while A01 and A02 appeared in no trace (0 of 200). In the later window, A02 is the first event of every trace (median position 0), A01 appears in every trace around the third-quarter position, A05 is still the second event, and A03 no longer occurs (0 of 200). [OCC001, OCC002, OCC003, POS001, POS002, POS003, POS005]

- **Edges rewired around the new activities.** Before, A03 split its outgoing flow almost evenly to A05 (about 50 in 100) and A04 (about 50 in 100), and A06 always led back to A03. In the later window, A02 leads to A04 (about 51 in 100) or A01 (about 48 in 100), A01 leads to A05 in about 995 of 1,000 observed transitions, and A06 now leads to A01 (about 53 in 100) or A04 (about 46 in 100) instead of to A03. [DIR001, DIR002, DIR003, DIR005]

- **Ordering with A05.** Before, A03 always co-occurred with A05, preceding it in 56% of traces and being interleaved or repeated with it in 44%. In the later window, A02 and A01 co-occur in every trace with A02 first in 195 of 200 traces, A01 precedes A05 in all traces, and A02 precedes A05 in 98% of traces. [REL001, REL004, REL008, REL011]

- **Rework pair (A04 with A06) repositioned.** Before, A04 and A06 always came as a pair in 44% of traces, co-occurring with A03 (interleaved with it in 44% of all traces) and never with A01 or A02. In the later window, the pair appears in 50% of traces and co-occurs with A02 and A01: A04 precedes A01 in 28 of 100 traces (interleaved in 22), A06 precedes A01 in 28 of 100 (interleaved in 22), and A02 precedes each of them in 28 of 100. Their internal spacing also changed: A04→A04 and A06→A06 self-distances moved from 3 steps to 2 and 4 steps, and the A04→A05 distance is now 3 steps (54%) or 5 steps (15%) versus always 3 before. [REL003, REL005, REL007, REL009, REL010, REL012, REL014, LAG001, LAG002, LAG005, LAG006]

- **Minor shifts.** A04 and A06 participation rose only from 44% to 50% of traces, with mean occurrences per trace slipping from about 1.01 to 0.94 — a difference within typical sampling variation (strength about 0.34). A05 is essentially unchanged. In the later window A05 is occasionally followed by A02, but this rests on only 4 observed transitions. [OCC004, OCC005, POS005, DIR004, REL013]

### Inference

Support level: Supported hypothesis

The evidence supports a structural reorganisation in which A03's role was taken over by two activities: in the later window, A02 opens every case and A01 runs directly before A05, while A03 is no longer executed; the rework pair A04/A06, which previously looped back into A03 (A06 → A03), is now placed between A02 and A01 and flows into A01, so the former A03 → A05 path now runs A02 → A01 → A05. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR005, REL001, REL004, REL008, REL011, REL003, REL005]

Supporting signs: the participation flips are complete (0 of 200 traces versus 200 of 200 traces), the gained and lost edges are observed directly rather than inferred from positions alone, and the occurrence, direction, position, relation and lag items all describe one coherent restructuring — they are consistent views of the same underlying difference, not independent confirmations. [OCC001, OCC003, DIR002, DIR005, POS001, REL001, LAG001]

Limitations: the exact internal sequence of the A04/A06 block (interleaved or repeated in about 22 of 100 traces) cannot be pinned down from the aggregates, and the evidence cannot rule out that the two windows capture different process variants or case mixes rather than a modification of a single flow — although the complete appearance of A01/A02 and disappearance of A03 make pure sampling fluctuation implausible. [REL007, REL009, OCC001, OCC003]

Other differences: A05 is occasionally followed by A02 in the later window (4 observed transitions), which could hint at a loop back to the start but is too weak to interpret; the slight participation increase of A04/A06 (44% to 50%) is within typical sampling variation. [DIR004, OCC004, OCC005]