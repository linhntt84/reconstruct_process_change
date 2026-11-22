### Observed differences

- In the earlier window, activity A01 was not observed at all (0 of 200 traces); in the later window it occurs in every trace, exactly once per trace (200 of 200 traces, mean 1.0 occurrence, no repetitions) [OCC001].
- The routing out of A05 changed completely: in the earlier window A05 was always followed by A06, while in the later window A05 is always followed by A01, and A01's observed successor is always A06 [DIR001, DIR002].
- A01's relations with the other activities flipped from complete separation to full co-occurrence: before, in 100 in 100 relevant traces A01 was absent while the other activity ran alone; after, A01 co-occurs with each of A02–A06 in 100 in 100 traces, placed after A02, A04 and A05 and before A03 and A06 [REL001, REL002, REL003, REL004, REL005].
- Event positions shifted as expected when one event is added mid-sequence: A04 moved from position 0.25 to 0.2, A05 from 0.5 to 0.4, A06 from 0.75 to 0.8, and A01 appears at 0.6 [POS001, POS002, POS003, POS004].
- Every measured gap between pairs of the original activities grew by exactly one step while their relative order stayed fixed (for example A05→A06 from 1 to 2 steps, A04→A06 from 2 to 3, A02→A03 from 4 to 5) [LAG001, LAG002, LAG003, LAG004, LAG005, LAG006].
- All seventeen items show an empirical strength of about 0.995 (the difference exceeds roughly 995 of 1,000 random re-splits) and each rests on 200 traces per window; they are mutually consistent but largely describe one and the same underlying difference rather than independent changes [OCC001, DIR001, DIR002, POS001, POS004, REL001, REL005, LAG001, LAG006].

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that a new activity, A01, was inserted into the fixed sequence between A05 and A06: traces consistent with A02 → A04 → A05 → A06 → A03 in the earlier window appear as A02 → A04 → A05 → A01 → A06 → A03 in the later window, with A01 executed exactly once in every case. This rests on direct structural evidence: the edge out of A05 was rerouted from A06 to A01 while A01 leads to A06, and A01 sits after A05 and before A06 in 100 in 100 later traces [OCC001, DIR001, DIR002, REL004, REL005].

The insertion reading is consistent across the remaining indicators: A01 co-occurs with all five pre-existing activities in every later trace in exactly the order the insertion implies, every measured pairwise gap among the original activities increased by precisely one step, and the position shifts of A04, A05 and A06 match a sequence growing from five to six events. Because these items largely reflect the same trace behaviour, they should not be counted as independent confirmations [REL001, REL002, REL003, POS001, POS002, POS003, POS004, LAG001, LAG002, LAG003, LAG004, LAG005, LAG006].

Limitations: no screening baseline is included in the evidence, so the number of qualifying items cannot be compared with the number expected if nothing had changed. Also, zero participation in the earlier window strictly establishes only that A01 was not executed there; the evidence cannot rule out that A01 already existed as a possible but never-taken path, although its appearance in all 200 later traces after 0 of 200 makes a pure sampling fluctuation unlikely [OCC001].