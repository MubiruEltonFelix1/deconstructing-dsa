"""
plot_comparison — overlays multiple algorithms' benchmark traces on a
single set of axes for side-by-side complexity comparison.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from visualization.themes import apply_theme, PALETTE, MARKERS


def plot_comparison(filepaths: list, output_path: str) -> None:
    """Load telemetry data for several algorithms and overlay them on one plot."""
    apply_theme()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    for i, fp in enumerate(filepaths):
        df = pd.read_json(fp, lines=True)
        label = Path(fp).stem
        colour = PALETTE[i % len(PALETTE)]
        marker = MARKERS[i % len(MARKERS)]

        ax1.plot(df["n"], df["elapsedMs"], label=label, color=colour,
                 marker=marker, linestyle="-", alpha=0.8)
        ax2.plot(df["n"], df["comparisons"], label=label, color=colour,
                 marker=marker, linestyle="-", alpha=0.8)

    ax1.set_xlabel("Input size (n)")
    ax1.set_ylabel("Time (ms)")
    ax1.set_title("Runtime Comparison")
    ax1.legend()

    ax2.set_xlabel("Input size (n)")
    ax2.set_ylabel("Comparisons")
    ax2.set_title("Operation Count Comparison")
    ax2.legend()

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig)
