from taller_2.get_data import get_data
from taller_2.iterative_solution import solucion_iterativa

if __name__ == "__main__":

    # Obtenemos los datos
    S = get_data('input_data.txt')
    A_Total = solucion_iterativa(S)
    print(A_Total)
