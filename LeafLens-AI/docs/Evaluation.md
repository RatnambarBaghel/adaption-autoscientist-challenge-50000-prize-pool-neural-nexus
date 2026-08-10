# 📊 LeafLens AI — Model Evaluation

## 1. Evaluation Overview

LeafLens AI was evaluated using the evaluation and training metrics provided by Adaption AutoScientist.

The primary comparison shown by the AutoScientist dashboard was the model's **Training Win Rate on the project dataset**, comparing the base model against the adapted model.

### 1.1 Base vs Adapted Model

The AutoScientist evaluation reported:

| Model | Training Win Rate |
|---|---:|
| Base model | 30% |
| Adapted model | 70% |

The adapted model therefore achieved a **40 percentage-point improvement** over the base model in the reported training win rate.

```text
Base Model
   30%
    │
    │ +40 percentage points
    ▼
Adapted Model
   70%

```

### 1.2 Model Used

The final AutoScientist training model was:

    adaption_gemma_3_27b_it_vlm_crop_disease_leaf_images_a0ca4386

The model was adapted from:

    google/gemma-3-27b-it-VLM

using supervised fine-tuning with LoRA.

### 1.3 Training Metrics

During the final training run, AutoScientist monitored:

- Training loss
- Validation loss
- Learning rate
- Gradient norm
- Global training step

The training dashboard recorded the progression of these metrics through 336 global steps.

### 1.4 Interpretation of the Win Rate

The reported 70% value represents the Training Win Rate on the project's dataset as provided by Adaption AutoScientist.

It should not be interpreted as:

- Classification accuracy
- Precision
- Recall
- F1 score
- Real-world field accuracy

The win-rate metric is reported according to Adaption's evaluation methodology.

### 1.5 Adaptive Data Quality Improvement

The Adaptive Data evaluation also reported an improvement in its text-quality assessment:

| Metric               | Before |  After |
| -------------------- | -----: | -----: |
| Text quality score   |    5.0 |    6.5 |
| Relative improvement |      — | +30.0% |


The platform also reported:

- Before grade: C
- After grade: C
- Before percentile: 7.8
- After percentile: 8.4

These metrics measure Adaptive Data quality, not crop-disease model accuracy.

### 1.6 Overall Result

The final adapted model achieved a substantially higher reported Training Win Rate than the base model:

    30% Base
        ↓
    70% Adapted

This demonstrates measurable improvement under Adaption AutoScientist's reported evaluation metric and supports the project's objective of adapting a general vision-language model to the agricultural crop-disease domain.

---

## 2. Training Metrics

The final AutoScientist training run was monitored using multiple optimization metrics.

The dashboard recorded these metrics throughout the training process:

- Training loss
- Validation loss
- Learning rate
- Gradient norm
- Global training step

### 2.1 Loss

The training dashboard tracked both training and validation loss.

Training loss decreased substantially during the early stages of training and continued to be monitored throughout the run.

Validation loss was monitored independently to observe the model's behavior on evaluation data during training.

The loss curves provide information about the optimization process but are not equivalent to crop-disease classification accuracy.

### 2.2 Learning Rate

The final configuration used a cosine learning-rate schedule.

The training configuration specified:

```text
Initial learning rate: 0.0001
Warmup ratio:          0.1
Scheduler:             cosine
Scheduler cycles:      0.5
Minimum LR ratio:      0.1

```

The learning rate was adjusted throughout training according to this schedule.

### 2.3 Gradient Norm

Gradient norm was monitored throughout training to observe the magnitude of optimization updates.

The final configuration used:

    Maximum gradient norm: 2

The training dashboard shows an initially high gradient norm followed by lower values and later fluctuations during optimization.

### 2.4 Global Training Steps

The final training dashboard records the training process through:

    336 global steps

These steps represent the optimization progress recorded by AutoScientist during the final run.

### 2.5 Metric Interpretation

The training metrics should be interpreted as indicators of the optimization process.

They do not directly represent:

- Crop-disease classification accuracy
- Precision
- Recall
- F1 score
- Field-level diagnostic reliability

The primary model-comparison result reported by Adaption for this experiment is the Training Win Rate, documented in Section 1.

---

## 3. Baseline Comparison

The final adapted model was compared with the base model using Adaption AutoScientist's reported Training Win Rate on the project dataset.

### 3.1 Comparison Results

| Model | Training Win Rate |
|---|---:|
| Base model | 30% |
| Adapted model | 70% |

The adapted model achieved a **40 percentage-point increase** in the reported Training Win Rate.

### 3.2 Relative Improvement

Using the reported win-rate values:

```text
Base win rate     = 30%
Adapted win rate  = 70%

Absolute increase = 70% - 30%
                  = 40 percentage points

```

Relative to the base model's 30% win rate, the increase is approximately:

    (70 - 30) / 30 × 100 ≈ 133.3%

However, the project uses 40 percentage points as the primary comparison because the AutoScientist dashboard reports win rate as a percentage.

### 3.3 Result Interpretation

The adapted model achieved a substantially higher Training Win Rate than the base model on the project dataset.

This indicates that the combination of:

- Curated agricultural training data
- Adaptive Data processing
- LoRA-based fine-tuning
- AutoScientist training optimization

produced measurable improvement over the base model under Adaption's reported evaluation metric.

### 3.4 Important Evaluation Scope

The comparison shown here is specifically the Training Win Rate on the project dataset reported by Adaption AutoScientist.

It should not be presented as a conventional machine-learning accuracy metric.

No unsupported claims are made regarding real-world field accuracy or clinical/agronomic diagnostic reliability.


---

## 4. Adaptive Data Results

Before model training, the curated dataset was processed through Adaption's Adaptive Data platform.

The platform reported measurable improvement in its data-quality evaluation after adaptation.

### 4.1 Quality Score

| Metric | Original | Adaptive |
|---|---:|---:|
| Text quality score | 5.0 | 6.5 |
| Percentile | 7.8 | 8.4 |
| Grade | C | C |

The platform reported:

```text
Relative improvement: +30.0%

```

### 4.2 Interpretation

The Adaptive Data quality evaluation indicates that the adapted dataset received a higher reported quality score than the original dataset.

The score increased from:

    5.0 → 6.5

This represents the improvement reported by the Adaptive Data evaluation system.

These quality metrics describe the training-data adaptation process and should not be interpreted as model accuracy.

### 4.3 Role in the Training Pipeline

The adapted dataset was subsequently used as the input for the AutoScientist training experiment.

The complete data flow was:

    Curated Dataset
    5,022 rows
        │
        ▼
    Adaptive Data
        │
        ├── Quality: 5.0 → 6.5
        └── Relative improvement: +30.0%
        │
        ▼
    Adapted Dataset
    9,488 rows
        │
        ▼
    AutoScientist Training
        │
        ▼
    Adapted Vision-Language Model

Adaptive Data therefore formed an important stage between dataset preparation and model fine-tuning.

---

## 5. Limitations

The evaluation results reported in this repository should be interpreted within the scope of the Adaption AutoScientist evaluation system.

### 5.1 Evaluation Metric

The primary model-comparison result available from the AutoScientist dashboard is the Training Win Rate on the project dataset.

The reported:

```text
Base model:     30%
Adapted model:  70%
```

should not be interpreted as conventional classification accuracy.

Additional metrics such as precision, recall, F1 score, or a complete independent test-set accuracy were not reported by the available AutoScientist dashboard for this experiment.

### 5.2 Dataset Scope

The model was trained and evaluated using the agricultural data prepared for this project.

Performance on completely different datasets, field conditions, camera devices, lighting conditions, or unseen crop varieties may differ from the reported results.

### 5.3 Real-World Usage

LeafLens AI is intended as an AI-assisted crop-disease detection system and should not be treated as a replacement for professional agronomic diagnosis.

Factors such as:

- Image quality
- Lighting
- Leaf orientation
- Disease stage
- Background conditions
- Multiple simultaneous diseases
- Unseen diseases
- Crop variety

can affect model predictions.

### 5.4 Interface Status

The LeafLens AI interface developed for the project is currently a demonstration/prototype interface.

The project does not claim that the current interface provides production-grade inference directly from the exported AutoScientist model unless a verified model-inference integration is available.

### 5.5 Future Evaluation

Future work can include independent evaluation using:

- A held-out agricultural test dataset
- Per-class accuracy
- Precision and recall
- F1 score
- Confusion matrix
- Cross-dataset evaluation
- Real-world field images

These evaluations would provide a more complete assessment of model performance beyond the AutoScientist Training Win Rate.