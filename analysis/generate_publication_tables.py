"""
Generate Publication Tables
===========================

Creates all publication-ready tables from the
baseline experimental CSV.

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path

import pandas as pd
import numpy as np


# -------------------------------------------------------
# Input / Output
# -------------------------------------------------------

INPUT_CSV = Path(
    "results/publication/baseline_full_results.csv"
)

OUTPUT_DIR = Path(
    "results/tables"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

df = pd.read_csv(INPUT_CSV)

print("=" * 60)
print("Generating Publication Tables")
print("=" * 60)

print()

print("Rows Loaded :", len(df))

print()

# ==========================================================
# TABLE 1
# Baseline Accuracy
# ==========================================================

table1 = (
    df[
        [
            "distance",
            "noise",
            "mean_accuracy",
            "std_accuracy",
        ]
    ]
    .sort_values(
        ["distance", "noise"]
    )
)

table1.to_csv(
    OUTPUT_DIR / "table1_accuracy.csv",
    index=False,
)

print("✓ Table 1 saved")

# ==========================================================
# TABLE 2
# Logical Error
# ==========================================================

table2 = (
    df[
        [
            "distance",
            "noise",
            "mean_logical_error",
            "std_logical_error",
        ]
    ]
    .sort_values(
        ["distance", "noise"]
    )
)

table2.to_csv(
    OUTPUT_DIR / "table2_logical_error.csv",
    index=False,
)

print("✓ Table 2 saved")

# ==========================================================
# TABLE 3
# Runtime
# ==========================================================

table3 = (
    df[
        [
            "distance",
            "noise",
            "mean_runtime",
            "std_runtime",
        ]
    ]
    .sort_values(
        ["distance", "noise"]
    )
)

table3.to_csv(
    OUTPUT_DIR / "table3_runtime.csv",
    index=False,
)

print("✓ Table 3 saved")

table4 = (
    df[
        [
            "distance",
            "noise",
            "mean_throughput",
            "std_throughput",
        ]
    ]
    .sort_values(
        ["distance", "noise"]
    )
)

table4.to_csv(
    OUTPUT_DIR / "table4_throughput.csv",
    index=False,
)

print("✓ Table 4 saved")

table5 = (
    df[
        [
            "distance",
            "detectors",
            "observables",
            "operations",
        ]
    ]
    .drop_duplicates()
    .sort_values(
        "distance"
    )
)

table5.to_csv(
    OUTPUT_DIR / "table5_decoder_statistics.csv",
    index=False,
)

print("✓ Table 5 saved")

table6 = (
    df.groupby("distance")
    .agg(
        mean_runtime=("mean_runtime", "mean"),
        mean_throughput=("mean_throughput", "mean"),
        mean_accuracy=("mean_accuracy", "mean"),
        mean_logical_error=("mean_logical_error", "mean"),
        detectors=("detectors", "mean"),
        operations=("operations", "mean"),
    )
    .reset_index()
)

table6.to_csv(
    OUTPUT_DIR / "table6_scaling_summary.csv",
    index=False,
)

print("✓ Table 6 saved")

summary = []

for distance in sorted(df["distance"].unique()):

    subset = df[
        df["distance"] == distance
    ]

    runtime = subset["mean_runtime"]

    logical = subset["mean_logical_error"]

    accuracy = subset["mean_accuracy"]

    summary.append({

        "distance": distance,

        "runtime_mean": runtime.mean(),

        "runtime_median": runtime.median(),

        "runtime_std": runtime.std(),

        "runtime_variance": runtime.var(),

        "runtime_min": runtime.min(),

        "runtime_max": runtime.max(),

        "logical_mean": logical.mean(),

        "logical_std": logical.std(),

        "accuracy_mean": accuracy.mean(),

        "accuracy_std": accuracy.std(),

    })

table7 = pd.DataFrame(summary)

table7.to_csv(
    OUTPUT_DIR / "table7_summary_statistics.csv",
    index=False,
)

print("✓ Table 7 saved")


print()

print("=" * 60)
print("All Publication Tables Generated Successfully")
print("=" * 60)

print()

print("Tables saved to:")

print(OUTPUT_DIR)
