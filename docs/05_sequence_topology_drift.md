# Notebook 05 — Sequence Topology Drift

## Results

| Metric | Value |
|--------|------:|
| Train accuracy | 0.895 |
| Test accuracy | 0.905 |
| Train drift rate | 0.105 |
| Test drift rate | 0.095 |
| Generalization gap | -0.010 |

## Figures

![accuracy_vs_drift](../figures/05_accuracy_vs_drift.png)

![drift_by_min_prefix_balance](../figures/05_drift_by_min_prefix_balance.png)

![residual_distribution](../figures/05_residual_distribution.png)

![confusion_matrix](../figures/05_confusion_matrix.png)


## Interpretation

```text
sequence fit ≠ structure preservation
local token features can drift from global nesting
residuals expose sequence topology drift
```

