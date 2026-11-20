"""Task 16: Estimate daily energy use from smart-meter power readings."""
import numpy as np
from scipy.integrate import simpson

# Power measured at two-hour intervals; integral of kW over hours is kWh.
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
trapezoid = np.trapezoid(power_kw, x=time_hours)
simpson_estimate = simpson(power_kw, x=time_hours)

print(f"Trapezoidal energy estimate: {trapezoid:.3f} kWh")
print(f"Simpson energy estimate: {simpson_estimate:.3f} kWh")
print(f"Difference: {abs(simpson_estimate-trapezoid):.3f} kWh")
print(f"Average power over 12 hours: {simpson_estimate/12:.3f} kW")

# Parameter experiment: a 10% increase in every power reading.
higher_use = simpson(power_kw * 1.10, x=time_hours)
print(f"Energy after a 10% power increase: {higher_use:.3f} kWh")
print("Interpretation: numerical integration estimates energy by accumulating "
      "power over time; higher power readings increase the energy estimate.")
