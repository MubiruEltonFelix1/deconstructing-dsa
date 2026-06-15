"""
parser — deserialises JSON telemetry lines emitted by the Java JAR into
TelemetryRecord objects (defined in schema.py).
"""

import json
from typing import List

from telemetry.schema import TelemetryRecord


def parse_line(line: str) -> TelemetryRecord:
    """Parse a single JSON string into a TelemetryRecord."""
    data = json.loads(line.strip())
    return TelemetryRecord(**data)


def parse_lines(lines: List[str]) -> List[TelemetryRecord]:
    """Parse multiple JSON lines, silently skipping malformed ones."""
    records: List[TelemetryRecord] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        try:
            records.append(parse_line(stripped))
        except (json.JSONDecodeError, ValueError, TypeError):
            pass  # skip malformed lines
    return records
