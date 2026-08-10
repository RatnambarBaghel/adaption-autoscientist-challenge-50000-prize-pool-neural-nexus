from pathlib import Path

# Supported image extensions
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp"
}

# Valid dataset splits
VALID_SPLITS = {
    "train",
    "test",
    "val",
    "valid",
    "validation"
}


def is_image_file(file_path: Path) -> bool:
    """Check whether a file is an image."""
    return file_path.suffix.lower() in IMAGE_EXTENSIONS


def get_dataset_folders(raw_path: Path):
    """Return all dataset folders."""
    return sorted(
        folder for folder in raw_path.iterdir()
        if folder.is_dir()
    )


def get_split_folders(dataset_path: Path):
    """
    Return train/val/test folders.
    If none exist, return the dataset itself.
    """

    splits = [
        folder
        for folder in dataset_path.iterdir()
        if folder.is_dir() and folder.name.lower() in VALID_SPLITS
    ]

    if not splits:
        return [dataset_path]

    return sorted(splits)


def get_class_folders(split_path: Path):
    """Return all class folders inside a split."""

    return sorted(
        folder
        for folder in split_path.iterdir()
        if folder.is_dir()
    )


def get_image_files(folder: Path):
    """Return all image files inside a folder."""

    return [
        file
        for file in folder.rglob("*")
        if file.is_file() and is_image_file(file)
    ]


def count_images(folder: Path) -> int:
    """Count image files inside a folder."""

    return len(get_image_files(folder))
