"""
schema — Pydantic models for telemetry records persisted as JSON lines
and loaded into DataFrames for analysis.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TelemetryRecord(BaseModel):
    """A single benchmark measurement from one algorithm run."""

    algo: str = Field(description="Algorithm name (e.g. QuickSort)")
    n: int = Field(gt=0, description="Input size")
    comparisons: int = Field(ge=0, description="Number of key comparisons")
    swaps: int = Field(ge=0, description="Number of swaps / assignments")
    elapsedMs: int = Field(ge=0, description="Wall-clock runtime in milliseconds")


class BenchmarkRun(BaseModel):
    """Wraps a TelemetryRecord with execution metadata."""

    record: TelemetryRecord
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    machine: Optional[str] = Field(default=None, description="Hostname or identifier")
    jvmArgs: Optional[str] = Field(default=None, description="JVM arguments used")
