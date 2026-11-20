"""Task 08: Jacobi and Gauss-Seidel methods for heat along a metal bar."""
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[4., -1., 0., 0.], [-1., 4., -1., 0.],
              [0., -1., 4., -1.], [0., 0., -1., 3.]])
b = np.array([80., 20., 20., 40.])

def jacobi(matrix, rhs, tolerance=1e-9, max_iter=1000):
    diagonal = np.diag(matrix)
    remainder = matrix - np.diagflat(diagonal)
    x = np.zeros_like(rhs)
    errors = []
    for _ in range(max_iter):
        updated = (rhs - remainder @ x) / diagonal
        errors.append(np.linalg.norm(updated - x, ord=np.inf))
        if errors[-1] < tolerance:
            return updated, errors
        x = updated
    raise RuntimeError("Jacobi method did not converge.")

def gauss_seidel(matrix, rhs, tolerance=1e-9, max_iter=1000):
    x = np.zeros_like(rhs)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(rhs)):
            x[i] = (rhs[i] - matrix[i, :i] @ x[:i]
                    - matrix[i, i+1:] @ old[i+1:]) / matrix[i, i]
        errors.append(np.linalg.norm(x - old, ord=np.inf))
        if errors[-1] < tolerance:
            return x, errors
    raise RuntimeError("Gauss-Seidel method did not converge.")

xj, ej = jacobi(A, b)
xg, eg = gauss_seidel(A, b)
xd = np.linalg.solve(A, b)
print("Estimated internal temperatures (Jacobi):", np.round(xj, 5))
print("Estimated internal temperatures (Gauss-Seidel):", np.round(xg, 5))
print("Direct solution:", np.round(xd, 5))
print(f"Iterations: Jacobi={len(ej)}, Gauss-Seidel={len(eg)}")

# Parameter experiment: stricter stopping tolerance.
strict_solution, strict_errors = gauss_seidel(A, b, tolerance=1e-11)
print("Iterations at 1e-11 tolerance:", len(strict_errors))
plt.semilogy(ej, label="Jacobi")
plt.semilogy(eg, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum update size")
plt.title("Convergence of heat-bar iterative methods")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
