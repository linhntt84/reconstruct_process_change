### Observed differences

- Activity A01 was not observed in the earlier window (0 of 200 traces); in the later window it occurs in all 200 traces, exactly once per case, with no repetitions. [OCC001]
- In the later window, A01 always sits at the same late position in the trace (normalised position about 0.83, with no variation across cases); it had no observed position earlier because it never occurred. [POS001]
- In the later window, every observed outgoing transition of A01 goes to A03; earlier, A01 had no observed outgoing transitions. [DIR001]
- Earlier, A02, A03, A04, A05, A06 and A07 each occurred without A01 in 100% of traces; in the later window each co-occurs with A01 in 100% of traces, with A02, A04, A05, A06 and A07 running before A01, and A01 running before A03. [REL001, REL002, REL003, REL004, REL005, REL006]
- Routing into A03 was redirected: earlier, A05's outgoing transitions went to A07 (about 52%) or A03 (about 48%), and A07's went to A03 (about 52%) or A05 (about 48%); in the later window A05 leads to A07 (about 53%) or A01 (about 47%), and A07 leads to A01 (about 53%) or A05 (about 47%). [DIR003, DIR004]
- Measured distances to A03 each grew by one step: A04→A03 from 3 to 4, A06→A03 from 4 to 5, A05→A03 from 1–2 to 2–3, and A07→A03 from 1–2 to 2–3. [LAG003, LAG007, LAG006, LAG010]
- The normalised positions of A04, A05, A06 and A07 each shift slightly earlier (by about 0.03–0.12), consistent with traces now containing one more event while these activities keep their step order. [POS002, POS003, POS004, POS005]
- The rest of the control flow is stable: A04 still splits to A05/A07 at about 52/48, the A05–A07 pair still occurs in both orders at about 52/48, and the other measured lags shift by only about one percentage point with low empirical strength (about 0.07), i.e. within what random re-splits of unchanged data produce. [DIR002, REL007, LAG001, LAG002, LAG004, LAG005, LAG008, LAG009]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new step, A01, was added to the sequence between the A05/A07 block and A03. In the earlier window a case ran A02, A06 and A04 early, then A05 and A07 in either order, with A03 following the pair; in the later window A01 runs once after that block and immediately before A03. The supporting signs are direct and consistent: A01 goes from 0 to 200 of 200 traces at a fixed late position and with a single fixed successor (A01→A03 in 100% of its transitions); A02, A04, A05, A06 and A07 all precede A01 in 100% of later traces; the outgoing transitions of A05 and A07 that previously reached A03 now reach A01; and every measured distance to A03 increases by exactly one step while distances among the other activities stay unchanged. Note that these many items largely re-describe one underlying trace-level difference rather than confirming it independently. [OCC001, POS001, DIR001, DIR003, DIR004, REL001, REL002, REL003, REL004, REL005, REL006, LAG003, LAG006, LAG007, LAG010]

Limitations: positions and lags are measured in event positions, not clock time, so the hypothesis concerns sequence placement only, not timing; and because activity identifiers are anonymous codes, the evidence cannot fully rule out that A01 corresponds to a re-labelled existing step, although no other activity disappeared from the traces. [POS001, POS002, POS003, POS004, POS005, REL001, REL002, REL003, REL004, REL005, REL006]

Other differences: only small fluctuations of about one percentage point in A04's routing split and in the A05–A07 ordering and lags, whose low empirical strength (about 0.07) is consistent with sampling variation rather than change. [DIR002, REL007, LAG001, LAG002, LAG004, LAG005, LAG008, LAG009]