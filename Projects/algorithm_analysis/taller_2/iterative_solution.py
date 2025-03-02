"""
#-------------------------------------------------------------------------
# iterative_solution: Iterativamente encuentra el area y las intersecciones de un conjunto de rectangulos, para luego calcular el area total.
# @inputs           : Un conjunto de m rectángulos representado como una secuencia S = ⟨S1, S2, . . . , Sm⟩.
# @outputs          : Un valor entero A ∈ N, donde A = A1 ∪ A2 ∪ A3 ∪ · · · ∪ An y A > 0.
# @author           : Ivan Dario Orozco Ibanez
#-------------------------------------------------------------------------
"""

def calculo_areas_absolutas(S):
    n = len(S)
    A = []

    # Iteramos sobre los rectangulos:
    for i in range(n):

        # Obtenemos el largo del rectangulo i:
        ancho = S[i][1][0] - S[i][0][0]

        # Obtenemos el ancho del rectangulo i:
        largo = S[i][0][1] - S[i][1][1]

        # Calculamos el area del rectangulo i:
        area = ancho * largo
        A.append(area)
    # end for
    return A


def calculo_intersecciones(S):
    n = len(S)
    I = []

    # Iteramos sobre los rectangulos:
    for i in range(n):

        # Definimos el espacio del rectangulo i:
        x_u_i, y_u_i = S[i][0]
        x_d_i, y_d_i = S[i][1]

        # Comparamos con los otros rectangulos:
        for j in range(i + 1, n):

            # Definimos el espacio del rectángulo j:
            x_u_j, y_u_j = S[j][0]
            x_d_j, y_d_j = S[j][1]

            # Conseguimos las coordenadas del rectangulo interseccion:
            x_izq = max(x_u_i, x_u_j)
            x_der = min(x_d_i, x_d_j)
            y_arr = min(y_u_i, y_u_j)
            y_aba = max(y_d_i, y_d_j)

            if x_izq < x_der and y_aba < y_arr:

                # Obtenemos el largo del rectangulo interseccion:
                largo = x_der - x_izq

                # Obtenemos el ancho del rectangulo interseccion:
                ancho = y_arr - y_aba

                # Calculamos el area del rectangulo interseccion:
                area = largo * ancho
                I.append(area)
            # end if
        # end for
    # end for
    return I

def area_total(A, I):
    return sum(A) - sum(I)


def solucion_iterativa(S):
    A = calculo_areas_absolutas(S)
    I = calculo_intersecciones(S)
    return area_total(A, I)