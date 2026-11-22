### Observed differences

- Two activity codes appear only in the later window: A01 and A02 are absent from all 200 earlier traces but occur exactly once in every one of the 200 later traces. [OCC001, OCC002]
- In the later window, A01 runs roughly three quarters of the way through the trace (median position 0.75) and every observed A01 transition leads to A04; A02 is the final event of every later trace (position 1.0 throughout). [POS001, POS002, DIR001]
- Routing into A04 changed: earlier, about 51 in 100 of A06's outgoing transitions went directly to A04, as did about 50 in 100 of A13's; in the later window those direct edges are no longer observed — A06 now leads to A13 (about 52 in 100) or A01 (about 48 in 100), and A13 leads to A01 (about 52 in 100) or A06 (about 48 in 100). [DIR004, DIR007]
- Step distances confirm this rewiring: A06 reaching A04 within one step fell from about 21 in 100 to 0 (the earliest observed distance is now two steps), and the same holds for A13 reaching A04 (about 20 in 100 to 0). [LAG003, LAG005]
- The end of the trace changed: earlier, A12 was always the last event (position 1.0 in every trace, with no outgoing transitions observed); in the later window A12 is followed by A02 in all traces and sits at about position 0.94. [POS005, DIR006, REL008]
- Distances from A06 and from A13 to A12 shifted one step later: two-step gaps (about 33 and 30 in 100) disappeared, with the mass moving to three and four steps. [LAG004, LAG006]
- A04, A06 and A13 now occur slightly earlier relative to trace length (mean positions 0.84 to 0.81, 0.73 to 0.65, and 0.72 to 0.65), while their frequencies stayed flat — A04 still runs about twice per trace in both windows. [POS003, POS004, POS006, OCC004]
- Relationally, A01 and A02 co-occur with A04, A06, A12 and A13 in every later trace but in none of the earlier traces; A01 always precedes A02, A06 and A13 always precede A01, and A12 always precedes A02. [REL001, REL002, REL003, REL004, REL005, REL006, REL007, REL008, REL009]

### Inference

Support level: Supported hypothesis

A hypothesis supported by the evidence is that two activities were added to the process: A01 was inserted between the A06/A13 stage and A04 — earlier, A06 and A13 handed over directly to A04, whereas in the later window they hand to A01, which always precedes A04 — and A02 was appended as a new final step after A12, which previously ended every trace. The support is direct and consistent: the successor changes at A06, A13 and A12 are observed outright, the new codes rise from 0 to 200 of 200 traces, the lag distributions to A04 and A12 shift by exactly one step, and the earlier relative positions of A04, A06 and A13 follow from the insertions; A04's own frequency is unchanged, which fits an insertion rather than a replacement of paths. [DIR001, DIR004, DIR006, DIR007, OCC001, OCC002, OCC004, LAG003, LAG004, LAG005, LAG006, POS003, POS004, POS005, POS006]

An important competing explanation the evidence cannot rule out is relabelling: the codes are anonymous, so A01 and A02 could be renamed versions of steps that existed under other codes before; behaviourally, however, two codes that were never observed now run in every trace and the flow rewires around them. Note also that "absent" earlier strictly means "not observed in that window". [OCC001, OCC002]

Other differences: small frequency and order wobbles that random re-splits of a stable process regularly produce — A03's mean occurrences per trace rose from about 4.06 to 4.24, A07 and A10 from about 2.05 to 2.20 (participation 0.69 to 0.71), and order shares between A04, A06, A12 and A13 moved by 2–3 points; all of these have empirical strengths of roughly 0.08–0.42. [OCC003, OCC006, OCC009, DIR002, REL010, REL011, REL012, REL013, LAG001]