"""Task 19: Minimize the cost of a small cloud-server capacity plan."""
import numpy as np
from scipy.optimize import minimize

# x = Type A capacity units; y = Type B capacity units.
# Cost units are illustrative budget points.
def cost(z):
    x, y = z
    return 12*x + 18*y

def capacity(z):
    x, y = z
    return 100*x + 170*y - 1000

result = minimize(cost, x0=[5, 3], method="SLSQP",
                  bounds=[(0, None), (0, None)],
                  constraints=[{"type": "ineq", "fun": capacity}],
                  options={"ftol": 1e-10, "maxiter": 500})
if not result.success:
    raise RuntimeError(result.message)

x, y = result.x
print("Continuous optimization successful:", result.success)
print(f"Type A units: {x:.3f}")
print(f"Type B units: {y:.3f}")
print(f"Capacity supplied: {100*x+170*y:.2f}")
print(f"Minimum continuous cost: {result.fun:.2f}")

# Actual servers are indivisible: search integer combinations.
candidates = [(12*a+18*b, a, b, 100*a+170*b)
              for a in range(0, 20) for b in range(0, 20)
              if 100*a+170*b >= 1000]
best = min(candidates)
print("Best whole-server plan (cost, A, B, capacity):", best)

# Parameter experiment: require 20% more capacity.
required = 1200
new_candidates = [(12*a+18*b, a, b, 100*a+170*b)
                  for a in range(0, 25) for b in range(0, 25)
                  if 100*a+170*b >= required]
print("Best plan for 1,200 capacity:", min(new_candidates))
print("Interpretation: the continuous solution is a planning benchmark; "
      "the integer search respects the fact that whole servers cannot be split.")
