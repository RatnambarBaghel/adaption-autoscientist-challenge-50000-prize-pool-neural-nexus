# Dataset

This directory contains lightweight metadata and manifest files used to document the LeafLens AI dataset pipeline.

The complete preprocessed agricultural dataset was prepared locally before the competition subset was created. Large image datasets are not stored in this GitHub repository.

## Dataset Pipeline

```text
Full Preprocessed Dataset
87,879 images
        │
        ▼
Competition Subset
5,018 examples
        │
        ▼
Adaptive Data
9,488 adapted examples
        │
        ▼
AutoScientist Training
```

### Full Preprocessed Dataset

The local preprocessing pipeline produced:

| Split      | Classes |     Images |
| ---------- | ------: | ---------: |
| Train      |      62 |     63,677 |
| Validation |      62 |     14,574 |
| Test       |      62 |      9,628 |
| **Total**  |  **62** | **87,879** |


The full image dataset is not included in this repository because of its size.

### Competition Subset

The competition subset documented by manifests/manifest_5018.csv contains 5,018 examples.

| Split      |  Examples |
| ---------- | --------: |
| Train      |     3,673 |
| Validation |       812 |
| Test       |       533 |
| **Total**  | **5,018** |


The manifest contains:

- image_path
- label
- split

Example:

    image_path,label,split
    train/Rice_Bacterial_Leaf_Stripe/...,Rice_Bacterial_Leaf_Stripe,train

### Adaptive Data

The competition data was subsequently processed through Adaption Adaptive Data.

The resulting adapted dataset contained 9,488 examples used for the AutoScientist training workflow.

The adapted dataset is publicly released through Hugging Face and Kaggle rather than stored directly in this repository.

Public Dataset Releases

- Hugging Face: https://huggingface.co/datasets/RatnambarBaghel/adaption-crop-disease-leaf-images-v1
- Kaggle: https://www.kaggle.com/datasets/ratnambarbaghel/adaption-crop-bf0ca919-980a-4865-bbc5-4227737ef45f

### Dataset Sources

The preprocessing pipeline combined agricultural plant-disease image datasets including:

- PlantVillage
- PlantDoc
- Cassava Leaf Disease
- Rice Leaf Disease
- Apple Plant Pathology / Apple Disease data

The datasets were standardized before the competition subset was created.

### Repository Policy

Large datasets, raw images, virtual environments, and generated binary artifacts are intentionally excluded from this GitHub repository.

This directory contains only lightweight metadata required to understand and reproduce the dataset-selection workflow.
