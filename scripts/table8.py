#!/usr/bin/env python3
"""
Table 8
Computational Complexity Analysis

Outputs:
    tables/table8.csv
    tables/table8.tex
"""

from pathlib import Path
import pandas as pd

# --------------------------------------------------------
# Output directory
# --------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "tables"
OUTPUT_DIR.mkdir(exist_ok=True)

# --------------------------------------------------------
# Complexity Table
# --------------------------------------------------------

table = pd.DataFrame({

    "Component":[
        "Noise-aware Circuit Generation",
        "Stim Circuit Simulation",
        "Syndrome Extraction",
        "Adaptive Neural Decoder",
        "Confidence Estimation",
        "BP / OSD Refinement",
        "Recovery Application",
        "Latency-aware Optimizer"
    ],

    "Time Complexity":[
        r"$O(n)$",
        r"$O(n)$",
        r"$O(n)$",
        r"$O(P)$",
        r"$O(C)$",
        r"$O(EI)$",
        r"$O(n)$",
        r"$O(KM)$"
    ],

    "Memory Complexity":[
        r"$O(n)$",
        r"$O(n)$",
        r"$O(n)$",
        r"$O(P)$",
        r"$O(C)$",
        r"$O(E)$",
        r"$O(n)$",
        r"$O(K)$"
    ],

    "Parallelization":[
        "Excellent",
        "Excellent",
        "Excellent",
        "GPU-native",
        "GPU-native",
        "Moderate",
        "Excellent",
        "Excellent"
    ],

    "Notes":[
        "Generate hardware-constrained stabilizer circuits",
        "Fast stabilizer simulation",
        "Detector measurement extraction",
        "Batch neural inference",
        "Threshold-based escalation",
        "Fallback high-accuracy decoding",
        "Logical correction",
        "Multi-objective search"
    ]

})

# --------------------------------------------------------
# Save CSV
# --------------------------------------------------------

csv_file = OUTPUT_DIR / "table8.csv"
table.to_csv(csv_file, index=False)

# --------------------------------------------------------
# Save LaTeX
# --------------------------------------------------------

latex_file = OUTPUT_DIR / "table8.tex"

latex = table.to_latex(
    index=False,
    escape=False,
    caption="Computational complexity of the proposed hardware-aware QEC co-design framework.",
    label="tab:complexity"
)

with open(latex_file, "w") as f:
    f.write(latex)

print("Generated:")
print(csv_file)
print(latex_file)
print("\nDone.")
