"""
storage — reads and writes TelemetryRecords to / from the data/results/
directory as newline-delimited JSON files.
"""

from typing import List

from telemetry.schema import TelemetryRecord


def save_records(records: List[TelemetryRecord], filepath: str) -> None:
    """
    TODO: Serialise each TelemetryRecord to a JSON line and write it
          to the given filepath, one record per line.
    """
    ...


def load_records(filepath: str) -> List[TelemetryRecord]:
    """
    TODO: Read a newline-delimited JSON file and parse each line into
          a TelemetryRecord. Skip malformed lines.
    """
    return []
