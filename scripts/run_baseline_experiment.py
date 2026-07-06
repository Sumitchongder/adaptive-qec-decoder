import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import csv
import yaml

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator

from decoder.pymatching.decoder import PyMatchingDecoder

from evaluation.logical_error import LogicalErrorEvaluator


CONFIG_FILE = "configs/default.yaml"

RESULT_FILE = "results/csv/baseline_results.csv"


distances = [3, 5, 7]

noise_values = [
    1e-4,
    5e-4,
    1e-3,
]

shots = 5000


results = []

for distance in distances:

    for noise in noise_values:

        print("=" * 60)

        print(f"Distance : {distance}")

        print(f"Noise    : {noise}")

        with open(CONFIG_FILE, "r") as f:

            config = yaml.safe_load(f)

        config["surface_code"]["distance"] = distance
        config["surface_code"]["rounds"] = distance
        config["noise"]["depolarizing_probability"] = noise
        config["experiment"]["shots"] = shots

        temporary = "configs/tmp.yaml"

        with open(temporary, "w") as f:

            yaml.dump(config, f)

        generator = CircuitGenerator(temporary)

        circuit = generator.generate()

        syndrome_generator = SyndromeGenerator(circuit)

        detectors, observables = syndrome_generator.sample(shots)

        dem = circuit.detector_error_model()

        decoder = PyMatchingDecoder(dem)

        predictions = decoder.decode(detectors)

        evaluator = LogicalErrorEvaluator()

        metrics = evaluator.evaluate(
            predictions,
            observables,
        )

        metrics["distance"] = distance
        metrics["noise"] = noise

        results.append(metrics)

        print(metrics)

Path("results/csv").mkdir(
    parents=True,
    exist_ok=True,
)

with open(
    RESULT_FILE,
    "w",
    newline="",
) as csvfile:

    writer = csv.DictWriter(
        csvfile,
        fieldnames=results[0].keys(),
    )

    writer.writeheader()

    writer.writerows(results)

print()

print("=" * 60)
print("Experiment Completed")
print("=" * 60)

print()

print("Results saved to")

print(RESULT_FILE)
