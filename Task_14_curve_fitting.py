"""Task 14: Fit a curve to electricity demand as household count grows."""
import numpy as np
import matplotlib.pyplot as plt

households = np.array([20, 40, 60, 80, 100, 120, 140], dtype=float)
demand_kw = np.array([8.1, 14.8, 22.5, 31.2, 41.5, 52.9, 66.0])

coefficients = np.polyfit(households, demand_kw, deg=2)
model = np.poly1d(coefficients)
predicted = model(households)
rmse = np.sqrt(np.mean((demand_kw - predicted)**2))
r_squared = 1 - np.sum((demand_kw-predicted)**2) / np.sum((demand_kw-demand_kw.mean())**2)

print("Quadratic model coefficients:", np.round(coefficients, 6))
print(f"RMSE: {rmse:.3f} kW")
print(f"R-squared: {r_squared:.4f}")
print(f"Estimated demand for 150 households: {model(150):.2f} kW")

# Parameter experiment: compare the prediction for 160 households.
print(f"Estimated demand for 160 households: {model(160):.2f} kW")
x_plot = np.linspace(households.min(), 160, 250)
plt.scatter(households, demand_kw, label="Measured data")
plt.plot(x_plot, model(x_plot), label="Quadratic least-squares fit")
plt.xlabel("Number of households")
plt.ylabel("Electricity demand (kW)")
plt.title("Community electricity-demand curve fitting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
