import numpy as np

def PLU_decomposition(A):
    """Performs PLU decomposition with partial pivoting"""
    n = A.shape[0]
    P = np.eye(n)  # Permutation matrix (identity at the start)
    L = np.eye(n)  # Lower triangular matrix with ones on the diagonal
    U = A.copy().astype(float)  # Upper triangular matrix

    for i in range(n):
        # Pivot: Find the row with the largest absolute value in column i
        pivot = np.argmax(np.abs(U[i:n, i])) + i
        if pivot != i:
            # Swap rows in U
            U[[i, pivot]] = U[[pivot, i]]
            # Swap rows in P
            P[[i, pivot]] = P[[pivot, i]]
            # Swap rows in L (except the diagonal part)
            if i > 0:
                L[[i, pivot], :i] = L[[pivot, i], :i]

        # Compute L and U using Gaussian elimination
        for j in range(i+1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j] -= L[j, i] * U[i]  # Row operation to make U upper triangular

            print(f"L_{j+1}{i+1} = {L[j, i]:.4f}")

    return P, L, U

def forward_substitution(L, Pb):
    """Solve L * y = Pb using forward substitution"""
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        y[i] = Pb[i] - sum(L[i, j] * y[j] for j in range(i))
    return y

def backward_substitution(U, y):
    """Solve U * x = y using backward substitution"""
    n = U.shape[0]
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i, j] * x[j] for j in range(i+1, n))) / U[i, i]
    return x

# Example matrix A and vector b
A = np.array([

    [1, 1, -1, 0],
    [1, 1, 4, 3],
    [2, -1, 2, 4],
    [2, -1, 2, 3]
              ], dtype=float)

b = np.array([10, -15, 20, 5], dtype=float)

# Perform PLU decomposition
P, L, U = PLU_decomposition(A)

# Print results
print("\nP matrix:\n", P)
print("\nL matrix:\n", L)
print("\nU matrix:\n", U)

# Verify decomposition: PA = LU
PA = P @ A
LU = L @ U
print("\nPA (should match LU):\n", PA)
print("\nLU:\n", LU)

# Solve Ax = b using PLU decomposition
Pb = P @ b  # Apply permutation to b
y = forward_substitution(L, Pb)
x = backward_substitution(U, y)

# Print solution
print("\nSolution x:\n", x)
