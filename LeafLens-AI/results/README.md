# Results

This directory contains evaluation and experiment-result documentation for LeafLens AI.

## AutoScientist Evaluation

The trained model was evaluated using the evaluation system provided by Adaption AutoScientist.

The evaluation reported an improvement over the provided baseline:

| Model | Training Win Rate |
|---|---:|
| Base model | 30% |
| Adapted model | 70% |

The Training Win Rate is the metric reported by the Adaption evaluation system. It should **not** be interpreted as conventional classification accuracy.

## Evaluation Interpretation

The result indicates that the adapted model performed better than the base model under the evaluation procedure used by the Adaption platform.

It does not by itself establish real-world agricultural diagnostic accuracy or generalization to unseen field conditions.

For additional context, see:

- [`docs/Evaluation.md`](../docs/Evaluation.md)
- [`model-card.md`](../model-card.md)

## Future Evaluation

Future experiments may include:

- Accuracy
- Precision
- Recall
- F1 score
- Per-class performance
- Confusion matrix
- Independent held-out evaluation
- Field-condition testing

Large model outputs and binary artifacts are not stored in this repository.