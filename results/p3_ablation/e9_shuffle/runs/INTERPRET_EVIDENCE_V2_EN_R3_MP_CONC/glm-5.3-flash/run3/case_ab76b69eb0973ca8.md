### Observed differences

- In the earlier window, A08 appeared in about 70 in 100 traces (about 1.1 occurrences per trace); in the later window it appears in none of the 200 traces. [OCC001, POS001]
- In the earlier window, every observed outgoing transition of A07 (219 in total) went to A08, and A08 in turn led to A05 (about 36 in 100), A03 (about 35 in 100), A04 (about 19 in 100) and A02 (about 10 in 100). In the later window, A08 receives none of A07's 97 observed outgoing transitions; A07 now leads directly to A05 (about 39 in 100), A03 (about 27 in 100), A04 (about 22 in 100) and A02 (about 12 in 100). [DIR001, DIR002]
- All traced relations with A08 collapsed: A07 co-occurred with A08 in about 70 in 100 earlier traces (A07 first in about 46 in 100, interleaved in about 25 in 100) but in the later window appears without A08 in about 67 in 100 and never together with it; A03, A04 and A05 each co-occurred with A08 in roughly 30 in 100 traces earlier (with A08 alone in about 40 in 100), and in the later window co-occurrence is zero, each partner appearing alone in about 33 in 100 traces. A07 itself remains about as frequent, in roughly 67–70 in 100 traces in both windows. [REL004, REL001, REL002, REL003]
- Distances from A07 to its former downstream activities shortened by about one step: A07→A05 moved from lag 2 (about 60 in 100) to lag 1 (about 42 in 100), A07→A04 from lags 2–3 to lags 1–2, and A07→A03 from lag 2 (about 59 in 100) to lag 1 (about 43 in 100). [LAG004, LAG003, LAG002]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A08 is no longer executed in the later window: traces that previously ran A07 followed by A08, with A08 then continuing to A05, A03, A04 or A02, now go from A07 directly to those four activities, and A03, A04 and A05 run without A08. The screening produced 13 qualifying control-flow items where fewer than one (about 0.21) would be expected if nothing had changed, so the pattern as a whole cannot be explained by random re-splits of the two windows. [OCC001, POS001, DIR001, DIR002, REL001, REL002, REL003, REL004, LAG001, LAG002, LAG003, LAG004, LAG005]

Supporting signs: A08's participation falls from about 70 in 100 traces to zero while A07's outflow is rewired from A08 alone to exactly the activities A08 used to feed; all four relations with A08 change from regular co-occurrence to none, with the partners now appearing alone; and every A07→successor distance shortens by about one step, as expected if A08 no longer sits between them. [OCC001, DIR001, DIR002, REL004, REL001, REL002, REL003, LAG002, LAG003, LAG004]

Limitations: zero participation establishes only that A08 was not observed in the later sample, so a complete removal cannot be distinguished from A08 becoming a rare or conditional variant absent from these 200 traces, or from A08 being replaced under a different code; the lag evidence also concerns event positions rather than clock time. [OCC001, LAG003]

Other differences: self-repetition distances shifted earlier — A07→A07 from lags 4–5 to lags 3–4, and A04→A04 from lags 3–5 to lags 2–4, on small supports (about 17–39 traces per window) — which may be a byproduct of the same shortening rather than an independent change. [LAG005, LAG001]