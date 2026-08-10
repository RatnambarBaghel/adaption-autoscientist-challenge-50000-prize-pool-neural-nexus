# ==========================================================
# Imports
# ==========================================================

from pathlib import Path
from PIL import Image
import pandas as pd
import shutil
import sys


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "03_rgb_images"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "04_resized_images"
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
# Resize Configuration
# ==========================================================

IMAGE_SIZE = (224, 224)


# ==========================================================
# Resize Images
# ==========================================================

def resize_images():

    resize_report = []

    datasets = get_dataset_folders(INPUT_PATH)

    for dataset_path in datasets:

        dataset_name = dataset_path.name

        resized = 0
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

                            img = img.resize(
                                IMAGE_SIZE,
                                Image.Resampling.BILINEAR
                            )

                            save_path = destination / image_path.name

                            if save_path.suffix.lower() in [".jpg", ".jpeg"]:
                                img.save(save_path, quality=95)
                            else:
                                img.save(save_path)

                        resized += 1

                    except Exception as e:

                        errors += 1

                        print(f"Error: {image_path}")

                        print(e)

        resize_report.append({

            "Dataset": dataset_name,

            "Images Resized": resized,

            "Errors": errors

        })

    # ==========================================================
    # Save Report
    # ==========================================================

    report = pd.DataFrame(resize_report)

    report.to_csv(
        REPORTS_PATH / "resize_report.csv",
        index=False
    )

    print("Image resizing completed successfully!")


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    resize_images()
