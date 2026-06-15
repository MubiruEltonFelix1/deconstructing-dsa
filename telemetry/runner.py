"""
runner — manages subprocess invocations of the core Java JAR and captures
its stdout telemetry lines.
"""

import subprocess
from typing import List


def run_jar(jar_path: str, args: List[str]) -> List[str]:
    """
    TODO: Execute `java -jar <jar_path> <args>`, return a list of captured
          stdout lines (each should be a JSON telemetry record).
    """
    return []


def run_algorithm(algo_name: str, n: int, jar_path: str) -> str:
    """
    TODO: Convenience wrapper — calls run_jar for a single algorithm/n pair
          and returns the raw JSON line.
    """
    return ""
