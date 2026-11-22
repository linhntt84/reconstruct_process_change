### Observed differences

- Activity A01 was absent from the earlier window (0 of 200 traces) but occurs in the later window in every trace, exactly once per trace, always at the same late position in the trace (normalized position about 0.83 in all cases). These differences are larger than in about 199 of 200 random re-splits of the pooled data. [OCC001, POS001]
- In the earlier window, A03, A05 and A07 each occurred without A01 in 100 in 100 traces; in the later window A01 co-occurs with each of them in 100 in 100 traces, always after A05 and after A07, and always before A03. [REL001, REL002, REL003]
- Successors changed accordingly: before, A05 led to A07 (about 52%) or A03 (about 48%), and A07 led to A03 (about 52%) or A05 (about 48%); after, A05 leads to A07 (about 53%) or A01 (about 47%), A07 leads to A05 (about 47%) or A01 (about 53%), and A01 leads only to A03. [DIR001, DIR003, DIR004]
- The distance from the A05/A07 block to A03 grew by one step: A05 reached A03 within 1–2 steps before (about 48% / 52%) but within 2–3 steps after (about 47% / 53%), and A07 shows the same one-step shift. [LAG001, LAG002]
- A05 and A07 now sit slightly earlier in the trace (mean normalized position about 0.70 before versus about 0.58 after for both). [POS002, POS003]
- Two indicators show no meaningful change: A04's split between A05 and A07 (about 52/48 in both windows) and the A05–A07 mutual order (they co-occur in all traces, in either order, about 52/48 in both windows); differences this small arise in the large majority of random re-splits. [DIR002, REL004]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that a step A01 now executes in every case between the A05/A07 block and A03: in the earlier window traces ran A04, then A05 and A07 in either order, then A03, whereas in the later window A01 runs once per case, after whichever of A05/A07 comes last and immediately before A03. This is shown directly by A01's successor profile (A01 → A03 on all of its outgoing transitions), by the new relations in which A01 follows A05 and A07 and precedes A03 in 100 in 100 later traces, by A01's fixed late position, and by the one-step increase in the A05→A03 and A07→A03 distances, while the A04 split and the A05/A07 internal order remained unchanged — which rules out a mere reordering of existing activities or a shift in how often existing paths are taken. [OCC001, DIR001, DIR003, DIR004, REL001, REL002, REL003, POS001, LAG001, LAG002, DIR002, REL004]

A competing explanation the evidence cannot rule out is that A01 was already part of the process but simply not observed in the earlier window, since zero participation there only means it did not appear in that sample; additionally, positions and lags are measured in event positions, so no statement about clock-time timing is possible. [OCC001, POS001, LAG001]