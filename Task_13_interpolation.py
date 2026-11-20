"""Task 13: Interpolate hourly rainfall observations for a farm."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, interp1d

hours = np.array([6, 7, 8, 9, 10, 11, 12], dtype=float)
rain_mm = np.array([0.0, 0.2, 1.4, 3.8, 2.6, 1.1, 0.3])
linear = interp1d(hours, rain_mm, kind="linear")
spline = CubicSpline(hours, rain_mm)
target = 8.5

print(f"Estimated rainfall at 08:30 (linear): {float(linear(target)):.2f} mm")
print(f"Estimated rainfall at 08:30 (cubic): {float(spline(target)):.2f} mm")
print("Observed maximum:", f"{rain_mm.max():.2f} mm at {hours[rain_mm.argmax()]:.0f}:00")

# Parameter experiment: estimate a different time within the observed interval.
second_time = 10.5
print(f"Estimate at 10:30 (cubic): {float(spline(second_time)):.2f} mm")

fine = np.linspace(hours.min(), hours.max(), 250)
plt.scatter(hours, rain_mm, label="Hourly observations", color="black")
plt.plot(fine, linear(fine), label="Linear interpolation")
plt.plot(fine, spline(fine), label="Cubic spline")
plt.xlabel("Hour")
plt.ylabel("Rainfall (mm per hour)")
plt.title("Estimated rainfall between farm gauge readings")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
