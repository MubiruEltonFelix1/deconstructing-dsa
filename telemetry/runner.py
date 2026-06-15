"""
runner — manages subprocess invocations of the core Java JAR and captures
its stdout telemetry lines.
"""

import subprocess
import sys
from typing import List


def run_jar(jar_path: str, args: List[str]) -> List[str]:
    """Execute `java -jar <jar_path> <args>` and return captured stdout lines."""
    cmd = ["java", "-jar", jar_path] + args
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,
        )
        result.check_returncode()
        return [line for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        print(f"JAR execution failed (exit {e.returncode}): {e.stderr}", file=sys.stderr)
        return []
    except subprocess.TimeoutExpired:
        print(f"JAR execution timed out for: {cmd}", file=sys.stderr)
        return []


def run_algorithm(algo_name: str, n: int, jar_path: str) -> str:
    """Convenience wrapper — runs jar for a single algorithm/n pair and returns the raw JSON line."""
    lines = run_jar(jar_path, [algo_name, str(n)])
    return lines[0] if lines else ""
