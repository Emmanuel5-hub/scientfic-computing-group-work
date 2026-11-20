"""Task 20: Monte Carlo estimate of daily water demand exceeding supply."""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(2026)
daily_supply_litres = 100_000
mean_demand = 92_000
demand_std = 9_000
simulations = 100_000

demand = rng.normal(mean_demand, demand_std, simulations)
shortage = demand > daily_supply_litres
probability = shortage.mean()
running_probability = np.cumsum(shortage)/np.arange(1, simulations+1)

print(f"Estimated shortage probability: {probability:.3%}")
print(f"Shortage scenarios: {shortage.sum():,} of {simulations:,}")
print(f"Mean simulated demand: {demand.mean():,.0f} litres")
print(f"95th percentile demand: {np.percentile(demand, 95):,.0f} litres")

# Parameter experiment: add a 5,000-litre reserve to daily supply.
reserve_supply = daily_supply_litres + 5_000
reserve_probability = np.mean(demand > reserve_supply)
print(f"Shortage probability with 5,000 L reserve: {reserve_probability:.3%}")

sample_indices = np.unique(np.logspace(1, np.log10(simulations), 250).astype(int))-1
plt.semilogx(sample_indices+1, running_probability[sample_indices])
plt.axhline(probability, linestyle="--", label=f"Final estimate = {probability:.2%}")
plt.xlabel("Number of simulated days")
plt.ylabel("Estimated shortage probability")
plt.title("Monte Carlo convergence for community water demand")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
