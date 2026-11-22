### Observed differences

- In the earlier window, A02 appeared in about 46 in 100 traces (roughly once per trace where present); in the later window it was not observed at all. [OCC002]
- A01 shows the mirror image: not observed in the earlier window, it appears in about 51 in 100 traces in the later window, once per trace and never repeated within a trace. [OCC001]
- Both activities sat early in the trace by event position: A02 at a mean relative position of about 0.14 (median about 0.11) in the earlier window, A01 at about 0.19 (median about 0.14) in the later one. [POS001, POS002]
- Their outgoing transitions are broadly similar. Earlier, A02's outgoing transitions went mainly to A03 (about 32%), A06 (about 22%), A11 (about 14%) and A13 (about 11%); later, A01's go to A06 (about 24%), A03 (about 19%), A10 (about 15%), A11 (about 15%) and A13 (about 11%). A02's small edge to A08 (about 1%) has no counterpart for A01. [DIR001, DIR002]
- A03, which appears in every trace in both windows, rerouted one connection: earlier about 7 in 100 of its outgoing edges led to A02, later about 8 in 100 lead to A01, with the rest of its profile nearly unchanged. [DIR003, REL002, REL004]
- Co-occurrence relations mirror the swap. Earlier, A02 co-occurred with A03 in 46 in 100 traces and with A06 in about 26; later, A02 co-occurs with neither, while A01 co-occurs with A03 in about 51 in 100 traces and with A06 in about 26. A01 and A02 never occur in the same trace in either window. [REL001, REL002, REL003, REL004, REL005]

### Inference

Support level: Supported hypothesis

The evidence supports the possibility that A01 took over the role previously played by A02 near the start of the process: in the later window A02 is no longer observed, while A01 appears in about half the traces at a similar early position and connects to largely the same successor activities (A03, A06, A10, A11, A13, A04, A05, A09). [OCC001, OCC002, DIR001, DIR002, POS001, POS002]

The support is direct and consistent: the appearance and disappearance are observed outright; A01's successor profile closely matches A02's former one; A03's outgoing edges switched from A02 to A01; and the co-occurrence relations A02 held with A03 and A06 disappeared exactly as the corresponding relations of A01 appeared. The screening comparison also backs the volume of signal: twelve control-flow items qualified where roughly 0.21 would be expected if nothing had changed, so the set of differences is far larger than random re-splits of a stable process would produce. [DIR003, REL001, REL002, REL003, REL004, REL005]

Limitations: the evidence cannot distinguish a genuine replacement from a relabelling of the same step, since the two activities never appear together and their profiles are similar but not identical (A01 sends relatively less to A03 and more to A10 and A05, and A02's edge to A08 is unmatched). Also, A02's absence in the later window strictly means only that it was not observed there. [DIR001, DIR002, OCC002]

Other differences: within A03's outgoing edges, the shares of the remaining targets shifted slightly (A10 up from about 32% to 37%, A11 down from about 24% to 19%), a small redistribution that may belong to the same rerouting. [DIR003]