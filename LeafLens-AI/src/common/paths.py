from pathlib import Path

# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# Input Directories
# ==========================================================

RAW_DATASETS = PROJECT_ROOT / "00_raw_datasets"

DUPLICATES_REMOVED = PROJECT_ROOT / "01_duplicates_removed"

STANDARDIZED_LABELS = PROJECT_ROOT / "02_labels_standardized"

RGB_IMAGES = PROJECT_ROOT / "03_rgb_images"

RESIZED_IMAGES = PROJECT_ROOT / "04_resized_images"

STANDARDIZED_SPLITS = PROJECT_ROOT / "05_standardized_splits"

# ==========================================================
# Output Directories
# ==========================================================

MERGED_DATASET = PROJECT_ROOT / "06_merged_dataset"

REPORTS_PATH = PROJECT_ROOT / "reports"
