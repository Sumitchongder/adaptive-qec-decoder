import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from experiments.baseline.parameter_grid import ParameterGrid

from experiments.baseline.experiment_runner import ExperimentRunner

grid = ParameterGrid(
    "configs/experiments/baseline.yaml"
)

parameters = grid.generate()

runner = ExperimentRunner()

results = runner.run_grid(
    parameters[:3]
)

print()

print("=" * 60)

print(results)

print()

print("Completed")
