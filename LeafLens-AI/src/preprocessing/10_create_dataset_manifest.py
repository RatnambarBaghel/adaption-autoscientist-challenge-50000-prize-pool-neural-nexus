# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
import pandas as pd
import sys

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "merged"
    / "06_merged_dataset"
)

REPORTS_PATH = (
    PROJECT_ROOT
    / "data"
    / "reports"
)

REPORTS_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================================
# Common Utilities
# ==========================================================

sys.path.append(str(PROJECT_ROOT / "src"))

from common.utils import (
    get_split_folders,
    get_class_folders,
)


# ==========================================================
# Create Dataset Manifest
# ==========================================================

def create_dataset_manifest():

    manifest = []

    split_folders = get_split_folders(INPUT_PATH)

    for split_path in split_folders:

        split_name = split_path.name

        class_folders = get_class_folders(split_path)

        for class_path in class_folders:

            class_name = class_path.name

            for image_path in sorted(class_path.iterdir()):

                if not image_path.is_file():
                    continue

                manifest.append({

                    "image_path": image_path.relative_to(INPUT_PATH).as_posix(),

                    "label": class_name,

                    "split": split_name

                })

    report = pd.DataFrame(manifest)

    report.to_csv(

        REPORTS_PATH / "dataset_manifest.csv",

        index=False

    )

    print("=" * 60)
    print("Dataset Manifest Created Successfully!")
    print("=" * 60)
    print(f"Total Images : {len(report)}")
    print(f"Manifest saved to : {REPORTS_PATH / 'dataset_manifest.csv'}")
    print("=" * 60)


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    create_dataset_manifest()
