"""
Evaluate a trained model on a noise-sweep dataset.
"""

import os

from evaluation.evaluator import Evaluator


def main():

    noise = os.environ["NOISE"]

    dataset = (
        f"datasets/processed/"
        f"surface_d7_r7_p{noise}_50000shots.npz"
    )

    checkpoint = "checkpoints/neural/d7/best_model.pt"

    output = (
        f"results/evaluation/"
        f"noise_{noise}.csv"
    )

    evaluator = Evaluator(
        dataset_path=dataset,
        checkpoint_path=checkpoint,
        batch_size=1024,
    )

    evaluator.evaluate(output)


if __name__ == "__main__":
    main()
