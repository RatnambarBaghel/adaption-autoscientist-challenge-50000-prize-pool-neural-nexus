# Model

This directory contains lightweight metadata and configuration information for the LeafLens AI trained model.

The model weights are not stored in this GitHub repository because of their size. The trained model is publicly released through Hugging Face.

## Base Model

The training pipeline used:

`google/gemma-3-27b-it-VLM`

## Training Approach

The model was fine-tuned using:

- Supervised Fine-Tuning (SFT)
- LoRA parameter-efficient fine-tuning
- Chat-format training data
- AutoScientist training infrastructure

The LoRA configuration and training hyperparameters are available in:

`configuration/training_config.json`

## Training Configuration

| Parameter | Value |
|---|---|
| Training method | SFT |
| Fine-tuning type | LoRA |
| Base model size | 27B |
| LoRA rank | 64 |
| LoRA alpha | 128 |
| LoRA dropout | 0 |
| Epochs | 16 |
| Learning rate | 0.0001 |
| Scheduler | Cosine |
| Warmup ratio | 0.1 |
| Weight decay | 0 |
| Max gradient norm | 2 |
| Evaluations | 5 |
| Train on inputs | No |
| LoRA modules | `q_proj,k_proj,v_proj,o_proj` |

## Trained Model

The trained model is:

`adaption_crop_disease_leaf_images`

### Hugging Face

https://huggingface.co/RatnambarBaghel/adaption_crop_disease_leaf_images

## Model Weights

The model weights and adapter artifacts are maintained on the public Hugging Face model repository rather than being duplicated in GitHub.

## Reproducibility

The complete training configuration is provided for transparency and reproducibility.

Training was performed using Adaption AutoScientist after processing the competition data through Adaptive Data.

See also:

- `docs/Training.md`
- `docs/Evaluation.md`
- `model-card.md`
- `configuration/training_config.json`