import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from utils.timer import Timer

from utils.system_info import get_system_info

from utils.logger import ExperimentLogger

print("=" * 60)

print("Testing Utilities")

print("=" * 60)

timer = Timer()

timer.start()

x = sum(range(1000000))

timer.stop()

print()

print("Elapsed")

print(timer.elapsed)

print()

info = get_system_info()

print(info)

logger = ExperimentLogger()

logger.write(

    "example_log.json",

    {

        "runtime": timer.elapsed,

        "system": info,

    },

)

print()

print("Utilities working successfully.")
