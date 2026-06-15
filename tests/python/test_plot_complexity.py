"""
test_plot_complexity — smoke tests for visualization/plot_complexity.py.
"""

import json
import tempfile
from pathlib import Path

import pytest
from visualization.plot_complexity import plot_algorithm


@pytest.fixture
def synthetic_data_file():
    """Create a temporary .jsonl file with synthetic benchmark data."""
    records = [
        {"algo": "QuickSort", "n": 1000, "comparisons": 9_876, "swaps": 3_456, "elapsedMs": 5},
        {"algo": "QuickSort", "n": 2000, "comparisons": 21_234, "swaps": 7_890, "elapsedMs": 11},
        {"algo": "QuickSort", "n": 5000, "comparisons": 61_728, "swaps": 23_456, "elapsedMs": 30},
        {"algo": "QuickSort", "n": 10000, "comparisons": 136_789, "swaps": 54_321, "elapsedMs": 68},
    ]
    fp = Path(tempfile.mktemp(suffix=".jsonl"))
    fp.write_text("\n".join(json.dumps(r) for r in records))
    yield fp
    fp.unlink(missing_ok=True)


class TestPlotAlgorithm:
    def test_plot_runs_without_error(self, synthetic_data_file):
        """Smoke test: ensure the plotting function completes and saves a file."""
        output = Path(tempfile.mktemp(suffix=".png"))
        try:
            plot_algorithm(str(synthetic_data_file), str(output))
            assert output.exists()
            assert output.stat().st_size > 0  # non-empty image
        finally:
            output.unlink(missing_ok=True)
