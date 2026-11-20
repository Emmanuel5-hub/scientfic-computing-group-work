import temperature_analysis as np

# Simulated hourly temperatures for Thika, Kenya (°C)
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# Calculate temperature statistics
mean_temp = np.mean(temperatures_c)
median_temp = np.median(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)
temp_range = np.ptp(temperatures_c)
std_temp = np.std(temperatures_c)

# Identify the coldest and hottest hours
coldest_hour = np.argmin(temperatures_c)
hottest_hour = np.argmax(temperatures_c)

# Convert Celsius to Fahrenheit
temperatures_f = (1.8 * temperatures_c) + 32

# Display results
print("THIKA WEATHER MONITORING REPORT")
print("--------------------------------")
print(f"Mean temperature: {mean_temp:.2f} °C")
print(f"Median temperature: {median_temp:.2f} °C")
print(f"Minimum temperature: {min_temp:.2f} °C")
print(f"Maximum temperature: {max_temp:.2f} °C")
print(f"Temperature range: {temp_range:.2f} °C")
print(f"Standard deviation: {std_temp:.2f} °C")
print(f"Coldest hour: {coldest_hour:02d}:00")
print(f"Hottest hour: {hottest_hour:02d}:00")
print(f"Mean temperature in Fahrenheit: {(1.8 * mean_temp) + 32:.2f} °F")

print("\nFirst six Fahrenheit readings:")
print(temperatures_f[:6])