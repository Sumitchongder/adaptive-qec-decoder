"""
Publication plotting style.

All publication figures import this file.
"""

import matplotlib.pyplot as plt


def set_style():

    plt.style.use("default")

    plt.rcParams.update({

        "figure.figsize": (7.2,5.4),

        "figure.dpi":300,

        "savefig.dpi":300,

        "savefig.bbox":"tight",

        "font.family":"serif",

        "font.size":12,

        "axes.labelsize":13,

        "axes.titlesize":14,

        "axes.linewidth":1.2,

        "xtick.labelsize":11,

        "ytick.labelsize":11,

        "legend.fontsize":10,

        "lines.linewidth":2.2,

        "lines.markersize":7,

        "grid.alpha":0.35,

        "grid.linestyle":"--",

        "axes.grid":True

    })
