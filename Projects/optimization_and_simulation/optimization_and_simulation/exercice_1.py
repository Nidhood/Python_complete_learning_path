from pulp import *

ruta = [i for i in range(1, 7)]
cliente = [j for j in range(1, 6)]

# Parametros:
distancias = {1 : 80, 2: 51, 3 : 60, 4 : 52, 5 : 60, 6 : 44}

compRutas = {1 :{1 : 1, 2 : 1, 3 : 1, 4 : 1, 5 : 0},
             2 : {1 : 0, 2 : 0, 3 : 1, 4 : 1, 5 : 1},
             3 : {1 : 1, 2 : 1, 3 : 0, 4 : 0, 5 : 1},
             4 : {1 : 0, 2 : 1, 3 : 1, 4 : 0, 5 : 1},
             5 : {1 : 1, 2 : 1, 3 : 0, 4 : 1, 5 : 0},
             6 : {1 : 1, 2 : 0, 3 : 1, 4 : 0, 5 : 1}}

# para todas las rutas se debe cumplir que y[r][c] tiene que se menor o igual

# Variables
x = LpVariable.dicts("x", (ruta), cat = "Binary")
y = LpVariable.dicts("y", (ruta, cliente), cat = "Binary")

# Función objetivo
prob = LpProblem("Asignacion", LpMinimize)
prob += lpSum(x[r] * distancias[r] for r in ruta)

# Restricciones:
for r in ruta:  # Restriccion de empalme:
    prob += lpSum(y[r][c] for c in cliente) <= x[r]*10

for c in cliente:  # Todos deben ser visitados:
    prob += lpSum(y[r][c] for r in ruta) >= 1

for r in ruta:  # Debe cumplirse la conformacion de las rutas:
    for c in cliente:
        prob += y[r][c] <= compRutas[r][c]


prob.solve()
print(LpStatus[prob.status])

for i in prob.variables():
    if i.varValue > 0:
        print(i.name, i.varValue)
print(value(prob.objective))



