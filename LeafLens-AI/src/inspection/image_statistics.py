import pandas as pd
from pathlib import Path
from PIL import Image
from statistics import mean

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
# Image Statistics
# ==========================================================

def image_statistics():

    report_data = []

    datasets = get_dataset_folders(RAW_DATA_PATH)

    for dataset in datasets:

        print("\n" + "=" * 70)
        print(f"DATASET : {dataset.name}")
        print("=" * 70)

        widths = []
        heights = []
        formats = {}
        modes = {}

        splits = get_split_folders(dataset)

        for split in splits:

            classes = get_class_folders(split)

            for cls in classes:

                image_files = get_image_files(cls)

                for image_path in image_files:

                    try:

                        with Image.open(image_path) as img:

                            width, height = img.size

                            widths.append(width)
                            heights.append(height)

                            formats[img.format] = (
                                formats.get(img.format, 0) + 1
                            )

                            modes[img.mode] = (
                                modes.get(img.mode, 0) + 1
                            )

                    except Exception:
                        continue


        if widths and heights:

            print("\nSummary")
            print("-" * 70)

            print(f"Total Images      : {len(widths)}")

            print(f"Minimum Width     : {min(widths)}")
            print(f"Maximum Width     : {max(widths)}")
            print(f"Average Width     : {mean(widths):.2f}")

            print()

            print(f"Minimum Height    : {min(heights)}")
            print(f"Maximum Height    : {max(heights)}")
            print(f"Average Height    : {mean(heights):.2f}")

            print()

            print(f"Image Formats     : {formats}")
            print(f"Color Modes       : {modes}")


            report_data.append({
                "Dataset": dataset.name,
                "Total Images": len(widths),
                "Min Width": min(widths),
                "Max Width": max(widths),
                "Avg Width": round(mean(widths), 2),
                "Min Height": min(heights),
                "Max Height": max(heights),
                "Avg Height": round(mean(heights), 2),
                "Formats": str(formats),
                "Color Modes": str(modes),
            })

    df = pd.DataFrame(report_data)

    output_file = REPORTS_PATH / "image_statistics.csv"

    df.to_csv(output_file, index=False)

    print(f"\nReport saved to: {output_file}")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    image_statistics()
