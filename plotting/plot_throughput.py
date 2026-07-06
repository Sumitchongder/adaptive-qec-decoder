from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(
    "results/throughput/throughput.csv"
)

plt.figure(figsize=(6,4))

plt.plot(

    df["batch_size"],

    df["throughput"],

    marker="o",

)

plt.xlabel("Batch Size")

plt.ylabel("Samples / Second")

plt.title("Neural Decoder Throughput")

plt.grid(True)

Path("figures").mkdir(exist_ok=True)

plt.tight_layout()

plt.savefig(

    "figures/Figure17_throughput.pdf",

    dpi=300,

)

plt.savefig(

    "figures/Figure17_throughput.png",

    dpi=300,

)

print("Figure 17 generated.")
