import numpy as np

def lu_crout(A):
    """Performs LU decomposition (Crout method) where L has full diagonal and U has ones on diagonal"""
    n = A.shape[0]
    L = np.zeros((n, n))  # Lower triangular matrix
    U = np.eye(n)  # Upper triangular matrix with ones on the diagonal

    for i in range(n):
        # Compute lower triangular matrix L
        L[i, i] = A[i, i] - sum(L[i, k] * U[k, i] for k in range(i))
        print(f"L_{i+1}{i+1} = {L[i, i]:.4f}")

        for j in range(i+1, n):
            L[j, i] = A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))
            L[j, i] /= U[i, i]  # Since U[i, i] = 1 in Crout's method
            print(f"L_{j+1}{i+1} = {L[j, i]:.4f}")

        # Compute upper triangular matrix U
        for j in range(i+1, n):
            U[i, j] = (A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))) / L[i, i]
            print(f"U_{i+1}{j+1} = {U[i, j]:.4f}")

    return L, U

def forward_substitution(L, b):
    """Solve Ly = b using forward substitution"""
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(L[i, j] * y[j] for j in range(i))) / L[i, i]
    return y

def backward_substitution(U, y):
    """Solve Ux = y using backward substitution"""
    n = U.shape[0]
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = y[i] - sum(U[i, j] * x[j] for j in range(i+1, n))
    return x

# Example matrix A and vector b
A = np.array([
    [3, 6, 9],
    [6, 3, 2],
    [9, 2, 3]
], dtype=float)

b = np.array([5, 8, 11], dtype=float)

# Perform LU decomposition (Crout)
L, U = lu_crout(A)

# Print results
print("\nL matrix:\n", L)
print("\nU matrix:\n", U)

# Solve Ax = b using LU decomposition
y = forward_substitution(L, b)
x = backward_substitution(U, y)

# Print solution
print("\nSolution y:\n", y)
print("\nSolution x:\n", x)
