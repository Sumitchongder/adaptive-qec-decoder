"""
Publication Plot Generator
==========================

Generates all publication-quality figures and tables from the
baseline experiment CSV.

Outputs
-------
plots/publication/
results/publication/tables/

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.ticker import ScalarFormatter

# ------------------------------------------------------------
# Global plotting style
# ------------------------------------------------------------

plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300

plt.rcParams["font.size"] = 12
plt.rcParams["axes.labelsize"] = 13
plt.rcParams["axes.titlesize"] = 15

plt.rcParams["legend.fontsize"] = 11

plt.rcParams["xtick.labelsize"] = 11
plt.rcParams["ytick.labelsize"] = 11

plt.rcParams["lines.linewidth"] = 2.5

plt.rcParams["axes.grid"] = True

plt.rcParams["grid.alpha"] = 0.30

plt.rcParams["figure.figsize"] = (7,5)

# ------------------------------------------------------------
# Directories
# ------------------------------------------------------------

RESULT_DIR = Path("results/publication")

PLOT_DIR = Path("plots/publication")

PDF_DIR = PLOT_DIR / "pdf"

TABLE_DIR = RESULT_DIR / "tables"

PLOT_DIR.mkdir(parents=True, exist_ok=True)

PDF_DIR.mkdir(parents=True, exist_ok=True)

TABLE_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------
# Read CSV
# ------------------------------------------------------------

csv_file = RESULT_DIR / "baseline_full_results.csv"

print("="*60)
print("Loading CSV")
print("="*60)

print(csv_file)

df = pd.read_csv(csv_file)

print()

print(df.head())

print()

print("Rows :", len(df))

print("Columns :", len(df.columns))

print()

# ------------------------------------------------------------
# Sort values
# ------------------------------------------------------------

df = df.sort_values(
    by=[
        "distance",
        "noise"
    ]
).reset_index(drop=True)

print("Distances")

print(sorted(df["distance"].unique()))

print()

print("Noise values")

print(sorted(df["noise"].unique()))

print()

# ------------------------------------------------------------
# Useful arrays
# ------------------------------------------------------------

distances = sorted(df.distance.unique())

noise_values = sorted(df.noise.unique())

print("Unique distances :", distances)

print("Unique noise :", noise_values)

print()

# ------------------------------------------------------------
# Helper function
# ------------------------------------------------------------

def save_figure(name):

    png = PLOT_DIR / f"{name}.png"

    pdf = PDF_DIR / f"{name}.pdf"

    plt.tight_layout()

    plt.savefig(
        png,
        dpi=300,
        bbox_inches="tight",
    )

    plt.savefig(
        pdf,
        bbox_inches="tight",
    )

    print("Saved")

    print(png)

    print(pdf)

    print()

    plt.close()

print("="*60)
print("Initialization complete")
print("="*60)

# ============================================================
# Figure 1
# Threshold Curve
# ============================================================

print("=" * 60)
print("Generating Figure 1 : Threshold Curve")
print("=" * 60)

plt.figure(figsize=(8, 6))

for distance in distances:

    subset = df[df["distance"] == distance]

    plt.plot(
        subset["noise"],
        subset["mean_logical_error"],
        marker="o",
        linewidth=2,
        markersize=6,
        label=f"d={distance}",
    )

plt.xlabel("Physical Error Probability")

plt.ylabel("Logical Error Rate")

plt.title("Threshold Curve")

plt.xscale("log")

plt.yscale("log")

plt.legend()

save_figure("Figure1_threshold_curve")

# ============================================================
# Figure 2
# Distance Scaling
# ============================================================

print("=" * 60)
print("Generating Figure 2 : Distance Scaling")
print("=" * 60)

lowest_noise = min(noise_values)

subset = df[df["noise"] == lowest_noise]

plt.figure(figsize=(8, 6))

plt.plot(
    subset["distance"],
    subset["mean_logical_error"],
    marker="o",
    linewidth=2,
)

plt.xlabel("Code Distance")

plt.ylabel("Logical Error Rate")

plt.title(
    f"Logical Error vs Distance (Noise={lowest_noise})"
)

plt.yscale("log")

save_figure("Figure2_distance_scaling")

# ============================================================
# Figure 3
# Accuracy Heatmap
# ============================================================

print("=" * 60)
print("Generating Figure 3 : Accuracy Heatmap")
print("=" * 60)

pivot = df.pivot(
    index="distance",
    columns="noise",
    values="mean_accuracy",
)

plt.figure(figsize=(9, 6))

image = plt.imshow(
    pivot,
    aspect="auto",
    origin="lower",
)

plt.colorbar(
    image,
    label="Accuracy",
)

plt.xticks(
    range(len(pivot.columns)),
    [f"{x:.4f}" for x in pivot.columns],
    rotation=45,
)

plt.yticks(
    range(len(pivot.index)),
    pivot.index,
)

plt.xlabel("Physical Error Probability")

plt.ylabel("Code Distance")

plt.title("Decoder Accuracy Heatmap")

save_figure("Figure3_accuracy_heatmap")

