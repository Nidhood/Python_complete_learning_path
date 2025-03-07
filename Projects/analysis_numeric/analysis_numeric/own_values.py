import numpy as np
import sympy as sp


def eigenvalues_characteristic(A):
    """Calcula los valores propios resolviendo det(A - λI) = 0"""
    n = A.shape[0]
    λ = sp.symbols('λ')  # Definimos el símbolo lambda
    I = np.eye(n)  # Matriz identidad de tamaño n
    A_lambda = A - λ * I  # Matriz (A - λI)

    # Calculamos el determinante de (A - λI)
    det_eq = sp.det(sp.Matrix(A_lambda))

    # Resolvemos la ecuación característica det(A - λI) = 0
    eigenvalues = sp.solve(det_eq, λ)

    return eigenvalues


# Ejemplo de matriz
A = sp.Matrix([
    [0, "1/4", "-1/4"],
    ["1/3", 0, "2/3"],
    ["-2/5", "2/5", 0]
]).applyfunc(sp.sympify)

# Calcular valores propios
eigvals = eigenvalues_characteristic(A)

# Mostrar resultados
print("Valores propios (solución de det(A - λI) = 0):", eigvals)
