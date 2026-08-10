import os
import shutil
from pathlib import Path

import pandas as pd

# ============================================================
# CONFIGURATION
# ============================================================

# Change this whenever needed
TARGET_IMAGES = 500

MIN_IMAGES_PER_CLASS = 5

PROJECT_ROOT = Path(__file__).resolve().parents[4]

INPUT_MANIFEST = PROJECT_ROOT / "data" / "reports" / "dataset_manifest.csv"

SOURCE_DATASET = PROJECT_ROOT / "data" / "merged" / "06_merged_dataset"

OUTPUT_DATASET = PROJECT_ROOT / "data" / "competition_subset"

RANDOM_STATE = 42

# ============================================================


def copy_image(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main():

    print("=" * 60)
    print("Creating Competition Dataset")
    print("=" * 60)

    df = pd.read_csv(INPUT_MANIFEST)

    total_images = len(df)

    print(f"Original Images : {total_images}")
    print(f"Target Images   : {TARGET_IMAGES}")

    sampled_parts = []

    classes = list(df.groupby("label"))

    num_classes = len(classes)

    # Reserve minimum images for every class
    reserved = MIN_IMAGES_PER_CLASS * num_classes

    remaining = TARGET_IMAGES - reserved

    if remaining < 0:
        raise ValueError("TARGET_IMAGES is too small for the chosen minimum.")

    total_images = len(df)

    for label, class_df in classes:

        # proportional share
        proportional = round((len(class_df) / total_images) * remaining)

        target_class = min(
            len(class_df),
            MIN_IMAGES_PER_CLASS + proportional
        )

        sampled_split = []

        split_groups = class_df.groupby("split")

        for split, split_df in split_groups:

            split_prop = len(split_df) / len(class_df)

            target_split = max(
                1,
                round(target_class * split_prop)
            )

            target_split = min(target_split, len(split_df))

            sampled_split.append(
                split_df.sample(
                    n=target_split,
                    random_state=RANDOM_STATE
                )
            )

        sampled_parts.append(pd.concat(sampled_split))

    subset = pd.concat(sampled_parts)

    # Trim if rounding exceeds target
    if len(subset) > TARGET_IMAGES:
        subset = subset.sample(
            TARGET_IMAGES,
            random_state=RANDOM_STATE
        )

    subset = subset.sample(
        frac=1,
        random_state=RANDOM_STATE
    ).reset_index(drop=True)

    print(f"Final Sample Size : {len(subset)}")

    # ----------------------------------------------------------
    # Copy Images
    # ----------------------------------------------------------

    print("\nCopying Images...\n")

    for _, row in subset.iterrows():

        relative_path = Path(row["image_path"])

        src = SOURCE_DATASET / relative_path
        dst = OUTPUT_DATASET / relative_path

        copy_image(src, dst)

    print("Images copied.")

    # ----------------------------------------------------------
    # Save Manifest
    # ----------------------------------------------------------

    manifest = subset.copy()

    manifest.to_csv(
        OUTPUT_DATASET / "manifest.csv",
        index=False
    )

    print("Manifest saved.")

    # ----------------------------------------------------------
    # Create Adaptive Dataset
    # ----------------------------------------------------------

    adaptive = pd.DataFrame({
        "image": subset["image_path"],
        "prompt": "Identify the crop disease shown in this leaf image.",
        "completion": subset["label"],
        "split": subset["split"]
    })

    adaptive.to_parquet(
        OUTPUT_DATASET / "adaptive_dataset.parquet",
        index=False
    )

    print("Adaptive Parquet created.")

    print("\nDONE")


if __name__ == "__main__":
    main()
