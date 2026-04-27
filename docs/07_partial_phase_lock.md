# Notebook 07 — Partial Phase-Lock

## Results

| Metric | Value |
|--------|------:|
| Baseline accuracy | 0.505 |
| Baseline drift rate | 0.495 |
| Baseline coherence score | 0.505 |
| Mid-strength drift rate | 0.247 |
| Mid-strength coherence score | 0.753 |
| Full-strength drift rate | 0.000 |
| Full-strength coherence score | 1.000 |

## Figures

![drift_coherence_vs_strength](../figures/07_drift_coherence_vs_strength.png)

![accuracy_residual_vs_strength](../figures/07_accuracy_residual_vs_strength.png)

![operating_points](../figures/07_operating_points.png)

![drift_by_hamming_weight_strength](../figures/07_drift_by_hamming_weight_strength.png)

![residual_distribution_by_strength](../figures/07_residual_distribution_by_strength.png)


## Interpretation

```text
phase-lock is a continuous control mechanism
strength controls drift reduction
coherence stabilizes as residual drift decreases
```

