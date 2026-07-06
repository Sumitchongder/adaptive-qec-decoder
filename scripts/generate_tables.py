from pathlib import Path

import pandas as pd


out = Path("tables")
out.mkdir(exist_ok=True)

distance = pd.read_csv("results/summary/distance_summary.csv")

noise = pd.read_csv("results/summary/noise_summary.csv")

distance.to_csv(out / "table7.csv", index=False)

noise.to_csv(out / "table8.csv", index=False)

distance.to_latex(out / "table7.tex", index=False)

noise.to_latex(out / "table8.tex", index=False)

print("Tables generated.")
