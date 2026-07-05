import sys
import time
from pathlib import Path

import pandas as pd
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator
from decoder.pymatching.decoder import PyMatchingDecoder
from evaluation.logical_error import LogicalErrorEvaluator

from configs.experiment_config import (
    DISTANCES,
    NOISE_LEVELS,
    SHOTS,
)

CONFIG_PATH = PROJECT_ROOT / "configs/default.yaml"

results = []

print("=" * 70)
print("AUTOMATED NOISE SWEEP")
print("=" * 70)

for distance in DISTANCES:

    for noise in NOISE_LEVELS:

        print()
        print("=" * 70)
        print(f"Distance : {distance}")
        print(f"Noise    : {noise}")
        print("=" * 70)

        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)

        config["surface_code"]["distance"] = distance
        config["noise"]["depolarizing_probability"] = noise
        config["experiment"]["shots"] = SHOTS

        with open(CONFIG_PATH, "w") as f:
            yaml.safe_dump(config, f)

        generator = CircuitGenerator(str(CONFIG_PATH))

        circuit = generator.generate()

        dem = circuit.detector_error_model()

        syndrome_generator = SyndromeGenerator(circuit)

        detectors, observables = syndrome_generator.sample(SHOTS)

        decoder = PyMatchingDecoder(dem)

        start = time.perf_counter()

        predictions = decoder.decode(detectors)

        runtime = time.perf_counter() - start

        evaluator = LogicalErrorEvaluator()

        metrics = evaluator.evaluate(
            predictions,
            observables,
        )

        metrics["distance"] = distance
        metrics["noise"] = noise
        metrics["runtime_seconds"] = runtime
        metrics["throughput"] = SHOTS / runtime

        results.append(metrics)

        print(metrics)

df = pd.DataFrame(results)

output = PROJECT_ROOT / "results/csv/noise_sweep.csv"

df.to_csv(output, index=False)

print()
print("=" * 70)
print("Experiment Finished")
print("=" * 70)
print(output)
