#!/usr/bin/env python3
"""
Table 6
Throughput Summary

Reads:
    results/table4_throughput.csv

Outputs:
    tables/table6.csv
    tables/table6.tex
"""

from pathlib import Path
import pandas as pd

# --------------------------------------------------------
# Project directories
# --------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

input_file = PROJECT_ROOT / "paper" / "tables" / "table4_throughput.csv"

output_dir = PROJECT_ROOT / "tables"
output_dir.mkdir(exist_ok=True)

if not input_file.exists():
    raise FileNotFoundError(input_file)

# --------------------------------------------------------
# Read CSV
# --------------------------------------------------------

df = pd.read_csv(input_file)

print("\nColumns detected:")
print(df.columns.tolist())

# --------------------------------------------------------
# Try to identify columns automatically
# --------------------------------------------------------

cols = {c.lower(): c for c in df.columns}

distance_col = None
throughput_col = None
std_col = None

for c in df.columns:

    lc = c.lower()

    if "distance" in lc:
        distance_col = c

    elif "throughput" in lc and "std" not in lc:
        throughput_col = c

    elif "std" in lc and "throughput" in lc:
        std_col = c

# --------------------------------------------------------
# If summary file format
# --------------------------------------------------------

if throughput_col is None:

    for c in df.columns:

        if "mean_throughput" in c.lower():
            throughput_col = c

        if "std_throughput" in c.lower():
            std_col = c

# --------------------------------------------------------

if distance_col is None or throughput_col is None:

    raise RuntimeError(
        "Unable to identify throughput columns.\n"
        "Detected columns:\n"
        + str(df.columns.tolist())
    )

# --------------------------------------------------------
# Create publication table
# --------------------------------------------------------

table = pd.DataFrame()

table["Code Distance"] = df[distance_col]

table["Mean Throughput (shots/s)"] = (
    df[throughput_col].round(2)
)

if std_col is not None:

    table["Std. Dev."] = (
        df[std_col].round(2)
    )

# --------------------------------------------------------
# Save CSV
# --------------------------------------------------------

csv_file = output_dir / "table6.csv"

table.to_csv(csv_file, index=False)

# --------------------------------------------------------
# Save LaTeX
# --------------------------------------------------------

latex_file = output_dir / "table6.tex"

latex = table.to_latex(
    index=False,
    float_format="%.2f",
    caption="Decoder throughput across code distances.",
    label="tab:throughput",
    escape=False
)

with open(latex_file, "w") as f:
    f.write(latex)

print("\nGenerated:")
print(csv_file)
print(latex_file)

print("\nDone.")
