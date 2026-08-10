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
    / "processed"
    / "06_merged_dataset"
)

REPORTS_PATH = (
    PROJECT_ROOT
    / "data"
    / "reports"
)

REPORTS_PATH.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Common Utilities
# ==========================================================

sys.path.append(str(PROJECT_ROOT / "src"))

from common.utils import (
    get_split_folders,
    get_class_folders,
)


# ==========================================================
# Create Final Dataset Report
# ==========================================================

def create_final_dataset():

    final_report = []

    split_folders = get_split_folders(INPUT_PATH)

    for split_path in split_folders:

        split_name = split_path.name

        class_folders = get_class_folders(split_path)

        total_images = 0

        total_classes = 0

        for class_path in class_folders:

            total_classes += 1

            image_count = len([
                img
                for img in class_path.iterdir()
                if img.is_file()
            ])

            total_images += image_count


        final_report.append({

            "Split": split_name,

            "Classes": total_classes,

            "Images": total_images

        })


    report = pd.DataFrame(final_report)

    report.to_csv(

        REPORTS_PATH / "final_dataset_report.csv",

        index=False

    )

    print("=" * 60)
    print("Final Dataset Created Successfully!")
    print("=" * 60)
    print(f"Report saved to : {REPORTS_PATH / 'final_dataset_report.csv'}")
    print("=" * 60)


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    create_final_dataset()
