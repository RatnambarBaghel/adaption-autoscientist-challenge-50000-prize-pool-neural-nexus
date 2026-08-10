# ==========================================================
# Imports
# ==========================================================

import pandas as pd
from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

REPORTS_PATH = PROJECT_ROOT / "data" / "reports"

COMMON_PATH = PROJECT_ROOT / "src" / "common"


# ==========================================================
# Load CSV
# ==========================================================

df = pd.read_csv(
    REPORTS_PATH / "label_mapping_completed.csv"
)

output_file = COMMON_PATH / "label_mapping.py"


# ==========================================================
# Generate Mapping
# ==========================================================

def generate_mapping():

    lines = []

    lines.append("# ================================================")
    lines.append("# AUTO-GENERATED FILE")
    lines.append("# Do NOT edit manually.")
    lines.append("# Generated from label_mapping_completed.csv")
    lines.append("# ================================================\n")

    lines.append("LABEL_MAPPING = {\n")

    # -----------------------------
    # Loop through every row
    # -----------------------------
    for _, row in df.iterrows():

        dataset = row["Dataset"]
        original = row["Class"]
        standard = row["Standard Label"]

        if pd.isna(standard) or standard == "":
            continue

        lines.append(
            f'    ("{dataset}", "{original}"): "{standard}",'
        )

    # -----------------------------
    # Close dictionary
    # -----------------------------
    lines.append("}")

    # -----------------------------
    # Write file
    # -----------------------------
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("label_mapping.py generated successfully!")


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":
    generate_mapping()
