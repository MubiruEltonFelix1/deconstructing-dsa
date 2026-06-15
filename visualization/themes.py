"""
themes — shared colour palettes, font scales, and matplotlib rcParams
used by all plotting modules for a consistent visual style.
"""

import matplotlib.pyplot as plt


def apply_theme() -> None:
    """
    TODO: Set global matplotlib rcParams (figure size, font family,
          colour cycle, grid style, etc.) for a clean report-ready look.
    """
    plt.style.use("seaborn-v0_8-whitegrid")
