"""
Train one neural decoder for a given distance dataset.

Run via Slurm.

Example:

python scripts/train_distance.py \
    --dataset datasets/processed/surface_d5_r5_p1e-03_50000shots.npz \
    --distance d5
"""

import argparse
from pathlib import Path

from training.trainer import Trainer


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dataset",
        required=True,
    )

    parser.add_argument(
        "--distance",
        required=True,
    )

    parser.add_argument(
        "--epochs",
        type=int,
        default=30,
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=256,
    )

    args = parser.parse_args()

    checkpoint_dir = Path(
        "checkpoints/neural"
    ) / args.distance

    history_file = Path(
        "results/training"
    ) / args.distance / "history.csv"

    trainer = Trainer(

        dataset_path=args.dataset,

        batch_size=args.batch_size,

        epochs=args.epochs,

        checkpoint_directory=str(checkpoint_dir),

        history_file=str(history_file),

    )

    trainer.train()


if __name__ == "__main__":
    main()
