### Observed differences

- In the earlier window, A03 was executed exactly once in every trace (200 of 200) and usually opened the case: A03 came before A02 in about 86 in 100 traces, while in the remaining traces A02 came first and led to A03. In the later window, A03 is not observed at all (0 of 200 traces), and A02 now sits at the first position in every trace. [OCC001, POS002, POS003, DIR002, DIR003, REL003]
- In the earlier window, A04 was followed directly by A01 in about 99 in 100 of its outgoing transitions, closing the trace. In the later window, A04 always leads to A07, and A07 always leads to A01; the distance from A04 to A01 grew from one step to two steps in essentially all traces. [DIR004, DIR007, LAG003, POS004]
- A07 was absent from the earlier window (0 of 200 traces) and appears exactly once in every trace of the later window (200 of 200), positioned between A04 and A01; it co-occurs with A01, A02 and A04 in all later traces, running after A02/A04 and before A01. [OCC004, POS005, REL002, REL004, REL007]
- All relations involving A03 collapsed: A01–A03, A02–A03 and A03–A04 co-occurrence fell from essentially every trace earlier to none later, with A01 and A04 now appearing without A03 in all traces. [REL001, REL003, REL005, REL006]
- The choice following A02 shifted slightly: A05 rose from about 47 to 53 in 100 traces and A06 fell from about 54 to 48, and A05/A06 now always lead to A04, whereas earlier a few percent of their transitions led to A03. [OCC002, OCC003, DIR002, DIR005, DIR006]

### Inference

Support level: Supported hypothesis

The evidence supports a structural change in which A03 was removed from the process and a new activity A07 was inserted between A04 and A01. Earlier, every trace contained A03 once — usually as the opening step before A02 — and ended with A04 feeding directly into A01; in the later window A03 never appears, A02 starts every trace, and the closing sequence is A04 → A07 → A01. This is shown directly by the successor profile of A04 (A01 in about 99 in 100 transitions earlier versus A07 in 100 in 100 later), by A07's position and lag profile between A04 and A01, and by A03's participation falling from all 200 traces to none, with every relation involving A03 disappearing in step. With 200 traces per window, a step present in every trace disappearing and a new step appearing in every trace are not what sampling variation between two windows produces. [OCC001, OCC004, DIR003, DIR004, DIR007, POS005, REL005, REL007, LAG003]

The evidence cannot show whether the removal of A03 and the insertion of A07 were one coordinated restructuring or two independent edits, nor can it distinguish a genuine removal of A03 from A03 simply never being triggered in the later window. [OCC001, OCC004]

Other differences: the split between A05 and A06 after A02 moved by about 6 in 100 traces (A05 from 46.5% to 52.5%, A06 from 53.5% to 47.5%); this difference is small and within the range that random re-splits of a stable process produce (empirical strength about 0.72), so it may be sampling noise rather than a routing change. [OCC002, OCC003, DIR002]