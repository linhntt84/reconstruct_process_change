### Observed differences

- In the later window, A15 and A16 each occur more often per trace: mean occurrences per trace for A15 rose from about 1.45 to 1.81, and for A16 from about 1.46 to 1.81; the share of traces with more than one occurrence rose from about 30% to 44% for both. [OCC001, OCC002]
- The outgoing transitions of A16 shifted: the share going to A15 increased from about 30% to 44%, while the share going to A42 decreased from about 37% to 26%; shares to A17 and A18 were roughly stable. [DIR001]
- The distance between A15 and A16 changed: the share of occurrences where A15 is immediately followed by A16 (lag 1) dropped from about 43% to 28%, with small increases at longer lags. [LAG001]

### Inference

Support level: Supported hypothesis

The evidence supports a hypothesis that the process changed in how A15 and A16 are executed: both activities are repeated more often per trace, and the routing from A16 shifted towards A15 and away from A42, while the direct adjacency of A15 followed by A16 became less frequent. The increase in occurrences and the shift in successor distribution are directly observed, and the lag change is consistent with A16 more often preceding A15. The number of evidence items (4) far exceeds the 0.47 expected by chance for control-flow indicators, so this is unlikely to be a sampling artefact. A competing explanation that the changes are independent coincidences is unlikely given the coherence, but the evidence does not reveal the underlying cause or whether other activities are involved.

Other differences: none.