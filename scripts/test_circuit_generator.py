import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from simulator.circuit_generator import CircuitGenerator

generator = CircuitGenerator("configs/default.yaml")

circuit = generator.generate()

dem = generator.detector_error_model()

metadata = generator.save_metadata()

print("=" * 60)
print("Circuit Generator Test")
print("=" * 60)

print()

print(metadata)

print()

print("Number of detectors :", circuit.num_detectors)

print("Number of observables :", circuit.num_observables)

print("Circuit length :", len(str(circuit).splitlines()))

print()

print("Detector Error Model")

print("-" * 60)

print(str(dem)[:1000])

print()

print("✓ Circuit generation successful.")
