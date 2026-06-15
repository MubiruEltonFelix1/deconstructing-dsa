"""
parser — deserialises JSON telemetry lines emitted by the Java JAR into
TelemetryRecord objects (defined in schema.py).
"""

import json
from typing import List

from telemetry.schema import TelemetryRecord


def parse_line(line: str) -> TelemetryRecord:
    """
    TODO: Parse a single JSON string into a TelemetryRecord.
    """
    ...


def parse_lines(lines: List[str]) -> List[TelemetryRecord]:
    """
    TODO: Parse multiple JSON lines and return a list of TelemetryRecords.
          Silently skip malformed lines.
    """
    return []
