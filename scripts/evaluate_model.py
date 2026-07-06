"""
Evaluate a trained neural decoder.

Usage:
    DATASET=...
    CHECKPOINT=...
    OUTPUT=...
    python scripts/evaluate_model.py
"""

import os

from evaluation.evaluator import Evaluator


def main():

    dataset = os.environ["DATASET"]

    checkpoint = os.environ["CHECKPOINT"]

    output = os.environ["OUTPUT"]

    evaluator = Evaluator(
        dataset_path=dataset,
        checkpoint_path=checkpoint,
        batch_size=1024,
    )

    evaluator.evaluate(output)


if __name__ == "__main__":
    main()
