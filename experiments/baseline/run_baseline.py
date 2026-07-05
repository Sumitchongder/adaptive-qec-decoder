"""
Publication Baseline Experiment
===============================

Runs PyMatching decoding experiments over
multiple code distances and physical error rates.

Outputs:

results/publication/baseline_full_results.csv

Author:
NVIDIA_QEC_Project
"""

import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import numpy as np
import pandas as pd

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator
from decoder.pymatching.decoder import PyMatchingDecoder
from evaluation.logical_error import LogicalErrorEvaluator


###########################################################
# Experiment Parameters
###########################################################

SHOTS = 5000          # validation run
REPEATS = 3           # increase to 5 later

DISTANCES = [
    3,
    5,
    7,
    9,
    11,
]

NOISES = [
    1e-4,
    2e-4,
    5e-4,
    1e-3,
    2e-3,
    5e-3,
]

###########################################################

generator = CircuitGenerator(
    "configs/default.yaml"
)

results = []

for distance in DISTANCES:

    for noise in NOISES:

        print("=" * 70)
        print(f"Distance : {distance}")
        print(f"Noise    : {noise}")

        runtime_list = []
        accuracy_list = []
        logical_error_list = []
        throughput_list = []

        detector_count = None
        observable_count = None
        operation_count = None

        for repeat in range(REPEATS):

            print(f"Repeat {repeat+1}/{REPEATS}")

            generator.config["surface_code"]["distance"] = distance
            generator.config["surface_code"]["rounds"] = distance
            generator.config["noise"]["depolarizing_probability"] = noise

            start = time.perf_counter()

            circuit = generator.generate()

            dem = circuit.detector_error_model()

            syndrome_generator = SyndromeGenerator(circuit)

            detectors, observables = syndrome_generator.sample(
                SHOTS
            )

            decoder = PyMatchingDecoder(dem)

            predictions = decoder.decode(detectors)

            evaluator = LogicalErrorEvaluator()

            metrics = evaluator.evaluate(
                predictions,
                observables,
            )

            runtime = time.perf_counter() - start

            throughput = SHOTS / runtime

            runtime_list.append(runtime)
            accuracy_list.append(metrics["accuracy"])
            logical_error_list.append(
                metrics["logical_error_rate"]
            )
            throughput_list.append(throughput)

            detector_count = circuit.num_detectors
            observable_count = circuit.num_observables
            operation_count = len(str(circuit).splitlines())

        results.append({

            "distance": distance,

            "noise": noise,

            "shots": SHOTS,

            "mean_runtime": np.mean(runtime_list),
            "std_runtime": np.std(runtime_list),

            "mean_accuracy": np.mean(accuracy_list),
            "std_accuracy": np.std(accuracy_list),

            "mean_logical_error":
                np.mean(logical_error_list),

            "std_logical_error":
                np.std(logical_error_list),

            "mean_throughput":
                np.mean(throughput_list),

            "std_throughput":
                np.std(throughput_list),

            "detectors":
                detector_count,

            "observables":
                observable_count,

            "operations":
                operation_count,

        })

print()
print("=" * 70)
print("Saving Results")
print("=" * 70)

df = pd.DataFrame(results)

output = "results/publication/baseline_full_results.csv"

df.to_csv(
    output,
    index=False,
)

print(df)

print()
print("Saved to")
print(output)
