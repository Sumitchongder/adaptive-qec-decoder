"""
Run complete baseline experiment.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from experiments.baseline.parameter_grid import ParameterGrid

from experiments.baseline.experiment_runner import ExperimentRunner

from experiments.baseline.save_results import ResultSaver

print("=" * 70)
print("Surface Code Baseline")
print("=" * 70)

grid = ParameterGrid(
    "configs/experiments/baseline.yaml"
)

parameters = grid.generate()

runner = ExperimentRunner()

results = runner.run_grid(
    parameters
)

saver = ResultSaver(
    "results/raw"
)

saver.save_csv(
    results,
    "experiment_results.csv"
)

print()

print("=" * 70)

print("Finished Successfully")

print("=" * 70)
