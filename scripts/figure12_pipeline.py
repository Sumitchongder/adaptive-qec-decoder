#!/usr/bin/env python3
"""
Figure 12
Hardware-Aware Co-Design Optimization Pipeline

Outputs:
    figures/figure12_pipeline.png
    figures/figure12_pipeline.pdf
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12
})

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 14)
ax.axis("off")


def box(x, y, w, h, text):
    rect = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.25",
        linewidth=2
    )
    ax.add_patch(rect)

    ax.text(
        x + w/2,
        y + h/2,
        text,
        ha="center",
        va="center",
        fontsize=12,
        weight="bold"
    )


def arrow(x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            lw=2
        )
    )


# -------------------------------------------------
# Pipeline
# -------------------------------------------------

box(5.0, 12.2, 4.0, 1.0,
    "Hardware Constraints\nConnectivity • Gate Set • Cycle Time")

box(5.0, 10.4, 4.0, 1.0,
    "Noise Model\nPauli • Correlated • Coherent")

box(5.0, 8.6, 4.0, 1.0,
    "Code Generator\nSurface / CSS / QLDPC")

box(5.0, 6.8, 4.0, 1.0,
    "Circuit Compilation\nStim-Compatible Circuits")

box(5.0, 5.0, 4.0, 1.0,
    "Syndrome Simulation")

box(5.0, 3.2, 4.0, 1.0,
    "Adaptive Decoder\nNeural + Refinement")

box(5.0, 1.4, 4.0, 1.0,
    "Evaluation\nLogical Error • Runtime • Throughput")


# -------------------------------------------------
# Vertical arrows
# -------------------------------------------------

arrow(7.0, 12.2, 7.0, 11.4)
arrow(7.0, 10.4, 7.0, 9.6)
arrow(7.0, 8.6, 7.0, 7.8)
arrow(7.0, 6.8, 7.0, 6.0)
arrow(7.0, 5.0, 7.0, 4.2)
arrow(7.0, 3.2, 7.0, 2.4)


# -------------------------------------------------
# Optimization block
# -------------------------------------------------

box(10.5, 5.6, 3.0, 2.6,
    "Multi-objective\nOptimizer")

arrow(9.0, 6.3, 10.5, 6.9)

box(10.5, 2.2, 3.0, 2.0,
    "Updated\nHyperparameters")

arrow(12.0, 5.6, 12.0, 4.2)

arrow(10.5, 3.2, 9.0, 3.7)


# -------------------------------------------------
# Feedback loop
# -------------------------------------------------

ax.annotate(
    "",
    xy=(5.0, 8.0),
    xytext=(5.0, 3.8),
    arrowprops=dict(
        arrowstyle="->",
        lw=2,
        connectionstyle="arc3,rad=0.45"
    )
)

ax.text(
    2.2,
    6.0,
    "Optimization Loop",
    rotation=90,
    fontsize=12,
    weight="bold"
)

# -------------------------------------------------
# Objective function
# -------------------------------------------------

ax.text(
    0.5,
    1.2,
    r"Objective: minimize  "
    r"$\mathcal{L}=w_1P_L+w_2T+w_3M+w_4C$",
    fontsize=13
)

ax.text(
    0.5,
    0.5,
    "PL = Logical Error    T = Runtime    M = Memory    C = Hardware Cost",
    fontsize=11
)

plt.title(
    "Hardware-Aware Co-Design Optimization Pipeline",
    fontsize=20,
    weight="bold",
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figures/figure12_pipeline.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "figures/figure12_pipeline.pdf",
    bbox_inches="tight"
)

print("Figure 12 saved successfully.")
