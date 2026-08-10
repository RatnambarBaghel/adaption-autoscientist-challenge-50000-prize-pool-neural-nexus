# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
import shutil
import random
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
    / "04_resized_images"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "05_standardized_splits"
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
# Configuration
# ==========================================================

VAL_RATIO = 0.10

TEST_RATIO = 0.10

RANDOM_SEED = 42


# ==========================================================
# Standardize Dataset Splits
# ==========================================================

def standardize_splits():

    random.seed(RANDOM_SEED)

    split_report = []

    datasets = get_dataset_folders(INPUT_PATH)

    for dataset_path in datasets:

        dataset_name = dataset_path.name

        report_entry = {
            "Dataset": dataset_name,
            "Created Validation": "No",
            "Created Test": "No"
        }

        split_folders = get_split_folders(dataset_path)

        split_names = [split.name for split in split_folders]

        # ----------------------------------------------------------
        # Cassava has an unlabeled test/0 folder.
        # Ignore it when deciding whether to create a test split.
        # ----------------------------------------------------------

        if dataset_name == "Cassava":
            split_names = ["train"]

        for split_path in split_folders:

            split_name = split_path.name

            class_folders = get_class_folders(split_path)

            for class_path in class_folders:

                class_name = class_path.name

                images = sorted([
                    img for img in class_path.iterdir()
                    if img.is_file()
                ])

                train_images = images.copy()
                val_images = []
                test_images = []

                if split_name == "train":

                    random.shuffle(train_images)

                    total_images = len(train_images)

                    val_count = 0
                    test_count = 0

                    if "val" not in split_names:
                        val_count = int(total_images * VAL_RATIO)
                        report_entry["Created Validation"] = "Yes"

                    if "test" not in split_names:
                        test_count = int(total_images * TEST_RATIO)
                        report_entry["Created Test"] = "Yes"

                    val_images = train_images[:val_count]

                    test_images = train_images[
                        val_count: val_count + test_count
                    ]

                    train_images = train_images[
                        val_count + test_count:
                    ]


                    for image in train_images:

                        destination = (
                            OUTPUT_PATH
                            / dataset_name
                            / "train"
                            / class_name
                        )

                        destination.mkdir(
                            parents=True,
                            exist_ok=True
                        )

                        shutil.copy2(
                            image,
                            destination / image.name
                        )

                    for image in val_images:

                        destination = (
                            OUTPUT_PATH
                            / dataset_name
                            / "val"
                            / class_name
                        )

                        destination.mkdir(
                            parents=True,
                            exist_ok=True
                        )

                        shutil.copy2(
                            image,
                            destination / image.name
                        )

                    for image in test_images:

                        destination = (
                            OUTPUT_PATH
                            / dataset_name
                            / "test"
                            / class_name
                        )

                        destination.mkdir(
                            parents=True,
                            exist_ok=True
                        )

                        shutil.copy2(
                            image,
                            destination / image.name
                        )

                if split_name == "val":

                    for image in images:

                        destination = (
                            OUTPUT_PATH
                            / dataset_name
                            / "val"
                            / class_name
                        )

                        destination.mkdir(
                            parents=True,
                            exist_ok=True
                        )

                        shutil.copy2(
                            image,
                            destination / image.name
                        )

                if split_name == "test":

                    # Skip unlabeled Cassava competition test set
                    if dataset_name == "Cassava":
                        continue

                    for image in images:

                        destination = (
                            OUTPUT_PATH
                            / dataset_name
                            / "test"
                            / class_name
                        )

                        destination.mkdir(
                            parents=True,
                            exist_ok=True
                        )

                        shutil.copy2(
                            image,
                            destination / image.name
                        )


        split_report.append(report_entry)

    report = pd.DataFrame(split_report)

    report.to_csv(
        REPORTS_PATH / "split_standardization_report.csv",
        index=False
    )

    print("Dataset split standardization completed successfully!")


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    standardize_splits()
