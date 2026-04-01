import unittest
from src import sistema
import numpy as np


class TestSistema(unittest.TestCase):


    def setUp(self):
        self.sistema_1 = np.array([[1, 1, 1, 6], [2, -1, 1, 3], [1, 2, -1, 3]], dtype=float)
        self.sistema_2 = np.array([[1, 2, 1, 7], [2, 7, 1, 21], [-3, -5, 2, -8]], dtype=float)
        self.sistema_3 = np.array([[1, 1, 1, 6], [2, 2, 2, 12], [1, -1, 1, 2]], dtype=float)
        self.sistema_4 = np.array([[1, 1, 1, 3], [2, 2, 2, 6], [1, 1, 1, 4]], dtype=int)

        self.sistema_5 = [[1, 1, 1, 6], [2, -1, 1, 3], [1, 2, -1, 3]]
        self.sistema_6 = np.array([[1, 1, 1], [2, 2, 2], [1, -1, 1]], dtype=float)
        self.sistema_7 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=float)
        self.sistema_8 = np.array([[1, 2, 'a', 7], [2, 7, 1, 21], [-3, -5, 2, -8]], dtype=object)


    def test_criar_sistema(self):
        resultado_1 = sistema.criar_sistema(3)
        resultado_2 = sistema.criar_sistema(5)

        np.testing.assert_array_equal(resultado_1, np.zeros((3, 4), dtype=float))
        np.testing.assert_array_equal(resultado_2, np.zeros((5, 6), dtype=float))


    def test_copiar_sistema(self):
        copia_1 = sistema.copiar_sistema(self.sistema_1)
        copia_2 = sistema.copiar_sistema(self.sistema_2)

        np.testing.assert_array_equal(copia_1, self.sistema_1)
        np.testing.assert_array_equal(copia_2, self.sistema_2)

        copia_1[0][0] = 999
        copia_2[1][1] = 888

        self.assertNotEqual(self.sistema_1[0][0], 999)
        self.assertNotEqual(self.sistema_2[1][1], 888)


    def test_validar_sistema(self):
        self.assertTrue(sistema.validar_sistema(self.sistema_1))
        self.assertTrue(sistema.validar_sistema(self.sistema_2))
        self.assertTrue(sistema.validar_sistema(self.sistema_3))
        self.assertTrue(sistema.validar_sistema(self.sistema_4))

        self.assertFalse(sistema.validar_sistema(self.sistema_5))
        self.assertFalse(sistema.validar_sistema(self.sistema_6))
        self.assertFalse(sistema.validar_sistema(self.sistema_7))
        self.assertFalse(sistema.validar_sistema(self.sistema_8))


    def test_obter_numero_de_variaveis(self):
        self.assertEqual(sistema.obter_numero_de_variaveis(self.sistema_1), 3)
        self.assertEqual(sistema.obter_numero_de_variaveis(self.sistema_2), 3)
        self.assertEqual(sistema.obter_numero_de_variaveis(self.sistema_3), 3)
        self.assertEqual(sistema.obter_numero_de_variaveis(self.sistema_4), 3)

        with self.assertRaises(ValueError):
            sistema.obter_numero_de_variaveis(self.sistema_7)


if __name__ == "__main__":
    unittest.main()
