"""Task 18: Simulate the charging of a phone-sized RC circuit."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

supply_v = 5.0
resistance_ohm = 1500.0
capacitance_f = 0.001
initial_v = 0.0
time_points = np.linspace(0, 8, 250)

def circuit_ode(t, voltage):
    return [(supply_v-voltage[0])/(resistance_ohm*capacitance_f)]

solution = solve_ivp(circuit_ode, (0, 8), [initial_v], t_eval=time_points,
                     rtol=1e-8, atol=1e-10)
if not solution.success:
    raise RuntimeError(solution.message)

exact = supply_v*(1-np.exp(-solution.t/(resistance_ohm*capacitance_f)))
print("Solver successful:", solution.success)
print(f"Voltage at 8 seconds: {solution.y[0, -1]:.4f} V")
print(f"Maximum error versus exact solution: "
      f"{np.max(np.abs(solution.y[0]-exact)):.3e} V")

# Parameter experiment: double the capacitance, doubling the time constant.
larger_c = 2*capacitance_f
slower = supply_v*(1-np.exp(-solution.t/(resistance_ohm*larger_c)))
print(f"Voltage at 1 second with doubled capacitance: "
      f"{slower[np.argmin(abs(solution.t-1))]:.3f} V")

plt.plot(solution.t, solution.y[0], label="SciPy solve_ivp")
plt.plot(solution.t, exact, "--", label="Analytical solution")
plt.plot(solution.t, slower, ":", label="Doubled capacitance")
plt.xlabel("Time (s)")
plt.ylabel("Capacitor voltage (V)")
plt.title("RC circuit charging response")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
