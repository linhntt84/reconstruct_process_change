### Observed differences

- Participation flipped for two activities: in the earlier window A05 ran in every trace (200 of 200, exactly once per trace) and A01 in none; in the later window A01 runs in every trace (200 of 200, once per trace) and A05 in none. [OCC001, OCC002]
- A01 now sits where A05 sat: A05's earlier position distribution (one fixed event position, mean 0.5, no spread) and A01's later distribution are identical. [POS001, POS002]
- The link to A03 transferred: earlier, every observed outgoing transition of A05 went to A03; later, every observed outgoing transition of A01 goes to A03. [DIR003, DIR001]
- The same upstream activities now lead into A01: A02's outgoing transitions pointed to A05 in about 72 in 100 earlier and point to A01 in about 75 in 100 later; A07 about 71 to 66; A06 about 28 to 29. [DIR002, DIR005, DIR004]
- Pairwise relations moved wholesale from A05 to A01: A06 preceded A05 in every earlier trace and now precedes A01 in every later trace; A03 co-occurred with A05 in every earlier trace (A05 first) and co-occurs with A01 in every later trace (A01 first); A01 and A05 never share a trace in either window. [REL008, REL004, REL007, REL002, REL003]
- The choice between A02 and A07 is preserved in kind: they remain mutually exclusive (about 47 vs 53 in 100 traces earlier, 50 vs 50 later), and whichever occurs now precedes A01 rather than A05. [REL001, REL005, REL006, REL009]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A01 has taken over the point in the flow that A05 occupied earlier: the step that in every trace ran after A06 and after whichever of the mutually exclusive activities A02 or A07 executed, directly before A03, is carried by A01 in the later window, while A05 is no longer observed at all. Participation flipped completely for both activities, the position distribution is unchanged, and the entire neighbourhood (A02, A07 and A06 upstream, A03 downstream) plus all pairwise order relations transferred from A05 to A01. [OCC001, OCC002, POS001, POS002, DIR001, DIR002, DIR003, DIR004, DIR005, REL002, REL004, REL007, REL008]

The screening comparison rules out chance as an explanation for the volume of differences: 18 control-flow items qualified where about 0.13 would be expected for an unchanged process, and every item's difference exceeds about 995 in 1000 random re-splits of the pooled traces. Note, however, that the items largely restate one coherent rewiring rather than constituting independent confirmations. [OCC001, OCC002, POS001, POS002, DIR001, DIR002, DIR003, DIR004, DIR005, REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009]

An important competing explanation cannot be ruled out: a relabelling of the same activity in event recording would look identical, since A01 and A05 never co-occur in either window and all neighbours and positions match exactly. [REL003, POS001, POS002]

Other differences: the split between the alternatives A02 and A07 moved from about 47/53 to 50/50, and small secondary transitions shifted a few points (A02 to A06 about 28 to 25 in 100, A07 to A06 about 29 to 34 in 100); the evidence cannot separate these from sampling variation between two 200-trace windows. [REL001, REL005, DIR002, DIR005]