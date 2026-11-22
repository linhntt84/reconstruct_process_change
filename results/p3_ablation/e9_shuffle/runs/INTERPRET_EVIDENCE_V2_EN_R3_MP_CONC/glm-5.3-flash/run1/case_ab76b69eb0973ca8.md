### Observed differences

- A08 disappeared from the observed behaviour: earlier it ran in about 71 in 100 traces (about 1.1 executions per trace, almost always at the very start of the case — median position 1); in the later window it is not observed in any of the 200 traces. [OCC001, POS001]
- A07's routing changed completely: earlier, all 219 observed outgoing transitions of A07 went to A08; in the later window none of its 97 observed transitions do, going instead to A05 (about 39 in 100), A03 (about 27), A04 (about 22) and A02 (about 12). [DIR001, DIR002]
- A08's relations collapsed: earlier it co-occurred with A07 in about 70 in 100 traces and with A05, A04 or A03 in about 29–33 in 100; in the later window it co-occurs with none of them, A07 appears without it in about 67 in 100 traces, and A05, A04 and A03 each appear alone in about 32–33 in 100 — down from roughly six in ten traces earlier for each of them. [REL004, REL003, REL002, REL001]
- Downstream work moved closer to A07: A05 now follows A07 one step later in about 42 in 100 observed pairs (earlier typically 2–3 steps), A03 one step later in about 43 in 100 (earlier mostly 2), and A04 at 1–2 steps (earlier 2–3). [LAG004, LAG002, LAG003]
- Repetitions also tightened: A07-to-A07 repetitions moved from 4–5 steps apart to 3–4, and A04-to-A04 from 3–5 to 2–4, though the latter rests on only about 17–18 observed pairs per window. [LAG005, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A08 is no longer executed in the later window: it previously ran in about seven in ten cases and is now absent from all 200 later traces, and the flow that ran through it — A07 always handing over to A08, with A05, A04 and A03 further downstream — now runs directly from A07 to A05, A04, A03 and A02, with those activities following A07 about one step sooner than they followed the old A07→A08 sequence. The signs are direct (occurrence, position and outgoing-transition items all show the disappearance), consistent (all four relation items show co-occurrence with A08 dropping to zero), and the 13 qualifying items far exceed the roughly 0.21 expected by chance in an unchanged process, so the pattern as a whole is not what random sampling produces. [OCC001, POS001, DIR001, DIR002, REL004, REL003, REL002, REL001, LAG004, LAG002, LAG003]

Limitations: zero participation establishes only that A08 was not observed in the later window, so a genuine removal cannot be separated from A08 becoming very rare or all later cases following a variant without it; most items describe the same underlying trace behaviour rather than independent confirmations; and the A04 repetition item rests on few observations. [OCC001, LAG001]