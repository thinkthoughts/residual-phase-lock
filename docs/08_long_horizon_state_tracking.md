# Notebook 08 — Long-Horizon State Tracking

## Results

| Metric | Value |
|--------|------:|
| First horizon | 4.000 |
| Last horizon | 128.000 |
| Baseline accuracy first | 1.000 |
| Baseline accuracy last | 0.461 |
| Baseline drift last | 0.539 |
| Partial drift last | 0.269 |
| Corrected drift last | 0.000 |
| Corrected coherence last | 1.000 |

## Figures

![accuracy_vs_horizon](../figures/08_accuracy_vs_horizon.png)

![drift_vs_horizon](../figures/08_drift_vs_horizon.png)

![coherence_vs_horizon](../figures/08_coherence_vs_horizon.png)

![residual_distribution_by_horizon](../figures/08_residual_distribution_by_horizon.png)


## Interpretation

```text
dynamic state tracking exposes horizon-dependent drift
residuals encode untracked state
phase-lock suppresses drift and stabilizes coherence
```

