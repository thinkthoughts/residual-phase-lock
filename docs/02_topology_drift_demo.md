# Notebook 02 — Topology Drift Demo

## Results

| Metric | Value |
|--------|------:|
| Train accuracy | 0.608 |
| Test accuracy | 0.504 |
| Train drift rate | 0.392 |
| Test drift rate | 0.496 |
| Generalization gap | 0.104 |

## Figures

![accuracy_vs_drift](../figures/02_accuracy_vs_drift.png)

![drift_by_hamming_weight](../figures/02_drift_by_hamming_weight.png)

![residual_distribution](../figures/02_residual_distribution.png)

![confusion_matrix](../figures/02_confusion_matrix.png)


## Interpretation

```text
accuracy ≠ coherence
local fit → topology drift
residuals expose structural violation
```

