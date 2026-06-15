"""
run_benchmark — orchestrates the full benchmark pipeline:

    1. Generate / load raw input arrays of varying sizes.
    2. Invoke the Java benchmark JAR for each algorithm and n.
    3. Capture stdout and parse JSON telemetry lines.
    4. Save parsed records and trigger visualisation.
"""


def main():
    # ---------------------------------------------------------------
    # Stage 1: Generate or load raw arrays of increasing sizes.
    #          Sizes might be e.g. [1_000, 2_000, 5_000, 10_000, ...]
    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    # Stage 2: Invoke the Java JAR for each (algorithm, n) pair.
    #          Use telemetry.runner.run_algorithm().
    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    # Stage 3: Capture stdout lines and parse them into TelemetryRecords
    #          via telemetry.parser.parse_lines().
    # ---------------------------------------------------------------

    # ---------------------------------------------------------------
    # Stage 4: Persist records, then call visualisation scripts to
    #          generate complexity and comparison plots.
    # ---------------------------------------------------------------
    pass


if __name__ == "__main__":
    main()
