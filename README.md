# Deconstructing DSA

A hands-on exploration of sorting, searching, and advanced data structures
implemented from first principles. This project benchmarks each algorithm
across a range of input sizes and visualises the empirical complexity
alongside theoretical bounds — making the runtime behaviour tangible rather
than abstract.

## Project Structure

The codebase is organised into three decoupled layers communicating through
the filesystem:

| Layer              | Language | Responsibility                                |
|--------------------|----------|----------------------------------------------|
| `core/`            | Java 17  | Algorithm implementations with instrumentation |
| `telemetry/`       | Python   | Benchmark orchestration, parsing, and storage |
| `visualization/`   | Python   | Complexity and comparison plots               |

- `data/` — the filesystem contract: raw inputs (`raw/`), parsed results
  (`results/`), and generated charts (`plots/`).
- `scripts/` — pipeline glue (`run_benchmark.py`, `build_core.sh`, etc.).
- `docs/` — architectural rationale and algorithm deep-dives.
