"""
Generate publication-quality figures.

Author:
NVIDIA_QEC_Project
"""

import matplotlib.pyplot as plt

from analysis.styles.paper_style import set_style
from analysis.helpers.load_results import load_results
from analysis.helpers.save_figure import save_figure

set_style()

df = load_results()

print("=" * 60)
print("Generating publication figures")
print("=" * 60)

print("Figure 4 : Runtime vs Distance")

runtime = (
    df.groupby("distance")["mean_runtime"]
      .mean()
      .reset_index()
)

fig, ax = plt.subplots()

ax.plot(
    runtime["distance"],
    runtime["mean_runtime"],
    marker="o",
)

ax.set_xlabel("Code Distance")

ax.set_ylabel("Runtime (s)")

ax.set_title("Runtime Scaling")

save_figure(fig, "figure4_runtime")

plt.close(fig)

print("Figure 5 : Throughput")

throughput = (
    df.groupby("distance")["mean_throughput"]
      .mean()
      .reset_index()
)

fig, ax = plt.subplots()

ax.plot(
    throughput["distance"],
    throughput["mean_throughput"],
    marker="s",
)

ax.set_xlabel("Code Distance")

ax.set_ylabel("Shots / Second")

ax.set_title("Decoder Throughput")

save_figure(fig, "figure5_throughput")

plt.close(fig)

print("Figure 6 : Detector Count")

detectors = (
    df.groupby("distance")["detectors"]
      .mean()
      .reset_index()
)

fig, ax = plt.subplots()

ax.plot(
    detectors["distance"],
    detectors["detectors"],
    marker="^",
)

ax.set_xlabel("Code Distance")

ax.set_ylabel("Number of Detectors")

ax.set_title("Detector Growth")

save_figure(fig, "figure6_detectors")

plt.close(fig)

print("Figure 7 : Circuit Size")

operations = (
    df.groupby("distance")["operations"]
      .mean()
      .reset_index()
)

fig, ax = plt.subplots()

ax.plot(
    operations["distance"],
    operations["operations"],
    marker="D",
)

ax.set_xlabel("Code Distance")

ax.set_ylabel("Circuit Operations")

ax.set_title("Circuit Complexity")

save_figure(fig, "figure7_operations")

plt.close(fig)

print("Figure 8 : Accuracy")

accuracy = (
    df.groupby("distance")["mean_accuracy"]
      .mean()
      .reset_index()
)

fig, ax = plt.subplots()

ax.bar(
    accuracy["distance"].astype(str),
    accuracy["mean_accuracy"],
)

ax.set_xlabel("Distance")

ax.set_ylabel("Mean Accuracy")

ax.set_title("Decoder Accuracy")

save_figure(fig, "figure8_accuracy")

plt.close(fig)

print("Figure 9 : Runtime Distribution")

fig, ax = plt.subplots()

ax.boxplot(
    df["mean_runtime"],
)

ax.set_ylabel("Runtime (s)")

ax.set_title("Runtime Distribution")

save_figure(fig, "figure9_runtime_box")

plt.close(fig)

print("Figure 10 : Throughput Distribution")

fig, ax = plt.subplots()

ax.boxplot(
    df["mean_throughput"],
)

ax.set_ylabel("Shots / Second")

ax.set_title("Throughput Distribution")

save_figure(fig, "figure10_throughput_box")

plt.close(fig)

print()
print("Finished.")


