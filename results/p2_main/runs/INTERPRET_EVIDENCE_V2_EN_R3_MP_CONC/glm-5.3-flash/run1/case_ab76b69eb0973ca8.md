### Observed differences

- Activity A08 disappeared: earlier it appeared in about 70 in 100 traces (about 1.1 occurrences per trace, very early in the trace, median event position 1); in the later window it was observed in none of the 200 traces. [OCC001, POS001]
- A07's routing changed completely: earlier, all of A07's roughly 219 observed outgoing transitions went to A08; in the later window its roughly 97 observed transitions go directly to A05 (about 39 in 100), A03 (about 27), A04 (about 22) and A02 (about 12), and never to A08. [DIR001]
- A08's own outgoing transitions — earlier mainly to A05 (about 36 in 100) and A03 (about 35), plus A04 (about 19) and A02 (about 10) — are no longer observed. [DIR002]
- A07 and A08 co-occurred earlier in about 70 in 100 traces (A07 before A08 in about 46, interleaved in about 25); in the later window they never co-occur, and A07 appears without A08 in about 67 in 100 traces. [REL004]
- A03, A04 and A05 each co-occurred with A08 earlier in roughly 30 in 100 traces, with A08 also appearing alone in about 38–42 in 100; in the later window co-occurrence with A08 is zero and each of them appears alone in about a third of traces. [REL001, REL002, REL003]
- The distance from A07 to its downstream activities shortened by about one position: A07→A03 was typically 2 positions earlier (about 59 in 100) and is typically 1 position in the later window (about 43 in 100); A07→A04 and A07→A05 show the same shift from about 2–3 positions to about 1–2. [LAG002, LAG003, LAG004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the flow no longer passes through A08: A07, which earlier always reached A05, A03, A04 and A02 by way of A08, now leads directly to those activities, and A08 is no longer executed at all (participation fell from about 70 in 100 traces to 0 of 200). The successor change at A07 and the disappearance of every observed relation involving A08 show this directly, and the one-position shortening of the A07→A03/A04/A05 gaps fits A08 no longer lying between them. Every item's difference exceeds about 199 of 200 random re-splits, and 13 items qualified where about 0.21 would be expected without a change, so chance sampling cannot account for the pattern as a whole. [OCC001, DIR001, DIR002, POS001, REL001, REL002, REL003, REL004, LAG002, LAG003, LAG004]

The evidence shows only that A08 was not observed in the later window; it cannot distinguish a genuine removal from A08 no longer being recorded or being merged into another activity, and it cannot indicate why the routing changed. [OCC001, DIR001]

Other differences: repetitions now occur at shorter intervals — A04→A04 gaps moved from mostly 4–5 positions to 2–3, and A07→A07 gaps from 4–5 to 3–4 — and A07 executes about half as often per trace (about 97 observed outgoing transitions versus about 219, over 200 traces in each window, with its trace participation roughly unchanged at about two-thirds); both fit a shortened loop after the rerouting but are not directly tied to A08 by the evidence. [LAG001, LAG005, DIR001, REL004]