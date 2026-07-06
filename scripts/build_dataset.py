"""
Dataset generation entry point.

Supports SLURM environment variables.

Example

DISTANCE=7
ROUNDS=7
NOISE=2e-04
SHOTS=50000
"""

import os

from simulator.dataset_builder import DatasetBuilder


def getenv_int(name, default=None):
    value = os.getenv(name)
    return int(value) if value is not None else default


def getenv_float(name, default=None):
    value = os.getenv(name)
    return float(value) if value is not None else default


def main():

    distance = getenv_int("DISTANCE")
    rounds = getenv_int("ROUNDS")
    noise = getenv_float("NOISE")
    shots = getenv_int("SHOTS")

    builder = DatasetBuilder("configs/publication.yaml")

    builder.build_dataset(
        output_directory="datasets/processed",
        distance=distance,
        rounds=rounds,
        noise=noise,
        shots=shots,
    )


if __name__ == "__main__":

    main()
