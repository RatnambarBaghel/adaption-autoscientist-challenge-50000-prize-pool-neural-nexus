# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
import shutil
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
    / "05_standardized_splits"
)

OUTPUT_PATH = (
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

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
REPORTS_PATH.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Common Utilities
# ==========================================================

sys.path.append(str(PROJECT_ROOT / "src"))

from common.utils import (
    get_dataset_folders,
    get_split_folders,
    get_class_folders,
)

# ==========================================================
# Merge Datasets
# ==========================================================

def merge_datasets():

    merge_report = []

    datasets = get_dataset_folders(INPUT_PATH)

    for dataset_path in datasets:

        dataset_name = dataset_path.name

        copied_images = 0

        split_folders = get_split_folders(dataset_path)

        for split_path in split_folders:

            split_name = split_path.name

            class_folders = get_class_folders(split_path)

            for class_path in class_folders:

                class_name = class_path.name

                destination = (
                    OUTPUT_PATH
                    / split_name
                    / class_name
                )

                destination.mkdir(
                    parents=True,
                    exist_ok=True
                )

                for image_path in sorted(class_path.iterdir()):

                    if not image_path.is_file():
                        continue


                    new_filename = (
                        f"{dataset_name}_{split_name}_{image_path.name}"
                    )

                    shutil.copy2(

                        image_path,

                        destination / new_filename

                    )

                    copied_images += 1


        merge_report.append({

            "Dataset": dataset_name,

            "Images Copied": copied_images

        })



    report = pd.DataFrame(merge_report)

    report.to_csv(

        REPORTS_PATH / "merge_report.csv",

        index=False

    )

    print("Dataset merging completed successfully!")


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    merge_datasets()
