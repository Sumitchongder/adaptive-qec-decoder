#!/usr/bin/env python3
"""
Figure 18
Adaptive Decoder Decision Flow

Outputs:
    figures/figure18_decoder_flow.pdf
    figures/figure18_decoder_flow.png
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12
})

fig, ax = plt.subplots(figsize=(12,9))

ax.set_xlim(0,12)
ax.set_ylim(0,12)
ax.axis("off")


# ----------------------------------------------------
# Helper Functions
# ----------------------------------------------------

def box(x,y,w,h,text):

    b = FancyBboxPatch(
        (x,y),
        w,
        h,
        boxstyle="round,pad=0.2",
        linewidth=2
    )

    ax.add_patch(b)

    ax.text(
        x+w/2,
        y+h/2,
        text,
        ha='center',
        va='center',
        fontsize=11,
        weight='bold'
    )


def diamond(cx,cy,w,h,text):

    pts = [
        (cx,cy+h/2),
        (cx+w/2,cy),
        (cx,cy-h/2),
        (cx-w/2,cy)
    ]

    poly = Polygon(
        pts,
        closed=True,
        fill=False,
        linewidth=2
    )

    ax.add_patch(poly)

    ax.text(
        cx,
        cy,
        text,
        ha='center',
        va='center',
        fontsize=10,
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


# ----------------------------------------------------
# Boxes
# ----------------------------------------------------

box(4.5,10.5,3,0.8,"Measured Syndrome")

box(4.5,9.0,3,0.8,"Neural Decoder")

box(4.5,7.4,3,0.8,"Probability Distribution")

diamond(6.0,5.8,3,1.8,"Confidence\n> Threshold?")

box(0.7,3.8,3.2,0.8,"Fast Local Correction")

box(8.1,3.8,3.2,0.8,"Graph / BP / OSD\nRefinement")

box(4.5,1.8,3,0.8,"Apply Recovery")

box(4.5,0.3,3,0.8,"Next QEC Cycle")


# ----------------------------------------------------
# Arrows
# ----------------------------------------------------

arrow(6.0,10.5,6.0,9.8)

arrow(6.0,9.0,6.0,8.2)

arrow(6.0,7.4,6.0,6.7)

arrow(4.5,5.8,3.9,4.2)

arrow(7.5,5.8,8.1,4.2)

arrow(2.3,3.8,5.3,2.6)

arrow(9.7,3.8,6.7,2.6)

arrow(6.0,1.8,6.0,1.1)


# ----------------------------------------------------
# Labels
# ----------------------------------------------------

ax.text(
    2.8,
    5.2,
    "YES",
    fontsize=11,
    weight='bold'
)

ax.text(
    8.4,
    5.2,
    "NO",
    fontsize=11,
    weight='bold'
)

ax.text(
    0.4,
    11.6,
    "Fast Path",
    fontsize=11,
    weight='bold'
)

ax.text(
    9.3,
    11.6,
    "Escalation Path",
    fontsize=11,
    weight='bold'
)

plt.title(
    "Adaptive Streaming Decoder Decision Flow",
    fontsize=18,
    weight='bold',
    pad=20
)

plt.tight_layout()

plt.savefig(
    "figures/figure18_decoder_flow.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    "figures/figure18_decoder_flow.pdf",
    bbox_inches="tight"
)

print("Figure 18 generated successfully.")
