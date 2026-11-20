"""Task 03: Vectorized processing of mobile-network latency measurements."""
import timeit
import numpy as np

rng = np.random.default_rng(2026)
latency_ms = rng.uniform(8, 220, 250_000)

def loop_version():
    squared_seconds = []
    for latency in latency_ms:
        seconds = latency / 1000.0
        squared_seconds.append(seconds ** 2)
    return squared_seconds

def vectorized_version():
    return (latency_ms / 1000.0) ** 2

loop_seconds = timeit.timeit(loop_version, number=1)
vector_seconds = timeit.timeit(vectorized_version, number=5) / 5
processed = vectorized_version()
slow_requests = np.count_nonzero(latency_ms > 150)

print("MOBILE NETWORK LATENCY ANALYSIS")
print("First five squared values (s²):", np.round(processed[:5], 8))
print(f"Mean latency: {np.mean(latency_ms):.2f} ms")
print(f"95th percentile: {np.percentile(latency_ms, 95):.2f} ms")
print(f"Requests above 150 ms: {slow_requests:,} ({slow_requests / latency_ms.size:.2%})")
print(f"Python-loop time: {loop_seconds:.4f} s")
print(f"NumPy vectorized time: {vector_seconds:.4f} s")
print(f"Measured speed-up: {loop_seconds / vector_seconds:.1f}x")
print(f"Requests above a 100 ms threshold: {np.count_nonzero(latency_ms > 100):,}")
print("Interpretation: vectorization applies the same operation to the whole "
      "array and avoids the overhead of a Python-level loop.")
