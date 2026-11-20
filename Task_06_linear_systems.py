"""Task 06: Solve a small water-blending model with linear equations."""
import numpy as np

# x and y are litres of two stock solutions.
# 2x + y = 14 (total solute units); x + 3y = 18 (second ingredient units).
A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([14.0, 18.0])
solution = np.linalg.solve(A, b)
x, y = solution

print(f"Stock solution A: {x:.2f} litres")
print(f"Stock solution B: {y:.2f} litres")
print("Equation check:", np.round(A @ solution, 6))
print("Residual norm:", np.linalg.norm(A @ solution - b))

# Parameter experiment: demand for the second ingredient increases by 3 units.
new_b = np.array([14.0, 21.0])
new_solution = np.linalg.solve(A, new_b)
print("New quantities after changing the second target:", np.round(new_solution, 3))
print("Interpretation: changing the target vector changes the required blend; "
      "the coefficient matrix still represents the same recipe relationships.")
