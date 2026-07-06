from pathlib import Path

import pandas as pd

from evaluation.adaptive_decoder import AdaptiveDecoder

decoder = AdaptiveDecoder(
    "results/evaluation/d7.csv"
)

rows = []

for threshold in [

    0.60,
    0.70,
    0.80,
    0.90,
    0.95,

]:

    rows.append(
        decoder.evaluate(threshold)
    )

df = pd.DataFrame(rows)

Path("results/adaptive").mkdir(
    parents=True,
    exist_ok=True,
)

df.to_csv(

    "results/adaptive/adaptive_results.csv",

    index=False,

)

print(df)
