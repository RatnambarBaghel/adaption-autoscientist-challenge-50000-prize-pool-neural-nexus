# 🏗 LeafLens AI — System Architecture

## Overview

LeafLens AI is an AI-powered crop disease detection project developed for the **HackIndia × Adaption AutoScientist Challenge Part 2**.

The project uses a vision-language model (VLM) approach to identify crop diseases from leaf images. The training pipeline combines dataset preprocessing, Adaptive Data optimization, and AutoScientist model training.

The overall workflow is:

```text
Agricultural Leaf Datasets
          │
          ▼
Dataset Inspection & Preprocessing
          │
          ▼
Cleaning, Deduplication & Label Standardization
          │
          ▼
Balanced Crop-Disease Dataset
          │
          ▼
Adaptive Data
          │
          ▼
AutoScientist Training
          │
          ▼
Fine-tuned Vision-Language Model
          │
          ▼
Evaluation Against Baseline
          │
          ▼
Open Model & Dataset Release
          │
          ▼
LeafLens AI Demo Interface

```
---


Core Components
1. Dataset Preparation

Multiple agricultural leaf-image datasets were collected and standardized into a unified crop-disease dataset.

The preprocessing pipeline included:

- Dataset inspection
- Image validation
- Corrupted-image checking
- Duplicate removal
- Label standardization
- RGB image conversion
- Class balancing
- Train/validation/test splitting

---
2. Adaptive Data

The prepared dataset was processed through Adaption's Adaptive Data platform to improve the quality and usefulness of the training data before model fine-tuning.

---

3. AutoScientist

The adapted dataset was used with Adaption AutoScientist to train and optimize the vision-language model.

AutoScientist was used to explore and optimize the training configuration with the objective of improving performance over the provided baseline.

---

4. Model Evaluation

The trained model was evaluated against the baseline using Adaption's evaluation system.

The final training run achieved a measurable improvement over the provided baseline. Detailed results are documented in Evaluation.md.

---

5. Open Release

The adapted dataset and trained model are being released through:

- Hugging Face
- Kaggle

The repository provides documentation describing the dataset preparation, training process, evaluation, and reproducibility information.

---

6. LeafLens AI Interface

LeafLens AI is a farmer-friendly demonstration interface designed around the trained crop-disease detection concept.

The interface allows users to upload leaf images and presents disease-detection results in a simple format.

---

Note: The current Adaption-generated interface is treated as a demonstration/prototype. The project does not claim a direct production inference connection between the interface and the exported AutoScientist model unless such integration is explicitly supported by the platform.
