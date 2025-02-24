#!usr/bin/env python3
import numpy as np

def LDLT_decomposition(A):
    """Performs LDLᵀ decomposition on a symmetric matrix A"""
    n = A.shape[0]
    L = np.eye(n)  # Identity matrix (unit lower triangular)
    D = np.zeros((n, n))  # Diagonal matrix

    for i in range(n):
        # Compute d_i (diagonal elements of D)
        D[i, i] = A[i, i] - sum(L[i, k]**2 * D[k, k] for k in range(i))
        print(f"d_{i+1} = {D[i, i]:.4f}")

        for j in range(i+1, n):
            # Compute l_ji (lower triangular elements of L)
            L[j, i] = (A[j, i] - sum(L[j, k] * L[i, k] * D[k, k] for k in range(i))) / D[i, i]
            print(f"l_{j+1}{i+1} = {L[j, i]:.4f}")

    return L, D

def forward_substitution(L, b):
    """Solve L * y = b using forward substitution"""
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
    return y

def diagonal_substitution(D, y):
    """Solve D * z = y (since D is diagonal)"""
    return y / np.diag(D)

def backward_substitution(LT, z):
    """Solve Lᵀ * x = z using backward substitution"""
    n = LT.shape[0]
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (z[i] - sum(LT[i, j] * x[j] for j in range(i+1, n))) / LT[i, i]
    return x

# Example matrix A (symmetric) and vector b
A = np.array([
    [2, -1, 0, 0, 0],
    [-1, 2, -1, 0, 0],
    [0, -1, 2, -1, 0],
    [0, 0, -1, 2, -1],
    [0, 0, 0, -1, 2]

], dtype=float)

b = np.array([5.0, -5.0, 4.0, -5.0, 5.0], dtype=float)
# Perform LDLᵀ decomposition
L, D = LDLT_decomposition(A)
LT = L.T  # Transpose of L

# Print results
print("\nL matrix:\n", L)
print("\nD matrix:\n", D)
print("\nLᵀ matrix:\n", LT)

# Verify decomposition: A = L D Lᵀ
A_reconstructed = L @ D @ LT
print("\nReconstructed A (should match original A):\n", A_reconstructed)

# Solve Ax = b using LDLᵀ decomposition
y = forward_substitution(L, b)
z = diagonal_substitution(D, y)
x = backward_substitution(LT, z)

# Print solution
print("\nSolution x:\n", x)
