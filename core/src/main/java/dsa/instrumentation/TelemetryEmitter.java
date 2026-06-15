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
        String json = String.format(
            "{\"algo\":\"%s\",\"n\":%d,\"comparisons\":%d,\"swaps\":%d,\"elapsedMs\":%d}",
            escapeJson(algoName),
            n,
            counter.getComparisons(),
            counter.getSwaps(),
            elapsedMs
        );
        System.out.println(json);
    }

    private static String escapeJson(String s) {
        if (s == null) return "";
        return s.replace("\\", "\\\\")
                .replace("\"", "\\\"")
                .replace("\n", "\\n")
                .replace("\r", "\\r")
                .replace("\t", "\\t");
    }
}
