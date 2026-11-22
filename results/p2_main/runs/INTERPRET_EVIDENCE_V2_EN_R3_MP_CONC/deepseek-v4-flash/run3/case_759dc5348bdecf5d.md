### Observed differences

- In the later window, activities A03 and A11 are absent from all 200 traces, whereas in the earlier window they appeared in about 29% and 20% of traces respectively, with mean occurrences per trace of 1.16 and 0.56. [OCC001, OCC002]
- A03's outgoing transitions (to A12, A19, A06, A11) and A11's outgoing transitions (to A03, A06) disappear entirely. [DIR001, DIR003]
- A06's outgoing transitions shift from mostly A03 (86%) and A11 (7%) in the earlier window to A19 (58%) and A12 (37%) in the later window, with no transitions to A03 or A11. [DIR002]
- A03 no longer co-occurs with A06, A12, or A19; in the earlier window these pairs co-occurred in about 29% of traces, and in the later window A06, A12, and A19 appear alone in about 22% of traces. [REL001, REL003, REL004]
- A12 and A19 appear earlier in traces (mean relative position drops from about 0.33 to 0.23 and from 0.32 to 0.22) and in fewer traces (from 29% to 22%). [POS003, POS004]
- The lags between consecutive occurrences of A06, A12, and A19 shorten: for A06-A06, lag 5 drops from 66% to 3% while lag 4 rises to 52%; for A06-A12, lag 1 rises from 2% to 14%; for A06-A19, lag 1 rises from 2% to 24%; for A12-A12, lag 5 drops from 54% to 11%; for A19-A19, lag 5 drops from 50% to 7%. [LAG001-LAG005]

### Inference

Support level: Supported hypothesis

The evidence supports the hypothesis that the process changed by removing activities A03 and A11, and that the remaining activities A06, A12, and A19 are now executed in a different order, with A06 directly followed by A12 and A19 instead of by A03. This is supported by the complete disappearance of A03 and A11 from all traces, the change in A06's outgoing transitions from A03 to A12/A19, and the shortened lags between A06 and A12/A19. The screening shows 18 control-flow items against 0.22 expected by chance, so the overall difference is not a sampling artifact. The evidence cannot rule out that A03 and A11 still exist but are extremely rare, but the magnitude of the change (from 29% and 20% participation to zero in 200 traces) makes that unlikely.

Other differences: A12 and A19 appear earlier and less frequently, and their repetitions are closer together; these are consistent with the removal of A03 and A11 and the new direct connections.