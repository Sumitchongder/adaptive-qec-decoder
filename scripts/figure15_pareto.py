#!/usr/bin/env python3
"""
Figure 15
Latency vs Logical Error Pareto Frontier

Input:
    results/summary_statistics.csv

Outputs:
    figures/figure15_pareto.pdf
    figures/figure15_pareto.png
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12
})

# ---------------------------------------------------------
# Read data
# ---------------------------------------------------------

csv_file = "paper/tables/summary_statistics.csv"

if not os.path.exists(csv_file):
    raise FileNotFoundError(f"{csv_file} not found")

df = pd.read_csv(csv_file)

runtime = df["mean_runtime"]
logical = df["mean_logical_error"]
distance = df["distance"]

# ---------------------------------------------------------
# Compute Pareto frontier
# ---------------------------------------------------------

points = list(zip(runtime, logical))

pareto = []

for i, (x, y) in enumerate(points):

    dominated = False

    for j, (x2, y2) in enumerate(points):

        if j == i:
            continue

        if (x2 <= x and y2 <= y) and (x2 < x or y2 < y):
            dominated = True
            break

    if not dominated:
        pareto.append(i)

pareto_df = df.iloc[pareto].sort_values("mean_runtime")

# ---------------------------------------------------------
# Plot
# ---------------------------------------------------------

fig, ax = plt.subplots(figsize=(8,6))

scatter = ax.scatter(
    runtime,
    logical,
    c=distance,
    s=80
)

# annotate distances

for _, row in df.iterrows():

    ax.text(
        row["mean_runtime"]*1.01,
        row["mean_logical_error"]+0.00005,
        f"d={int(row['distance'])}",
        fontsize=9
    )

# Pareto line

ax.plot(
    pareto_df["mean_runtime"],
    pareto_df["mean_logical_error"],
    linewidth=2,
    label="Pareto Frontier"
)

# highlight Pareto points

ax.scatter(
    pareto_df["mean_runtime"],
    pareto_df["mean_logical_error"],
    s=150,
    marker="*",
    label="Pareto-optimal"
)

cbar = plt.colorbar(scatter)
cbar.set_label("Code Distance")

ax.set_xlabel("Mean Runtime (s)")
ax.set_ylabel("Mean Logical Error Rate")

ax.set_title(
    "Latency–Logical Error Pareto Frontier",
    fontsize=16,
    weight="bold"
)

ax.grid(True)

ax.legend()

plt.tight_layout()

os.makedirs("figures", exist_ok=True)

plt.savefig(
    "figures/figure15_pareto.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "figures/figure15_pareto.pdf",
    bbox_inches="tight"
)

print("Figure 15 generated successfully.")
