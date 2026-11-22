### Observed differences

- In the earlier window, A03 was executed exactly once in every trace (200 of 200) and sat at the very start of traces (median relative position 0); in the later window it is not observed at all (0 of 200). [OCC001, POS002]
- A07 shows the mirror image: not observed earlier, it runs exactly once in every trace in the later window, at a stable position about three quarters into the trace. [OCC002, POS004]
- Routing changed at both ends of the trace. Earlier, A03's outgoing transitions led to A02 in about 86 in 100 cases, with small shares to A06 (about 6 in 100), A05 (about 5 in 100), A04 (about 2 in 100) and A01 (about 1 in 100); in the later window A03 has no observed outgoing transitions. A04, which earlier led to A01 in about 99 in 100 cases, now leads to A07 in every case, and A07 leads to A01 in every case. [DIR001, DIR002, DIR003]
- A02 now opens the traces (median relative position 0.25 earlier, 0 in the later window) and A04 sits earlier (median 0.75 earlier, 0.5 in the later window). [POS001, POS003]
- Co-occurrence with A03 flipped to separation: earlier, A03 appeared together with A01, A02 and A04 in every trace and preceded them (before A01 in about 199 of 200 traces, before A02 in about 86 in 100, before A04 in about 99 in 100); in the later window A01, A02 and A04 always appear without A03. A07 now co-occurs with A01, A02 and A04 in every trace, always after A02 and A04 and before A01. [REL001, REL003, REL005, REL006, REL002, REL004, REL007]
- Distances shifted at the end of the trace: A04 reached A01 in one step in about 99 in 100 traces earlier and now takes two steps, with A07 in between, in all traces; A02 reached A01 in three steps in about 87 in 100 traces earlier and now needs four steps in all traces; the A02→A04 distance stayed at two steps (about 88 in 100 earlier, all traces in the later window). [LAG003, LAG001, LAG002]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility of a structural restructuring involving A03, A02, A04, A07 and A01: in the later window, A03 — previously a mandatory opening activity that passed control to A02 in about 86 in 100 cases — is no longer executed, traces begin with A02, and a new mandatory activity A07 runs between A04 and A01, so the earlier shape A03 → A02 → … → A04 → A01 appears as A02 → … → A04 → A07 → A01. [OCC001, OCC002, DIR001, DIR002, DIR003, POS001, POS003, POS004, REL002, REL004, REL005, REL007, LAG001, LAG003]

The screening qualified 19 control-flow items against roughly 0.13 expected if nothing had changed, so chance sampling cannot account for the ensemble; the change is shown directly by successor, relation, position and distance evidence, all items point to the same restructuring, and the middle segment A02 → A04 (two steps apart) is unchanged between the windows. [DIR002, DIR003, REL004, REL007, LAG001, LAG002, LAG003]

Limitations: the evidence cannot establish whether dropping A03 and inserting A07 were one coordinated redesign or two independent changes, and A03's zero participation only shows it was not observed in the later window; the evidence also says nothing about A05 and A06 or about the activity sitting between A02 and A04, which it does not identify. [OCC001, DIR001]

Other differences: earlier, about 14 in 100 traces routed A03 to a continuation other than A02 (A05 about 5 in 100, A06 about 6 in 100), and about 13 in 100 traces showed a three-step A02→A04 distance; neither is observed in the later window, where A02→A04 is always two steps. [DIR001, LAG002]