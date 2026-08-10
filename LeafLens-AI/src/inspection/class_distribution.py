from pathlib import Path
import pandas as pd

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
# Class Distribution
# ==========================================================

def class_distribution():

    report_data = []

    datasets = get_dataset_folders(RAW_DATA_PATH)

    for dataset in datasets:

        print("\n" + "=" * 70)
        print(f"DATASET : {dataset.name}")
        print("=" * 70)

        total_images = 0
        total_classes = 0

        splits = get_split_folders(dataset)

        for split in splits:

            print(f"\n{split.name}")
            print("-" * 40)

            classes = get_class_folders(split)

            for cls in classes:

                image_count = len(get_image_files(cls))

                total_images += image_count
                total_classes += 1

                print(f"{cls.name:<40} {image_count}")

                report_data.append({
                    "Dataset": dataset.name,
                    "Split": split.name,
                    "Class": cls.name,
                    "Images": image_count,
                })

        print("\nSummary")
        print("-" * 70)
        print(f"Total Classes : {total_classes}")
        print(f"Total Images  : {total_images}")


    df = pd.DataFrame(report_data)

    output_file = REPORTS_PATH / "class_distribution.csv"

    df.to_csv(output_file, index=False)

    print(f"\nReport saved to: {output_file}")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    class_distribution()
