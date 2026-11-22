### Observed differences

- Activity A02 disappeared from execution: in the earlier window it ran exactly once in every trace (participation 100 in 100 traces, mean 1.0 occurrence per trace); in the later window it appears in 0 of 200 traces. [OCC001]
- Before, A02 was typically the opening event (median position 0) and always passed control on, mainly to A03 (about 48 in 100 outgoing transitions) and A04 (about 42 in 100), with small shares to A05, A06 and A07; in the later window A02 has no observed outgoing transitions at all, simply because it never occurs. [POS001, DIR002]
- Consequently, A03 and A04 moved from always running together with A02 to always running without it: earlier, A02 and A03 co-occurred in all traces (A02 first in 89 in 100) and A02 and A04 likewise co-occurred in all traces (A02 first in 88 in 100); in the later window co-occurrence is zero and each of A03 and A04 occurs alone in every trace. [REL001, REL002]
- A03 and A04 now also start traces: earlier their occurrences began no earlier than about one-sixth into the trace (first quartile about 0.17 for both; A04 median about one-third in), while in the later window at least a quarter of A03 occurrences and at least half of A04 occurrences are the very first event. This reads as a knock-on effect of the missing opening step rather than an independent relocation. [POS002, POS003]
- Small routing shifts elsewhere largely mirror the lost A02 edge: for example, transitions from A04 to A03 rose from about 28 to 36 in 100 while A04's edge to A02 (7 in 100 before) vanished; similar minor shifts appear at A03, A05 and A06. [DIR003, DIR004, DIR005, DIR006]
- A01's outgoing mix is essentially unchanged (A05 about 62 to 64 in 100, A03 about 33 to 36; the small edge to A02, 5 in 100 before, is gone), and with only about 21 versus 28 observed transitions this stays within normal variation. [DIR001]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A02 was removed from the process or has become completely skipped: in the earlier window it was a mandatory step, executed exactly once in each of 200 traces, always at or near the start and followed mainly by A03 or A04; in the later window it is observed in none of 200 traces, while A03 and A04 keep full participation but now execute without A02 and frequently as the first event of the trace. [OCC001, DIR002, POS001, REL001, REL002, POS002, POS003]

Supporting signs: the disappearance is complete rather than partial (100 in 100 versus 0 in 200 traces), it is shown directly by participation, position and relation indicators, and the downstream pattern — an empty transition profile for A02, A03 and A04 starting traces, and the A02 component dropping out of other activities' outgoing profiles — is exactly what removing the first step would produce. [OCC001, DIR002, POS001, REL001, REL002, POS002, POS003, DIR003, DIR004]

Limitations: zero participation only establishes that A02 was not observed in the later window; the evidence cannot distinguish a genuine removal or full skipping of A02 from a change in recording that no longer captures its events. The earlier start positions of A03 and A04 are consequences of the missing opening step, not evidence of an independent move. [OCC001, POS002, POS003]

Other differences:

- The relative order of A03 and A04 tilted from about 53/47 favouring A03-first to about 44/56 favouring A04-first; both orders remain frequent in both windows, so their execution still follows no fixed order. [REL003]
- When A03 precedes A04, the distance is now almost always one or two steps (two steps in about 68 in 100 cases, up from about 56), and three-step gaps no longer occur. [LAG001]
- The reverse distance (A04 before A03) is essentially unchanged. [LAG002]