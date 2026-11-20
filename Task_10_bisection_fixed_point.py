"""Task 10: Find the equilibrium temperature of a solar water tank."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def balance(t):
    return t - 24 - 12 * np.exp(-t / 18)

def fixed_point(t):
    return 24 + 12 * np.exp(-t / 18)

root = root_scalar(balance, bracket=[20, 40], method="bisect", xtol=1e-10)
estimate = 30.0
history = [estimate]
for _ in range(200):
    updated = fixed_point(estimate)
    history.append(updated)
    if abs(updated - estimate) < 1e-10:
        break
    estimate = updated
else:
    raise RuntimeError("Fixed-point iteration did not converge.")

print(f"Bisection equilibrium: {root.root:.6f} °C ({root.iterations} iterations)")
print(f"Fixed-point equilibrium: {history[-1]:.6f} °C ({len(history)-1} iterations)")
print(f"Difference between methods: {abs(root.root-history[-1]):.3e} °C")

# Parameter experiment: raise the constant heat input from 24 to 26.
changed_root = root_scalar(lambda t: t - 26 - 12*np.exp(-t/18),
                           bracket=[20, 45], method="bisect")
print(f"Equilibrium with higher heat input: {changed_root.root:.4f} °C")
grid = np.linspace(18, 45, 300)
plt.plot(grid, balance(grid), label="Heat-balance function")
plt.axhline(0, color="black", linewidth=.8)
plt.axvline(root.root, linestyle="--", label=f"Root = {root.root:.2f} °C")
plt.xlabel("Tank temperature (°C)")
plt.ylabel("Net heat balance")
plt.title("Solar water-tank equilibrium")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
