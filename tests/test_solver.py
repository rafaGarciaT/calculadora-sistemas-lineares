import unittest
from src import solver
import numpy as np

class TestSolver(unittest.TestCase):

    def setUp(self):
        # SPD
        self.sistema_escalonado_1 = np.array([[2, -1, 1, 3], [0, 2.5, -1.5, 1.5], [0, 0, 1.4, 3.6]], dtype=float)
        self.sistema_escalonado_2 = np.array([[1, 2, 1, 7], [0, 1, 5, 13], [0, 0, -16, -32]], dtype=float)
        # SPI
        self.sistema_escalonado_3 = np.array([[2, 2, 2, 12], [0, -2, 0, -4], [0, 0, 0, 0]], dtype=float)
        # SI
        self.sistema_escalonado_4 = np.array([[2, 2, 2, 6], [0, 0, 0, 0, ], [0, 0, 0, 1]], dtype=int)


    def test_classificar_sistema(self):
        self.assertEqual(solver.classificar_sistema(self.sistema_escalonado_1), "SPD")
        self.assertEqual(solver.classificar_sistema(self.sistema_escalonado_2), "SPD")
        self.assertEqual(solver.classificar_sistema(self.sistema_escalonado_3), "SPI")
        self.assertEqual(solver.classificar_sistema(self.sistema_escalonado_4), "SI")

    def test_substituicao_retroativa(self):
        np.testing.assert_almost_equal(solver.substituicao_retroativa(self.sistema_escalonado_1), [1.28, 2.14, 2.57], decimal=2)
        np.testing.assert_array_equal(solver.substituicao_retroativa(self.sistema_escalonado_2), np.array([-1, 3, 2], dtype=float))

    def test_resolver(self):
        resultado_1 = solver.resolver(self.sistema_escalonado_1)
        resultado_2 = solver.resolver(self.sistema_escalonado_2)
        resultado_3 = solver.resolver(self.sistema_escalonado_3)
        resultado_4 = solver.resolver(self.sistema_escalonado_4)

        np.testing.assert_almost_equal(resultado_1, [1.28, 2.14, 2.57], decimal=2)
        np.testing.assert_array_equal(resultado_2, np.array([-1, 3, 2], dtype=float))
        self.assertEqual(resultado_3, "SPI")
        self.assertEqual(resultado_4, "SI")

if __name__ == "__main__":
    unittest.main()