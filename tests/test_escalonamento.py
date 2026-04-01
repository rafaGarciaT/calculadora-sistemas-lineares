import unittest
from src import escalonamento
import numpy as np

class TestEscalonamento(unittest.TestCase):

    def setUp(self):
        self.sistema_1 = np.array([[1, 1, 1, 6], [2, -1, 1, 3], [1, 2, -1, 3]], dtype=float)
        self.sistema_2 = np.array([[1, 2, 1, 7], [2, 7, 1, 21], [-3, -5, 2, -8]], dtype=float)
        self.sistema_3 = np.array([[1, 1, 1, 6], [2, 2, 2, 12], [1, -1, 1, 2]], dtype=float)
        self.sistema_4 = np.array([[1, 1, 1, 3], [2, 2, 2, 6], [1, 1, 1, 4]], dtype=int)

    def test_escalonar_sistema(self):
        resultado_1 = escalonamento.escalonar_sistema(self.sistema_1)
        resultado_2 = escalonamento.escalonar_sistema(self.sistema_2)
        resultado_3 = escalonamento.escalonar_sistema(self.sistema_3)
        resultado_4 = escalonamento.escalonar_sistema(self.sistema_4)

        np.testing.assert_almost_equal(resultado_1, [[2, -1, 1, 3], [0, 2.5, -1.5, 1.5], [0, 0, 1.4, 3.6]], decimal=2)
        np.testing.assert_almost_equal(resultado_2,  [[-3, -5, 2, -8], [0, 3.66, 2.33, 15.66], [0, 0 ,1.45, 2.90]], decimal=2)
        np.testing.assert_almost_equal(resultado_3, [[2, 2, 2, 12], [0, -2, 0, -4], [0, 0, 0, 0]], decimal=2)
        np.testing.assert_array_equal(resultado_4, [[2, 2, 2, 6], [0, 0, 0, 0, ], [0, 0, 0, 1]])

if __name__ == "__main__":
    unittest.main()