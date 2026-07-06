from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("results/summary/noise_summary.csv")

df = df.sort_values("noise")

plt.figure(figsize=(6,4))

plt.plot(
    df["noise"],
    df["accuracy"],
    marker="o",
)

plt.xlabel("Physical error probability")

plt.ylabel("Logical accuracy")

plt.grid(True)

plt.tight_layout()

Path("figures").mkdir(exist_ok=True)

plt.savefig("figures/figure16_noise_accuracy.pdf")

plt.savefig("figures/figure16_noise_accuracy.png")

plt.close()
