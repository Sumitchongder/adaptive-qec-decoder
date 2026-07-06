import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from experiments.common.experiment_runner import ExperimentRunner

runner = ExperimentRunner()

result = runner.run_once(
    distance=3,
    noise=0.001,
    shots=1000,
)

print()

for key, value in result.items():
    print(f"{key:20s}: {value}")
