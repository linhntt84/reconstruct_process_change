### Observed differences

- In the earlier window, A01 ran in about 27 in 100 traces, late in the trace (mean relative position about 0.82), and every observed outgoing transition went to A05. In the later window, A01 runs in about 22 in 100 traces, is the first event of every trace that contains it (mean relative position 0.0), and every outgoing transition now goes to A06. [OCC001, DIR001, POS001]

- The repeating A11/A12 block changed its connections. Earlier, A11's outgoing transitions went to A01 (about 57%) or A12 (43%), A12's to A11 (57%) or A01 (43%); A11 and A12 each preceded A01 in about 27 in 100 traces (never the reverse), and A05 was reached from them only after 2–3 steps via A01. In the later window, A11 sends about 70% of its transitions directly to A05 and A12 about 30%, A01 precedes A11 and A12 (about 21–22 in 100 traces each), and the A11/A12-to-A05 distance shortened to 1–2 steps. [DIR007, DIR008, REL005, REL006, LAG007, LAG008]

- Distances and positions shifted accordingly: the A01-to-A05 distance grew from 1 step (all cases) to 4 steps (in 22 of the 43 traces where A05 still follows within five steps), A06-to-A05 shortened from 4 steps to about 3 in roughly half the cases, and A06, A11 and A12 now sit later in the trace (mean relative positions about 0.35, 0.75 and 0.67, previously about 0.22, 0.55 and 0.52). [LAG001, LAG002, POS003, POS005, POS006]

- A02 is not observed in the later window: earlier it ran in 53 of 200 traces (about 27 in 100) with outgoing transitions to A03, A07, A05, A08 and A13, and it co-occurred with A05 (always before it) and with A07 (in either order) in about 27 in 100 traces; afterwards none of these edges or co-occurrences appear (0 of 200 traces). [OCC002, DIR002, POS002, REL007, REL008, REL009, REL010, REL011]

- Routing around A02 moved onto the remaining paths: A03 now goes to A05 in about 85% of its outgoing transitions (about 65% before), A07 goes to A03 (48% vs 21%) and A13 (29% vs 7%) instead of to A02 (34%), A08 goes to A05 (62% vs 30%), and A13 goes to A08 (62% vs 37%); A07 also runs earlier in the trace (mean relative position about 0.06 vs 0.24). [DIR003, DIR005, DIR006, DIR009, POS004]

- Smaller participation shifts: A05 now occurs in about 46 in 100 traces (previously 54), A06 in about 22 (previously 27, and repeating less often: about 0.43 occurrences per trace vs 0.60), A10 in about 11 (previously 15), while A04 (about 23→28) and A09 (about 24→27) occur somewhat more often. [OCC004, OCC005, OCC006, OCC009, OCC010]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A01 changed its place in the control flow while the repeating A11/A12 block took over the handover to A05: earlier the sequence around this block read A06 → (A11/A12, repeating) → A01 → A05, whereas in the later window it reads A01 → A06 → (A11/A12, repeating) → A05. This rests on direct relational evidence — the relative order of A01 versus A11, A12 and A06 each flipped between the windows — on the replaced successors at A01, A11 and A12, on A01's shift from about 82% of the trace length to the very start, and on the matching lag changes; the key order and successor differences exceed those seen in about 995 of 1,000 random re-splits of the pooled traces. [REL003, REL005, REL006, DIR001, DIR007, DIR008, POS001, LAG001, LAG002, LAG007, LAG008]

Limitations: positions are event positions rather than clock time, each window holds 200 traces, and the evidence cannot distinguish A01 having been moved from the block's exit having been rewired to A05 while A01 was re-inserted as a new first step — both readings fit the same observed relations. [REL005, REL006, POS001, DIR007, DIR008]

Other differences:
- A02, executed in about 27 in 100 traces earlier, is not observed at all later, together with all its observed edges and co-occurrences; strictly, this means only that it did not appear in the later sample. [OCC002, DIR002, POS002, REL007, REL008, REL009, REL010, REL011]
- The routing in that region shifted onto the remaining paths (A03→A05, A07→A03/A13, A08→A05, A13→A08) and A07 now runs earlier in the trace. [DIR003, DIR005, DIR006, DIR009, POS004]
- Participation also drifted: A05, A06 (which repeats less) and A10 occur in fewer traces, A04 and A09 in somewhat more. [OCC004, OCC005, OCC006, OCC009, OCC010]
- An important competing explanation for these latter shifts is that they are knock-on effects of A02 no longer being executed rather than separate routing or frequency changes; the evidence cannot rule this out. [OCC002, DIR003, DIR005, DIR006, DIR009]