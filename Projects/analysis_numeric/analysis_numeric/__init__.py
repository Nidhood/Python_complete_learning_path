import numpy as np

def cholesky_decomposition(A):
    """Performs LLᵀ decomposition on a symmetric positive definite matrix A"""
    n = A.shape[0]
    L = np.zeros((n, n))  # Lower triangular matrix

    for i in range(n):
        # Compute diagonal elements L_ii
        L[i, i] = np.sqrt(A[i, i] - sum(L[i, k]**2 for k in range(i)))
        print(f"L_{i+1}{i+1} = {L[i, i]:.4f}")

        for j in range(i+1, n):
            # Compute lower triangular elements L_ji
            L[j, i] = (A[j, i] - sum(L[j, k] * L[i, k] for k in range(i))) / L[i, i]
            print(f"L_{j+1}{i+1} = {L[j, i]:.4f}")

    return L

def forward_substitution(L, b):
    """Solve L * y = b using forward substitution"""
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, j] * y[j] for j in range(i))) / L[i, i]
    return y

def backward_substitution(LT, y):
    """Solve Lᵀ * x = y using backward substitution"""
    n = LT.shape[0]
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(LT[i, j] * x[j] for j in range(i+1, n))) / LT[i, i]
    return x

# Example symmetric positive definite matrix A and vector b
A = np.array([[4, 2, 4],
              [2, 10, 5],
              [4, 5, 6]], dtype=float)

b = np.array([3, -3, 1], dtype=float)

# Perform LLᵀ decomposition
L = cholesky_decomposition(A)
LT = L.T  # Transpose of L

# Print results
print("\nL matrix:\n", L)
print("\nLᵀ matrix:\n", LT)

# Verify decomposition: A = LLᵀ
A_reconstructed = L @ LT
print("\nReconstructed A (should match original A):\n", A_reconstructed)

# Solve Ax = b using Cholesky decomposition
y = forward_substitution(L, b)
x = backward_substitution(LT, y)

# Print solution
print("\nSolution x:\n", x)
