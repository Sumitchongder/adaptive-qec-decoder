import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from configs.experiment_config import (
    DISTANCES,
    NOISE_LEVELS,
    SHOTS,
)

print("=" * 60)
print("Experiment Configuration")
print("=" * 60)

print()

print("Distances")
print(DISTANCES)

print()

print("Noise Levels")
print(NOISE_LEVELS)

print()

print("Shots")
print(SHOTS)

print()

print("Configuration loaded successfully.")
