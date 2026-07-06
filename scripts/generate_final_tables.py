from pathlib import Path

import pandas as pd

Path("tables").mkdir(exist_ok=True)

# Table 7
pd.read_csv(
    "results/adaptive/adaptive_results.csv"
).to_csv(
    "tables/Table7_AdaptiveRouting.csv",
    index=False,
)

# Table 8
pd.read_csv(
    "results/summary/noise_summary.csv"
).to_csv(
    "tables/Table8_NoiseSweep.csv",
    index=False,
)

# Table 9
pd.read_csv(
    "results/summary/distance_summary.csv"
).to_csv(
    "tables/Table9_DistanceSweep.csv",
    index=False,
)

# Table 10
pd.read_csv(
    "results/throughput/throughput.csv"
).to_csv(
    "tables/Table10_Throughput.csv",
    index=False,
)

print("Publication tables generated.")
