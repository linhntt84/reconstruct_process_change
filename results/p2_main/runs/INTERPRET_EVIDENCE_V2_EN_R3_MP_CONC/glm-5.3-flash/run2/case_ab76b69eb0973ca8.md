### Observed differences

- Activity A08 was present in about 70 in 100 traces in the earlier window (about 1.1 occurrences per trace, repeated within the same trace in roughly a quarter of the traces containing it); in the later window it was not observed in any of the 200 traces. [OCC001]
- When present in the earlier window, A08 appeared early in the trace (median position 1); in the later window there are no occurrences to place. [POS001]
- In the earlier window, every observed outgoing transition of A07 led to A08; in the later window, A07's outgoing transitions go to A05 (about 39 in 100), A03 (about 27), A04 (about 22) and A02 (about 12). [DIR001]
- In the earlier window, A08's outgoing transitions led mainly to A05 (about 36 in 100), A03 (about 35), A04 (about 19) and A02 (about 10); in the later window A08 has no observed outgoing transitions. [DIR002]
- A07 and A08 occurred together in about 70 in 100 traces in the earlier window (A07 before A08 in about 46, interleaved or repeated in about 25); in the later window A07 still occurs in about two thirds of traces but never together with A08. [REL004]
- The pairs A03–A08, A04–A08 and A05–A08 show the same pattern: co-occurrence of about 29–33 in 100 traces before fell to zero, while A03, A04 and A05 now appear alone in about 31–33 in 100 traces. [REL001, REL002, REL003]
- Distances from A07 to its successors shortened by roughly one step: A07→A03 was within 2 steps in about 59 in 100 observations before versus within 1 step in about 43 in 100 after; A07→A05 was mostly 2 steps before (about 60 in 100) and mostly 1 step after (about 42 in 100); A07→A04 sat at 2–3 steps before and 1–2 steps after. [LAG002, LAG003, LAG004]
- Repetition gaps also shortened by about one step: A07→A07 at 4–5 steps before versus 3–4 after, and A04→A04 centred at 4–5 steps before versus 2–4 after. [LAG005, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A08 is no longer executed. In the earlier window, A07 was always followed by A08, which in turn led to A02, A03, A04 or A05; in the later window, A08 is absent from all traces and A07 leads directly to those four activities. The one-step shortening of the distances from A07 to A03, A04 and A05, and of the repetition gaps of A07 and A04, fits the disappearance of this intermediate step. [OCC001, DIR001, DIR002, REL004, LAG002, LAG003, LAG004, LAG005, LAG001]

Supporting signs: thirteen control-flow items qualified against about 0.21 expected if nothing had changed, so chance sampling cannot account for the set as a whole; the change is shown directly by participation (A08 from about 70 in 100 traces to zero), by A07's rerouted successors, and by the collapse of A07–A08 co-occurrence, with the distance shifts all agreeing in direction. [OCC001, DIR001, REL004]

Limitations: zero participation only shows that A08 was not observed, so complete removal cannot be distinguished from A08 becoming very rare; the distance profiles rest on modest counts (roughly 17–47 observations per window), so their exact shapes are indicative rather than precise; and several items describe the same underlying trace behaviour rather than independent confirmations. [LAG001, LAG002, LAG003, LAG004, LAG005]