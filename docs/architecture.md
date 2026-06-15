# Architecture

The project enforces strict decoupling between three layers. Each layer
has exactly one responsibility and communicates with its neighbours only
through well-defined filesystem contracts.

## Boundary Rationale

### `core/` (Java)

- Contains all algorithm implementations and an instrumentation harness
  (`OperationCounter`, `TelemetryEmitter`).
- Has **zero dependencies** beyond the JDK. No third-party libraries,
  no logging frameworks, no configuration files.
- Every class is self-contained: given an input array it produces a sorted
  array (or search result) and emits a single JSON line describing the
  operation count and elapsed time.
- The only way to interact with `core/` is via stdout or a JAR invocation.

### `telemetry/` (Python)

- Orchestrates benchmark runs by spawning the Java JAR as a subprocess.
- **Never touches the Java source code** — it only reads the JSON lines
  that `core/` emits to stdout.
- Parses and validates those lines into Pydantic models, then persists
  them as newline-delimited JSON in `data/results/`.
- Has no knowledge of the visualization layer. Its output is a file.

### `visualization/` (Python)

- Reads only from `data/results/` — never invokes Java, never reads
  raw telemetry, never knows how the data was produced.
- Produces matplotlib charts saved to `data/plots/`.
- Can be run independently of the benchmark pipeline if pre-existing
  result files are present.

### `data/` (Filesystem Contract)

- `data/raw/` — generated input arrays (optional; algorithms can also
  generate their own data).
- `data/results/` — the only bridge between telemetry and visualization.
  Newline-delimited JSON, one record per line.
- `data/plots/` — output directory for all generated charts.

This layout means any layer can be swapped out independently:
replace `core/` with a C implementation and the pipeline still works as
long as it speaks the same JSON-line stdout protocol; swap the plotting
library and the telemetry layer never notices.
