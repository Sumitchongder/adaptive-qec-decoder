#!/usr/bin/env python3
"""
===========================================================
Table 9
Scalability Summary
===========================================================

Reads:
    results/summary_statistics.csv

Outputs:
    tables/table9.csv
    tables/table9.tex
===========================================================
"""

from pathlib import Path
import pandas as pd

# --------------------------------------------------------
# Project paths
# --------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

summary_file = PROJECT_ROOT / "paper" / "tables" / "summary_statistics.csv"

if not summary_file.exists():
    raise FileNotFoundError(summary_file)

output_dir = PROJECT_ROOT / "tables"
output_dir.mkdir(exist_ok=True)

# --------------------------------------------------------
# Read summary statistics
# --------------------------------------------------------

df = pd.read_csv(summary_file)

# --------------------------------------------------------
# Group by code distance
# --------------------------------------------------------

summary = (
    df.groupby("distance")
      .agg({
          "detectors":"mean",
          "operations":"mean",
          "mean_runtime":"mean",
          "mean_accuracy":"mean",
          "mean_logical_error":"mean",
          "mean_throughput":"mean"
      })
      .reset_index()
)

summary.columns = [
    "Code Distance",
    "Detectors",
    "Operations",
    "Runtime (s)",
    "Accuracy",
    "Logical Error",
    "Throughput (shots/s)"
]

# --------------------------------------------------------
# Formatting
# --------------------------------------------------------

summary["Detectors"] = summary["Detectors"].astype(int)
summary["Operations"] = summary["Operations"].astype(int)

summary["Runtime (s)"] = summary["Runtime (s)"].map("{:.6f}".format)

summary["Accuracy"] = summary["Accuracy"].map("{:.6f}".format)

summary["Logical Error"] = summary["Logical Error"].map("{:.6e}".format)

summary["Throughput (shots/s)"] = (
    summary["Throughput (shots/s)"]
    .round(2)
)

# --------------------------------------------------------
# Save CSV
# --------------------------------------------------------

csv_out = output_dir / "table9.csv"

summary.to_csv(csv_out,index=False)

# --------------------------------------------------------
# Save LaTeX
# --------------------------------------------------------

latex = summary.to_latex(
    index=False,
    escape=False,
    caption="Scalability of the proposed QEC co-design framework across code distances.",
    label="tab:scalability"
)

tex_out = output_dir / "table9.tex"

with open(tex_out,"w") as f:
    f.write(latex)

print()

print("Generated:")

print(csv_out)

print(tex_out)

print()
print(summary)
