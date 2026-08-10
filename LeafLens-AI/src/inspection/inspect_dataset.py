from pathlib import Path

from common.utils import (
    get_dataset_folders,
    get_split_folders,
    get_class_folders,
    count_images,
)

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

# ==========================================================
# Dataset Inspection
# ==========================================================

def inspect_dataset():

    datasets = get_dataset_folders(RAW_DATA_PATH)

    for dataset in datasets:

        print("\n" + "=" * 70)
        print(f"DATASET : {dataset.name}")
        print("=" * 70)

        dataset_total = 0

        splits = get_split_folders(dataset)

        for split in splits:

            print(f"\nSplit : {split.name}")

            classes = get_class_folders(split)

            print(f"Classes : {len(classes)}")

            split_total = 0

            for cls in classes:

                image_count = count_images(cls)

                split_total += image_count

                print(f"{cls.name:<45} {image_count}")

            dataset_total += split_total

            print("-" * 70)
            print(f"Split Total Images : {split_total}")

        print("=" * 70)
        print(f"Dataset Total Images : {dataset_total}")
        print("=" * 70)


if __name__ == "__main__":
    inspect_dataset()
