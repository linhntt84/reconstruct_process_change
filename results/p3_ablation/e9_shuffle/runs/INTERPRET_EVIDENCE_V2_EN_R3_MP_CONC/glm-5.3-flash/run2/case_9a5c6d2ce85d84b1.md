### Observed differences

- Activity A01 was not observed at all in the earlier window (0 of 200 traces); in the later window it occurs exactly once in every trace (participation about 100 in 100 cases, mean 1.0 occurrences per trace, at a consistent event position). [OCC001, POS001]
- The relationship between A01 and A04 changed completely: in the earlier window A04 was present in all 200 traces while A01 never was (about 200 in 200 cases "A04 only"); in the later window both activities occur together in every trace, always in the order A04 before A01 (about 200 in 200 cases). [REL001]
- The observed outgoing transitions of A04 changed: in the earlier window none were observed (0 of 200), while in the later window all observed transitions from A04 lead directly to A01 (100%). [DIR001]
- A04 itself remained in every trace in both windows; its mean event position shifted slightly earlier, from 1.0 to 0.75, a small shift consistent with A01 being added directly after it. [POS002]

### Inference

Support level: Supported hypothesis

Main hypothesis: a new step A01 was inserted immediately after A04 — in the later window every case executes A04 and then A01, with A01 occurring exactly once per trace, whereas in the earlier window A01 was never observed and A04 had no observed outgoing transition. [OCC001, POS001, REL001, DIR001]

Supporting signs: A01's participation rose from 0 to all 200 traces; the A01–A04 relation moved from "A04 only" in every trace to co-occurrence with A04 before A01 in every trace; A04's successors moved from none observed to A01 in 100% of transitions; and A04's slight position shift fits an insertion right after it. The screening produced 5 qualifying control-flow items where about 0.02 would be expected if nothing had changed, so random sampling is an unlikely explanation for the pattern as a whole. [OCC001, POS001, POS002, REL001, DIR001]

Limitations: all five items describe one underlying trace behaviour, so they are not independent confirmations; and the evidence cannot rule out that A01 already existed as a rare branch in the earlier window (zero participation only means it was not observed there) which then became universal. [OCC001, REL001]

Other differences: none beyond the above; the small position shift of A04 is part of the same picture. [POS002]