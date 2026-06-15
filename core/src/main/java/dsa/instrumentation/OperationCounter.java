package dsa.instrumentation;

/**
 * OperationCounter — tracks the number of key comparisons and swaps
 * performed during an algorithm run.
 *
 * Used by TelemetryEmitter to produce structured benchmark output.
 */
public class OperationCounter {

    private long comparisons;
    private long swaps;

    public void incrementComparisons() {
        comparisons++;
    }

    public void incrementSwaps() {
        swaps++;
    }

    public long getComparisons() {
        return comparisons;
    }

    public long getSwaps() {
        return swaps;
    }

    public void reset() {
        comparisons = 0;
        swaps = 0;
    }
}
