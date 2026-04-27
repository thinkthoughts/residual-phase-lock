# Notebook 03 — Phase-Lock Correction Loop

## Results

| Metric | Value |
|--------|------:|
| Baseline accuracy | 0.497 |
| Baseline drift rate | 0.503 |
| Corrected accuracy | 1.000 |
| Corrected drift rate | 0.000 |
| Relative drift reduction | 1.000 |
| Corrected coherence score | 1.000 |

## Figures

![phase_lock_sweep](../figures/03_phase_lock_sweep.png)

![before_after_phase_lock](../figures/03_before_after_phase_lock.png)

![residual_distribution_before_after](../figures/03_residual_distribution_before_after.png)

![drift_by_hamming_weight_before_after](../figures/03_drift_by_hamming_weight_before_after.png)


## Interpretation

```text
residual → drift signal
phase-lock → correction loop
coherence stabilizes against drift
```

