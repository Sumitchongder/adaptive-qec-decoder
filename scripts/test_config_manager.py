import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from configs.config_manager import ConfigManager

manager = ConfigManager(
    "configs/default.yaml"
)

config = manager.update(
    distance=7,
    rounds=7,
    noise=0.002,
    shots=50000,
)

print("=" * 60)
print("Updated Configuration")
print("=" * 60)

print(config)

manager.save(
    config,
    "results/raw/example_config.yaml"
)

print()
print("Configuration saved successfully.")
