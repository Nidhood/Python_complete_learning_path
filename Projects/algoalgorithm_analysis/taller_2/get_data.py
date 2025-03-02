"""
#-------------------------------------------------------------------------
# get_data  : Lee un archivo de entrada y extrae los rectángulos con validación de restricciones.
# @inputs   : Un archivo de texto donde cada línea representa un rectángulo en el formato x_u, y_u, x_d, y_d.
# @outputs  : Una lista de m rectángulos, cada uno representado como una tupla de tuplas S = ⟨S1, S2, . . . , Sm⟩.
# @author   : Ivan Dario Orozco Ibanez
#-------------------------------------------------------------------------
"""


def get_data(input_file):
    with open(input_file, 'r') as file:
        data = []
        previous_x_u = None  # Para validar x_i^u < x_{i+1}^u

        for line in file:

            # Dividir la línea por comas y eliminar espacios en blanco
            values = line.strip().split(',')

            # Intentar convertir los valores a enteros
            try:
                int_values = list(map(int, values))
            except ValueError:
                print(f"Error: La línea '{line.strip()}' contiene valores no numéricos.")
                continue

            # Verificar que hay exactamente 4 valores
            if len(int_values) != 4:
                print(f"Error: La línea '{line.strip()}' no tiene 4 valores.")
                continue

            x_u, y_u, x_d, y_d = int_values

            # Validaciones de las condiciones del problema
            if x_u < 0 or y_u < 0 or x_d < 0 or y_d < 0:
                print(f"Error: Coordenadas negativas en la línea '{line.strip()}'.")
                continue

            if x_u >= x_d or y_d >= y_u:
                print(
                    f"Error: Coordenadas inválidas (no cumplen con x_u < x_d y y_d < y_u) en la línea '{line.strip()}'.")
                continue

            if previous_x_u is not None and x_u <= previous_x_u:
                print(f"Error: Coordenadas x no están ordenadas en la línea '{line.strip()}'.")
                continue

            # Guardar el rectángulo si todas las condiciones son correctas
            rectangulo = ((x_u, y_u), (x_d, y_d))
            data.append(rectangulo)
            previous_x_u = x_u  # Actualizar el último x_u registrado

    return data