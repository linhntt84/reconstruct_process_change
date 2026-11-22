### Observed differences

- Participation flipped for three activities: in the earlier window A04 ran exactly once in every trace (200 of 200), while A01 and A03 were not observed at all; in the later window A04 is not observed (0 of 200) while A01 and A03 each run exactly once in every trace (200 of 200). [OCC001, OCC002, OCC003]
- The routing around A02 changed completely: earlier, every observed departure from A02 went to A04, and every departure from A04 went to A05; later, every departure from A02 goes to A03, every departure from A03 goes to A05, and A06 — which earlier had no observed successor — now always leads to A01. [DIR001, DIR002, DIR003, DIR004]
- Order and co-occurrence changed accordingly: earlier A02 preceded A04, and A04 preceded both A05 and A06; later A02 precedes A03, A03 precedes A05 and A06, and A05 and A06 both precede A01, co-occurring with it in every trace. [REL006, REL007, REL009, REL010, REL001, REL004, REL005, REL011, REL012]
- Event positions are consistent with traces growing from four to five events: A04 always sat about one third into the trace earlier and is unobserved later; A03 now sits at about one quarter and A01 at the final position; A05 moved from about two thirds to one half and A06 from the last position to three quarters. [POS001, POS002, POS003, POS004, POS005]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility of a structural control-flow change in the fragment formed by A02, A03, A04, A05, A06 and A01: in the earlier window every trace ran A02 → A04 → A05 → A06, while in the later window every trace runs A02 → A03 → A05 → A06 → A01 — A04 no longer executes, A03 has taken over its position between A02 and A05, and A01 was added as a new final step after A06. [OCC001, OCC002, OCC003, DIR001, DIR002, DIR003, DIR004, REL006, REL011, POS001, POS002]

The screening found 24 qualifying items where fewer than one (about 0.12) would be expected if nothing had changed, so the pattern as a whole cannot be explained by random sampling; all items describe one and the same re-sequencing, each comparison rests on all 200 traces in both windows, and the successor changes (A02 leading to A04 versus A03, A06 gaining A01 as successor) show the structural change directly rather than as a mere shift in how often existing paths are taken. [DIR001, DIR004, REL011, POS003]

An important competing explanation remains: zero participation only shows that an activity was not observed, so it cannot be fully excluded that A04 still exists but is never triggered, or that A01 and A03 existed earlier but were never sampled — implausible at 0 versus 200 of 200 traces, but not logically excluded. The evidence also covers only the control flow of these six activities, so behaviour elsewhere is untested. [OCC001, OCC002, OCC003]

Other differences: none beyond this change; the position shifts of A05 (from about two thirds to one half) and A06 (from the last position to three quarters) follow from A03 replacing A04 and A01 extending the traces, not from independent relocations. [POS004, POS005]