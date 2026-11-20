"""Task 04: Floating-point error in financial and measurement calculations."""
import math
import numpy as np

print("FLOATING-POINT REPRESENTATION")
computed = 0.1 + 0.2
reference = 0.3
print(f"0.1 + 0.2 = {computed:.17f}")
print("Exact equality:", computed == reference)
print("Tolerance comparison:", np.isclose(computed, reference, atol=1e-12))

true_value = math.sqrt(2)
approximation = 1.414
absolute_error = abs(true_value - approximation)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.10f}")
print(f"Relative error: {relative_error:.6%}")

print("\nCANCELLATION EXPERIMENT")
for x in (1e-4, 1e-8, 1e-12):
    direct = (math.sqrt(1 + x) - 1) / x
    stable = 1 / (math.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

for tolerance in (1e-8, 1e-15):
    print(f"Tolerance {tolerance:.0e}: "
          f"{np.isclose(computed, reference, atol=tolerance, rtol=0)}")

print("Interpretation: binary floating-point values are approximations. "
      "Tolerance-based comparisons are safer than exact equality, while "
      "the algebraically equivalent stable expression reduces cancellation.")
