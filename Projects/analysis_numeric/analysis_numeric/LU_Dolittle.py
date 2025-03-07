import numpy as np

def lu_doolittle(A):
    """Performs LU decomposition (Doolittle) where L has diagonal ones and U is upper triangular"""
    n = A.shape[0]
    L = np.eye(n)  # Lower triangular matrix with ones on diagonal
    U = np.zeros((n, n))  # Upper triangular matrix

    for i in range(n):
        # Compute upper triangular matrix U
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        # Compute lower triangular matrix L
        for j in range(i+1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

    return L, U

def forward_substitution(L, b):
    """Solve Ly = b using forward substitution"""
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i, j] * y[j] for j in range(i))
    return y

def backward_substitution(U, y):
    """Solve Ux = y using backward substitution"""
    n = U.shape[0]
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i+1, n))) / U[i, i]
    return x

# Example matrix A and vector b
A = np.array([
    [4, -1, 1],
    [-1, 3, -2],
    [2, -2, 5]
], dtype=float)

b = np.array([5, -4, 1], dtype=float)

# Perform LU decomposition
L, U = lu_doolittle(A)

# Print results
print("\nU matrix:\n", U)
print("\nL matrix:\n", L)

# Solve Ax = b using LU decomposition
y = forward_substitution(L, b)
x = backward_substitution(U, y)

print("\nSolution y:\n", y)

# Print solution
print("\nSolution x:\n", x)
