import os

from simulator.dataset_builder import DatasetBuilder


def main():
    noise = float(os.environ["NOISE"])
    distance = int(os.environ.get("DISTANCE", "7"))
    rounds = int(os.environ.get("ROUNDS", str(distance)))
    shots = int(os.environ.get("SHOTS", "50000"))

    builder = DatasetBuilder()

    dataset_name = (
        f"surface_d{distance}_r{rounds}_"
        f"p{noise:.0e}_{shots}shots"
    )

    builder.build_dataset(
        output_directory="datasets/processed",
        dataset_name=dataset_name,
        distance=distance,
        rounds=rounds,
        noise=noise,
        shots=shots,
    )


if __name__ == "__main__":
    main()
