"""
Generate publication datasets for all code distances.

This script is intended to be run through Slurm.

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path

from simulator.dataset_builder import DatasetBuilder

CONFIG = "configs/default.yaml"

DISTANCES = [3, 5, 7, 9, 11]

ROUNDS = {
    3: 3,
    5: 5,
    7: 7,
    9: 9,
    11: 11,
}

NOISE = 0.001

SHOTS = 50000


def main():

    builder = DatasetBuilder(CONFIG)

    output_dir = Path("datasets/processed")

    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Distance Sweep")
    print("=" * 70)

    for distance in DISTANCES:

        rounds = ROUNDS[distance]

        dataset_name = (
            f"surface_d{distance}"
            f"_r{rounds}"
            f"_p1e-03"
            f"_{SHOTS}shots"
        )

        print()
        print("=" * 70)
        print(dataset_name)
        print("=" * 70)

        builder.build_dataset(
            output_directory=output_dir,
            dataset_name=dataset_name,
            distance=distance,
            rounds=rounds,
            noise=NOISE,
            shots=SHOTS,
        )

    print()
    print("=" * 70)
    print("Distance sweep completed")
    print("=" * 70)


if __name__ == "__main__":
    main()
