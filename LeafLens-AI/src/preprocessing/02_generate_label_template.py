import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORTS_PATH = PROJECT_ROOT / "data" / "reports"

df = pd.read_csv(
    REPORTS_PATH / "class_distribution.csv"
)

df = df[["Dataset", "Class"]]

df = df.drop_duplicates()

df = df.sort_values(
    by=["Dataset", "Class"]
).reset_index(drop=True)

df["Standard Label"] = ""


output_file = REPORTS_PATH / "label_mapping_template.csv"

df.to_csv(
    output_file,
    index=False
)

print(f"Template saved to:\n{output_file}")
