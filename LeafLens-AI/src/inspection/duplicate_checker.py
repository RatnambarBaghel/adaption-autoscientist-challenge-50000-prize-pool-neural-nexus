from pathlib import Path
import hashlib
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
# Duplicate Checker
# ==========================================================

def duplicate_checker():

    report_data = []

    image_hashes = {}

    datasets = get_dataset_folders(RAW_DATA_PATH)

    for dataset in datasets:

        print("\n" + "=" * 70)
        print(f"DATASET : {dataset.name}")
        print("=" * 70)

        duplicate_count = 0

        splits = get_split_folders(dataset)

        for split in splits:

            classes = get_class_folders(split)

            for cls in classes:

                image_files = get_image_files(cls)

                for image_path in image_files:

                    try:

                        with open(image_path, "rb") as f:

                            file_hash = hashlib.sha256(f.read()).hexdigest()

                        if file_hash in image_hashes:

                            duplicate_count += 1

                            report_data.append({
                                "Dataset": dataset.name,
                                "Split": split.name,
                                "Class": cls.name,
                                "Image": str(image_path),
                                "Duplicate Of": image_hashes[file_hash],
                                "SHA256": file_hash,
                            })

                            print(f"[DUPLICATE] {image_path}")

                        else:

                            image_hashes[file_hash] = str(image_path)

                    except Exception:
                        continue

        print("\nSummary")
        print("-" * 70)
        print(f"Duplicate Images : {duplicate_count}")

    df = pd.DataFrame(
            report_data,
            columns=[
                "Dataset",
                "Split",
                "Class",
                "Image",
                "Duplicate Of",
                "SHA256"
            ]
        )

    output_file = REPORTS_PATH / "duplicate_images.csv"

    df.to_csv(output_file, index=False)

    print(f"\nReport saved to: {output_file}")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    duplicate_checker()
