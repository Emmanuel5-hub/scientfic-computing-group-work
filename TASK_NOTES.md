# Individual Task Notes — BIT 2118 Scientific Computing

These notes explain the inputs, numerical operation, parameter experiment and interpretation for each program. All numerical datasets are illustrative classroom examples, not measured official records.

## Task 02 — NumPy arrays: Thika hourly weather
- **Inputs:** 24 hourly temperatures in degrees Celsius.
- **Operations:** NumPy mean, median, minimum, maximum, range, standard deviation, argmin/argmax and vectorized Celsius-to-Fahrenheit conversion.
- **Parameter change:** Add 2 °C to every reading.
- **Expected effect:** Mean, median, minimum and maximum each rise by 2 °C; range and standard deviation do not change.
- **Related case:** The same array workflow can summarize hourly humidity or rainfall observations.
- **Assumption:** One illustrative reading is assigned to each hour from 00:00 to 23:00.

## Task 03 — Vectorization: mobile-network latency
- **Inputs:** 250,000 reproducible simulated latency values between 8 and 220 milliseconds.
- **Operations:** Convert milliseconds to seconds, square values, calculate a percentile and count values above a service threshold; compare a Python loop with NumPy vectorization.
- **Parameter change:** Compare counts above 150 ms and 100 ms.
- **Expected effect:** The lower threshold classifies more requests as slow. Vectorized execution should generally be faster, although timing depends on the computer.
- **Related case:** Batch processing of sensor readings or website response times.
- **Assumption:** Uniformly generated values are used only to demonstrate computation and timing.

## Task 04 — Floating-point numerical error
- **Inputs:** Decimal addition, an approximation to square root of two, and small positive values.
- **Operations:** Exact versus tolerance comparison, absolute and relative error, and a stable algebraic rearrangement.
- **Parameter change:** Tighten the absolute comparison tolerance from 1e-8 to 1e-15.
- **Expected effect:** A stricter tolerance can reject values previously considered sufficiently close.
- **Related case:** Precision checks in currency, scientific measurements or sensor calibration.
- **Assumption:** Floating-point arithmetic uses finite binary precision.

## Task 05 — Matrix algebra: coordinate mapping
- **Inputs:** Four two-dimensional points, rotation angle, horizontal/vertical scale factors and translation vector.
- **Operations:** Matrix multiplication for scaling and rotation, vector addition for translation, and determinant for area scaling.
- **Parameter change:** Double the horizontal scale.
- **Expected effect:** The determinant/area factor doubles; the transformed coordinates change.
- **Related case:** Mapping a robot's work area or transforming image coordinates.
- **Assumption:** Coordinates are planar and measured in metres.

## Task 06 — Linear systems: water blending
- **Inputs:** A 2-by-2 coefficient matrix and target vector for two blend constraints.
- **Operations:** `numpy.linalg.solve` computes the two unknown quantities; residuals verify the result.
- **Parameter change:** Increase the second target from 18 to 21.
- **Expected effect:** The required blend quantities change while the constraint coefficients remain fixed.
- **Related case:** Material mixtures, production planning or two-source resource allocation.
- **Assumption:** The two equations represent exact linear relationships and ignore process losses.

## Task 07 — LU decomposition
- **Inputs:** A 3-by-3 matrix and right-hand-side vector.
- **Operations:** SciPy LU factorization, followed by forward and backward triangular substitution.
- **Parameter change:** Increase the final right-hand-side requirement by 10%.
- **Expected effect:** The computed solution changes; the factorization of the unchanged matrix can be reused.
- **Related case:** Repeatedly solving production or engineering balances with different demand vectors.
- **Assumption:** The matrix is nonsingular.

## Task 08 — Iterative linear methods
- **Inputs:** A diagonally dominant matrix representing internal points along a heated bar.
- **Operations:** Jacobi and Gauss-Seidel updates; compare with a direct NumPy solution and plot update errors.
- **Parameter change:** Tighten the stopping tolerance from 1e-9 to 1e-11.
- **Expected effect:** More iterations are generally required for the stricter tolerance.
- **Related case:** Approximate temperature or voltage values in discretized engineering systems.
- **Assumption:** The chosen system is diagonally dominant and converges for these methods.

## Task 09 — Eigenvalues and eigenvectors
- **Inputs:** An adjacency matrix describing links among four campus Wi-Fi access points.
- **Operations:** Compute eigenpairs and normalize the dominant eigenvector to obtain relative centrality scores.
- **Parameter change:** Add a link between the first and fourth access points.
- **Expected effect:** The network structure and relative importance scores may change.
- **Related case:** Ranking connected web pages, transport nodes or communication devices.
- **Assumption:** Links are undirected and have equal weight.

## Task 10 — Bisection and fixed-point iteration
- **Inputs:** A heat-balance function and an interval containing its root; initial fixed-point estimate.
- **Operations:** SciPy bisection and repeated fixed-point substitution.
- **Parameter change:** Increase the constant heat-input term from 24 to 26.
- **Expected effect:** The equilibrium temperature rises.
- **Related case:** Finding equilibrium temperature in a solar water heater.
- **Assumption:** The simplified heat-balance expression captures the system sufficiently for demonstration.

## Task 11 — Newton-Raphson and secant methods
- **Inputs:** An initial investment and four future cash flows.
- **Operations:** Net present value and its derivative; find the rate at which NPV is zero using Newton and secant methods.
- **Parameter change:** Increase the final cash inflow by 500 currency units.
- **Expected effect:** The estimated internal rate of return increases.
- **Related case:** Evaluating a small business or equipment investment.
- **Assumption:** Cash flows occur at equally spaced year-end periods.

## Task 12 — Nonlinear equations
- **Inputs:** Two nonlinear equations in two unknowns and an initial guess.
- **Operations:** `scipy.optimize.root` solves the simultaneous equations and residuals verify the result.
- **Parameter change:** Change the squared-radius constraint from 25 to 36.
- **Expected effect:** The solution moves to satisfy the larger constraint.
- **Related case:** Solving geometric, chemical-mixture or mechanical equilibrium constraints.
- **Assumption:** The numerical solver converges to the root near the initial guess.

## Task 13 — Interpolation
- **Inputs:** Hourly rainfall observations.
- **Operations:** Linear interpolation and cubic spline interpolation estimate values between measured hours.
- **Parameter change:** Estimate at 10:30 as well as 08:30.
- **Expected effect:** The estimated value depends on the selected time and interpolation method.
- **Related case:** Estimating missing sensor readings between observations.
- **Assumption:** The data vary smoothly enough between the sampled hours; interpolation is not extrapolation.

## Task 14 — Curve fitting
- **Inputs:** Household counts and corresponding illustrative electricity-demand measurements.
- **Operations:** Quadratic least-squares fit, root mean square error and coefficient of determination.
- **Parameter change:** Predict demand for 160 rather than 150 households.
- **Expected effect:** The model predicts a larger demand for the larger community.
- **Related case:** Forecasting resource requirements as a customer base grows.
- **Assumption:** A quadratic curve is an adequate local approximation; predictions beyond the data range are less certain.

## Task 15 — Numerical differentiation
- **Inputs:** GPS-like distance observations at one-second intervals.
- **Operations:** `numpy.gradient` estimates the derivative of distance with respect to time; convert metres/second to kilometres/hour.
- **Parameter change:** Repeat the estimate using every second sample.
- **Expected effect:** Coarser sampling changes the number and possibly smoothness of the estimates.
- **Related case:** Estimating vehicle speed from GPS positions.
- **Assumption:** Position measurements are ordered and time intervals are known; measurement noise is ignored.

## Task 16 — Numerical integration
- **Inputs:** Power readings in kilowatts at two-hour intervals.
- **Operations:** Trapezoidal and Simpson integration estimate energy in kilowatt-hours.
- **Parameter change:** Increase all power readings by 10%.
- **Expected effect:** Estimated energy also rises by 10% because integration is linear in the measured power.
- **Related case:** Estimating electricity consumption from smart-meter readings.
- **Assumption:** The sampled power profile represents the changes between observations.

## Task 17 — Euler method
- **Inputs:** Initial tea temperature, ambient temperature, cooling constant, time interval and step size.
- **Operations:** Forward Euler approximates the cooling ODE; compare with its analytical solution.
- **Parameter change:** Halve the time step from one minute to half a minute.
- **Expected effect:** The Euler approximation should become more accurate for this smooth problem.
- **Related case:** Modelling cooling of food, liquids or equipment.
- **Assumption:** Ambient temperature and cooling constant remain constant.

## Task 18 — SciPy ODE solver
- **Inputs:** Supply voltage, resistance, capacitance, initial capacitor voltage and evaluation times.
- **Operations:** `solve_ivp` numerically solves the RC charging differential equation; compare with the analytical curve.
- **Parameter change:** Double the capacitance.
- **Expected effect:** The circuit charges more slowly because the time constant RC doubles.
- **Related case:** Modelling charging in electronic circuits.
- **Assumption:** Ideal resistor and capacitor; supply voltage is constant.

## Task 19 — Optimization
- **Inputs:** Cost and capacity coefficients for two server types, non-negativity bounds and a minimum capacity.
- **Operations:** SLSQP continuous constrained optimization; a finite search checks integer server counts.
- **Parameter change:** Raise required capacity from 1,000 to 1,200 units.
- **Expected effect:** The least-cost plan must provide more capacity and generally costs more.
- **Related case:** Planning cloud-computing or warehouse capacity.
- **Assumption:** Costs and capacities are linear and each server type has fixed unit characteristics.

## Task 20 — Monte Carlo simulation
- **Inputs:** Simulated daily demand from a normal distribution, supply capacity and 100,000 trials.
- **Operations:** Estimate the probability that demand exceeds supply; plot the running estimate to show convergence.
- **Parameter change:** Add a 5,000-litre reserve.
- **Expected effect:** The estimated shortage probability decreases.
- **Related case:** Assessing water, electricity or inventory shortage risk.
- **Assumption:** Demand is normally distributed with fixed mean and standard deviation; this is an illustrative risk model, not a forecast.
