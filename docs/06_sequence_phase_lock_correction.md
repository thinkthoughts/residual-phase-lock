# Notebook 06 — Sequence Phase-Lock Correction

## Results

| Metric | Value |
|--------|------:|
| Baseline test accuracy | 0.908 |
| Baseline test drift rate | 0.092 |
| Corrected test accuracy | 1.000 |
| Corrected test drift rate | 0.000 |
| Relative drift reduction | 1.000 |
| Corrected coherence score | 1.000 |

## Figures

![before_after_sequence_phase_lock](../figures/06_before_after_sequence_phase_lock.png)

![residual_distribution_before_after](../figures/06_residual_distribution_before_after.png)

![drift_by_min_prefix_before_after](../figures/06_drift_by_min_prefix_before_after.png)

![confusion_matrix_before_after](../figures/06_confusion_matrix_before_after.png)


## Interpretation

```text
sequence topology drift is detectable
phase-lock correction checks global structure
coherence stabilizes against drift
```

