### Observed differences

- In the earlier window, the stretch between A43 and A28 contained exactly one of five alternative activities per case: A14 in about 17 of 100 traces, A17 in about 25, A18 in about 27, A19 in about 14 and A20 in about 19; these shares sum to 1.0 and no two of the five ever occurred in the same trace. [OCC001, OCC004, OCC005, OCC006, OCC007, REL003, REL029, REL037, REL044]
- In that earlier window, A43's outgoing transitions went only to these five activities (with shares matching their frequencies), and each of them led on only to A28. [DIR001, DIR004, DIR005, DIR006, DIR007, DIR011]
- In the later window, none of A14, A17, A18, A19, A20 was observed (0 of 200 traces each), while five previously unobserved activities — A15, A16, A25, A26, A27 — each occurred exactly once in every one of the 200 traces. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, OCC007, OCC008, OCC009, OCC010]
- The five new activities always occur together and in no fixed order: for every pair, both orders appear in nearly equal shares (for example, A15 precedes A16 in about 52 of 100 traces and follows it in about 48). [REL010, REL015, REL016, REL017, REL024, REL025, REL051, REL052, REL055]
- The block is still framed by A43 and A28: A43 precedes each new activity in all 200 traces, each new activity precedes A28 in all 200 traces, and the new activities' observed outgoing transitions go only to one another and to A28 (component shares roughly 0.13–0.27). [REL018, REL019, REL027, REL028, REL053, REL056, REL058, REL059, DIR002, DIR003, DIR008, DIR009, DIR010, DIR011]
- Consistent with the block growing from one activity to five, A28's mean relative position moved later (about 0.39 to about 0.47) and A43's moved earlier (about 0.32 to about 0.29); both still appear in every trace in both windows. [POS011, POS012]

### Inference

Support level: Supported hypothesis

The evidence supports a structural replacement of the segment between A43 and A28: in the earlier window each case executed exactly one of A14, A17, A18, A19, A20 between A43 and A28, whereas in the later window every case executes all five of A15, A16, A25, A26, A27 in that stretch, in no fixed order among themselves, with A43 still before the block and A28 still after it. [OCC001, OCC002, OCC008, DIR011, REL010, REL018, REL019, REL029, REL059]

This is direct and consistent rather than a chance sampling pattern: 92 control-flow items qualified versus roughly 0.72 expected for an unchanged process, the participation changes are maximal (0 versus 1.0 with 200 traces per window), and the relational items show the co-occurrence and ordering change directly rather than inferring it from positions alone. [screening, OCC002, REL010, REL018, REL019]

Limitations: the evidence cannot show whether the five new activities are genuinely new steps or relabelled counterparts of the five old ones, and a mixed order (both orders in similar proportions) cannot distinguish a concurrent block from a sequence whose order simply varies from case to case. [REL010, REL015, REL052]

Other differences: none beyond this restructuring; the position shifts of A28 (later) and A43 (earlier) fit the same change rather than forming a separate difference. [POS011, POS012]