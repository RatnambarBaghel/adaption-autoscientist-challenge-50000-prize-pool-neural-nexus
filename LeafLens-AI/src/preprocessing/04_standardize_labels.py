# ==========================================================
# Imports
# ==========================================================

import shutil
from pathlib import Path
import pandas as pd
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

from common.utils import (
    get_dataset_folders,
    get_split_folders,
    get_class_folders,
)

from common.label_mapping import LABEL_MAPPING



# ==========================================================
# Project Paths
# ==========================================================


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "01_duplicates_removed"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "02_labels_standardized"
)

REPORTS_PATH = (
    PROJECT_ROOT
    / "data"
    / "reports"
)

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
REPORTS_PATH.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Standardize Labels
# ==========================================================


def standardize_labels():

    mapping_report = []

    datasets = get_dataset_folders(INPUT_PATH)

    for dataset_path in datasets:

        dataset_name = dataset_path.name

        split_folders = get_split_folders(dataset_path)

        for split_path in split_folders:

            split_name = split_path.name

            class_folders = get_class_folders(split_path)

            for class_path in class_folders:

                original_label = class_path.name

                standard_label = LABEL_MAPPING.get(
                    (dataset_name, original_label),
                    original_label
                )

                destination = (
                    OUTPUT_PATH
                    / dataset_name
                    / split_name
                    / standard_label
                )

                destination.mkdir(
                    parents=True,
                    exist_ok=True
                )

                for image in sorted(class_path.iterdir()):

                    if image.is_file():

                        shutil.copy2(
                            image,
                            destination / image.name
                        )


                mapping_report.append({

                    "Dataset": dataset_name,

                    "Split": split_name,

                    "Original Label": original_label,

                    "Standard Label": standard_label

                })


    report = pd.DataFrame(mapping_report)

    report.to_csv(

        REPORTS_PATH / "label_standardization_report.csv",

        index=False

    )

    print("Label standardization completed successfully!")

# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    standardize_labels()
