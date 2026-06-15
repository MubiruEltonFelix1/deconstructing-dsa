"""
themes — shared colour palettes, font scales, and matplotlib rcParams
used by all plotting modules for a consistent visual style.
"""

import matplotlib as mpl
import matplotlib.pyplot as plt

# Colour-blind friendly palette from Paul Tol
PALETTE = [
    "#4477AA", "#CC6677", "#DDCC77", "#117733",
    "#AA4499", "#44AA99", "#999933", "#882255",
]

MARKERS = ["o", "s", "D", "^", "v", "p", "*", "h"]


def apply_theme() -> None:
    """Set global matplotlib rcParams for a clean report-ready look."""
    plt.style.use("seaborn-v0_8-whitegrid")
    mpl.rcParams.update({
        "figure.figsize": (10, 6),
        "figure.dpi": 150,
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "legend.fontsize": 10,
        "lines.linewidth": 2,
        "lines.markersize": 6,
        "axes.prop_cycle": mpl.cycler(color=PALETTE),
        "grid.alpha": 0.4,
        "savefig.bbox": "tight",
        "savefig.dpi": 200,
    })
