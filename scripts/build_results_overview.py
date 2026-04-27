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
}

rows = []

for path in sorted(RESULTS_DIR.glob("*_summary.json")):
    notebook_id = path.name.split("_")[0]
    title = NOTEBOOK_TITLES.get(notebook_id, f"Notebook {notebook_id}")

    with open(path) as f:
        data = json.load(f)

    for metric, value in data.items():
        rows.append({
            "notebook": notebook_id,
            "title": title,
            "metric": metric,
            "value": value,
        })

df = pd.DataFrame(rows)
df.to_csv(DOCS_DIR / "results_table.csv", index=False)

# Markdown table
md_table = df.to_markdown(index=False)

overview = f"""# Results Overview — Residual Phase Lock

Residual phase-lock detects structure via residuals and stabilizes coherence against drift.

## Results Table

{md_table}

## Notebook Arc

| Notebook | Role |
|---|---|
| 01 | Residuals reveal structure |
| 02 | Topology drift appears |
| 03 | Phase-lock corrects known drift |
| 04 | Learned residual correction generalizes |
| 05 | Sequence topology drift appears |
| 06 | Sequence phase-lock corrects drift |
"""

(DOCS_DIR / "results_overview.md").write_text(overview)

print("Wrote docs/results_table.csv")
print("Wrote docs/results_overview.md")
