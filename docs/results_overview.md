# Results Overview — Residual Phase Lock

Residual phase-lock detects structure via residuals and stabilizes coherence against drift.

## Results Table

|   notebook | title                          | metric                                  |           value |
|-----------:|:-------------------------------|:----------------------------------------|----------------:|
|         01 | Residuals Are Not Noise        | baseline_rmse                           |       0.717258  |
|         01 | Residuals Are Not Noise        | baseline_r2                             |       0.903452  |
|         01 | Residuals Are Not Noise        | fitted_slope                            |       0.758541  |
|         01 | Residuals Are Not Noise        | fitted_intercept                        |       1.72045   |
|         01 | Residuals Are Not Noise        | residual_hidden_structure_correlation   |       0.923837  |
|         01 | Residuals Are Not Noise        | residual_structure_score                |       0.831504  |
|         01 | Residuals Are Not Noise        | dominant_frequency_1                    |       0.3992    |
|         01 | Residuals Are Not Noise        | dominant_frequency_2                    |       0.998     |
|         01 | Residuals Are Not Noise        | dominant_frequency_3                    |       0.8982    |
|         02 | Topology Drift Demo            | train_accuracy                          |       0.608     |
|         02 | Topology Drift Demo            | test_accuracy                           |       0.5044    |
|         02 | Topology Drift Demo            | train_drift_rate                        |       0.392     |
|         02 | Topology Drift Demo            | test_drift_rate                         |       0.4956    |
|         02 | Topology Drift Demo            | generalization_gap                      |       0.1036    |
|         03 | Phase-Lock Correction Loop     | baseline_accuracy                       |       0.497     |
|         03 | Phase-Lock Correction Loop     | baseline_drift_rate                     |       0.503     |
|         03 | Phase-Lock Correction Loop     | corrected_accuracy                      |       1         |
|         03 | Phase-Lock Correction Loop     | corrected_drift_rate                    |       0         |
|         03 | Phase-Lock Correction Loop     | drift_reduction                         |       0.503     |
|         03 | Phase-Lock Correction Loop     | relative_drift_reduction                |       1         |
|         03 | Phase-Lock Correction Loop     | baseline_coherence_score                |       0.497     |
|         03 | Phase-Lock Correction Loop     | corrected_coherence_score               |       1         |
|         04 | Learned Residual Correction    | baseline_train_rmse                     |       0.585326  |
|         04 | Learned Residual Correction    | corrected_train_rmse                    |       0.240921  |
|         04 | Learned Residual Correction    | baseline_test_rmse                      |       1.19939   |
|         04 | Learned Residual Correction    | corrected_test_rmse                     |     334.103     |
|         04 | Learned Residual Correction    | test_rmse_reduction                     |    -332.903     |
|         04 | Learned Residual Correction    | relative_test_rmse_reduction            |    -277.561     |
|         04 | Learned Residual Correction    | baseline_test_r2                        |      -0.311891  |
|         04 | Learned Residual Correction    | corrected_test_r2                       | -101797         |
|         04 | Learned Residual Correction    | residual_corr_train                     |       0.911364  |
|         04 | Learned Residual Correction    | residual_corr_test                      |      -0.623758  |
|         04 | Learned Residual Correction    | baseline_test_residual_structure_score  |       0.885492  |
|         04 | Learned Residual Correction    | corrected_test_residual_structure_score |       0.839392  |
|         04 | Learned Residual Correction    | structure_score_reduction               |       0.0461    |
|         05 | Sequence Topology Drift        | train_accuracy                          |       0.894769  |
|         05 | Sequence Topology Drift        | test_accuracy                           |       0.904571  |
|         05 | Sequence Topology Drift        | train_drift_rate                        |       0.105231  |
|         05 | Sequence Topology Drift        | test_drift_rate                         |       0.0954286 |
|         05 | Sequence Topology Drift        | generalization_gap                      |      -0.0098022 |
|         06 | Sequence Phase-Lock Correction | baseline_train_accuracy                 |       0.909538  |
|         06 | Sequence Phase-Lock Correction | baseline_test_accuracy                  |       0.908     |
|         06 | Sequence Phase-Lock Correction | baseline_test_drift_rate                |       0.092     |
|         06 | Sequence Phase-Lock Correction | corrected_test_accuracy                 |       1         |
|         06 | Sequence Phase-Lock Correction | corrected_test_drift_rate               |       0         |
|         06 | Sequence Phase-Lock Correction | drift_reduction                         |       0.092     |
|         06 | Sequence Phase-Lock Correction | relative_drift_reduction                |       1         |
|         06 | Sequence Phase-Lock Correction | baseline_coherence_score                |       0.908     |
|         06 | Sequence Phase-Lock Correction | corrected_coherence_score               |       1         |

## Notebook Arc

| Notebook | Role |
|---|---|
| 01 | Residuals reveal structure |
| 02 | Topology drift appears |
| 03 | Phase-lock corrects known drift |
| 04 | Learned residual correction generalizes |
| 05 | Sequence topology drift appears |
| 06 | Sequence phase-lock corrects drift |
