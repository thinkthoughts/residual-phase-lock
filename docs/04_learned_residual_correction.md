# Notebook 04 — Learned Residual Correction

## Results

| Metric | Value |
|--------|------:|
| Baseline test RMSE | 0.567 |
| Corrected test RMSE | 0.180 |
| Relative test RMSE reduction | 0.683 |
| Residual correlation test | 0.949 |
| Baseline residual structure score | 0.798 |
| Corrected residual structure score | 0.180 |
| Unstable polynomial test RMSE | 0.311 |

## Figures

![signal_with_hidden_structure](../figures/04_signal_with_hidden_structure.png)

![learned_residual_structure](../figures/04_learned_residual_structure.png)

![heldout_correction](../figures/04_heldout_correction.png)

![rmse_before_after](../figures/04_rmse_before_after.png)

![residuals_before_after](../figures/04_residuals_before_after.png)

![residual_spectrum_before_after](../figures/04_residual_spectrum_before_after.png)

![guardrail_comparison](../figures/04_guardrail_comparison.png)


## Interpretation

```text
residual → learn missing structure
bounded residual learner → correction
coherence stabilizes as structured residual is removed
unbounded residual chasing can destabilize correction
```

