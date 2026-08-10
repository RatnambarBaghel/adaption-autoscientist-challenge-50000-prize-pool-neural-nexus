import pandas as pd
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORTS_PATH = PROJECT_ROOT / "data" / "reports"

INPUT_FILE = REPORTS_PATH / "dataset_manifest.csv"

OUTPUT_FILE = REPORTS_PATH / "adaptive_dataset.parquet"

# ==========================================================
# Universal Prompt
# ==========================================================

PROMPT = "Identify the crop disease shown in this leaf image."

# ==========================================================
# Create Adaptive Data Parquet
# ==========================================================

def create_adaptive_parquet():

    df = pd.read_csv(INPUT_FILE)

    print(df.columns.tolist())

    df = df.rename(columns={
        "image_path": "image",
        "label": "completion"
    })

    df["prompt"] = PROMPT

    df = df[
        [
            "image",
            "prompt",
            "completion",
            "split"
        ]
    ]

    df.to_parquet(
        OUTPUT_FILE,
        index=False,
        engine="pyarrow"
    )

    print("=" * 60)
    print("Adaptive Data Parquet Created Successfully!")
    print("=" * 60)
    print(f"Total Samples : {len(df)}")
    print(f"Saved to : {OUTPUT_FILE}")
    print("=" * 60)

# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    create_adaptive_parquet()
