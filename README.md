# Deconstructing DSA

A hands-on exploration of sorting, searching, and advanced data structures
implemented from first principles. Each algorithm is built one layer at a
time — from a naive first pass through to an optimised version — benchmarked
across a range of input sizes, and visualised alongside its theoretical
complexity bound so the runtime behaviour becomes tangible rather than
abstract.

## Motivation

Textbooks teach Big-O notation. This repo makes you *feel* it. By
instrumenting every comparison and swap, running the same algorithm at
exponentially growing input sizes, and plotting the measured cost against
the predicted curve, the gap between theory and practice shrinks to zero.
You can literally see O(n log n) vs O(n^2) diverge on a chart.

## What's Inside

### Sorting Algorithms (Java)

| Algorithm    | File                                                                   | Expected Complexity |
|--------------|------------------------------------------------------------------------|---------------------|
| QuickSort    | [QuickSort.java](core/src/main/java/dsa/sorting/QuickSort.java)        | O(n log n) avg     |
| MergeSort    | [MergeSort.java](core/src/main/java/dsa/sorting/MergeSort.java)        | O(n log n) stable  |
| HeapSort     | [HeapSort.java](core/src/main/java/dsa/sorting/HeapSort.java)          | O(n log n) in-place|

### Searching Algorithms (Java)

| Algorithm          | File                                                                               | Expected Complexity |
|--------------------|------------------------------------------------------------------------------------|---------------------|
| BinarySearch       | [BinarySearch.java](core/src/main/java/dsa/searching/BinarySearch.java)            | O(log n)            |
| RangeBinarySearch  | [RangeBinarySearch.java](core/src/main/java/dsa/searching/RangeBinarySearch.java)  | O(log n)            |

### Data Structures (Java)

| Structure      | File                                                                            | Notes                              |
|----------------|---------------------------------------------------------------------------------|------------------------------------|
| Node           | [Node.java](core/src/main/java/dsa/structures/Node.java)                       | Generic tree node used internally  |
| ScapegoatTree  | [ScapegoatTree.java](core/src/main/java/dsa/structures/ScapegoatTree.java)     | Self-balancing BST with tuneable α |

### Instrumentation (Java)

Every algorithm reports its work through
[OperationCounter](core/src/main/java/dsa/instrumentation/OperationCounter.java)
(tracks comparisons + swaps) and
[TelemetryEmitter](core/src/main/java/dsa/instrumentation/TelemetryEmitter.java)
(prints a JSON line to stdout on each benchmark run).

## Architecture

The repo is split into **three strictly decoupled layers** that communicate
through the filesystem — no in-process calls, no shared memory.

```
┌──────────────────────────────────────────────────────────┐
│                      scripts/                            │
│  build_core.sh  |  run_benchmark.py  |  generate_report  │
└──────────┬───────────────────────────────┬───────────────┘
           │ spawns JAR                    │ reads results
           ▼                               ▼
┌─────────────────────┐        ┌──────────────────────────┐
│      core/ (Java)   │ stdout │     telemetry/ (Python)   │
│  algorithms + instr │ ──────►│  parse + validate + save  │
│  (zero deps)        │  JSON  │  (Pydantic models)        │
└─────────────────────┘        └───────────┬──────────────┘
                                           │ writes
                                           ▼
                                 ┌──────────────────┐
                                 │   data/results/   │
                                 │  .jsonl records  │
                                 └────────┬─────────┘
                                          │ reads
                                          ▼
                                 ┌──────────────────────────┐
                                 │  visualization/ (Python)  │
                                 │  matplotlib plots         │
                                 │  → data/plots/            │
                                 └──────────────────────────┘
```

| Layer            | Path               | Language | Responsibility                                      |
|------------------|--------------------|----------|-----------------------------------------------------|
| **Core**         | `core/`            | Java 17  | Algorithm implementations + instrumentation harness |
| **Telemetry**    | `telemetry/`       | Python   | Benchmark orchestration, stdout capture, parsing    |
| **Visualisation**| `visualization/`   | Python   | Complexity + comparison charts (matplotlib)         |
| **Data**         | `data/`            | —        | Filesystem contract between layers                 |
| **Scripts**      | `scripts/`         | Mixed    | Pipeline glue (build, run, report)                 |
| **Documentation**| `docs/`            | Markdown | Architecture rationale + algorithm deep-dives       |
| **Tests**        | `tests/`           | Java/Py  | Unit + smoke tests for every module                 |

### Data Directory Contract

```
data/
├── raw/        Input arrays (optional — algorithms can self-generate)
├── results/    Parsed telemetry as newline-delimited JSON (.jsonl)
└── plots/      Output charts (.png / .pdf)
```

Each layer is independently replaceable: swap `core/` for a C
implementation and the pipeline still works as long as it speaks the same
JSON-line stdout protocol. Swap matplotlib for Plotly and telemetry never
notices.

## Prerequisites

- **Java 17+** and **Maven 3.8+** on PATH (to build `core/`)
- **Python 3.10+** with `pip`
- Install Python dependencies:

  ```bash
  pip install -r requirements.txt
  ```

## Quick Start

```bash
# 1. Build the Java JAR
./scripts/build_core.sh          # runs: mvn -f core/pom.xml package

# 2. Run the full benchmark pipeline
python scripts/run_benchmark.py  # generates arrays → invokes JAR → parses → plots

# 3. Generate a summary report
python scripts/generate_report.py
```

Output lands in:
- `data/results/` — parsed telemetry as `.jsonl` files
- `data/plots/` — complexity and comparison charts
- `data/results/report.md` — summary report

## Running Tests

```bash
# Java tests
mvn -f core/pom.xml test

# Python tests
pytest tests/python/
```

## Project File Reference

| File | Purpose |
|------|---------|
| [.gitignore](.gitignore) | Ignores build artifacts, caches, IDE junk, generated data |
| [pom.xml](pom.xml) | Maven build config (Java 17, JUnit 5.10) |
| [requirements.txt](requirements.txt) | Python pinned dependencies (pandas, matplotlib, numpy, pydantic, pytest) |
| [setup.cfg](setup.cfg) | flake8 config (100-char line length) |
| [scripts/build_core.sh](scripts/build_core.sh) | Builds the core JAR via Maven |
| [scripts/run_benchmark.py](scripts/run_benchmark.py) | Full pipeline orchestrator |
| [scripts/generate_report.py](scripts/generate_report.py) | Aggregates results into a markdown report |
| [docs/architecture.md](docs/architecture.md) | Deep-dive into layer decoupling rationale |
| [docs/algorithms/range-binary-search.md](docs/algorithms/range-binary-search.md) | Range binary search explainer |
| [docs/algorithms/scapegoat-tree.md](docs/algorithms/scapegoat-tree.md) | Scapegoat tree explainer |

## Roadmap

- [ ] Implement all algorithm bodies (QuickSort, MergeSort, HeapSort, etc.)
- [ ] Add naive-vs-optimised variants for each algorithm
- [ ] Support additional data structure benchmarks (BST, AVL, Red-Black)
- [ ] Add command-line argument parsing to `run_benchmark.py`
- [ ] Generate PDF reports with embedded plots
