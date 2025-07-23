import math

# 1) Define la funcion f(x) = x^2 e^x
def f(x):
    return x**2 * math.exp(x)

# 2) Implementamos la regla compuesta de Simpson según
#    ∫_a^b f(x) dx ≈ h/3 [ f(a) + f(b)
#                         + 4 * Σ_{j=1}^{n/2} f(x_{2j-1})
#                         + 2 * Σ_{j=1}^{n/2 - 1} f(x_{2j}) ]
def simpson_compuesta(a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par")
    h = (b - a) / n

    # 2.1) Terminos en los extremos
    suma_extremos = f(a) + f(b)
    print(f"f(a) + f(b) = {suma_extremos:.6f}")

    # 2.2) Suma sobre indices impares: x_{2j-1}, j = 1..n/2
    suma_impares = 0.0
    for j in range(1, n//2 + 1):
        x_2j_1 = a + (2*j - 1)*h
        valor = f(x_2j_1)
        print(f"f(x_{{2*{j}-1}}) = f({x_2j_1:.6f}) = {valor:.6f}")
        suma_impares += valor
    print(f"Suma impares Σ f(x_{{2j-1}}) = {suma_impares:.6f}")

    # 2.3) Suma sobre indices pares: x_{2j}, j = 1..n/2-1
    suma_pares = 0.0
    for j in range(1, n//2):
        x_2j = a + (2*j)*h
        valor = f(x_2j)
        print(f"f(x_{{2*{j}}}) = f({x_2j:.6f}) = {valor:.6f}")
        suma_pares += valor
    print(f"Suma pares Σ f(x_{{2j}}) = {suma_pares:.6f}")

    # 2.4) Aplica el factor 4 y 2
    termino_4 = 4 * suma_impares
    termino_2 = 2 * suma_pares
    print(f"4 * Σ impares = {termino_4:.6f}")
    print(f"2 * Σ pares   = {termino_2:.6f}")

    # 2.5) Resultado final
    integral = (h/3) * (suma_extremos + termino_4 + termino_2)
    print(f"h = {h:.6f}")
    print(f"Integral ≈ (h/3) * [extremos + 4 Σ impares + 2 Σ pares] = {integral:.6f}")
    return integral

# 3) Evaluamos para n=4 y n=8
a, b = 0.0, 4.0
for n in (4, 8):
    print(f"\n--- Simpson compuesta con n = {n} ---")
    simpson_compuesta(a, b, n)