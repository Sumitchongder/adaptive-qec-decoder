"""
Summarize the noise sweep evaluation results.
"""

from pathlib import Path

import pandas as pd


def main():

    rows = []

    for csv_file in sorted(Path("results/evaluation").glob("noise_*.csv")):

        df = pd.read_csv(csv_file)

        noise = csv_file.stem.replace("noise_", "")

        rows.append(
            {
                "noise": noise,
                "samples": len(df),
                "accuracy": df["correct"].mean(),
                "avg_confidence": df["confidence"].mean(),
                "avg_latency_us": df["latency_us"].mean(),
                "throughput": 1e6 / df["latency_us"].mean(),
            }
        )

    summary = pd.DataFrame(rows)

    output = Path("results/summary")
    output.mkdir(parents=True, exist_ok=True)

    summary.to_csv(output / "noise_summary.csv", index=False)

    print(summary)


if __name__ == "__main__":
    main()
