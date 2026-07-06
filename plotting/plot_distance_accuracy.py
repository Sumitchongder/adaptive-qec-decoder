from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("results/summary/distance_summary.csv")

plt.figure(figsize=(6,4))

plt.plot(
    df["distance"],
    df["accuracy"],
    marker="o",
)

plt.xlabel("Code distance")

plt.ylabel("Logical accuracy")

plt.grid(True)

plt.tight_layout()

Path("figures").mkdir(exist_ok=True)

plt.savefig("figures/figure13_distance_accuracy.pdf")

plt.savefig("figures/figure13_distance_accuracy.png")

plt.close()
