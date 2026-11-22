### Observed differences

- In the earlier window, A05 was executed in every case: it appears in all 200 of 200 traces, about once per trace, early in the flow (mean relative position about 0.25). In the later window, A05 is not observed at all (0 of 200 traces). [OCC001, POS002]
- The flow out of A01 changed completely: before, all of A01's outgoing flow went to A05; in the later window, all of it goes to A02, and A05's own outgoing flow to A02 has disappeared along with A05. [DIR001, DIR002]
- The activity relationships changed accordingly: before, A01 and A05 always occurred together (A01 before A05 in 100 in 100 cases) and A05 and A02 always occurred together (A05 before A02 in 100 in 100 cases); in the later window, A05 co-occurs with neither, and A01 and A02 each appear without it in 100 in 100 cases. [REL001, REL002]
- As a result, A02 now follows A01 immediately (a gap of one step in essentially all cases, versus two steps before) and sits earlier in the trace (mean relative position about 0.33 versus about 0.50). [LAG001, POS001]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that A05 was dropped from the flow between A01 and A02: A05 was a mandatory step, executed in every earlier case in the sequence A01 → A05 → A02, and in the later window it is no longer executed, with A01 leading directly to A02. The support is direct and consistent: A05's participation fell from all cases to none, A01's successor changed from A05 to A02, A05's co-occurrence with both A01 and A02 collapsed to zero, and the A01→A02 gap and A02's position shifted by exactly the amount expected if one intervening step disappeared; every item's difference also exceeds about 995 of 1000 random re-splits of the pooled data. These items describe one underlying difference rather than independent confirmations. [OCC001, DIR001, DIR002, POS002, REL001, REL002, LAG001, POS001]

Limitations: zero participation only shows that A05 was not observed in the later window, so the evidence cannot distinguish a permanent removal from A05 becoming an optional step that was not taken in this sample, nor rule out that A05 was replaced by an activity outside the analysed set; positions and gaps are based on event order, not clock time. [OCC001, POS002, LAG001]