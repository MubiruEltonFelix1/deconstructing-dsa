"""
storage — reads and writes TelemetryRecords to / from the data/results/
directory as newline-delimited JSON files.
"""

from typing import List

from telemetry.parser import parse_lines
from telemetry.schema import TelemetryRecord


def save_records(records: List[TelemetryRecord], filepath: str) -> None:
    """Serialise each TelemetryRecord to a JSON line and write to filepath."""
    with open(filepath, "w", encoding="utf-8") as f:
        for record in records:
            f.write(record.model_dump_json() + "\n")


def load_records(filepath: str) -> List[TelemetryRecord]:
    """Read a newline-delimited JSON file into TelemetryRecords."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return parse_lines(f.readlines())
    except FileNotFoundError:
        return []
