"""Task 11: Estimate a project's internal rate of return."""
from scipy.optimize import root_scalar

cash_flows = [-12000, 3500, 4000, 4500, 4000]

def npv(rate):
    if rate <= -1:
        raise ValueError("Rate must be greater than -1.")
    return sum(amount / (1 + rate)**year
               for year, amount in enumerate(cash_flows))

def derivative(rate):
    return sum(-year * amount / (1 + rate)**(year + 1)
               for year, amount in enumerate(cash_flows) if year)

newton = root_scalar(npv, fprime=derivative, x0=.12, method="newton")
secant = root_scalar(npv, x0=.05, x1=.25, method="secant")
print(f"Newton-Raphson IRR: {newton.root:.4%}")
print(f"Secant IRR: {secant.root:.4%}")
print(f"NPV at estimated IRR: {npv(newton.root):.8f}")
print(f"Iterations: Newton={newton.iterations}, Secant={secant.iterations}")

# Parameter experiment: increase year-four cash inflow by KSh 500.
changed = cash_flows.copy()
changed[-1] += 500
new_rate = root_scalar(
    lambda r: sum(cf/(1+r)**t for t, cf in enumerate(changed)),
    bracket=[0, 1], method="brentq"
).root
print(f"IRR after extra KSh 500 in year four: {new_rate:.4%}")
print("Interpretation: both methods seek the rate that makes the present value "
      "of inflows equal the initial investment.")
