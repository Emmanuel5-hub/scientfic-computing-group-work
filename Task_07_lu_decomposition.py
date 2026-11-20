"""Task 07: LU factorization for a three-variable production model."""
import numpy as np
from scipy.linalg import lu, solve_triangular

A = np.array([[3., 2., -1.], [2., -2., 4.], [-1., .5, -1.]])
b = np.array([1., -2., 0.])

P, L, U = lu(A)
intermediate = solve_triangular(L, P @ b, lower=True, unit_diagonal=True)
solution = solve_triangular(U, intermediate)

print("Permutation matrix P:\n", P)
print("Lower triangular matrix L:\n", L)
print("Upper triangular matrix U:\n", U)
print("Solution:", np.round(solution, 6))
print("Factorization check ||A - PLU||:", np.linalg.norm(A - P @ L @ U))
print("System residual:", np.linalg.norm(A @ solution - b))

# Parameter experiment: increase the final requirement by 10%.
b_changed = b.copy()
b_changed[-1] *= 1.10
z = solve_triangular(L, P @ b_changed, lower=True, unit_diagonal=True)
changed_solution = solve_triangular(U, z)
print("Solution after changing final requirement:", np.round(changed_solution, 6))
print("Interpretation: LU reuses the matrix factorization when only the right-hand "
      "side changes, making repeated solves more efficient.")
