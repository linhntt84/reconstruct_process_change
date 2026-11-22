### Observed differences

- Activity A01 was not observed at all in the earlier window (0 of 200 traces); in the later window it occurs exactly once in every trace (200 of 200, mean 1.0 occurrence per trace, never repeated). [OCC001]
- The outgoing flow of A05 changed completely: earlier, every observed outgoing transition of A05 went to A06; later, every one goes to A01. [DIR002]
- In the later window, all observed outgoing transitions of A01 go to A06. [DIR001]
- A05 and A01: earlier, A05 always occurred without A01; later, the two always co-occur and A05 always comes before A01. [REL001]
- A01 and A06: earlier, A06 always occurred without A01; later, the two always co-occur and A01 always comes before A06. [REL002]
- The distance from A05 to A06 grew from exactly 1 step in all earlier cases to exactly 2 steps in all later cases. [LAG001]
- Positions shifted consistently with one event inserted between A05 and A06: A05's median position moved from 0.5 to 0.4, A06's from 0.75 to 0.8, and A01 sits at 0.6, between them. [POS001, POS002, POS003]
- Every item's difference exceeds those of about 995 in 1000 random re-splits of the pooled traces; however, all items describe the same single underlying difference and are not independent confirmations. [OCC001, DIR001, DIR002, POS001, POS002, POS003, REL001, REL002, LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that a new step, A01, was inserted between A05 and A06. In the earlier window, each trace ran with A05 immediately followed by A06; in the later window, A05 leads to A01 and A01 leads to A06, so A06 now comes two steps after A05, slightly later in the trace (median position 0.75 to 0.8), while A05 comes slightly earlier (0.5 to 0.4). A01 executes exactly once per trace and appears in every later trace after being absent earlier.

The change is shown directly and consistently: the successor data shows A05's outgoing edge switching entirely from A06 to A01 and A01's edge going to A06 [DIR001, DIR002]; the order relations show A05 before A01 and A01 before A06 in all co-occurrences [REL001, REL002]; the A05-to-A06 distance grows from 1 to 2 steps [LAG001]; and the positions of all three activities fit a single inserted event [POS001, POS002, POS003]. All differences are larger than about 995 in 1000 random re-splits.

Limitations: the evidence cannot rule out that A01 was already executed earlier but not recorded in the logs, which would make this a recording change rather than a process change. No screening expectation was provided, so the comparison against chance rests on the directness and consistency of the items rather than on a quantified baseline. The evidence also locates A01 only relative to A05 and A06; its relation to the remaining steps of the trace is not shown.