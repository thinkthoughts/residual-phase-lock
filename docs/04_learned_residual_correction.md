# Notebook 04 — Learned Residual Correction

## Results

| Metric | Value |
|--------|------:|
| Baseline test RMSE | 1.199 |
| Corrected test RMSE | 334.103 |
| Relative test RMSE reduction | -277.561 |
| Residual correlation test | -0.624 |
| Baseline residual structure score | 0.885 |
| Corrected residual structure score | 0.839 |

## Figures

![signal_with_hidden_structure](../figures/04_signal_with_hidden_structure.png)

![learned_residual_structure](../figures/04_learned_residual_structure.png)

![heldout_correction](../figures/04_heldout_correction.png)

![rmse_before_after](../figures/04_rmse_before_after.png)

![residuals_before_after](../figures/04_residuals_before_after.png)

![residual_spectrum_before_after](../figures/04_residual_spectrum_before_after.png)


## Interpretation

```text
residual → learn missing structure
learned residual → correction
coherence stabilizes without hard-coded constraint
```

