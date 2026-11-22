### Observed differences

- Activity A01 appears only in the later window: it is absent from all 200 earlier traces, while in the later window every one of the 200 traces contains it exactly once, almost always at the end of the trace (median at the last event, mean relative position about 0.94). [OCC001, POS001]
- A08's hand-off changed: in the earlier window its outgoing transitions went mainly to A05 (about 51 in 100), A02 (about 24) and A06 (about 20), and A08 itself was frequently the final activity (median at the last event); in the later window about 82 in 100 of its outgoing transitions go to A01, with A05, A06, A02 and A04 each at roughly 7 in 100 or less. [DIR002, POS004]
- Where A01 has a successor (53 observed outgoing transitions in the later window), it leads to A05 (about 45 in 100) or A06 (about 45 in 100); in the remaining later traces A01 is the last activity. [DIR001, POS001]
- A01 now co-occurs with A05, A06 and A08 in every trace, whereas it never co-occurred with any of them before; A08 precedes A01 in all traces, A05 precedes A01 in about 87 in 100 traces and A06 in about 75 in 100. [REL001, REL002, REL003]
- The pre-existing activities sit slightly earlier in the trace: mean relative position falls for A08 (about 0.87 to 0.77), A06 (about 0.74 to 0.66) and A05 (about 0.52 to 0.44). [POS002, POS003, POS004]
- Where A05 or A06 still follows A08, the gap is longer: one-step A08→A05 gaps fall from about 66 to 33 in 100 of these pairs, with three- or four-step gaps now appearing (about 19 in 100); two-step A08→A06 gaps fall from about 52 to 23 in 100, while three-to-five-step gaps rise to about 58 in 100. [LAG001, LAG002]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A01 was added to the process and is now executed exactly once per case at the end, typically directly after A08; consequently A08's former successors A05, A06, A02 and A04 no longer follow A08 directly but either precede A01 or hang off A01 instead. [OCC001, DIR001, DIR002, REL003]

The signs are direct and consistent: participation rises from 0 to 200 of 200 traces with exactly one execution per trace; A08's successor profile flips to about 82 in 100 towards A01; the relational items show A08 always before A01 and A05/A06 usually before it; and A08's earlier end-position, the slightly earlier positions of A05/A06/A08 and the longer A08→A05/A06 gaps all fit an activity appended after A08. Twelve control-flow items qualified against roughly 0.1 expected for an unchanged process, far beyond what chance produces, although most items describe this same single underlying difference rather than independent confirmations. [OCC001, POS001, POS002, POS003, POS004, DIR002, REL001, REL002, REL003, LAG001, LAG002]

Limitations: zero participation in the earlier window shows only that A01 was not executed then, so the evidence cannot distinguish a genuinely added activity from an existing path that was previously never taken and is now always taken; nor is A01's placement strictly fixed, since it precedes A05 in about 13 in 100 traces and A06 in about 26 in 100. [OCC001, REL001, REL002]