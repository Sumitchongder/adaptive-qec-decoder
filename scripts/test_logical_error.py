import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator

from decoder.pymatching.decoder import PyMatchingDecoder

from evaluation.logical_error import LogicalErrorEvaluator

print("=" * 60)
print("Logical Error Evaluation Test")
print("=" * 60)

generator = CircuitGenerator(
    "configs/default.yaml"
)

circuit = generator.generate()

dem = circuit.detector_error_model()

syndrome_generator = SyndromeGenerator(circuit)

config = generator.config

shots = config["experiment"]["shots"]

detectors, observables = syndrome_generator.sample(
    shots
)

decoder = PyMatchingDecoder(dem)

predictions = decoder.decode(detectors)

evaluator = LogicalErrorEvaluator()

results = evaluator.evaluate(
    predictions,
    observables,
)

print()

print("Evaluation Results")

print("-" * 40)

for key, value in results.items():
    print(f"{key:25s}: {value}")

print()

print("✓ Logical error evaluation successful.")
