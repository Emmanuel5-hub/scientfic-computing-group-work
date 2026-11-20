"""Task 12: Solve a two-variable mixing constraint using nonlinear equations."""
import numpy as np
from scipy.optimize import root

def system(v):
    x, y = v
    return np.array([x**2 + y**2 - 25, x - y - 1])

result = root(system, x0=[3.5, 2.5])
print("Converged:", result.success)
print("Solution [x, y]:", np.round(result.x, 7))
print("Residuals:", np.round(system(result.x), 10))
print("Residual norm:", np.linalg.norm(system(result.x)))

# Parameter experiment: increase the total squared constraint from 25 to 36.
def changed_system(v):
    x, y = v
    return np.array([x**2 + y**2 - 36, x - y - 1])

changed = root(changed_system, x0=[4., 3.])
print("Solution when the total constraint is 36:", np.round(changed.x, 6))
print("Interpretation: the solver finds values satisfying both constraints "
      "simultaneously; the starting guess can affect which root is found.")
