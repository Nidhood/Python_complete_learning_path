#!usr/bin/env python3
import numpy as np


# Comprobamos que la matriz 'A' es diagonalmente dominante:
def is_diagonally_dominant(A):
    n = A.shape[0]
    for i in range(n):

        # Suma de los valores absolutos fuera de la diagonal
        row_sum = 0
        for j in range(n):
            if j != i:
                row_sum += abs(A[i, j])

        if abs(A[i, i]) < row_sum:

            # Si una fila no cumple, la matriz no es diagonalmente dominante
            return False

    # Si ninguna fila falla, la matriz es diagonalmente dominante
    return True


# Comprobamos si la matriz es definida positiva:
def is_positive_definite(A):

    # Comprobamos si todos los valores propios son positivos (la profe nos dejo una funcion que ya hace esto):
    return np.all(np.linalg.eigvals(A) > 0)


# Encontramos los valores propios (la profe nos dejo una funcion que ya hace esto):
def dominant_eigenvalue(T):

    # Encuentra el valor propio dominante de la matriz T (mayor en magnitud):
    return max(abs(np.linalg.eigvals(T)))


# Encontramos el factor de relajacion w (SOR) ideal:
def optimal_omega(T):
    rho = dominant_eigenvalue(T)

    # Fórmula del omega optimo
    return 2 / (1 + np.sqrt(1 - rho ** 2))

# Metodo iterativo SOR
def sor(A, b, omega, tol=0.000001):
    n = A.shape[0]
    x = np.zeros(n)  # Valor inicial
    iterations = 0
    error = float('inf')

    while error > tol:
        x_old = x.copy()
        for i in range(n):

            # Sumar los términos ya actualizados
            sum1 = 0
            for j in range(i):
                sum1 += A[i, j] * x[j]

            sum2 = 0
            for j in range(i + 1, n):
                sum2 += A[i, j] * x_old[j]

            # Actualizamos el valor de x[i] según SOR:
            x[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)

        error = np.linalg.norm(x - x_old)
        iterations += 1
    return x, iterations, error


# Metodo iterativo de Jacobi
def jacobi(A, b, tol=0.000001):
    n = A.shape[0]
    x = np.zeros(n)
    iterations = 0
    error = float('inf')  # Iniciamos con un valor grande

    while error > tol:
        x_old = x.copy()
        for i in range(n):
            sum_terms = 0  # Acumulamos términos excepto la diagonal
            for j in range(n):
                if j != i:
                    sum_terms += A[i, j] * x_old[j]

            x[i] = (b[i] - sum_terms) / A[i, i]

        error = np.linalg.norm(x - x_old)
        iterations += 1

    return x, iterations, error

# Metodo iterativo de Gauss-Seidel
def gauss_seidel(A, b, tol=0.000001):
    n = A.shape[0]
    x = np.zeros(n)
    iterations = 0
    error = float('inf')

    while error > tol:
        x_old = x.copy()  # Para calcular error, pero no para actualizar valores
        for i in range(n):
            sum1 = 0  # Acumulamos valores ya actualizados
            for j in range(i):
                sum1 += A[i, j] * x[j]

            sum2 = 0  # Usamos valores anteriores
            for j in range(i + 1, n):
                sum2 += A[i, j] * x[j]

            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        error = np.linalg.norm(x - x_old)
        iterations += 1

    return x, iterations, error

# Sistema de ecuaciones
A = np.array([
    [4, 1, -1],
    [-1, 3, 1],
    [2, 1, 5]],
    dtype=float)
b = np.array([5, -4, 1], dtype=float)

# Calculamos la matriz Tj
Tj = np.zeros_like(A, dtype=float)

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if i != j:
            Tj[i, j] = -(A[i, j] / A[i, i])

# Encontramos los valores propios de Tj
eigenvalues_Tj = np.linalg.eigvals(Tj)

# Encontramos el valor propio dominante de Tj (de mayor magnitud):
rho_Tj = dominant_eigenvalue(Tj)

# Encontramos el factor de relajacion w (SOR) ideal:
omega_opt = optimal_omega(Tj)

# Verificamos si la matriz es diagonalmente dominante y definida positiva:

# Incluya en su algoritmo un metodo que eval´ue si la matriz del sistema cumple la condicion de ser Diagonal Dominante:
print("¿La matriz es diagonalmente dominante?", is_diagonally_dominant(A))

# Incluya e su algoritmo un metodo que determine si la matriz es definida positiva.
print("¿La matriz es definida positiva?", is_positive_definite(A))

# Los valores propios para la matriz Tj:
print("\nValores propios de Tj:", eigenvalues_Tj)

# El radio espectral ρ(Tj):
print("Radio espectral de Tj:", rho_Tj)

# Un valor optimo para ω:
print("Factor de relajación óptimo (ω) en SOR:", omega_opt)

# Resolvemos el sistema con los metodos iterativos:
x_jacobi, iter_jacobi, error_jacobi = jacobi(A, b)
x_gauss, iter_gauss, error_gauss = gauss_seidel(A, b)
x_sor, iter_sor, error_sor = sor(A, b, omega_opt)

# A partir de los algoritmos de Gauss Jacobi y Gauss Seidel, compare el numero de iteraciones necesarias con cada metodo.
print("\nNúmero de iteraciones:")
print(f"Método de Jacobi:       {iter_jacobi}")
print(f"Método de Gauss-Seidel: {iter_gauss}")
print(f"Método SOR (ω={omega_opt:.4f}): {iter_sor}")

# Determine el error en la ultima iteracion:
print("\nErrores finales:")
print(f"Jacobi:         {error_jacobi:.8f}")
print(f"Gauss-Seidel:   {error_gauss:.8f}")
print(f"SOR:            {error_sor:.8f}")

# La solucion del sistema.
print("\nSoluciones obtenidas:")
print(f"Jacobi:         {x_jacobi}")
print(f"Gauss-Seidel:   {x_gauss}")
print(f"SOR:            {x_sor}")
