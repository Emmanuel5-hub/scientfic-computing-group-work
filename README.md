# BIT 2118 Scientific Computing — Individual Practical Work

**Student:** Emmanuel Makur  
**Repository:** `Emmanuel5-hub/scientfic-computing-group-work`

This individual version uses a set of distinct applied examples to demonstrate the numerical methods in Tasks 02–20. The examples include weather observations, network measurements, coordinate transformations, water blending, heat transfer, finance, interpolation, GPS data, electricity use, circuits, optimization and Monte Carlo risk analysis.

## Software requirements

- Python 3.10 or later
- NumPy
- SciPy
- Matplotlib

Install dependencies from the project folder:

```bash
python -m pip install -r requirements.txt
```

Run one task:

```bash
python Task_02_numpy_arrays.py
```

Run a graph-producing task the same way. Close the Matplotlib window to return to the terminal.

Check syntax for all scripts:

```bash
python -m compileall .
```

## Task index

| Task | Numerical concept | Applied example |
|---|---|---|
| 02 | NumPy arrays and statistics | Thika hourly weather |
| 03 | Vectorization | Mobile-network latency |
| 04 | Floating-point error | Measurement and financial precision |
| 05 | Matrix algebra | Robot-floor coordinates |
| 06 | Linear systems | Water-solution blending |
| 07 | LU decomposition | Repeated production-system solve |
| 08 | Iterative methods | Temperature in a metal bar |
| 09 | Eigenvalues/eigenvectors | Campus Wi-Fi network importance |
| 10 | Bisection/fixed point | Solar water-tank equilibrium |
| 11 | Newton/secant methods | Investment internal rate of return |
| 12 | Nonlinear systems | Two-variable mixing constraints |
| 13 | Interpolation | Farm rainfall readings |
| 14 | Curve fitting | Community electricity demand |
| 15 | Numerical differentiation | Vehicle speed from GPS |
| 16 | Numerical integration | Smart-meter energy consumption |
| 17 | Euler method | Cooling tea |
| 18 | SciPy ODE solver | RC circuit charging |
| 19 | Optimization | Cloud-server capacity planning |
| 20 | Monte Carlo simulation | Community water-shortage risk |

## How to interpret the experiments

Each script prints its input-derived result and includes at least one parameter experiment. Where a graph is produced, the measured/simulated values and numerical approximation are labelled. The companion `TASK_NOTES.md` records the assumptions, methods, parameter changes and interpretation for each task.

## Reproducibility and limitations

Randomized tasks use fixed NumPy random seeds so that the results can be reproduced. The datasets are illustrative teaching data, not official weather, network, utility or financial records. Numerical models simplify real systems; conclusions should therefore be interpreted within the assumptions stated in the notes.
