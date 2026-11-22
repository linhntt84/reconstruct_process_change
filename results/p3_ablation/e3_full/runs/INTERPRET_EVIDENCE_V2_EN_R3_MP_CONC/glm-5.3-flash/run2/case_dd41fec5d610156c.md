### Observed differences

- **A03 disappeared; A01 and A02 appeared.** In the earlier window every trace contained A03, about twice per trace on average (mean 2.01, repeated in about 44 in 100 traces), while A01 and A02 appeared in no trace at all. In the later window A03 occurs in none of the 200 traces, and A01 and A02 each occur exactly once in all 200 traces. [OCC001, OCC002, OCC003, POS001, POS002, POS003]

- **New entry and exit wiring.** In the later window A02 sits at the very start of the trace (median position 0) and its outgoing transitions split about 51 in 100 to A04 and 48 in 100 to A01; A01 sits about two-thirds into the trace (median position 0.75) and leads to A05 in about 199 of its 200 outgoing transitions. [DIR001, DIR002, POS001, POS002]

- **The block's routing partner changed.** Earlier, A03's outgoing transitions went about 50 in 100 to A04 and 50 in 100 to A05, and A06 led only back to A03; later, A06 leads to A01 in about 53 in 100 and to A04 in about 46 in 100 of its outgoing transitions. [DIR003, DIR005]

- **Relations flipped from "never together" to "always together".** Earlier, A05 always appeared without A01 or A02; later, A01 precedes A05 in every trace, A02 precedes A01 in about 195 of 200 traces, and A04 precedes A01 in the 100 traces containing both (56 strictly before, 44 with interleaving or repetition). [REL001, REL003, REL004, REL008]

- **Block participation and spacing.** The A04–A06 block appears in 100 of 200 later traces versus 88 of 200 earlier traces; on the occurrence indicator this difference is well within what random re-splits produce (empirical strength about 0.34). Where A04 or A06 repeats, the gap between the two executions moved from typically three steps to typically two, and A06 is now typically followed immediately by A04 (based on about 44–50 paired observations per window). [OCC004, OCC005, LAG001, LAG004, LAG006]

- **A05 unchanged; a rare new variant.** A05 remains a single execution in the final position in both windows. In the later window, about 2 in 100 traces place A02 after A05 (A05 → A02 observed in four transitions) and about 5 in 100 place A01 before A02. [POS005, DIR004, REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that the way traces run around the optional A04–A06 block was restructured. In the earlier window, every trace passed through A03 — about twice per trace — which entered the block via A04 or went directly to the closing A05, with the block returning to A03 (A06 → A03) before the trace ended in A05. In the later window, A03 is not observed; A02 opens every trace and leads either into the block (via A04) or directly to A01, and the newly observed A01, executed once per trace, always precedes the closing A05. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR005, REL001, REL004]

The supporting signs are direct and consistent across indicator families: participation flips between 0 and 200 of 200 traces with differences larger than in about 995 of 1000 random re-splits; the directional, positional, relational and step-spacing items all describe the same wiring; and the shortened repetition gaps match an activity having been removed from the block's cycle. A05's unchanged final position in both windows anchors the reading. [DIR005, REL001, LAG001, LAG004, POS005]

Other differences: the rise in block participation from 88 to 100 of 200 traces is within chance variation on the occurrence indicator and is not counted as part of the hypothesis; the roughly 2–5 in 100 later traces with A02 after A05 or A01 before A02 form a rare variant of the new routing. [OCC004, OCC005, DIR004, REL001]

The main competing explanation the evidence cannot rule out is that A01 and A02 were rare, unobserved paths in the earlier window and A03 a rare path in the later one, since zero participation only means the activity was not observed; moreover, the occurrence, position, direction and relation items largely describe the same underlying trace changes rather than independent confirmations. [OCC001, OCC003]