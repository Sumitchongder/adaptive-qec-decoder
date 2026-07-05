import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator

generator = CircuitGenerator("configs/default.yaml")

circuit = generator.generate()

sampler = SyndromeGenerator(circuit)

detectors, observables = sampler.sample(shots=10)

print("=" * 60)
print("Syndrome Generator Test")
print("=" * 60)

print()

print("Detector array shape:")
print(detectors.shape)

print()

print("Observable array shape:")
print(observables.shape)

print()

print("First detector sample:")
print(detectors[0])

print()

print("First observable:")
print(observables[0])

print()

print("✓ Syndrome generation successful.")
