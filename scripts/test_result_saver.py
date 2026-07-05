import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from experiments.baseline.save_results import ResultSaver

data = pd.DataFrame({

    "distance":

        [3, 5, 7],

    "logical_error":

        [0.01, 0.003, 0.0008]

})

saver = ResultSaver(

    "results/raw"

)

saver.save_csv(

    data,

    "example.csv"

)
