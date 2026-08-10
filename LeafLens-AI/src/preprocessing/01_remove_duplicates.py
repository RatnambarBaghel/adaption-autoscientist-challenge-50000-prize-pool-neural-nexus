from pathlib import Path
import hashlib
import shutil
import pandas as pd

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

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

PROCESSED_ROOT = PROJECT_ROOT / "data" / "processed"

OUTPUT_PATH = PROCESSED_ROOT / "01_duplicates_removed"

REPORTS_PATH = PROJECT_ROOT / "data" / "reports"

LOGS_PATH = PROJECT_ROOT / "data" / "logs"

PROCESSED_ROOT.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
REPORTS_PATH.mkdir(parents=True, exist_ok=True)
LOGS_PATH.mkdir(parents=True, exist_ok=True)


# ==========================================================
# Remove Duplicates
# ==========================================================

def remove_duplicates():

    report_data = []

    image_hashes = {}

    mapping_data = []

    image_counter = 1

    datasets = get_dataset_folders(RAW_DATA_PATH)

    for dataset in datasets:

        print("\n" + "=" * 70)
        print(f"DATASET : {dataset.name}")
        print("=" * 70)

        splits = get_split_folders(dataset)

        for split in splits:

            classes = get_class_folders(split)

            for cls in classes:

                image_files = get_image_files(cls)

                output_class = (
                    OUTPUT_PATH
                    / dataset.name
                    / split.name
                    / cls.name
                )

                output_class.mkdir(
                    parents=True,
                    exist_ok=True
                )

                for image_path in image_files:
                    try:

                        with open(image_path, "rb") as f:

                            file_hash = hashlib.sha256(
                                f.read()
                            ).hexdigest()

                        if file_hash not in image_hashes:

                            image_hashes[file_hash] = str(image_path)

                            extension = image_path.suffix.lower()

                            new_filename = (
                                f"{dataset.name}_"
                                f"{split.name}_"
                                f"{cls.name}_"
                                f"{image_counter:06d}"
                                f"{extension}"
                            )

                            destination = output_class / new_filename

                            shutil.copy2(
                                image_path,
                                destination
                            )

                            mapping_data.append({

                                "Dataset": dataset.name,

                                "Split": split.name,

                                "Class": cls.name,

                                "New Image Name": new_filename,

                                "Original Path": str(image_path)

                            })

                            image_counter += 1

                        else:

                            report_data.append({

                                "Dataset": dataset.name,

                                "Split": split.name,

                                "Class": cls.name,

                                "Duplicate Image": str(image_path),

                                "Original Image": image_hashes[file_hash],

                                "SHA256": file_hash

                            })

                    except Exception:

                        continue

    print("\n" + "=" * 70)
    print("Duplicate Removal Summary")
    print("=" * 70)

    print(f"Unique Images Copied : {len(image_hashes)}")
    print(f"Duplicate Images     : {len(report_data)}")


    df = pd.DataFrame(
        report_data,
        columns=[
            "Dataset",
            "Split",
            "Class",
            "Duplicate Image",
            "Original Image",
            "SHA256",
        ]
    )

    output_file = REPORTS_PATH / "duplicate_removal.csv"

    df.to_csv(output_file, index=False)

    print(f"\nReport saved to: {output_file}")

    mapping_df = pd.DataFrame(
        mapping_data,
        columns=[
            "Dataset",
            "Split",
            "Class",
            "New Image Name",
            "Original Path"
        ]
    )

    mapping_df.to_csv(
        REPORTS_PATH / "image_mapping.csv",
        index=False
    )

    print("Image mapping saved successfully!")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    remove_duplicates()
