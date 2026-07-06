"""
===========================================================
Publication Figure Generator
===========================================================

Generates publication-quality figures and tables
from baseline_full_results.csv

Outputs

plots/publication/png/
plots/publication/pdf/
tables/publication/

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import ticker

from scipy.interpolate import interp1d

# ==========================================================
# Create output directories
# ==========================================================

PNG_DIR = Path("plots/publication/png")
PDF_DIR = Path("plots/publication/pdf")
TABLE_DIR = Path("tables/publication")

PNG_DIR.mkdir(parents=True, exist_ok=True)
PDF_DIR.mkdir(parents=True, exist_ok=True)
TABLE_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Read experiment results
# ==========================================================

CSV_FILE = "results/publication/baseline_full_results.csv"

df = pd.read_csv(CSV_FILE)

print()

print("=" * 60)
print("Publication Results Loaded")
print("=" * 60)

print(df.head())

print()

print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")

# ==========================================================
# Journal plotting style
# ==========================================================

plt.rcParams.update({

    "figure.figsize": (7.0, 5.2),

    "figure.dpi": 150,

    "savefig.dpi": 600,

    "font.size": 12,

    "axes.titlesize": 14,

    "axes.labelsize": 13,

    "xtick.labelsize": 11,

    "ytick.labelsize": 11,

    "legend.fontsize": 11,

    "lines.linewidth": 2.2,

    "lines.markersize": 7,

    "axes.grid": True,

    "grid.alpha": 0.30,

    "axes.spines.top": False,

    "axes.spines.right": False,

    "savefig.bbox": "tight",

    "savefig.pad_inches": 0.05,
})

# ==========================================================
# Save figure
# ==========================================================

def save_figure(fig, filename):

    png_file = PNG_DIR / f"{filename}.png"

    pdf_file = PDF_DIR / f"{filename}.pdf"

    fig.savefig(
        png_file,
        dpi=600,
    )

    fig.savefig(
        pdf_file,
    )

    plt.close(fig)

    print(f"Saved : {png_file}")

    print(f"Saved : {pdf_file}")

    print()

# ==========================================================
# Axis formatting
# ==========================================================

def publication_axes(ax):

    ax.grid(True)

    ax.tick_params(
        direction="in",
        length=6,
        width=1,
    )

    ax.minorticks_on()

    ax.grid(
        which="minor",
        alpha=0.15,
    )

    return ax

# ==========================================================
# Publication colors
# ==========================================================

COLORS = [

    "#1f77b4",

    "#d62728",

    "#2ca02c",

    "#9467bd",

    "#ff7f0e",

    "#8c564b",

    "#17becf",

    "#e377c2",
]

# ==========================================================
# Figure 1
# Threshold Curve
# ==========================================================

def figure1_threshold():

    fig, ax = plt.subplots()

    distances = sorted(df["distance"].unique())

    for i, distance in enumerate(distances):

        subset = (
            df[df["distance"] == distance]
            .sort_values("noise")
        )

        ax.plot(
            subset["noise"],
            subset["mean_logical_error"],
            marker="o",
            color=COLORS[i % len(COLORS)],
            label=f"d={distance}",
        )

    ax.set_xlabel("Physical Error Probability")

    ax.set_ylabel("Logical Error Rate")

    ax.set_title("Logical Error Threshold")

    ax.set_xscale("log")

    ax.set_yscale("log")

    publication_axes(ax)

    ax.legend()

    save_figure(
        fig,
        "figure1_threshold_curve",
    )

# ==========================================================
# Figure 2
# Distance Scaling
# ==========================================================

def figure2_distance_scaling():

    fig, ax = plt.subplots()

    noise_levels = sorted(df["noise"].unique())

    for i, noise in enumerate(noise_levels):

        subset = (
            df[df["noise"] == noise]
            .sort_values("distance")
        )

        ax.plot(
            subset["distance"],
            subset["mean_logical_error"],
            marker="s",
            linewidth=2,
            color=COLORS[i % len(COLORS)],
            label=f"p={noise}",
        )

    ax.set_xlabel("Code Distance")

    ax.set_ylabel("Logical Error Rate")

    ax.set_title("Logical Error Scaling with Distance")

    ax.set_yscale("log")

    publication_axes(ax)

    ax.legend(
        fontsize=9,
        ncol=2,
    )

    save_figure(
        fig,
        "figure2_distance_scaling",
    )

# ==========================================================
# Figure 3
# Accuracy Heatmap
# ==========================================================

def figure3_accuracy_heatmap():

    fig, ax = plt.subplots(figsize=(8,6))

    heatmap = df.pivot(
        index="distance",
        columns="noise",
        values="mean_accuracy",
    )

    image = ax.imshow(
        heatmap.values,
        aspect="auto",
        origin="lower",
    )

    ax.set_xticks(
        np.arange(len(heatmap.columns))
    )

    ax.set_xticklabels(
        [
            f"{x:.0e}"
            for x in heatmap.columns
        ],
        rotation=45,
    )

    ax.set_yticks(
        np.arange(len(heatmap.index))
    )

    ax.set_yticklabels(
        heatmap.index,
    )

    ax.set_xlabel("Physical Error Probability")

    ax.set_ylabel("Code Distance")

    ax.set_title("Decoder Accuracy Heatmap")

    cbar = plt.colorbar(
        image,
        ax=ax,
    )

    cbar.set_label("Accuracy")

    save_figure(
        fig,
        "figure3_accuracy_heatmap",
    )


# ==========================================================
# Figure 4
# Runtime
# ==========================================================

def figure4_runtime():

    fig, ax = plt.subplots()

    runtime = (
        df.groupby("distance")
        .agg(
            runtime=("mean_runtime", "mean"),
            runtime_std=("std_runtime", "mean"),
        )
        .reset_index()
    )

    ax.errorbar(
        runtime["distance"],
        runtime["runtime"],
        yerr=runtime["runtime_std"],
        marker="o",
        markersize=7,
        linewidth=2.5,
        capsize=5,
        color=COLORS[0],
    )

    ax.set_xlabel("Code Distance")

    ax.set_ylabel("Runtime (seconds)")

    ax.set_title("Decoder Runtime")

    publication_axes(ax)

    save_figure(
        fig,
        "figure4_runtime",
    )

# ==========================================================
# Figure 5
# Throughput
# ==========================================================

def figure5_throughput():

    fig, ax = plt.subplots()

    throughput = (
        df.groupby("distance")
        .agg(
            throughput=("mean_throughput", "mean"),
            throughput_std=("std_throughput", "mean"),
        )
        .reset_index()
    )

    ax.errorbar(
        throughput["distance"],
        throughput["throughput"],
        yerr=throughput["throughput_std"],
        marker="s",
        markersize=7,
        linewidth=2.5,
        capsize=5,
        color=COLORS[2],
    )

    ax.set_xlabel("Code Distance")

    ax.set_ylabel("Throughput (Shots / Second)")

    ax.set_title("Decoder Throughput")

    ax.ticklabel_format(
        axis="y",
        style="sci",
        scilimits=(0, 0),
    )

    publication_axes(ax)

    save_figure(
        fig,
        "figure5_throughput",
    )

# ==========================================================
# Figure 6
# Detector Growth
# ==========================================================

def figure6_detectors():

    fig, ax = plt.subplots()

    detector_df = (
        df.groupby("distance")
        .agg(
            detectors=("detectors", "mean"),
        )
        .reset_index()
    )

    ax.plot(
        detector_df["distance"],
        detector_df["detectors"],
        marker="^",
        linewidth=2.5,
        markersize=8,
        color=COLORS[3],
    )

    ax.set_xlabel("Code Distance")

    ax.set_ylabel("Number of Detectors")

    ax.set_title("Growth of Detector Count")

    publication_axes(ax)

    save_figure(
        fig,
        "figure6_detector_growth",
    )

# ==========================================================
# Figure 7
# Circuit Size Growth
# ==========================================================

def figure7_operations():

    fig, ax = plt.subplots()

    operations = (
        df.groupby("distance")
        .agg(
            operations=("operations", "mean"),
        )
        .reset_index()
    )

    ax.plot(
        operations["distance"],
        operations["operations"],
        marker="D",
        linewidth=2.5,
        markersize=8,
        color=COLORS[4],
    )

    ax.set_xlabel("Code Distance")
    ax.set_ylabel("Circuit Operations")
    ax.set_title("Circuit Size Growth")

    publication_axes(ax)

    save_figure(
        fig,
        "figure7_circuit_growth",
    )

# ==========================================================
# Figure 8
# Decoder Accuracy
# ==========================================================

def figure8_accuracy():

    fig, ax = plt.subplots()

    accuracy = (
        df.groupby("distance")
        .agg(
            accuracy=("mean_accuracy", "mean"),
            accuracy_std=("std_accuracy", "mean"),
        )
        .reset_index()
    )

    ax.errorbar(
        accuracy["distance"],
        accuracy["accuracy"],
        yerr=accuracy["accuracy_std"],
        marker="o",
        linewidth=2.5,
        markersize=7,
        capsize=5,
        color=COLORS[5],
    )

    ax.set_ylim(0.98, 1.001)

    ax.set_xlabel("Code Distance")
    ax.set_ylabel("Accuracy")
    ax.set_title("Baseline Decoder Accuracy")

    publication_axes(ax)

    save_figure(
        fig,
        "figure8_accuracy",
    )

# ==========================================================
# Figure 9
# Runtime Scaling
# ==========================================================

def figure9_runtime_scaling():

    fig, ax = plt.subplots()

    runtime = (
        df.groupby("distance")
        .agg(
            runtime=("mean_runtime", "mean"),
        )
        .reset_index()
    )

    ax.loglog(
        runtime["distance"],
        runtime["runtime"],
        marker="o",
        linewidth=2.5,
        markersize=8,
        color=COLORS[6],
    )

    ax.set_xlabel("Code Distance")
    ax.set_ylabel("Runtime (s)")
    ax.set_title("Runtime Scaling")

    publication_axes(ax)

    save_figure(
        fig,
        "figure9_runtime_scaling",
    )

# ==========================================================
# Figure 10
# Estimated Memory Growth
# ==========================================================

def figure10_memory():

    fig, ax = plt.subplots()

    memory = (
        df.groupby("distance")
        .agg(
            detectors=("detectors", "mean"),
        )
        .reset_index()
    )

    # Approximate bytes per detector state (proxy)
    memory["memory_mb"] = memory["detectors"] * 8 / (1024 * 1024)

    ax.plot(
        memory["distance"],
        memory["memory_mb"],
        marker="s",
        linewidth=2.5,
        markersize=8,
        color=COLORS[7],
    )

    ax.set_xlabel("Code Distance")
    ax.set_ylabel("Estimated Memory (MB)")
    ax.set_title("Estimated Decoder Memory Growth")

    publication_axes(ax)

    save_figure(
        fig,
        "figure10_memory",
    )

# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    print()

    print("=" * 60)

    print("Publication Figure Generation")

    print("=" * 60)

    print()

    print("Generating Figure 1")
    figure1_threshold()

    print("Generating Figure 2")
    figure2_distance_scaling()

    print("Generating Figure 3")
    figure3_accuracy_heatmap()

    print("Generating Figure 4")
    figure4_runtime()

    print("Generating Figure 5")
    figure5_throughput()

    print("Generating Figure 6")
    figure6_detectors()

    print("Generating Figure 7")
    figure7_operations()

    print("Generating Figure 8")
    figure8_accuracy()

    print("Generating Figure 9")
    figure9_runtime_scaling()

    print("Generating Figure 10")
    figure10_memory()

    print()

    print("=" * 60)
    print("Figures 1-10 completed.")
    print("=" * 60)
