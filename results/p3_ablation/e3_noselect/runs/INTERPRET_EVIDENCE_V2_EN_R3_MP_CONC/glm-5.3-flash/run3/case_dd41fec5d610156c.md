### Observed differences

- **A01 and A02 appear; A03 disappears.** In the earlier window, A01 and A02 were not observed in any of the 200 traces, while A03 ran in every trace, about twice per trace on average and repeated in roughly 44 in 100 traces. In the later window, A01 and A02 each occur exactly once in all 200 traces, and A03 is not observed at all. [OCC001, OCC002, OCC003, POS003]

- **New routing through A02 and A01.** In the later window, A02 is the first event of the trace (median normalised position 0); of A02's observed outgoing transitions, about 51 in 100 go to A04 and about 48 in 100 to A01, and A01 in turn leads to A05 in about 199 of 200 transitions. In the earlier window, A03's outgoing transitions split about 50/50 between A05 and A04. [POS002, DIR001, DIR002, DIR003]

- **A06 re-routed.** Earlier, all of A06's roughly 200 observed outgoing transitions went to A03; in the later window, about 53 in 100 go to A01 and about 46 in 100 to A04. [DIR005]

- **A05 unchanged as the closing activity, but reached differently.** A05 sits at the final position in both windows. Earlier it always appeared without A01/A02 and together with A03 (A03 first in 56 of 100 traces, interleaved by A03's repetition in the rest); in the later window it co-occurs with A01 and A02 in every trace, with A01 before A05 in all traces and A02 before A01 in about 98 of 100 traces. [POS005, REL004, REL008, REL001, REL011]

- **Secondary shifts around A04 and A06.** Participation in A04 and A06 rose from about 44 to 50 in 100 traces; the repeat gap A04→A04 and A06→A06 shortened from about 3 steps to mostly 2, and the A04→A05 gap changed from always 3 steps to a mix of 3 and 5. [OCC004, OCC005, LAG001, LAG002, LAG005, LAG006]

- **A rare new edge.** In the later window, 4 outgoing transitions from A05 to A02 were observed; A05 had no observed outgoing transitions earlier. This rests on very few observations. [DIR004]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in which A03 is no longer executed and A01 and A02 now run in every trace: in the earlier window every trace contained A03 about twice, A03 routed to A04 or directly to the closing A05, and A06 always fed into A03; in the later window A03 is not observed, A02 opens the trace and routes to A04 or A01, A01 precedes A05, and A06 routes to A01 or A04 instead. The participation flips are direct (0 vs 200 of 200 traces), the new and lost edges are observed directly in the direction profiles, and the relation, position and gap evidence all fit one coherent picture; each key difference is larger than in about 199 of 200 random re-splits of the pooled traces, so sampling variation or a rare one-window variant cannot account for the pattern as a whole. A limitation: zero participation only means an activity was not observed, so the evidence cannot distinguish removing A03 from the later window simply never taking its path, and the apparent A05→A02 edge rests on only 4 observations. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR005, REL001, REL004, REL008]

Other differences: the modest rise in A04/A06 participation (about 44 to 50 in 100 traces) and the shortened repeat gaps around A04 and A06 (from about 3 to about 2 steps) accompany the re-routing but are not required by the main hypothesis. [OCC004, OCC005, LAG001, LAG006]