#!usr/bin/env python3
import numpy as np


# Check if the matrix is diagonally dominant
def is_diagonally_dominant(A):
    n = A.shape[0]
    for i in range(n):
        if abs(A[i, i]) < sum(abs(A[i, j]) for j in range(n) if j != i):
            return False
    return True


# Check if the matrix is positive definite
def is_positive_definite(A):
    return np.all(np.linalg.eigvals(A) > 0)


# Compute the spectral radius (largest absolute eigenvalue)
def spectral_radius(T):
    return max(abs(np.linalg.eigvals(T)))


# Compute the optimal relaxation factor w (SOR)
def optimal_omega(T):
    rho = spectral_radius(T)
    return 2 / (1 + np.sqrt(1 - rho ** 2))  # Optimal omega formula


# SOR Iterative Method
def sor(A, b, omega, tol=1e-6, max_iter=1000):
    n = A.shape[0]
    x = np.zeros(n)  # Initial guess
    iterations = 0

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))
            sum2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (1 - omega) * x_old[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)

        # Stopping condition
        error = np.linalg.norm(x - x_old) / np.linalg.norm(x)
        iterations += 1
        if error < tol:
            break

    return x, iterations, error


# Jacobi Method
def jacobi(A, b, tol=1e-6, max_iter=1000):
    n = A.shape[0]
    x = np.zeros(n)
    iterations = 0

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum_terms = sum(A[i, j] * x_old[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_terms) / A[i, i]

        error = np.linalg.norm(x - x_old) / np.linalg.norm(x)
        iterations += 1
        if error < tol:
            break

    return x, iterations, error


# Gauss-Seidel Method
def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    n = A.shape[0]
    x = np.zeros(n)
    iterations = 0

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))
            sum2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        error = np.linalg.norm(x - x_old) / np.linalg.norm(x)
        iterations += 1
        if error < tol:
            break

    return x, iterations, error


# Given system
A = np.array([[4, 1, -1],
              [-1, 3, 1],
              [2, 1, 5]], dtype=float)

b = np.array([5, -4, 1], dtype=float)

# Construct the Jacobi iteration matrix Tj
D = np.diag(np.diag(A))  # Diagonal matrix
L = np.tril(A, -1)  # Lower triangular part
U = np.triu(A, 1)  # Upper triangular part
Tj = -np.linalg.inv(D) @ (L + U)  # Jacobi iteration matrix

# Compute spectral radius of Tj
rho_Tj = spectral_radius(Tj)

# Compute optimal omega
omega_opt = optimal_omega(Tj)

# Check matrix properties
print("Is the matrix diagonally dominant?", is_diagonally_dominant(A))
print("Is the matrix positive definite?",   is_positive_definite(A))
print("Spectral radius of Tj:",             rho_Tj)
print("Optimal omega (SOR):",               omega_opt)

# Solve the system using Jacobi, Gauss-Seidel, and SOR
x_jacobi, iter_jacobi, error_jacobi = jacobi(A, b)
x_gauss, iter_gauss, error_gauss = gauss_seidel(A, b)
x_sor, iter_sor, error_sor = sor(A, b, omega_opt)

# Print results
print("\nNumber of iterations:")
print(f"Jacobi:             {iter_jacobi}")
print(f"Gauss-Seidel:       {iter_gauss}")
print(f"SOR (ω={omega_opt:.4f}):     {iter_sor}")

print("\nFinal errors:")
print(f"Jacobi:         {error_jacobi:.8f}")
print(f"Gauss-Seidel:   {error_gauss:.8f}")
print(f"SOR:            {error_sor:.8f}")

print("\nSolutions:")
print(f"Jacobi:         {x_jacobi}")
print(f"Gauss-Seidel:   {x_gauss}")
print(f"SOR:            {x_sor}")
