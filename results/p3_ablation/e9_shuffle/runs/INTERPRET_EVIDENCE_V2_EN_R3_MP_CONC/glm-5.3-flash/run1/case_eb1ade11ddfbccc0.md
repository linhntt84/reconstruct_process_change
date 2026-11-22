### Observed differences

- A03 is no longer observed: in the earlier window it appears in all 200 traces, once per trace, as the first event (median position ~0); in the later window it appears in none of the 200 traces. [OCC001, POS002]
- A07 appears for the first time: previously unobserved, in the later window it occurs exactly once in every trace, at median position 0.75. [OCC002, POS004]
- The step after A04 is rerouted: earlier, about 99 in 100 of A04's outgoing transitions led to A01 (about 1 in 100 to A03); in the later window all of them lead to A07, and all of A07's outgoing transitions lead to A01. The distance from A04 to A01 grows from one step (99 in 100 cases) to two steps (all cases). [DIR002, DIR003, LAG003]
- A02 and A04 sit earlier in the trace: A02's median position moves from 0.25 to 0 (now the first event) and A04's from 0.75 to 0.5; the A02→A04 distance tightens from 2–3 steps to always 2, while A02→A01 becomes always 4 steps (previously 3 in about 87 of 100 cases, otherwise 4). [POS001, POS003, LAG001, LAG002]
- Co-occurrence flips from A03 to A07: earlier, A03 co-occurred with A01, A02 and A04 in every trace (A03 first in roughly 86–100 of 100 cases); in the later window A03 co-occurs with none of them, while A07 co-occurs with A02, A04 and A01 in every trace, always in the order A02 → A07, A04 → A07, A07 → A01. [REL001, REL003, REL005, REL006, REL002, REL004, REL007]

### Inference

Support level: Supported hypothesis

The evidence supports a structural reorganisation of the case sequence: A03, which opened every case in the earlier window, is no longer observed in any trace, and A07, previously unobserved, now runs exactly once per case between A04 and A01. The earlier chain A03 → A02 → … → A04 → A01 appears in the later window as A02 → … → A04 → A07 → A01, with A02 as the first event and A04 about a quarter of the trace earlier. [OCC001, OCC002, DIR002, DIR003, REL006, REL002, LAG003]

The screening makes chance an unlikely explanation: 19 control-flow items qualified where only about 0.13 would be expected if nothing had changed, and the items agree across occurrence, routing, positional and relational indicators — including two-sided participation evidence (A03 from 100 in 100 traces to 0, A07 from 0 to 100 in 100, 200 traces each way) and direct successor evidence (A04 now routes to A07, and A07 to A01). [OCC001, OCC002, DIR002, DIR003, POS004]

Limitations: zero participation only shows that A03 was not observed in the later sample, so the evidence cannot fully exclude that A03 still occurs outside these 200 traces, nor determine whether A07 is a newly added step or one that simply did not appear in the earlier sample. [OCC001, OCC002]

Other differences: in the earlier window, A03's outgoing transitions also went to A05 (about 5 in 100), A06 (about 6 in 100), A04 (about 2 in 100) and A01 (about 1 in 100); with A03 unobserved in the later window, none of these exits is observed any more, and their fate cannot be assessed. [DIR001]