# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
from PIL import Image
import shutil
import pandas as pd


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "02_labels_standardized"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "03_rgb_images"
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

import sys

sys.path.append(str(PROJECT_ROOT / "src"))

from common.utils import (
    get_dataset_folders,
    get_split_folders,
    get_class_folders,
)


# ==========================================================
# Convert Images to RGB
# ==========================================================

def convert_to_rgb():

    conversion_report = []

    datasets = get_dataset_folders(INPUT_PATH)


    for dataset_path in datasets:

        dataset_name = dataset_path.name

        converted = 0
        already_rgb = 0
        errors = 0

        split_folders = get_split_folders(dataset_path)

        for split_path in split_folders:

            split_name = split_path.name

            class_folders = get_class_folders(split_path)

            for class_path in class_folders:

                class_name = class_path.name

                destination = (
                    OUTPUT_PATH
                    / dataset_name
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

                    try:

                       with Image.open(image_path) as img:

                        original_mode = img.mode

                        if original_mode != "RGB":
                            img = img.convert("RGB")

                        img.save(destination / image_path.name, quality=95)

                        if original_mode == "RGB":
                            already_rgb += 1
                        else:
                            converted += 1

                    except Exception as e:

                        errors += 1

                        print(f"Error: {image_path}")
                        print(e)

        conversion_report.append({

            "Dataset": dataset_name,

            "Already RGB": already_rgb,

            "Converted": converted,

            "Errors": errors

        })

    # ==========================================================
    # Save Report
    # ==========================================================

    report = pd.DataFrame(conversion_report)

    report.to_csv(
        REPORTS_PATH / "rgb_conversion_report.csv",
        index=False
    )

    print("RGB conversion completed successfully!")


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    convert_to_rgb()
