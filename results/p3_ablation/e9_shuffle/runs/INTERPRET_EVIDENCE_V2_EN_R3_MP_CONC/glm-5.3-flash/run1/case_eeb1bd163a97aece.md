### Observed differences

- Activity A01 was absent from the earlier window (0 of 200 traces) and occurs exactly once in every trace of the later window (200 of 200; mean 1.0 occurrence per trace, no repeats within a trace). [OCC001]
- In the earlier window, A05 (event position 0.5) was directly followed by A06 (position 0.75): the pair A05→A06 occurred at a distance of one step in all 200 traces. In the later window, A05 sits earlier (0.4), A06 sits later (0.8), and A01 sits between them (0.6); the A05→A06 distance is now two steps in all traces. [POS002, POS003, POS001, LAG001]
- A05's observed outgoing transitions changed from always leading to A06 to always leading to A01; A01, which had no observed outgoing transitions in the earlier window (consistent with its absence there), now always leads to A06. [DIR002, DIR001]
- The pairwise relations changed accordingly: before, A05 and A06 each always occurred without A01; afterwards, A01 co-occurs with A05 in all traces with A05 first, and with A06 in all traces with A01 first. [REL001, REL002]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A01 was inserted as a new step between A05 and A06: in the earlier window every trace ran A05 directly followed by A06, while in the later window A05 leads to A01, which in turn leads to A06, with A05 shifted one position earlier and A06 one position later. The screening produced 9 qualifying control-flow items where roughly 0.04 would be expected if nothing had changed, and all 9 items describe this single difference consistently; each relation rests on all 200 traces per window, and A01's appearance in 200 of 200 traces after being absent from 200 of 200 makes a rare-variant explanation implausible. [OCC001, POS001, POS002, POS003, DIR001, DIR002, REL001, REL002, LAG001]

Limitations: the evidence covers only the neighbourhood of A05, A01 and A06, so any further effects of the change elsewhere in the process are not visible, and the two windows remain finite samples. The evidence also cannot rule out that the earlier window simply did not sample a pre-existing variant containing A01, although its complete absence from 200 traces weighs against this. [OCC001, REL001, REL002]