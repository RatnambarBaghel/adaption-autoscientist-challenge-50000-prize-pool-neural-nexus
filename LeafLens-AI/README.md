# 🌿 LeafLens AI

## AI-Powered Crop Disease Detection

LeafLens AI is an agricultural vision-language project developed for the **HackIndia × Adaption AutoScientist Challenge Part 2**.

The project adapts a general-purpose vision-language model to the crop-disease domain using a curated agricultural dataset, Adaption's **Adaptive Data**, and **AutoScientist** fine-tuning.

> **Snap a leaf. Identify the disease. Protect the crop.**

### 🎯 Project Goal

The goal is to improve crop-disease identification from leaf images by adapting a large vision-language model to specialized agricultural data.

The project focuses on:

- Crop disease identification
- Healthy-vs-diseased leaf recognition
- Agricultural image understanding
- AI-assisted crop-health screening

### 🚀 Key Result

The final AutoScientist evaluation reported:

| Model | Training Win Rate |
|---|---:|
| Base model | **30%** |
| Adapted model | **70%** |

This represents a **40 percentage-point improvement** in the reported Training Win Rate on the project dataset.

> **Note:** The reported win rate is Adaption AutoScientist's evaluation metric and should not be interpreted as conventional classification accuracy.

### 🧠 Technology

```text
Agricultural Leaf Data
        ↓
Preprocessing
        ↓
5,022-row Curated Dataset
        ↓
Adaptive Data
        ↓
9,488-row Adapted Dataset
        ↓
AutoScientist
        ↓
Gemma 3 27B Vision-Language Model
        ↓
LoRA Fine-tuning
        ↓
LeafLens AI
```

---

## ✨ Key Features

### 🌱 Crop Disease Identification

The adapted vision-language model is specialized for identifying crop-disease conditions from agricultural leaf images.

### 🧹 Curated Agricultural Dataset

The project uses a multi-stage data pipeline involving:

- Dataset inspection
- Image validation
- Corrupted-image checking
- Duplicate removal
- Label standardization
- RGB conversion
- Class balancing
- Train / validation / test standardization

A curated **5,022-row experiment dataset** was prepared before Adaptive Data processing.

### 🔄 Adaptive Data Optimization

The curated dataset was processed through Adaption Adaptive Data.

The platform produced an adapted dataset containing **9,488 rows** and reported a **30% relative improvement** in its text-quality evaluation.

### 🤖 AutoScientist Fine-tuning

The adapted dataset was used with Adaption AutoScientist to fine-tune:

```text
google/gemma-3-27b-it-VLM
```

using:

Supervised Fine-Tuning (SFT)
LoRA
16 training epochs
Cosine learning-rate scheduling
📈 Measurable Model Improvement

Adaption AutoScientist reported:

    Base model       → 30% Training Win Rate
    Adapted model    → 70% Training Win Rate
    Improvement      → +40 percentage points

🌾 Farmer-Focused Demo

The project also includes a LeafLens AI demonstration interface designed around a simple farmer workflow:

Upload Leaf Image
        ↓
Select / Detect Crop
        ↓
Analyze
        ↓
Disease Information
        ↓
Treatment & Prevention Guidance

The interface is currently presented as a demonstration/prototype and is not claimed to be a production inference system directly connected to the exported model.

---

## 📊 Dataset & Data Pipeline

LeafLens AI uses a multi-stage agricultural data pipeline designed to improve data consistency and prepare the data for vision-language model training.

### Data Pipeline

```text
Agricultural Leaf Datasets
          │
          ▼
Dataset Inspection
          │
          ▼
Image Validation & Cleaning
          │
          ▼
Duplicate Removal
          │
          ▼
Label Standardization
          │
          ▼
RGB Conversion
          │
          ▼
Class Balancing
          │
          ▼
Train / Validation / Test Standardization
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

```

### Dataset Preparation

The preprocessing workflow was used to create a consistent crop-disease dataset from multiple agricultural image sources.

The process included:

- Dataset inspection
- Image validation
- Corrupted-image detection
- Duplicate removal
- Label standardization
- RGB conversion
- Class balancing
- Dataset split standardization

### Curated Experiment Dataset

The dataset selected for the Adaptive Data experiment contained:

5,022 rows

These examples were structured for crop-disease identification using leaf images and corresponding diagnostic responses.

Adaptive Data Output

Adaption's Adaptive Data platform processed the curated dataset and generated:

9,488 adapted rows

The platform reported:

- Text quality score: 5.0 → 6.5
- Relative improvement: +30.0%
- Percentile: 7.8 → 8.4
- Grade: C → C

These quality metrics describe the data adaptation process and are not model accuracy measurements.

For complete dataset preparation details, see:

        docs/Dataset.md

---

## 🧪 Training & Evaluation

The final model was trained using **Adaption AutoScientist** with the 9,488-row adapted dataset.

### Base Model

```text
google/gemma-3-27b-it-VLM
```

### Fine-tuning

The model was adapted using:

- Supervised Fine-Tuning (SFT)
- Low-Rank Adaptation (LoRA)
- 16 epochs
- Learning rate: 0.0001
- Cosine learning-rate scheduler
- Warmup ratio: 0.1
- LoRA rank: 64
- LoRA alpha: 128
- LoRA dropout: 0
- Maximum gradient norm: 2
- LoRA target modules: q_proj, k_proj, v_proj, o_proj
- Evaluation Result

Adaption AutoScientist reported the following Training Win Rate on the project dataset:

| Model         | Training Win Rate |
| ------------- | ----------------: |
| Base model    |           **30%** |
| Adapted model |           **70%** |



### Improvement

        70% - 30% = +40 percentage points

The adapted model therefore achieved a 40 percentage-point improvement over the base model under Adaption's reported Training Win Rate metric.

        Important: Training Win Rate is an Adaption evaluation metric. It should not be interpreted as conventional classification accuracy, precision, recall, or F1 score.

For detailed training configuration and results, see:

        docs/Training.md
        docs/Evaluation.md
        model-card.md

---

## 🔗 Public Model & Dataset Releases

### 🤗 Hugging Face

**Trained Model**

https://huggingface.co/RatnambarBaghel/adaption_crop_disease_leaf_images

**Adapted Dataset**

https://huggingface.co/datasets/RatnambarBaghel/adaption-crop-disease-leaf-images-v1

### 📊 Kaggle

**Adapted Dataset**

https://www.kaggle.com/datasets/ratnambarbaghel/adaption-crop-bf0ca919-980a-4865-bbc5-4227737ef45f

**Kaggle Model**

⏳ Model export pending.

The Kaggle model link will be added after the trained model weights have been successfully published.

### 💻 GitHub

https://github.com/RatnambarBaghel/LeafLens-AI

The GitHub repository contains the project source code and technical documentation required to understand and reproduce the training pipeline.

---

## 🖥️ LeafLens AI Demo Interface

LeafLens AI includes a farmer-friendly demonstration interface designed around a simple crop-disease screening workflow.

### User Workflow

```text
Upload / Capture Leaf Image
          │
          ▼
Choose Crop or Auto Detect
          │
          ▼
Add Optional Notes
          │
          ▼
Analyze Leaf
          │
          ▼
Display Diagnosis
          │
          ▼
Treatment / Prevention Information

```

### Interface Features

The prototype interface includes:

- 📷 Camera capture
- 🖼️ Image upload
- 🖱️ Drag-and-drop image support
- 🌾 Crop selection
- 🤖 Automatic crop detection option
- 📝 Optional observations/notes
- 🔍 Leaf analysis workflow
- 💊 Treatment information
- 🛡️ Prevention guidance
- 🌧️ Disease-spread information
- 🌱 Fertilizer guidance
- 🐛 Similar-disease information
- 🚨 Emergency-action guidance
- 📄 Report generation
- 🌐 English / Hindi interface support

### Supported Crop Options

The current prototype provides crop-selection options including:

        Apple
        Tomato
        Rice
        Potato
        Grape
        Corn
        Pepper
        Soybean
        Cherry
        Orange
        Other

### Prototype Status

The current interface is a demonstration/prototype created to show how the trained crop-disease model could be presented to end users.

The interface should not be considered a production deployment of the exported AutoScientist model unless a verified inference connection has been established.

The core hackathon contribution is the dataset adaptation, AutoScientist training, model improvement, and open release. The interface serves as an additional demonstration layer.

---

## 📚 Documentation

Detailed technical documentation is available in the `docs/` directory.

| Document | Description |
|---|---|
| [`Architecture.md`](docs/Architecture.md) | Overall LeafLens AI system architecture and project workflow |
| [`Dataset.md`](docs/Dataset.md) | Dataset sources, preprocessing, cleaning, and Adaptive Data pipeline |
| [`Training.md`](docs/Training.md) | AutoScientist training process and final training configuration |
| [`Evaluation.md`](docs/Evaluation.md) | Training metrics, baseline comparison, and evaluation results |
| [`model-card.md`](model-card.md) | Model information, intended use, training, evaluation, and limitations |

### Repository Structure

```text
LeafLens-AI/
│
├── README.md
├── model-card.md
├── .gitignore
│
└── docs/
    ├── Architecture.md
    ├── Dataset.md
    ├── Training.md
    └── Evaluation.md

```

The repository is intended to provide a transparent record of the project's dataset preparation, model training, evaluation, and open-release process.

---

## ⚠️ Limitations & Responsible Use

LeafLens AI is an experimental agricultural AI project and should be used as an **AI-assisted screening tool**, not as a definitive agricultural diagnosis system.

### Model Limitations

Predictions may be affected by:

- Poor image quality
- Low or uneven lighting
- Leaf orientation
- Complex backgrounds
- Disease severity
- Crop varieties not represented in the training data
- Multiple diseases appearing on the same leaf
- Diseases not included in the training data
- Unseen field conditions

### Evaluation Limitations

The primary model-comparison result reported in this project is the **Training Win Rate provided by Adaption AutoScientist**.

The reported improvement:

```text
Base model     → 30%
Adapted model  → 70%
```

should not be interpreted as 70% real-world classification accuracy.

Independent evaluation using held-out datasets and conventional metrics such as accuracy, precision, recall, F1 score, and confusion matrices would provide additional evidence of model generalization.

### Responsible Use

The model should not be used as the sole basis for:

- Pesticide or chemical application
- Disease-control decisions with significant financial consequences
- Large-scale crop treatment
- Definitive agricultural diagnosis

Important decisions should be verified using qualified agricultural professionals or trusted agricultural resources.

### Interface Status

The LeafLens AI interface is currently a demonstration/prototype.

The project does not claim production-grade inference through the interface unless a verified connection to the exported AutoScientist model is established.

### Future Work

Future development can include:

- Verified model inference integration
- Independent held-out testing
- Per-class performance evaluation
- Confusion-matrix analysis
- Field-condition testing
- Additional crops and diseases
- Multilingual agricultural assistance
- Production deployment