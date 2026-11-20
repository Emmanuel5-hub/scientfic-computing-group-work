"""Task 17: Euler approximation of hot tea cooling to room temperature."""
import numpy as np
import matplotlib.pyplot as plt

ambient = 22.0
initial = 85.0
cooling_constant = 0.10  # per minute
step = 1.0
duration = 30.0

def rate(temp):
    return -cooling_constant * (temp - ambient)

time = np.arange(0, duration + step, step)
euler = np.zeros_like(time)
euler[0] = initial
for i in range(len(time)-1):
    euler[i+1] = euler[i] + step * rate(euler[i])

exact = ambient + (initial-ambient)*np.exp(-cooling_constant*time)
print(f"Euler estimate after 30 min: {euler[-1]:.3f} °C")
print(f"Exact value after 30 min: {exact[-1]:.3f} °C")
print(f"Absolute error: {abs(euler[-1]-exact[-1]):.4f} °C")

# Parameter experiment: halve the time step.
fine_time = np.arange(0, duration + step/2, step/2)
fine = np.zeros_like(fine_time)
fine[0] = initial
for i in range(len(fine_time)-1):
    fine[i+1] = fine[i] + (step/2)*rate(fine[i])
print(f"Error with 0.5-minute step: {abs(fine[-1]-exact[-1]):.4f} °C")

plt.plot(time, euler, "o-", markevery=3, label="Euler, 1-minute step")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)")
plt.ylabel("Tea temperature (°C)")
plt.title("Cooling of tea in a room")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
