"""
schema — Pydantic models for telemetry records persisted as JSON lines
and loaded into DataFrames for analysis.
"""

from pydantic import BaseModel


class TelemetryRecord(BaseModel):
    """
    TODO: Define fields:
          algo (str), n (int), comparisons (int),
          swaps (int), elapsedMs (int)
    """
    pass


class BenchmarkRun(BaseModel):
    """
    TODO: Define a higher-level record that wraps TelemetryRecord with
          metadata (e.g. timestamp, machine info, JVM args).
    """
    pass
