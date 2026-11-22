### Observed differences

- Activity A07 was a regular step in the earlier window, appearing in about 53 in 100 traces (106 of 200); in the later window it does not appear in any of the 200 traces. [OCC001, POS002]
- Earlier, A07 was tightly coupled to A03 and A06: A03 and A07 always occurred together (co-occurrence in 53 in 100 traces, never one without the other), A07 typically ran after A03 (A03 first in 24 in 100, interleaved in 29) and before A06 (A07 first in about 21 in 100), and A06 and A07 likewise always co-occurred. [REL001, REL002]
- Earlier, A03 passed control to A07 in about 39 in 100 of its outgoing transitions (about 56 went to A05 and about 5 to A06), and A07 passed control on to A06 in about 92 in 100 of its outgoing transitions. [DIR001, DIR002]
- In the later window, A03 still occurs in about 52 in 100 traces but never together with A07, and its outgoing flow is redistributed: about 49 in 100 go to A05 and about 51 in 100 now go directly to A06, with no transition to A07; A06 appears in about 52 in 100 traces, always without A07. [DIR001, REL001, REL002]
- The A03-to-A06 distance shrank: in the later window about 19 in 100 of the observed A03→A06 pairs are one step apart, whereas earlier the pair was typically two or four steps apart (about 23 and 20 in 100). [LAG001]
- A03's relative position shifted slightly later within traces (median from about 0.39 to about 0.45 of the trace length); these are event positions, not clock times. [POS001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A07 was removed from the process, or is no longer executed: the earlier chain in which A03 led to A07 and A07 led on to A06 was replaced by A03 proceeding directly to A06 (or to A05). The change is shown directly by the collapse of A03–A07 and A06–A07 co-occurrence from 53 in 100 traces to zero, the disappearance of all outgoing transitions from A07, the redirection of A03's flow from A07 to A05 and A06, and the shorter A03-to-A06 distance; the occurrence, direction, relation and lag indicators all agree, and the screening found 8 qualifying control-flow items where about 0.1 would be expected if nothing had changed [OCC001, DIR001, DIR002, REL001, REL002, LAG001]. Limitation: zero participation only means A07 was not observed in the later window, so a residual, very rare execution of A07 cannot be ruled out, and the evidence cannot distinguish a structural removal from the activity simply no longer being recorded [OCC001, POS002].

Other differences: apart from the slight later placement of A03 noted above, which may be related to the same change, the evidence shows no further behavioural differences at the configured thresholds [POS001].