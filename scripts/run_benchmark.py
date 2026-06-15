"""
run_benchmark — orchestrates the full benchmark pipeline:

    1. Generate / load raw input arrays of varying sizes.
    2. Invoke the Java benchmark JAR for each algorithm and n.
    3. Capture stdout and parse JSON telemetry lines.
    4. Save parsed records and trigger visualisation.
"""

import random
from pathlib import Path

from telemetry.parser import parse_lines
from telemetry.runner import run_jar
from telemetry.storage import save_records
from visualization.plot_comparison import plot_comparison
from visualization.plot_complexity import plot_algorithm

ALGORITHMS = ["QuickSort", "MergeSort", "HeapSort"]
SIZES = [1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000]
JAR_PATH = "core/target/core-1.0.0.jar"
RAW_DIR = Path("data/raw")
RESULTS_DIR = Path("data/results")
PLOTS_DIR = Path("data/plots")


def generate_arrays(sizes, output_dir: Path):
    """Generate random integer arrays and save them as text files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    for n in sizes:
        arr = [random.randint(0, 1_000_000) for _ in range(n)]
        filepath = output_dir / f"array_{n}.txt"
        filepath.write_text("\n".join(map(str, arr)))


def main():
    print("=== Stage 1: Generating input arrays ===")
    generate_arrays(SIZES, RAW_DIR)

    print("=== Stage 2: Invoking Java JAR ===")
    all_records = []
    for algo in ALGORITHMS:
        for n in SIZES:
            print(f"  Running {algo} n={n}...")
            lines = run_jar(JAR_PATH, [algo, str(n)])
            if lines:
                records = parse_lines(lines)
                all_records.extend(records)

    if not all_records:
        print("WARNING: No telemetry records captured. Skipping stages 3-4.")
        return

    print("=== Stage 3: Persisting parsed records ===")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    for algo in ALGORITHMS:
        algo_records = [r for r in all_records if r.algo == algo]
        if algo_records:
            filepath = RESULTS_DIR / f"{algo.lower()}.jsonl"
            save_records(algo_records, str(filepath))

    print("=== Stage 4: Generating visualizations ===")
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)
    for algo in ALGORITHMS:
        result_file = RESULTS_DIR / f"{algo.lower()}.jsonl"
        if result_file.exists():
            plot_path = PLOTS_DIR / f"{algo.lower()}_complexity.png"
            plot_algorithm(str(result_file), str(plot_path))
            print(f"  Saved {plot_path}")

    comparison_files = [
        str(RESULTS_DIR / f"{algo.lower()}.jsonl")
        for algo in ALGORITHMS
    ]
    comparison_files = [f for f in comparison_files if Path(f).exists()]
    if comparison_files:
        plot_comparison(comparison_files, str(PLOTS_DIR / "comparison.png"))
        print(f"  Saved {PLOTS_DIR / 'comparison.png'}")

    print("=== Done ===")


if __name__ == "__main__":
    main()
