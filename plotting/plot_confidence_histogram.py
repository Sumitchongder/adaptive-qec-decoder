from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("results/evaluation/d7.csv")

plt.figure(figsize=(6,4))

plt.hist(
    df["confidence"],
    bins=30,
)

plt.xlabel("Prediction Confidence")
plt.ylabel("Samples")
plt.title("Confidence Distribution (Distance = 7)")

Path("figures").mkdir(exist_ok=True)

plt.tight_layout()

plt.savefig(
    "figures/Figure13_confidence_histogram.pdf",
    dpi=300,
)

plt.savefig(
    "figures/Figure13_confidence_histogram.png",
    dpi=300,
)

print("Figure 13 generated.")
