"""Task 02: NumPy arrays for hourly weather observations in Thika."""
import numpy as np

# Assumption: one observation was recorded at the start of each hour.
hours = np.arange(24)
temperature_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8,
    25.6, 27.1, 28.3, 29.0, 29.4, 29.1, 28.5, 27.6,
    26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0
], dtype=float)

if temperature_c.size != 24:
    raise ValueError("Exactly 24 hourly readings are required.")

temperature_f = temperature_c * 9 / 5 + 32
hottest_hour = int(np.argmax(temperature_c))
coolest_hour = int(np.argmin(temperature_c))

print("THIKA: 24-HOUR WEATHER SUMMARY")
print(f"Mean: {np.mean(temperature_c):.2f} °C")
print(f"Median: {np.median(temperature_c):.2f} °C")
print(f"Lowest: {np.min(temperature_c):.2f} °C at {coolest_hour:02d}:00")
print(f"Highest: {np.max(temperature_c):.2f} °C at {hottest_hour:02d}:00")
print(f"Daily range: {np.ptp(temperature_c):.2f} °C")
print(f"Population standard deviation: {np.std(temperature_c):.2f} °C")
print("First six Fahrenheit readings:", np.round(temperature_f[:6], 2))

# Parameter experiment: examine a day that is 2 °C warmer throughout.
warmer_day = temperature_c + 2.0
print(f"Mean after a +2 °C change: {np.mean(warmer_day):.2f} °C")
print("Interpretation: adding 2 °C raises the mean and both extremes by 2 °C; "
      "the range and standard deviation remain unchanged.")
