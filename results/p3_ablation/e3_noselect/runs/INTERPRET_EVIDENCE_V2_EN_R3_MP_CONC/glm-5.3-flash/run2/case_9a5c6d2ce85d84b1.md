### Observed differences

- Activity A01 is absent from the earlier window — it appears in 0 of 200 traces — while in the later window it occurs exactly once in every trace (mean 1.0 occurrence per trace, participation 100 in 100 cases). [OCC001]
- In the later window, A01 always sits at the same event position (mean position 1.0 with no variation across traces); in the earlier window there were no observations of it at all. [POS001]
- The relation between A01 and A04 changed completely: earlier, A04 occurred without A01 in all 200 traces (the two never appeared together); later, both occur together in every trace, with A04 before A01 in 100 in 100 cases. [REL001]
- A04's outgoing flow changed: earlier, no outgoing transitions from A04 were observed; later, all 200 observed outgoing transitions of A04 lead to A01. [DIR001]
- A04's own mean event position moved earlier, from 1.0 to 0.75, a pattern consistent with a step having been added after it (positions are event positions, not clock times). [POS002]
- All five items describe one underlying difference rather than independent changes, and each difference is larger than in about 199 of 200 random re-splits of the pooled data. [OCC001, DIR001, POS001, POS002, REL001]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that activity A01 was added as a new, mandatory step executed after A04: in the earlier window, traces contained A04 but never A01, whereas in the later window every trace runs A04 and then A01 exactly once, in that order. The support is direct and consistent: the pair changed from never co-occurring to co-occurring in every trace with a fixed A04-before-A01 order [REL001]; the edge A04 → A01 now carries all of A04's observed outgoing flow [DIR001]; A01's participation rose from 0 to 100 in 100 traces at a constant position [OCC001, POS001]; and A04's position shift is consistent with a step inserted after it [POS002]. Because A01 appears in every after trace and in no before trace, sampling fluctuation or a rare one-window variant is not a plausible explanation, and the pattern is an addition of a step rather than a redistribution of shares between existing paths.

Limitations: zero participation in the earlier window only means A01 was not observed then, so the evidence cannot distinguish a genuinely new activity from a pre-existing optional one that was previously always skipped and is now always executed; and whether A01 is the final step of the trace, rather than merely following A04, rests on event-position evidence, which does not measure clock time.

Other differences: none — the five items all describe the same underlying change and should not be read as independent confirmations of it. [OCC001, DIR001, POS001, POS002, REL001]