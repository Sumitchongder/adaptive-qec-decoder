import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator
from decoder.pymatching.decoder import PyMatchingDecoder

print("=" * 60)
print("PyMatching Decoder Test")
print("=" * 60)

generator = CircuitGenerator(
    "configs/default.yaml"
)

circuit = generator.generate()

detector_error_model = circuit.detector_error_model()

generator = SyndromeGenerator(circuit)

detectors, observables = generator.sample(20)

decoder = PyMatchingDecoder(detector_error_model)

predictions = decoder.decode(detectors)

print()

print("Detector samples")

print(detectors.shape)

print()

print("Actual observables")

print(observables.shape)

print()

print("Predicted observables")

print(predictions.shape)

print()

print("First prediction")

print(predictions[0])

print()

print("✓ Decoder working successfully.")
