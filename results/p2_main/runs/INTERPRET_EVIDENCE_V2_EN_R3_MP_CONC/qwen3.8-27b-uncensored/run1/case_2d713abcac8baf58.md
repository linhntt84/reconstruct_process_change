

### Observed differences

- In the earlier window, A19, A20 and A21 were alternatives: A19 occurred in about 35 in 100 traces, A20 in about 30 in 100, A21 in about 36 in 100, and they almost never co-occurred; in the later window, A19 occurs in about 1 in 100 traces and A20/A21 in about 1 in 200 traces. [OCC001, OCC002, OCC003, REL001, REL002, REL008]
- A26, A27 and A28 were absent in the earlier window, but in the later window they occur in about 100 in 100 traces and about once per trace, with almost no repetition. [OCC004, OCC005, OCC006, POS004, POS005, POS006]
- Among observed outgoing transitions of A44, the earlier window shows about 31 in 100 to A19, 30 in 100 to A21 and 25 in 100 to A20; the later window shows about 31 in 100 to A26, 27 in 100 to A27 and 26 in 100 to A28. [DIR007]
- In the earlier window, A44 precedes A19/A20/A21 when they occur and those activities precede A29; in the later window, A44 precedes A26/A27/A28 in about 99 in 100 traces and A26/A27/A28 precede A29 in about 98-99 in 100 traces, while the A44-to-A29 distance moves from mostly 2 steps to mostly 4 steps. [REL006, REL007, REL012, REL013, REL017, REL018, REL021, REL022, REL024, REL025, REL026, REL027, LAG001]
- A26, A27 and A28 are executed together in the later window: they co-occur in about 100 in 100 traces, and each pair appears in both orders in roughly half of traces, so their internal order is mixed. [REL019, REL020, REL023, DIR004, DIR005, DIR006]
- A29 remains in about 100 in 100 traces in both windows, but its mean event position shifts slightly later, from about 0.40 to 0.44. [POS007]

### Inference

Support level: Supported hypothesis

- The control-flow family contains 48 evidence items, far above the about 1 expected without change, so the differences are not what an unchanged process typically produces. [screening, OCC001, OCC004, DIR007, REL019, LAG001]
- A supported possibility is that, in the later window, the earlier alternative branch A19/A20/A21 after A44 was replaced by a new mandatory cluster A26/A27/A28 before A29: the group A19/A20/A21 went from about 100 in 100 traces as one of the three alternatives to about 2 in 100 traces, while A26/A27/A28 went from absent to present in about 100 in 100 traces. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, REL001, REL002, REL008]
- The placement is directly supported: in the earlier window A44 preceded A19/A20/A21 and those activities preceded A29; in the later window A44's main successors shift to A26/A27/A28, A44 precedes the new cluster, the new cluster precedes A29, the A44-to-A29 distance increases from mostly 2 steps to mostly 4 steps, and A29's mean event position shifts slightly later. [DIR007, REL006, REL007, REL012, REL013, REL017, REL018, REL021, REL022, REL024, REL025, REL026, REL027, LAG001, POS007]
- The new cluster is executed together without a fixed order, which is consistent with a new unordered sub-process rather than a single ordered step. [REL019, REL020, REL023, DIR004, DIR005, DIR006]
- Other differences: the rare later A19/A20/A21 have different successors (A19 to A09/A10, A20 to A45, A21 to A34), but these rest on 1-2 observed outgoing transitions and are not needed for the main replacement hypothesis. [DIR001, DIR002, DIR003]
- Limitation: the evidence contains only control-flow items, and the windows are finite samples, so rare residual occurrences may be sampling noise. [screening, OCC001, OCC002, OCC003, DIR001, DIR002, DIR003]
- Competing explanation: the evidence cannot rule out that the old branch was made optional or suppressed and the new cluster was added independently, rather than a direct replacement of one branch by the other. [OCC001, OCC002, OCC003, OCC004, OCC005, OCC006, LAG001]