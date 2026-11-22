### Observed differences

- Activity A01 was absent from the earlier window (0 of 200 traces) and appears in every trace of the later window (200 of 200), exactly once per trace, always at the same late position (mean normalized position about 0.83 with no variation). [OCC001, POS001]
- In the later window, A01's only observed outgoing transition is to A03 (in all cases). [DIR001]
- Before, A05 passed control to A03 in about 48 in 100 of its observed outgoing transitions (otherwise to A07), and A07 passed to A03 in about 52 in 100 (otherwise to A05). In the later window, A03 no longer appears as a direct successor of either: A05 now leads to A01 in about 47 in 100 of its transitions and A07 in about 53 in 100, while the A05–A07 transitions continue at similar shares. [DIR003, DIR004, DIR002]
- Before, A01 never co-occurred with any of A02–A07 (each of these appeared without A01 in all 200 traces). In the later window, A01 co-occurs with each of them in all traces, always after A02, A04, A05, A06 and A07, and always before A03. [REL001, REL002, REL003, REL004, REL005, REL006]
- Every measured distance to A03 grew by exactly one step: A04→A03 from 3 to 4 steps, A06→A03 from 4 to 5, A05→A03 from 1–2 to 2–3, and A07→A03 from 1–2 to 2–3. [LAG003, LAG007, LAG006, LAG010]
- The positions of A04, A05, A06 and A07 each shifted slightly earlier (for example A04 from about 0.40 to 0.33, A06 from about 0.20 to 0.17), consistent with one event being inserted near the end of the trace; the execution order of A05 and A07 remains mixed and essentially unchanged (A05 first in about 52 in 100 traces before, about 53 in 100 after). [POS002, POS003, POS004, POS005, REL007]
- The remaining differences are small (about 1 percentage point) shifts in branch shares and lags with low empirical strength (about 0.07, i.e. most random re-splits produce larger differences), typical of sampling noise in stable behaviour. [DIR002, LAG001, LAG002, LAG004, LAG005, LAG008, LAG009]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A01 was added as a new activity, executed exactly once in every case, inserted between the A05/A07 stage and A03: before, whichever of A05 or A07 executed last passed directly to A03, whereas in the later window both pass to A01, and A01 always leads to A03. This rests on direct relational evidence — A01→A03 in all later traces, A03 disappearing from the successors of A05 and A07, and A01 co-occurring with A02–A07 in a fixed order — together with a uniform one-step increase in all distances to A03, A01 appearing in 200 of 200 later traces versus 0 of 200 earlier, and stable behaviour elsewhere (A04's branch split and the A05/A07 order mix unchanged). About 19 items, each larger than roughly 199 of 200 random re-splits, describe this single coherent structure. [OCC001, DIR001, DIR003, DIR004, POS001, REL001, REL002, REL003, REL004, REL005, REL006, LAG003, LAG006, LAG007, LAG010]

Limitations: the windows are finite samples, and zero participation before only means A01 was not observed in that window; the evidence cannot rule out that A01 was already executed earlier but not recorded, or that it replaced some unobserved step between the A05/A07 stage and A03. [OCC001, DIR003, DIR004]

Other differences: none beyond the small (about 1 percentage point) branch-share and lag shifts noted above, which fall within what random re-splits of unchanged behaviour produce. [DIR002, REL007, LAG001, LAG002, LAG004, LAG005, LAG008, LAG009]