### Observed differences

- In the later window, A30, A31, A36, A37 and A38 still run in every trace, but each is executed about three times per trace instead of about once: mean occurrences rose from roughly 1.0 to roughly 3.1, and about 67 in 100 traces now contain repeats of each activity, versus almost none before. [OCC006, OCC007, OCC008, OCC009, OCC010]
- The fixed sequencing around these activities largely dissolved into interleaving: pairs that previously followed a single order in about 97–100 in 100 traces (for example A14 before A30, or A30 before A46) now do so in only about 32–33 in 100, with about 67 in 100 interleaved or repeated; A38 now leads back to A30 in about 66 in 100 of its outgoing transitions, where before it almost always led to A25. [REL014, REL029, REL034, REL040, DIR007]
- Distances between the repeated activities spread out: A31 was followed by A36 within one to two steps in about 98 in 100 observed cases before, whereas afterwards the distance is dispersed over one to five steps. [LAG005, LAG006, LAG008, LAG010]
- A10 dropped from about 71 in 100 traces to about 25 in 100 and is largely bypassed: A44 now leads to A45 in about 80 in 100 of its outgoing transitions (about 27 before) and rarely to A10 (about 5, versus 72 before), A10's own transitions to A45 fell from about 89 in 100 to about 14 in 100, and when A10 does run it sits much earlier in the trace (median relative position about 0.31 versus 0.90). [OCC005, DIR004, DIR008, POS001, LAG013]
- A02, A04, A06 and A08 became more common, from roughly 5–9 in 100 traces to roughly 18–26 in 100. [OCC001, OCC002, OCC003, OCC004]
- Smaller shifts: A22 runs slightly later and in somewhat fewer traces (about 46 versus 55 in 100), A28 and A30–A38 sit slightly later and more variably, and several A44-outgoing distances shortened by about one step (A44 to A45 now usually one step instead of two). [POS004, POS005, POS006, LAG014, LAG015, LAG016]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that, in the later window, the activities A30, A31, A36, A37 and A38 are repeated about three times per case instead of once, and that the previously fixed ordering between them and neighbouring activities such as A14, A15, A28, A44 and A46 gave way to interleaving. The repetition is measured directly (about 1.0 to about 3.1 executions per trace with participation unchanged at 100 in 100, and repeats in about 67 in 100 traces), and it is corroborated by position distributions spreading across the trace and by fixed-order relations collapsing to about one third while interleaving rises to about two thirds. Chance is an unlikely account of the ensemble: 114 control-flow items qualified against roughly 1.2 expected without change. The added executions also look specific to these five activities rather than a general lengthening of traces, since A14 and A15 still occur in every trace at nearly unchanged positions. [OCC006, OCC007, OCC008, OCC009, OCC010, POS002, POS003, POS006, POS010, REL014, REL034, REL040, DIR007]

Limitations: the evidence cannot show how the repetition is organised (for example whether a loop re-executes the five activities or the extra executions arise some other way), and the interleaving may be a by-product of the repetition rather than an independently loosened ordering constraint; a few lag comparisons rest on only one before-window observation. [LAG002, LAG004, LAG009]

Other differences:

- A10 became rare and is bypassed in most cases, with A44 connecting directly to A45; given the direct predecessor-to-successor rerouting, this reads as A10 becoming skippable rather than a mere re-weighting of existing paths. [OCC005, DIR004, DIR008, POS001, LAG001, LAG013]
- A02, A04, A06 and A08 now appear in roughly three to four times as many traces as before; these smaller participation shifts are the least certain part of the picture. [OCC001, OCC002, OCC003, OCC004]
- A22 occurs slightly later and somewhat less often, and several A44-outgoing distances shortened by about one step. [POS004, LAG014, LAG015, LAG016]