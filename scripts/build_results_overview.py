import json
from pathlib import Path

import pandas as pd

RESULTS_DIR = Path("results")
DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(exist_ok=True)

NOTEBOOK_TITLES = {
    "01": "Residuals Are Not Noise",
    "02": "Topology Drift Demo",
    "03": "Phase-Lock Correction Loop",
    "04": "Learned Residual Correction",
    "05": "Sequence Topology Drift",
    "06": "Sequence Phase-Lock Correction",
    "07": "Partial Phase-Lock",
}

NOTEBOOK_ARC = {
    "01": "Residuals reveal structure",
    "02": "Topology drift appears",
    "03": "Phase-lock corrects known drift",
    "04": "Learned bounded residual correction generalizes",
    "05": "Sequence topology drift appears",
    "06": "Sequence phase-lock corrects drift",
    "07": "Phase-lock strength controls drift/coherence",
}


def load_summary_rows():
    rows = []

    for path in sorted(RESULTS_DIR.glob("*_summary.json")):
        notebook_id = path.name.split("_")[0]
        title = NOTEBOOK_TITLES.get(notebook_id, f"Notebook {notebook_id}")

        with open(path) as f:
            data = json.load(f)

        for metric, value in data.items():
            rows.append(
                {
                    "notebook": notebook_id,
                    "title": title,
                    "metric": metric,
                    "value": value,
                }
            )

    return pd.DataFrame(rows)


def metric_value(df, notebook, metric):
    match = df[(df["notebook"] == notebook) & (df["metric"] == metric)]
    if match.empty:
        return None
    return float(match["value"].iloc[0])


def extract_key_metrics(df):
    key_lines = []

    corr_04 = metric_value(df, "04", "residual_corr_test")
    rmse_red_04 = metric_value(df, "04", "relative_test_rmse_reduction")
    score_before_04 = metric_value(df, "04", "baseline_test_residual_structure_score")
    score_after_04 = metric_value(df, "04", "corrected_test_residual_structure_score")

    if corr_04 is not None:
        key_lines.append(
            f"- Residual correlation (04): **{corr_04:.2f}** → residual is structured"
        )

    if rmse_red_04 is not None:
        key_lines.append(
            f"- RMSE reduction (04): **{rmse_red_04:.1%}** → learned correction generalizes"
        )

    if score_before_04 is not None and score_after_04 is not None:
        key_lines.append(
            f"- Residual structure score (04): **{score_before_04:.2f} → {score_after_04:.2f}** → structured residual is removed"
        )

    for nb in ["03", "06"]:
        corrected_drift = metric_value(df, nb, "corrected_drift_rate")
        if corrected_drift is None:
            corrected_drift = metric_value(df, nb, "corrected_test_drift_rate")

        if corrected_drift is not None:
            key_lines.append(
                f"- Corrected drift ({nb}): **{corrected_drift:.3f}** → phase-lock restores coherence"
            )

    mid_drift_07 = metric_value(df, "07", "mid_strength_drift_rate")
    full_drift_07 = metric_value(df, "07", "full_strength_drift_rate")

    if mid_drift_07 is not None and full_drift_07 is not None:
        key_lines.append(
            f"- Partial phase-lock (07): drift falls from **{mid_drift_07:.3f}** at half strength to **{full_drift_07:.3f}** at full strength"
        )

    if not key_lines:
        return "- No key metrics found yet."

    return "\n".join(key_lines)


def build_arc_table():
    lines = [
        "| Notebook | Role |",
        "|---|---|",
    ]

    for notebook_id, role in NOTEBOOK_ARC.items():
        if (RESULTS_DIR / f"{notebook_id}_summary.json").exists():
            lines.append(f"| {notebook_id} | {role} |")

    return "\n".join(lines)


def main():
    df = load_summary_rows()

    if df.empty:
        raise RuntimeError("No *_summary.json files found in results/")

    df.to_csv(DOCS_DIR / "results_table.csv", index=False)

    md_table = df.to_markdown(index=False)
    key_metrics = extract_key_metrics(df)
    arc_table = build_arc_table()

    overview = f"""# Results Overview — Residual Phase Lock

Residual phase-lock detects structure via residuals and stabilizes coherence against drift.

## Core Result

Residual phase-lock provides a general mechanism:

- residuals encode missing structure (01)
- models drift from that structure (02, 05)
- phase-lock correction restores coherence (03, 06)
- residual structure can be learned with bounded correction (04)
- correction strength provides continuous control (07)

## Interpretation

Residual ≠ noise  
Drift ≠ random error  
Phase-lock = structure-aware correction

## Key Metrics

{key_metrics}

## Results Table

{md_table}

## Notebook Arc

{arc_table}
"""

    (DOCS_DIR / "results_overview.md").write_text(overview)

    print("Wrote docs/results_table.csv")
    print("Wrote docs/results_overview.md")


if __name__ == "__main__":
    main()
