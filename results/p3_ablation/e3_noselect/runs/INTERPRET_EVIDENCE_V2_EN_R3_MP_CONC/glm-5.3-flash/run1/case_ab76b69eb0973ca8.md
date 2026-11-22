### Observed differences

- Activity A08 disappears from the later window: it ran in about 70 in 100 traces before (roughly 1.1 times per trace on average) and in none of the 200 traces after. [OCC007, POS005]
- Before, every observed outgoing transition of A07 (about 219 transitions) went to A08. In the later window, A07's outgoing transitions go instead to A05 (about 39 in 100), A03 (27), A04 (22) and A02 (12). [DIR007]
- A08's own outgoing transitions, previously mainly to A05 (about 36 in 100), A03 (35), A04 (19) and A02 (10), are no longer observed at all. [DIR008]
- Every checked pair involving A08 collapses from frequent co-occurrence to none: A07–A08 co-occurred in about 70 in 100 traces before (A07 first in 46, interleaved/repeated in 25) but never after, with A07 now running without A08 in about 67 in 100 traces; A03–A08, A04–A08 and A05–A08 likewise drop from roughly 29–33 in 100 co-occurring to zero. [REL010, REL004, REL007, REL009]
- A07's former successors now follow it one step sooner: A07→A03 was usually 2 positions apart before (about 59 in 100) and is 1 apart after (about 43); A07→A04 and A07→A05 shorten from lags 2–3 to lags 1–2. [LAG013, LAG014, LAG015]
- Smaller shifts: repeats of A03, A04, A05 and A07 itself now recur at shorter gaps (e.g. A04→A04 moved from mostly 4–5 positions apart to 2–3); most other activities' participation moves by only 2–3 points in either direction, and A04 and A05 appear slightly earlier in the trace (median position down about 0.05). [LAG001, LAG006, LAG011, LAG016, OCC001, OCC003, OCC006, POS002, POS003, POS004]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A08 was removed from, or bypassed in, the process in the later window: A08 ran in about 70 in 100 traces before and in none after, and A07, which previously always handed control to A08, now leads directly to A08's former successors A05, A04, A03 and A02, shortening the loop through A07 by one step. This rests on direct and mutually consistent relational and successor evidence — the complete successor change at A07, the disappearance of A08's outgoing edges, the collapse of all A08 pairs, and the lag shortening from 2 to 1 for A07→successor — and the A08 collapse (141 of 200 traces to 0 of 200) is far larger than differences that random re-splits of unchanged behaviour produce. [OCC007, DIR007, DIR008, REL004, REL007, REL009, REL010, LAG013, LAG014, LAG015]

Limitations: zero participation strictly shows only that A08 was not recorded in the later window, so a drastic reduction or a relabelling of A08 cannot be distinguished from removal with these anonymous codes; the smaller frequency and position shifts could still be sampling variation. [OCC007, POS002, POS003]

Other differences: the shorter repetition gaps for A03, A04, A05 and A07 (e.g. A04→A04 from mostly 4–5 positions apart to 2–3) are consistent with the shortened loop but are not themselves part of the removal hypothesis, and the small participation and position movements of the remaining activities stay within the range expected for unchanged behaviour. [LAG001, LAG006, LAG011, LAG016, OCC001, OCC003, OCC006, POS002, POS003, POS004]