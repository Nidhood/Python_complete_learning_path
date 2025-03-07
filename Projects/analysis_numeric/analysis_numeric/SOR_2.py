import numpy as np


def reorganize_system(A, b):
    """Reorganiza el sistema Ax = b para hacerlo diagonalmente dominante si es posible."""
    n = A.shape[0]
    for i in range(n):
        # Encontrar la fila con el mayor valor absoluto en la columna i
        max_row = max(range(i, n), key=lambda r: abs(A[r, i]))
        # Intercambiar filas si es necesario
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
    # Verificar si la matriz ahora es diagonalmente dominante
    for i in range(n):
        if abs(A[i, i]) < sum(abs(A[i, j]) for j in range(n) if j != i):
            raise ValueError("No se pudo hacer la matriz diagonalmente dominante.")
    return A, b


def direct_T(A):
    """
    Construye la matriz de iteración despejando cada variable:
      x_i = (1/a_ii) * (b_i - sum_{j ≠ i} a_ij * x_j)
    Esto implica:
      T[i,j] = -a_ij / a_ii   para j ≠ i, y T[i,i] = 0.
    """
    n = A.shape[0]
    T = np.zeros_like(A)
    for i in range(n):
        for j in range(n):
            if i != j:
                T[i, j] = -A[i, j] / A[i, i]
    return T


def optimal_omega(A):
    """
    Calcula el factor de relajación óptimo ω usando el máximo valor propio
    (en valor absoluto) de la matriz de iteración T.
    """
    T = direct_T(A)
    print("\nMatriz de iteración T (despejada):")
    print(T)

    # Calcular los valores propios de T
    eigenvalues = np.linalg.eigvals(T)
    print("\nValores propios de T:")
    print(eigenvalues)

    # Seleccionar el valor propio con mayor valor absoluto
    max_eigen = max(eigenvalues, key=lambda ev: abs(ev))
    rho = abs(max_eigen)
    print(f"\nValor propio absoluto máximo: {rho}")

    # Verificar convergencia
    if rho >= 1:
        raise ValueError("El método SOR puede no converger, ya que ρ(T) ≥ 1.")

    # Cálculo del ω óptimo usando la fórmula
    omega_opt = 2 / (1 + np.sqrt(1 - rho ** 2))
    return omega_opt


def sor(A, b, x0, tol=1e-6, max_iter=10, omega=None):
    """Resuelve el sistema Ax = b usando el metodo SOR."""
    n = A.shape[0]
    x = np.array(x0, dtype=float)

    if omega is None:
        omega = optimal_omega(A)

    print(f"\nUsando ω = {omega:.4f}\n")

    for k in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            # Sumar las partes ya actualizadas y no actualizadas
            sum1 = sum(A[i, j] * x_new[j] for j in range(i))
            sum2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            x_new[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)

        print(f"Iteración {k + 1}: x = {x_new}")
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x


# Definir el sistema de ecuaciones
A = np.array([
    [4, -1, 1],
    [-1, 3, -2],
    [2, -2, 5]
], dtype=float)

b = np.array([5, -4, 1], dtype=float)

# Reorganizar el sistema si es necesario para hacerlo diagonalmente dominante
A_np, b_np = reorganize_system(A, b)

# Vector inicial
x0 = [0, 0, 0]

# Definir número de iteraciones
num_iteraciones = 2

# Resolver el sistema usando el metodo SOR
x_sor = sor(A_np, b_np, x0, max_iter=num_iteraciones)

print("\nSolución final después de", num_iteraciones, "iteraciones:", x_sor)
