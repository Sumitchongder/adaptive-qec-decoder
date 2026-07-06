#!/usr/bin/env python3
"""
Figure 11
Overall Hardware-Aware QEC Co-Design Framework

Outputs:
    figures/figure11_framework.png
    figures/figure11_framework.pdf
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# --------------------------------------------------------
# Figure settings
# --------------------------------------------------------

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 18,
    "font.family": "DejaVu Sans"
})

fig, ax = plt.subplots(figsize=(14,8))

ax.set_xlim(0,16)
ax.set_ylim(0,10)
ax.axis("off")


# --------------------------------------------------------
# Helper
# --------------------------------------------------------

def draw_box(x,y,w,h,text):

    box = FancyBboxPatch(
        (x,y),
        w,
        h,
        boxstyle="round,pad=0.2",
        linewidth=2
    )

    ax.add_patch(box)

    ax.text(
        x+w/2,
        y+h/2,
        text,
        ha='center',
        va='center',
        fontsize=12,
        weight='bold'
    )


def arrow(x1,y1,x2,y2):

    ax.annotate(
        "",
        xy=(x2,y2),
        xytext=(x1,y1),
        arrowprops=dict(
            arrowstyle="->",
            lw=2
        )
    )


# --------------------------------------------------------
# Boxes
# --------------------------------------------------------

draw_box(0.5,7.5,2.5,1.0,"Noise Model")

draw_box(3.8,7.5,2.8,1.0,"Hardware Constraints")

draw_box(7.5,7.5,2.8,1.0,"Code Generator")

draw_box(11.5,7.5,3.0,1.0,"Circuit Synthesis")

draw_box(11.5,5.5,3.0,1.0,"Stim Simulation")

draw_box(7.5,5.5,2.8,1.0,"Syndrome Dataset")

draw_box(3.8,5.5,2.8,1.0,"Adaptive Neural Decoder")

draw_box(0.5,5.5,2.5,1.0,"Confidence Estimator")

draw_box(0.5,3.2,2.5,1.0,"Fast Decoder")

draw_box(3.8,3.2,2.8,1.0,"Graph Refinement")

draw_box(7.5,3.2,2.8,1.0,"Correction")

draw_box(11.5,3.2,3.0,1.0,"Logical Metrics")

draw_box(7.5,1.0,3.5,1.0,"Latency-Constrained Optimizer")


# --------------------------------------------------------
# Horizontal arrows
# --------------------------------------------------------

arrow(3.0,8.0,3.8,8.0)
arrow(6.6,8.0,7.5,8.0)
arrow(10.3,8.0,11.5,8.0)

arrow(13.0,7.5,13.0,6.5)

arrow(11.5,6.0,10.3,6.0)
arrow(7.5,6.0,6.6,6.0)
arrow(3.8,6.0,3.0,6.0)

arrow(1.75,5.5,1.75,4.2)

arrow(3.0,3.7,3.8,3.7)

arrow(6.6,3.7,7.5,3.7)

arrow(10.3,3.7,11.5,3.7)

arrow(9.0,3.2,9.0,2.0)

arrow(9.0,2.0,9.0,7.5)


# --------------------------------------------------------
# Title
# --------------------------------------------------------

plt.title(
    "Hardware-Aware Quantum Error Correction Co-Design Framework",
    pad=25,
    fontsize=20,
    weight='bold'
)

plt.tight_layout()

plt.savefig(
    "figures/figure11_framework.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "figures/figure11_framework.pdf",
    bbox_inches="tight"
)


print("Figure 11 saved.")
