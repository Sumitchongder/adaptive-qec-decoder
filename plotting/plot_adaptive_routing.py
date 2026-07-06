from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "results/adaptive/adaptive_results.csv"
)

plt.figure(figsize=(6,4))

plt.plot(

    df["threshold"],

    df["accuracy"],

    marker="o",

)

plt.xlabel("Confidence Threshold")
plt.ylabel("Logical Accuracy")
plt.title("Adaptive Neural/PyMatching Routing")

Path("figures").mkdir(exist_ok=True)

plt.tight_layout()

plt.savefig(
    "figures/Figure14_adaptive.pdf",
    dpi=300,
)

plt.savefig(
    "figures/Figure14_adaptive.png",
    dpi=300,
)

print("Figure 14 generated.")
