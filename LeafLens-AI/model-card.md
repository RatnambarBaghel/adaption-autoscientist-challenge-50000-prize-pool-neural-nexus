# 🌿 LeafLens AI — Crop Disease Detection Model

## 1. Model Summary

**LeafLens AI** is a vision-language model adapted for crop disease identification from leaf images.

The model was developed for the **HackIndia × Adaption AutoScientist Challenge Part 2** under the Agriculture category.

The project adapts a general-purpose vision-language model to a specialized agricultural domain using:

- Curated crop-disease image data
- Adaption Adaptive Data
- Adaption AutoScientist
- Supervised Fine-Tuning (SFT)
- Low-Rank Adaptation (LoRA)

### Model Information

| Property | Details |
|---|---|
| Model name | `adaption_gemma_3_27b_it_vlm_crop_disease_leaf_images_a0ca4386` |
| Base model | `google/gemma-3-27b-it-VLM` |
| Base model size | 27B parameters |
| Training method | Supervised Fine-Tuning (SFT) |
| Fine-tuning method | LoRA |
| Domain | Agriculture |
| Primary task | Crop disease identification |
| Input | Leaf image |
| Output | Crop / disease diagnosis |
| Training dataset | Adaption Adaptive Data |
| Adapted dataset size | 9,488 rows |

### Training Objective

The primary objective was to improve the ability of the base vision-language model to recognize crop diseases from leaf images and provide disease-identification responses for agricultural use cases.

The final adapted model achieved a reported **70% Training Win Rate**, compared with **30% for the base model**, on the project dataset using Adaption AutoScientist's evaluation system.

---

## 2. Intended Use

LeafLens AI is intended to assist with preliminary crop-disease identification from leaf images.

### Primary Use Cases

The model can be used for:

- Preliminary crop disease screening
- Agricultural image analysis
- Farmer and gardener decision support
- Educational crop-disease identification
- Agricultural research and experimentation
- Building crop-health monitoring applications

### Supported Interaction

The model is designed to analyze a leaf image and identify the most likely crop-disease condition represented in the training data.

A typical workflow is:

```text
Leaf Image
    │
    ▼
Vision-Language Model
    │
    ▼
Crop / Disease Identification
    │
    ▼
Agricultural Guidance

```

### Intended Users

The model is primarily intended for:

- Farmers and growers
- Agricultural students
- Researchers
- Agronomists and extension workers
- Developers building agricultural AI applications

### Not Intended For

The model should not be used as:

- A replacement for professional agronomic diagnosis
- A sole basis for pesticide or chemical application decisions
- A guarantee of disease presence or absence
- A medical or veterinary diagnostic system
- An autonomous agricultural decision-making system

Predictions should be treated as AI-assisted suggestions and verified using appropriate agricultural expertise when decisions may affect crop health or economic outcomes.

---

## 3. Dataset

The model was trained using an adapted agricultural dataset produced through Adaption's **Adaptive Data** platform.

### Dataset Pipeline

The data preparation followed this workflow:

```text
Agricultural Leaf Datasets
          │
          ▼
Preprocessing & Cleaning
          │
          ▼
Curated Experiment Dataset
5,022 rows
          │
          ▼
Adaptive Data
          │
          ▼
Adapted Dataset
9,488 rows
          │
          ▼
AutoScientist Training

```

### Curated Dataset

The initial curated experiment dataset contained 5,022 rows representing crop-disease identification examples based on leaf images.

The data was prepared with a focus on:

- Crop-disease identification
- Healthy and diseased plant conditions
- Consistent labeling
- Valid image examples
- Multimodal training structure
- Adapted Dataset

The curated dataset was processed through Adaptive Data before model training.

The resulting adapted dataset contained:

- 9,488 rows
- Language: English
- Domain: Agriculture
- Task: Crop disease identification
- Format: Chat
- Input: Leaf images and disease-identification prompts
- Output: Crop / disease diagnosis

### Dataset Quality

Adaptive Data reported:

| Metric             | Before | After |
| ------------------ | -----: | ----: |
| Text quality score |    5.0 |   6.5 |
| Percentile         |    7.8 |   8.4 |
| Grade              |      C |     C |


The platform reported a 30% relative improvement in its text-quality evaluation.

These quality metrics describe the Adaptive Data transformation and should not be interpreted as model accuracy.

### Dataset Documentation

Detailed information about the original agricultural datasets, preprocessing pipeline, label standardization, and Adaptive Data transformation is available in:

    docs/Dataset.md

---

## 4. Training

The model was fine-tuned using **Adaption AutoScientist** with supervised fine-tuning and LoRA.

### Base Model

```text
google/gemma-3-27b-it-VLM
```

### Training Configuration

| Parameter               | Value             |
| ----------------------- | ----------------- |
| Training method         | SFT               |
| Fine-tuning method      | LoRA              |
| Epochs                  | 16                |
| Batch size              | Maximum supported |
| Learning rate           | 0.0001            |
| Learning-rate scheduler | Cosine            |
| Scheduler cycles        | 0.5               |
| Warmup ratio            | 0.1               |
| Minimum LR ratio        | 0.1               |
| LoRA rank               | 64                |
| LoRA alpha              | 128               |
| LoRA dropout            | 0                 |
| Weight decay            | 0                 |
| Maximum gradient norm   | 2                 |
| Evaluation runs         | 5                 |
| Train on inputs         | False             |


### LoRA Target Modules

LoRA adapters were applied to the following attention projection modules:

- q_proj
- k_proj
- v_proj
- o_proj

### Training Objective

The objective of fine-tuning was to specialize the general-purpose vision-language model for agricultural crop-disease identification using the adapted dataset.

The complete training configuration and process are documented in:

    docs/Training.md

---

## 5. Evaluation

The model was evaluated using the evaluation system provided by Adaption AutoScientist.

### Baseline Comparison

The reported Training Win Rate on the project dataset was:

| Model | Training Win Rate |
|---|---:|
| Base model | 30% |
| Adapted model | 70% |

The adapted model therefore achieved a **40 percentage-point improvement** over the base model.

### Evaluation Interpretation

The reported 70% value represents the **Training Win Rate on the project dataset** reported by Adaption AutoScientist.

It should not be interpreted as conventional classification accuracy, precision, recall, or F1 score.

The evaluation result demonstrates measurable improvement under Adaption's reported evaluation methodology.

### Adaptive Data Evaluation

Adaptive Data also reported an improvement in its data-quality evaluation:

| Metric | Before | After |
|---|---:|---:|
| Text quality score | 5.0 | 6.5 |
| Relative improvement | — | +30.0% |
| Percentile | 7.8 | 8.4 |
| Grade | C | C |

These metrics describe the data-adaptation stage rather than model accuracy.

Detailed evaluation information is available in:

```text
docs/Evaluation.md

```
---

## 6. Limitations & Responsible Use

The model is an experimental agricultural AI system and should be used with appropriate caution.

### Model Limitations

Performance may vary depending on:

- Image quality
- Lighting conditions
- Leaf orientation
- Background complexity
- Disease severity
- Crop variety
- Multiple simultaneous diseases
- Diseases not represented in the training data
- Unseen environmental conditions

The model may produce incorrect or uncertain predictions when an image differs significantly from the examples represented in its training data.

### Evaluation Limitations

The primary reported model-comparison metric available for this experiment is Adaption AutoScientist's **Training Win Rate on the project dataset**.

The reported 70% adapted win rate should not be interpreted as a 70% real-world disease-classification accuracy.

Independent evaluation using additional held-out agricultural datasets and conventional classification metrics would provide stronger evidence of generalization.

### Responsible Use

The model should be used as an **AI-assisted screening and research tool**, rather than as a definitive agricultural diagnosis system.

For decisions involving significant crop loss, pesticide application, disease containment, or other high-impact agricultural actions, predictions should be verified by qualified agricultural professionals or trusted agricultural resources.

### Interface Limitations

The LeafLens AI interface included in this project is a demonstration/prototype interface.

The project does not claim production-grade inference through the interface unless a verified connection to the exported model is established.

### Future Improvements

Future versions can improve evaluation and reliability through:

- Independent held-out test datasets
- Per-class precision and recall
- F1 score
- Confusion matrices
- Cross-dataset testing
- Field-condition images
- More crop and disease classes
- Verified production inference integration

---

## 7. License & Project Links

### License

The project contains multiple artifacts with different licensing information.

#### Model

The Hugging Face model is published with:

```yaml
license: other
```

The model is a LoRA adapter based on:

google/gemma-3-27b-it-VLM

Therefore, users should review the licensing terms and usage restrictions of the underlying Gemma model before using, modifying, or redistributing the adapter.

Hugging Face model:

https://huggingface.co/RatnambarBaghel/adaption_crop_disease_leaf_images

Dataset Artifacts

The current dataset artifacts have the following licensing information:

| Artifact                                     | License              |
| -------------------------------------------- | -------------------- |
| Original 5,022-row Hugging Face dataset      | Apache-2.0           |
| 9,488-row Hugging Face Adaptive Data dataset | No license specified |
| Kaggle adapted dataset                       | CC0 / Public Domain  |


Because the project combines and derives data from multiple agricultural datasets, users should also review the licenses and attribution requirements of the original source datasets before redistributing the data or derived artifacts.

The repository does not claim that all source datasets share the same license.

### Public Model

**Hugging Face Model:**

https://huggingface.co/RatnambarBaghel/adaption_crop_disease_leaf_images

### Public Datasets

**Hugging Face Dataset:**

https://huggingface.co/datasets/RatnambarBaghel/adaption-crop-disease-leaf-images-v1

**Kaggle Dataset:**

https://www.kaggle.com/datasets/ratnambarbaghel/adaption-crop-bf0ca919-980a-4865-bbc5-4227737ef45f

### Source Repository

**GitHub:**

https://github.com/RatnambarBaghel/LeafLens-AI

### Kaggle Model

The trained model has not yet been exported to Kaggle.

A Kaggle model link will be added after the model weights have been successfully published.

### Documentation

Additional project documentation is available in the GitHub repository:

- `docs/Architecture.md`
- `docs/Dataset.md`
- `docs/Training.md`
- `docs/Evaluation.md`
- `model-card.md`
