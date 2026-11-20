"""Task 15: Estimate a vehicle's speed from GPS position samples."""
import numpy as np
import matplotlib.pyplot as plt

time_s = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
distance_m = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
# np.gradient uses central differences internally and one-sided endpoints.
speed_ms = np.gradient(distance_m, time_s)
speed_kmh = speed_ms * 3.6

for t, d, v in zip(time_s, distance_m, speed_kmh):
    print(f"t={t:.0f} s | distance={d:5.1f} m | estimated speed={v:5.1f} km/h")
print(f"Average trip speed: {distance_m[-1]/time_s[-1]*3.6:.2f} km/h")
print(f"Maximum estimated speed: {speed_kmh.max():.2f} km/h")

# Parameter experiment: estimate using every second sample.
coarse_speed = np.gradient(distance_m[::2], time_s[::2])
print("Coarser-sampling speed estimates (m/s):", np.round(coarse_speed, 2))
plt.plot(time_s, speed_kmh, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated speed (km/h)")
plt.title("Vehicle speed estimated from GPS positions")
plt.grid(True)
plt.tight_layout()
plt.show()
