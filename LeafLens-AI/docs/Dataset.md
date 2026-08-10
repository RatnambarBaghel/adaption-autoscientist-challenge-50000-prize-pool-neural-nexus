# 📊 LeafLens AI — Dataset

## 1. Dataset Overview

LeafLens AI uses a multi-source agricultural leaf-image dataset for crop disease identification.

The dataset combines images from several publicly available crop-disease datasets covering multiple crops and disease conditions. The purpose of combining these sources was to create a broader and more diverse training set than relying on a single dataset.

The major source datasets used in the project include:

- PlantVillage
- PlantDoc
- Cassava Leaf Disease
- Rice Leaf Disease
- Apple / Plant Pathology

The combined data contains both **healthy leaves and diseased leaves**, allowing the model to learn disease-specific visual patterns as well as healthy crop conditions.

The dataset was prepared and standardized before being submitted to Adaption's **Adaptive Data** platform for further data optimization and model training.

---


## 2. Dataset Statistics

The project uses multiple dataset stages. To keep the experiment reproducible and avoid confusing the original data with Adaption's transformed output, the dataset stages are documented separately.

### 2.1 Prepared Dataset

The original agricultural datasets were inspected, cleaned, standardized, and prepared before the AutoScientist experiment.

The preprocessing-stage dataset contained:

- **Total images:** 94,929
- **Source datasets:** PlantVillage, PlantDoc, Cassava Leaf Disease, Rice Leaf Disease, and Apple / Plant Pathology
- **Data type:** Crop leaf images
- **Labels:** Crop disease / healthy condition
- **Splits:** Train, validation, and test

The preprocessing pipeline was used to create a consistent and higher-quality dataset for downstream experimentation.

### 2.2 AutoScientist Experiment Dataset

A curated **5,022-row dataset** was subsequently prepared for the AutoScientist experiment and submitted to Adaption's Adaptive Data platform.

This dataset formed the starting point for the specific training experiment documented in this repository.

### 2.3 Adaptive Data Output

Adaption's Adaptive Data platform transformed the 5,022-row experiment dataset into an adapted dataset containing:

- **Adapted dataset size:** 9,488 rows
- **Language:** English
- **Domain:** Agriculture
- **Task:** Crop disease identification from leaf images

The resulting adapted dataset was used as the training data for the AutoScientist model.

### Dataset Flow

```text
94,929-image preprocessing dataset
              │
              ▼
     Curated 5,022-row dataset
              │
              ▼
        Adaptive Data
              │
              ▼
     9,488-row adapted dataset
              │
              ▼
        AutoScientist

```

---

## 3. Preprocessing Pipeline

The original agricultural datasets contained differences in image format, labels, directory structure, dataset splits, and data quality.

A preprocessing pipeline was therefore used to standardize the data before creating the dataset used for the AutoScientist experiment.

### 3.1 Dataset Inspection

Each source dataset was inspected to understand:

- Dataset structure
- Available crops and disease classes
- Number of images
- Existing train, validation, and test splits
- Missing or inconsistent labels
- Image formats
- Potential data-quality issues

### 3.2 Image Validation

Images were checked for readability and basic integrity before being included in the processed dataset.

Corrupted or unreadable images were identified so they would not introduce invalid samples into the training pipeline.

### 3.3 Duplicate Removal

Duplicate images were detected and removed from the combined dataset.

This step reduced repeated samples and helped prevent duplicated images from artificially influencing model training and evaluation.

### 3.4 Label Standardization

Different source datasets used different naming conventions for crops and diseases.

Labels were standardized into a consistent naming scheme so that equivalent disease classes could be represented consistently across datasets.

A label-mapping process was used to maintain the relationship between the original labels and the standardized labels.

### 3.5 RGB Conversion

Images were converted to a consistent RGB representation.

This reduced differences caused by varying image modes and ensured that the processed images followed a consistent input format.

### 3.6 Dataset Split Standardization

The datasets were standardized into consistent:

- Training
- Validation
- Test

splits.

A consistent splitting strategy was applied where required so that the final dataset structure could be used reliably during model training and evaluation.

### 3.7 Class Balancing

Class distributions were analyzed after preprocessing.

The dataset was balanced to reduce excessive representation of individual classes and provide a more useful distribution for crop-disease model training.

### 3.8 Final Prepared Dataset

After preprocessing, validation, deduplication, label standardization, RGB conversion, splitting, and balancing, the resulting data was used to create the curated dataset for the AutoScientist experiment.

The curated experiment dataset contained **5,022 rows** before being processed by Adaption's Adaptive Data platform.

---

## 4. Label Standardization

The source datasets used different naming conventions for crops and disease classes. Before creating the final training data, these labels were standardized into a consistent representation.

### 4.1 Why Label Standardization Was Required

Different datasets may represent the same or related conditions using different naming formats.

Examples of possible differences include:

- Different capitalization
- Different spacing or separators
- Dataset-specific naming conventions
- Crop names included in some labels but not others
- Different representations of healthy conditions

Without standardization, these variations can cause the same semantic class to be treated as separate classes during training.

### 4.2 Label Mapping

A label-mapping process was created to maintain a consistent relationship between:

```text
Original Dataset Label
          │
          ▼
Standardized Crop / Disease Label

```

The mapping was maintained separately so that the original dataset labels could be traced back to their standardized representation.

### 4.3 Standardized Labels

The standardized labels were used throughout the processed dataset so that:

Equivalent labels follow a consistent naming convention.
Crop and disease information remains identifiable.
Class distribution can be analyzed consistently.
The resulting dataset is easier to use for Adaptive Data and AutoScientist.

### 4.4 Reproducibility

The label-standardization process and mapping information are documented separately from the raw datasets.

This allows the standardized dataset to be reproduced without modifying the original source data.


---

## 5. Dataset Preparation for AutoScientist

After completing the preprocessing and label-standardization stages, a curated dataset was prepared for the AutoScientist experiment.

### 5.1 Curated Experiment Dataset

The curated experiment dataset contained:

- **5,022 rows**
- Leaf-image-based crop disease examples
- Crop and disease information
- Healthy and diseased conditions
- English-language training prompts and completions

The dataset was structured so that each example could be processed by Adaption's Adaptive Data platform and subsequently used for AutoScientist training.

### 5.2 Training Data Format

The experiment data was represented as prompt-completion examples suitable for multimodal model training.

Conceptually, each example contains:

```text
Leaf Image
    +
Disease Identification Prompt
    │
    ▼
Expected Crop / Disease Answer

```

This format allows the vision-language model to associate visual characteristics of a leaf with the corresponding crop-disease condition.

### 5.3 Data Quality

Before submission to Adaptive Data, the curated dataset was checked for consistency with the intended crop-disease identification task.

The preparation process focused on:

Consistent labels
Valid image examples
Relevant crop-disease information
Appropriate training structure
Reduction of duplicated or inconsistent samples

### 5.4 Adaptive Data Input

The resulting 5,022-row curated dataset was submitted to Adaption's Adaptive Data platform.

Adaptive Data subsequently produced the adapted dataset used for AutoScientist training.

The adapted dataset contained 9,488 rows.

Curated dataset
5,022 rows
      │
      ▼
Adaptive Data
      │
      ▼
Adapted dataset
9,488 rows

---

## 6. Adaptive Data

The curated 5,022-row dataset was submitted to Adaption's **Adaptive Data** platform for further data optimization.

Adaptive Data processed the experiment dataset and generated an adapted dataset that was subsequently used for AutoScientist training.

### 6.1 Adapted Dataset

The resulting Adaptive Data dataset contained:

- **9,488 rows**
- **Language:** English
- **Domain:** Agriculture
- **Task:** Crop disease identification
- **Input:** Leaf images and disease-identification prompts
- **Output:** Crop / disease diagnosis

### 6.2 Data Quality Improvement

According to the Adaptive Data evaluation shown on the Adaption platform, the adapted dataset achieved a **30% relative improvement in the platform's text-quality measure**, increasing the reported score from **5.0 to 6.5**.

The platform also reported:

- **Before grade:** C
- **After grade:** C
- **Before percentile:** 7.8
- **After percentile:** 8.4

These metrics describe the Adaptive Data quality evaluation and should not be interpreted as the model's disease-classification accuracy.

### 6.3 Dataset Used for Training

The resulting **9,488-row adapted dataset** was used as the training dataset for the AutoScientist experiment.

```text
5,022-row curated dataset
          │
          ▼
     Adaptive Data
          │
          ▼
9,488-row adapted dataset
          │
          ▼
    AutoScientist

```

The adapted dataset and its associated metadata are intended to be released publicly as part of the hackathon's open-release requirement.