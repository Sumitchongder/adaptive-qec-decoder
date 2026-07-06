from pathlib import Path
import re

import pandas as pd


rows = []

for csv_file in sorted(Path("results/evaluation").glob("d*.csv")):

    distance = int(re.findall(r"\d+", csv_file.stem)[0])

    df = pd.read_csv(csv_file)

    rows.append({

        "distance": distance,
        "samples": len(df),
        "accuracy": df["correct"].mean(),
        "avg_confidence": df["confidence"].mean(),
        "avg_latency_us": df["latency_us"].mean(),
        "throughput": len(df) / (df["latency_us"].sum()/1e6),

    })

summary = pd.DataFrame(rows)

summary = summary.sort_values("distance")

output = Path("results/summary")
output.mkdir(parents=True, exist_ok=True)

summary.to_csv(
    output/"distance_summary.csv",
    index=False,
)

print(summary)
