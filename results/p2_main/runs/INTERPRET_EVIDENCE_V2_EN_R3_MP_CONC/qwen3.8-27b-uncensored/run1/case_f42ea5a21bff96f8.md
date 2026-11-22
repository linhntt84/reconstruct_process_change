

### Observed differences

- In the earlier window, A21, A22 and A23 each occurred in about 75 in 100 traces and were often executed together without a fixed order; in the later window, each occurred in about 25 in 100 traces and were mostly absent together. [OCC004, OCC005, OCC006, REL025, REL026, REL034]
- In the earlier window, A24, A25 and A26 each occurred in about 25 in 100 traces and were rarely executed together; in the later window, each occurred in about 75 in 100 traces and were often executed together without a fixed order. [OCC007, OCC008, OCC009, REL049, REL050, REL055]
- A20's observed outgoing transitions shifted from A21, A22 and A23 (about 75 in 100 combined) in the earlier window to A24, A25 and A26 (about 75 in 100 combined) in the later window. [DIR002]
- A19 was before A21, A22 and A23 in about 74-75 in 100 traces in the earlier window, and before A24, A25 and A26 in about 75 in 100 traces in the later window, with co-occurrence shifting in the same direction. [REL013, REL014, REL015, REL016, REL017, REL018]
- A06 occurred in about 17 in 100 traces in the earlier window and about 52 in 100 traces in the later window, and its trace position shifted later, with the median position moving from about 0.48 to about 0.96. [OCC002, POS001]
- In the earlier window, A06 was before A34 and A35 in about 14 and 17 in 100 traces respectively; in the later window, A34 is followed by A06 in about 50 in 100 of A34's observed outgoing transitions, A06 is before A35 in about 48 in 100 traces, the A06-to-A35 distance is 1 in about 97 in 100 observed pairs, and the A34-to-A35 distance shifts from 1 in about 90 in 100 earlier pairs to 2 in about 51 in 100 later pairs. [REL011, REL012, DIR005, DIR001, LAG001, LAG013]
- A06's co-occurrence with A24, A25 and A26 increased from about 5 in 100 traces to about 39-40 in 100 traces, with A24, A25 or A26 before A06 in about 35 in 100 traces in the later window. [REL006, REL007, REL008]
- A02 and A08 became less frequent, from about 17 and 13 in 100 traces to about 7 and 5 in 100 traces. [OCC001, OCC003]

### Inference

Support level: Supported hypothesis

- The main hypothesis is that the shares between two existing alternative middle paths shifted: the path involving A21, A22 and A23 was dominant in the earlier window (about 75 in 100 traces), while the path involving A24, A25 and A26 became dominant in the later window (about 75 in 100 traces), with A20's outgoing transitions and A19's co-occurrence following the same shift. [OCC004, OCC005, OCC006, OCC007, OCC008, OCC009, DIR002, REL013, REL014, REL015, REL016, REL017, REL018, REL019, REL020, REL021, REL022, REL023, REL024, REL027, REL035, REL042]
- The signs are direct and consistent: the activities in both groups are observed in both windows, the groups' internal co-occurrence reverses, the alternative relations between the groups reverse, and 92 control-flow evidence items qualified against about 1 expected without change. [screening, OCC004, OCC005, OCC006, OCC007, OCC008, OCC009, DIR002, REL025, REL026, REL034, REL049, REL050, REL055, REL027, REL035, REL042]
- Other differences: A06 became more frequent and later in the trace, with A34 now often followed by A06 and A06 immediately followed by A35; A06's co-occurrence with A24-A26 increased; A02 and A08 became less frequent. [OCC002, POS001, DIR005, DIR001, LAG001, LAG013, REL011, REL012, REL006, REL007, REL008, OCC001, OCC003]
- This is a supported possibility rather than a confirmed modification because the windows are finite samples, the activity codes are anonymous, the evidence is limited to control-flow indicators, and it does not rule out a change in case mix or that A06's later placement is a separate change. [screening, OCC002, POS001, DIR002, REL013, REL016, REL006]