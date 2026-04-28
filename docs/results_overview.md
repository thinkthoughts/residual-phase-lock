# Results Overview — Residual Phase Lock

Residual phase-lock detects structure via residuals and stabilizes coherence against drift.

## Core Result

Residual phase-lock provides a general mechanism:

- residuals encode missing structure (01)
- models drift from that structure (02, 05)
- phase-lock correction restores coherence (03, 06)
- residual structure can be learned with bounded correction (04)
- correction strength provides continuous control (07)
- long-horizon state tracking exposes drift over sequence length (08)

## Interpretation

Residual ≠ noise  
Drift ≠ random error  
Phase-lock = structure-aware correction that restores coherence

## Key Metrics

- Residual correlation (04): **0.95** → residual is structured
- RMSE reduction (04): **68.3%** → learned correction generalizes
- Residual structure score (04): **0.80 → 0.18** → structured residual is removed
- Corrected drift (03): **0.000** → phase-lock restores coherence
- Corrected drift (06): **0.000** → phase-lock restores coherence
- Partial phase-lock (07): drift falls from **0.247** at half strength to **0.000** at full strength
- Long-horizon tracking (08): horizon **4 → 128**, baseline drift ends at **0.539**, phase-lock drift ends at **0.000**
- Long-horizon coherence (08): partial drift ends at **0.269**, corrected coherence ends at **1.000**

## Results Table

|   notebook | title                          | metric                                  |       value |
|-----------:|:-------------------------------|:----------------------------------------|------------:|
|         01 | Residuals Are Not Noise        | baseline_rmse                           |   0.717258  |
|         01 | Residuals Are Not Noise        | baseline_r2                             |   0.903452  |
|         01 | Residuals Are Not Noise        | fitted_slope                            |   0.758541  |
|         01 | Residuals Are Not Noise        | fitted_intercept                        |   1.72045   |
|         01 | Residuals Are Not Noise        | residual_hidden_structure_correlation   |   0.923837  |
|         01 | Residuals Are Not Noise        | residual_structure_score                |   0.831504  |
|         01 | Residuals Are Not Noise        | dominant_frequency_1                    |   0.3992    |
|         01 | Residuals Are Not Noise        | dominant_frequency_2                    |   0.998     |
|         01 | Residuals Are Not Noise        | dominant_frequency_3                    |   0.8982    |
|         02 | Topology Drift Demo            | train_accuracy                          |   0.608     |
|         02 | Topology Drift Demo            | test_accuracy                           |   0.5044    |
|         02 | Topology Drift Demo            | train_drift_rate                        |   0.392     |
|         02 | Topology Drift Demo            | test_drift_rate                         |   0.4956    |
|         02 | Topology Drift Demo            | generalization_gap                      |   0.1036    |
|         03 | Phase-Lock Correction Loop     | baseline_accuracy                       |   0.497     |
|         03 | Phase-Lock Correction Loop     | baseline_drift_rate                     |   0.503     |
|         03 | Phase-Lock Correction Loop     | corrected_accuracy                      |   1         |
|         03 | Phase-Lock Correction Loop     | corrected_drift_rate                    |   0         |
|         03 | Phase-Lock Correction Loop     | drift_reduction                         |   0.503     |
|         03 | Phase-Lock Correction Loop     | relative_drift_reduction                |   1         |
|         03 | Phase-Lock Correction Loop     | baseline_coherence_score                |   0.497     |
|         03 | Phase-Lock Correction Loop     | corrected_coherence_score               |   1         |
|         04 | Learned Residual Correction    | baseline_train_rmse                     |   0.591027  |
|         04 | Learned Residual Correction    | corrected_train_rmse                    |   0.196415  |
|         04 | Learned Residual Correction    | baseline_test_rmse                      |   0.566638  |
|         04 | Learned Residual Correction    | corrected_test_rmse                     |   0.179584  |
|         04 | Learned Residual Correction    | test_rmse_reduction                     |   0.387053  |
|         04 | Learned Residual Correction    | relative_test_rmse_reduction            |   0.68307   |
|         04 | Learned Residual Correction    | baseline_test_r2                        |   0.936076  |
|         04 | Learned Residual Correction    | corrected_test_r2                       |   0.993579  |
|         04 | Learned Residual Correction    | residual_corr_train                     |   0.943169  |
|         04 | Learned Residual Correction    | residual_corr_test                      |   0.948973  |
|         04 | Learned Residual Correction    | baseline_test_residual_structure_score  |   0.797906  |
|         04 | Learned Residual Correction    | corrected_test_residual_structure_score |   0.179739  |
|         04 | Learned Residual Correction    | structure_score_reduction               |   0.618167  |
|         04 | Learned Residual Correction    | unstable_polynomial_test_rmse           |   0.311215  |
|         05 | Sequence Topology Drift        | train_accuracy                          |   0.894769  |
|         05 | Sequence Topology Drift        | test_accuracy                           |   0.904571  |
|         05 | Sequence Topology Drift        | train_drift_rate                        |   0.105231  |
|         05 | Sequence Topology Drift        | test_drift_rate                         |   0.0954286 |
|         05 | Sequence Topology Drift        | generalization_gap                      |  -0.0098022 |
|         06 | Sequence Phase-Lock Correction | baseline_train_accuracy                 |   0.909538  |
|         06 | Sequence Phase-Lock Correction | baseline_test_accuracy                  |   0.908     |
|         06 | Sequence Phase-Lock Correction | baseline_test_drift_rate                |   0.092     |
|         06 | Sequence Phase-Lock Correction | corrected_test_accuracy                 |   1         |
|         06 | Sequence Phase-Lock Correction | corrected_test_drift_rate               |   0         |
|         06 | Sequence Phase-Lock Correction | drift_reduction                         |   0.092     |
|         06 | Sequence Phase-Lock Correction | relative_drift_reduction                |   1         |
|         06 | Sequence Phase-Lock Correction | baseline_coherence_score                |   0.908     |
|         06 | Sequence Phase-Lock Correction | corrected_coherence_score               |   1         |
|         07 | Partial Phase-Lock             | baseline_accuracy                       |   0.5054    |
|         07 | Partial Phase-Lock             | baseline_drift_rate                     |   0.4946    |
|         07 | Partial Phase-Lock             | baseline_coherence_score                |   0.5054    |
|         07 | Partial Phase-Lock             | mid_strength                            |   0.5       |
|         07 | Partial Phase-Lock             | mid_strength_accuracy                   |   0.7526    |
|         07 | Partial Phase-Lock             | mid_strength_drift_rate                 |   0.2474    |
|         07 | Partial Phase-Lock             | mid_strength_coherence_score            |   0.7526    |
|         07 | Partial Phase-Lock             | full_strength_accuracy                  |   1         |
|         07 | Partial Phase-Lock             | full_strength_drift_rate                |   0         |
|         07 | Partial Phase-Lock             | full_strength_coherence_score           |   1         |
|         07 | Partial Phase-Lock             | full_relative_drift_reduction           |   1         |
|         08 | Long-Horizon State Tracking    | first_horizon                           |   4         |
|         08 | Long-Horizon State Tracking    | last_horizon                            | 128         |
|         08 | Long-Horizon State Tracking    | baseline_accuracy_first                 |   1         |
|         08 | Long-Horizon State Tracking    | baseline_accuracy_last                  |   0.461333  |
|         08 | Long-Horizon State Tracking    | baseline_accuracy_change                |  -0.538667  |
|         08 | Long-Horizon State Tracking    | baseline_drift_first                    |   0         |
|         08 | Long-Horizon State Tracking    | baseline_drift_last                     |   0.538667  |
|         08 | Long-Horizon State Tracking    | baseline_drift_change                   |   0.538667  |
|         08 | Long-Horizon State Tracking    | partial_drift_last                      |   0.269333  |
|         08 | Long-Horizon State Tracking    | corrected_drift_last                    |   0         |
|         08 | Long-Horizon State Tracking    | corrected_coherence_last                |   1         |
|         08 | Long-Horizon State Tracking    | full_relative_drift_reduction_last      |   1         |

## Notebook Arc

| Notebook | Role |
|---|---|
| 01 | Residuals reveal structure |
| 02 | Topology drift appears |
| 03 | Phase-lock corrects known drift |
| 04 | Learned bounded residual correction generalizes |
| 05 | Sequence topology drift appears |
| 06 | Sequence phase-lock corrects drift |
| 07 | Phase-lock strength controls drift/coherence |
| 08 | Long-horizon state tracking validates drift over sequence length |
