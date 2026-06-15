"""
plot_complexity — takes a single algorithm's benchmark results and
produces a scatter plot with fitted complexity curve (O(n), O(n log n),
O(n^2), etc.).
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from visualization.themes import apply_theme, PALETTE

# Reference lines: maps label → function(n, scale_factor)
_REFERENCE_CURVES = {
    "O(n)":       lambda n, c: c * n,
    "O(n log n)": lambda n, c: c * n * np.log2(n),
    "O(n²)":      lambda n, c: c * n ** 2,
}


def plot_algorithm(filepath: str, output_path: str) -> None:
    """Load telemetry data for one algorithm and produce a complexity plot."""
    apply_theme()
    df = pd.read_json(filepath, lines=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left: raw elapsed time ---
    ax1.scatter(df["n"], df["elapsedMs"], color=PALETTE[0], alpha=0.7, label="Measured")
    ax1.set_xlabel("Input size (n)")
    ax1.set_ylabel("Time (ms)")
    ax1.set_title(f"{Path(filepath).stem} — Runtime")
    ax1.legend()

    # --- Right: comparisons ---
    ax2.scatter(df["n"], df["comparisons"], color=PALETTE[1], alpha=0.7, label="Comparisons")
    ax2.set_xlabel("Input size (n)")
    ax2.set_ylabel("Comparisons")
    ax2.set_title(f"{Path(filepath).stem} — Operations")
    ax2.legend()

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close(fig)
