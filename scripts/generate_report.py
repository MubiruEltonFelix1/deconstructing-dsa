"""
generate_report — aggregates benchmark results from data/results/ and
produces a human-readable summary (Markdown) with key findings.
"""

from pathlib import Path

import pandas as pd

RESULTS_DIR = Path("data/results")
REPORT_PATH = RESULTS_DIR / "report.md"


def _load_all_results() -> pd.DataFrame:
    """Load all .jsonl result files into a single DataFrame."""
    frames = []
    for fp in sorted(RESULTS_DIR.glob("*.jsonl")):
        df = pd.read_json(fp, lines=True)
        frames.append(df)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def main():
    """Load telemetry records, compute per-algorithm stats, and write report.md."""
    df = _load_all_results()
    if df.empty:
        print("No result files found in data/results/. Run run_benchmark.py first.")
        return

    lines = ["# Benchmark Report\n"]

    for algo in sorted(df["algo"].unique()):
        subset = df[df["algo"] == algo]
        lines.append(f"## {algo}\n")
        lines.append(f"| n | avg time (ms) | avg comparisons | avg swaps | runs |")
        lines.append(f"|---|--------------:|----------------:|----------:|-----:|")
        for _, row in subset.groupby("n", sort=True).agg(
            avg_time=("elapsedMs", "mean"),
            avg_comparisons=("comparisons", "mean"),
            avg_swaps=("swaps", "mean"),
            count=("elapsedMs", "count"),
        ).iterrows():
            lines.append(
                f"| {row.name} | {row.avg_time:,.1f} | "
                f"{row.avg_comparisons:,.0f} | {row.avg_swaps:,.0f} | "
                f"{row.count} |"
            )
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to {REPORT_PATH}")


if __name__ == "__main__":
    main()
