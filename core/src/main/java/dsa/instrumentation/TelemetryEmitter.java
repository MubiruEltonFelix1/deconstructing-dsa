package dsa.instrumentation;

/**
 * TelemetryEmitter — prints a structured JSON line to stdout after each
 * benchmark run so the Python telemetry layer can capture and parse it.
 *
 * Output format (one line per run):
 * {"algo":"QuickSort","n":1000,"comparisons":12345,"swaps":6789,"elapsedMs":42}
 */
public class TelemetryEmitter {

    public void emit(String algoName, int n, OperationCounter counter, long elapsedMs) {
        // TODO: build a JSON string from the arguments and print it to stdout
    }
}
