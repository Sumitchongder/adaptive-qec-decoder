"""
Dataset Builder Test
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from simulator.dataset_builder import DatasetBuilder

print("=" * 60)
print("Dataset Builder Test")
print("=" * 60)

builder = DatasetBuilder(
    config_path="configs/default.yaml"
)

detectors, observables = builder.build_dataset()

print()

print("Detector shape:")

print(detectors.shape)

print()

print("Observable shape:")

print(observables.shape)

print()

print("✓ Dataset generated successfully.")
