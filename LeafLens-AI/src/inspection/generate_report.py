from pathlib import Path
import pandas as pd

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORTS_PATH = PROJECT_ROOT / "data" / "reports"

# ==========================================================
# Generate Final Report
# ==========================================================

def generate_report():

    corrupted = pd.read_csv(REPORTS_PATH / "corrupted_images.csv")

    statistics = pd.read_csv(REPORTS_PATH / "image_statistics.csv")

    classes = pd.read_csv(REPORTS_PATH / "class_distribution.csv")

    duplicates = pd.read_csv(REPORTS_PATH / "duplicate_images.csv")

    total_datasets = statistics["Dataset"].nunique()

    total_images = statistics["Total Images"].sum()

    total_classes = classes["Class"].nunique()

    corrupted_images = len(corrupted)

    duplicate_images = len(duplicates)

    summary = pd.DataFrame({
        "Metric": [
            "Total Datasets",
            "Total Images",
            "Total Classes",
            "Corrupted Images",
            "Duplicate Images"
        ],
        "Value": [
            total_datasets,
            total_images,
            total_classes,
            corrupted_images,
            duplicate_images
        ]
    })

    summary.to_csv(
        REPORTS_PATH / "inspection_summary.csv",
        index=False
    )

    with open(REPORTS_PATH / "inspection_summary.txt", "w") as f:

        f.write("INSPECTION SUMMARY\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Total Datasets    : {total_datasets}\n")
        f.write(f"Total Images      : {total_images}\n")
        f.write(f"Total Classes     : {total_classes}\n")
        f.write(f"Corrupted Images  : {corrupted_images}\n")
        f.write(f"Duplicate Images  : {duplicate_images}\n")


    print("\nInspection report generated successfully!")

    print(f"\nSaved to: {REPORTS_PATH}")

if __name__ == "__main__":
    generate_report()
