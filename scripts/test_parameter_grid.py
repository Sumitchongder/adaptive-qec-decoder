import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from experiments.baseline.parameter_grid import ParameterGrid

grid = ParameterGrid(

    "configs/experiments/baseline.yaml"

)

parameters = grid.generate()

print()

print("=" * 60)

print("Generated Parameter Grid")

print("=" * 60)

print()

for p in parameters:

    print(p)

print()

print("Total Experiments")

print(len(parameters))
