import pandas as pd
from pathlib import Path
from PIL import Image

from common.utils import (
    get_dataset_folders,
    get_split_folders,
    get_class_folders,
    get_image_files,
)

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

REPORTS_PATH = PROJECT_ROOT / "data" / "reports"
REPORTS_PATH.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Check Corrupted Images
# ==========================================================

def check_corrupted():

    report_data = []

    datasets = get_dataset_folders(RAW_DATA_PATH)

    for dataset in datasets:

        print("\n" + "=" * 70)
        print(f"DATASET : {dataset.name}")
        print("=" * 70)

        total_images = 0
        corrupted_images = 0

        splits = get_split_folders(dataset)

        for split in splits:

            classes = get_class_folders(split)

            for cls in classes:

                image_files = get_image_files(cls)

                for image_path in image_files:

                    total_images += 1

                    try:
                        with Image.open(image_path) as img:
                            img.verify()

                    except Exception:
                        corrupted_images += 1

                        report_data.append({
                            "Dataset": dataset.name,
                            "Split": split.name,
                            "Class": cls.name,
                            "Image": str(image_path),
                        })

                        print(f"[CORRUPTED] {image_path}")


        print("\nSummary")
        print("-" * 70)
        print(f"Total Images      : {total_images}")
        print(f"Corrupted Images  : {corrupted_images}")


    df = pd.DataFrame(
    report_data,
    columns=[
        "Dataset",
        "Split",
        "Class",
        "Image"
        ]
    )

    output_file = REPORTS_PATH / "corrupted_images.csv"

    df.to_csv(output_file, index=False)

    print(f"\nReport saved to: {output_file}")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    check_corrupted()
