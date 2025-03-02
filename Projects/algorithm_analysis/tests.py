import unittest

from taller_2.iterative_solution import calculo_areas_absolutas, calculo_intersecciones, solucion_iterativa


def area_manual(S):
    """ Calcula manualmente el área total de los rectángulos (sin intersecciones). """
    return sum((x_d - x_u) * (y_u - y_d) for (x_u, y_u), (x_d, y_d) in S)


class TestAreaCalculation(unittest.TestCase):

    def asserts_call(self, data):
        """ Función auxiliar para probar todas las funciones en una sola llamada """
        A = calculo_areas_absolutas(data)
        I = calculo_intersecciones(data)
        area_calculada = solucion_iterativa(data)

        # Verificar que todas las áreas individuales sean positivas
        self.assertTrue(all(a > 0 for a in A), "Error: Se encontró un área negativa en A.")

        # Verificar que las intersecciones sean válidas
        self.assertTrue(all(i >= 0 for i in I), "Error: Se encontró un área negativa en I.")

        # Verificar que el área total sea coherente
        self.assertTrue(area_calculada > 0, "Error: El área total calculada es incorrecta.")

    def test_no_intersection(self):
        """ Prueba con rectángulos sin intersecciones """
        data = [
            ((0, 6), (3, 3)),
            ((4, 6), (6, 4)),
            ((7, 5), (9, 2))
        ]
        self.asserts_call(data)
        self.assertEqual(solucion_iterativa(data), area_manual(data))

    def test_full_overlap(self):
        """ Prueba con un rectángulo completamente dentro de otro """
        data = [
            ((0, 6), (6, 2)),  # Rectángulo grande
            ((2, 5), (4, 3))   # Rectángulo dentro del grande
        ]
        self.asserts_call(data)

    def test_partial_overlap(self):
        """ Prueba con intersección parcial entre dos rectángulos """
        data = [
            ((1, 5), (5, 1)),  # Rectángulo 1
            ((3, 6), (7, 2))   # Rectángulo 2 (se cruza con el primero)
        ]
        self.asserts_call(data)

    def test_multiple_overlaps(self):
        """ Prueba con múltiples intersecciones entre tres rectángulos """
        data = [
            ((1, 5), (4, 1)),  # Rectángulo 1
            ((2, 6), (6, 2)),  # Rectángulo 2
            ((3, 4), (5, 0))   # Rectángulo 3
        ]
        self.asserts_call(data)

    def test_complex_case(self):
        """ Prueba con una combinación de intersecciones complejas """
        data = [
            ((0, 6), (3, 3)),
            ((1, 3), (4, 2)),
            ((2, 4), (5, 3)),
            ((4, 6), (6, 1))
        ]
        self.asserts_call(data)

    def test_large_input(self):
        """ Prueba con un conjunto grande de rectángulos generados dinámicamente """
        data = [((i, 10), (i + 2, 5)) for i in range(0, 100, 2)]  # Rectángulos de tamaño fijo
        self.asserts_call(data)


if __name__ == '__main__':
    unittest.main()
