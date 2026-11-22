### Observed differences

- Activity A01 was not observed in the earlier window (0 of 200 traces); in the later window it occurs exactly once in every trace (200 of 200, mean 1.0 occurrence per trace, never repeated within a trace) [OCC001].
- In the later window A01 sits at the end of traces: its median normalised position is 1.0 (mean about 0.94), and it has no observed successor in about 147 of its 200 occurrences, so it ends roughly 3 of 4 traces [POS001, DIR001].
- The relationship of A01 with A05, A06 and A08 flipped from no co-occurrence to full co-occurrence: in the earlier window each of these activities always appeared without A01, while in the later window A08 precedes A01 in all traces, A05 in about 87 of 100 traces and A06 in about 75 of 100 [REL001, REL002, REL003].
- Where A01 has a successor in the later window (53 observed outgoing transitions), it leads to A05 in about 45 in 100 and A06 in about 45 in 100, rarely to A02 or A04 [DIR001].
- A08 lost its terminal role: in the earlier window it had an observed successor in only 75 of 200 traces (ending the trace in roughly 6 of 10 cases, with successors mainly A05, about 51 in 100, and A02, about 24 in 100); in the later window it always has a successor and leads to A01 in about 83 in 100 of its outgoing transitions [DIR008, POS004].
- Late activities shifted earlier in relative position: A05's mean normalised position fell from about 0.52 to 0.44, A06's from about 0.74 to 0.66, and A08's from about 0.87 to 0.77 [POS002, POS003, POS004].
- Gaps after A08 lengthened: A08 followed by A05 within one step fell from about 66 to 33 in 100 (two steps rose from about 34 to 49), and A08 followed by A06 within two steps fell from about 52 to 23 in 100 while three steps rose from about 27 to 46; A05 followed directly by A06 fell from about 76 to 63 in 100 [LAG004, LAG005, LAG001, DIR005].
- A01 also appears as a new, small destination in the later window, receiving about 6 in 100 of A05's outgoing transitions and about 11 in 100 of A06's [DIR005, DIR006].

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 was added to the process and is now executed exactly once per trace at the end: it was absent from all 200 earlier traces, occurs in all 200 later traces, always after A08 and usually after A05 and A06, and typically ends the trace, taking over the terminal role A08 held in roughly 6 of 10 earlier traces [OCC001, POS001, REL001, REL002, REL003, DIR001, DIR008].

The placement signs are direct and mutually consistent: the participation and position of A01 itself, its pairwise relations (from never co-occurring to always co-occurring in a fixed order with A08, A05 and A06), the switch of A08's outgoing transitions to A01, and the downstream consequences — earlier relative positions for A05, A06 and A08, longer gaps from A08 to A05/A06, and A01 appearing as a new successor of A05, A06, A02 and A04 — all point to the same underlying addition near the end of the process [POS002, POS003, POS004, LAG004, LAG005, DIR002, DIR004, DIR005, DIR006].

Limitations: zero participation in the earlier window shows only that A01 was not observed there, so the competing explanation that A01 existed but was missed in that sample cannot be fully ruled out, although its complete absence across 200 traces makes this unlikely; the position and gap indicators measure event order, not clock time, so no statement about timing is possible [OCC001, POS001, LAG004].

Other differences: small redistributions of outgoing shares at A02, A03, A04 and A07 (for example A02 to A07 rising from about 10 to 15 in 100) come with empirical strengths of roughly 0.20–0.66, within the range random re-splits of a stable process produce, and the share of traces in which A05 precedes A08 rose slightly from about 71 to 78 in 100; these are minor and may reflect sampling variation [DIR002, DIR003, DIR004, DIR007, REL004].