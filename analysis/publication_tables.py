"""
Generate publication tables.

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path

import pandas as pd


RESULT_FILE = "results/publication/baseline_full_results.csv"

OUTPUT_DIR = Path("paper/tables")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


df = pd.read_csv(RESULT_FILE)

print("=" * 60)
print("Generating Publication Tables")
print("=" * 60)

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

table1.to_markdown(
    OUTPUT_DIR / "table1_accuracy.md",
    index=False,
)

table1.to_latex(
    OUTPUT_DIR / "table1_accuracy.tex",
    index=False,
    float_format="%.6f",
)

print("Table 1 saved.")

table2 = (
    df[
        [
            "distance",
            "noise",
            "mean_logical_error",
            "std_logical_error",
        ]
    ]
)

table2.to_csv(
    OUTPUT_DIR / "table2_logical_error.csv",
    index=False,
)

table2.to_markdown(
    OUTPUT_DIR / "table2_logical_error.md",
    index=False,
)

table2.to_latex(
    OUTPUT_DIR / "table2_logical_error.tex",
    index=False,
    float_format="%.6e",
)

print("Table 2 saved.")

table3 = (
    df[
        [
            "distance",
            "noise",
            "mean_runtime",
            "std_runtime",
        ]
    ]
)

table3.to_csv(
    OUTPUT_DIR / "table3_runtime.csv",
    index=False,
)

table3.to_markdown(
    OUTPUT_DIR / "table3_runtime.md",
    index=False,
)

table3.to_latex(
    OUTPUT_DIR / "table3_runtime.tex",
    index=False,
)

print("Table 3 saved.")

table4 = (
    df[
        [
            "distance",
            "noise",
            "mean_throughput",
            "std_throughput",
        ]
    ]
)

table4.to_csv(
    OUTPUT_DIR / "table4_throughput.csv",
    index=False,
)

table4.to_markdown(
    OUTPUT_DIR / "table4_throughput.md",
    index=False,
)

table4.to_latex(
    OUTPUT_DIR / "table4_throughput.tex",
    index=False,
)

print("Table 4 saved.")

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
)

table5.to_csv(
    OUTPUT_DIR / "table5_hardware.csv",
    index=False,
)

table5.to_markdown(
    OUTPUT_DIR / "table5_hardware.md",
    index=False,
)

table5.to_latex(
    OUTPUT_DIR / "table5_hardware.tex",
    index=False,
)

print("Table 5 saved.")

summary = df.describe()

summary.to_csv(
    OUTPUT_DIR / "summary_statistics.csv"
)

summary.to_markdown(
    OUTPUT_DIR / "summary_statistics.md"
)

summary.to_latex(
    OUTPUT_DIR / "summary_statistics.tex"
)

print("Summary saved.")

print()
print("=" * 60)
print("All publication tables generated.")
print("=" * 60)


