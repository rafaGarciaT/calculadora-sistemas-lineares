import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from src import input_output
import numpy as np

class TestInputOutput(unittest.TestCase):

    def setUp(self):
        self.sistema_1 = np.array([[1, 1, 1, 6], [2, -1, 1, 3], [1, 2, -1, 3]], dtype=float)
        self.sistema_2 = np.array([[1, 2, 1, 7], [2, 7, 1, 21], [-3, -5, 2, -8]], dtype=float)
        self.sistema_3 = np.array([[1, 1, 1, 6], [2, 2, 2, 12], [1, -1, 1, 2]], dtype=float)
        self.sistema_4 = np.array([[1, 1, 1, 3], [2, 2, 2, 6], [1, 1, 1, 4]], dtype=int)

        self.sistema_5 = [[1, 1, 1, 6], [2, -1, 1, 3], [1, 2, -1, 3]]
        self.sistema_6 = np.array([[1, 1, 1], [2, 2, 2], [1, -1, 1]], dtype=float)
        self.sistema_7 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=float)
        self.sistema_8 = np.array([[1, 2, 'a', 7], [2, 7, 1, 21], [-3, -5, 2, -8]], dtype=object)


    def test_parse_numero(self):
        self.assertEqual(input_output.parse_numero("3.14"), 3.14)
        self.assertEqual(input_output.parse_numero("2,718"), 2.718)
        self.assertEqual(input_output.parse_numero("   42   "), 42.0)
        self.assertIsNone(input_output.parse_numero("abc"))
        self.assertIsNone(input_output.parse_numero(""))

    @patch("builtins.input", side_effect=["abc", "11", "3"])
    def test_solicitar_tamanho_de_sistema(self, _mock_input):
        valor = input_output.solicitar_tamanho_de_sistema()
        self.assertEqual(valor,3)

    @patch("builtins.input", side_effect=["1", "2,5", "3", "4", "x", "5", "6"])
    def test_solicitar_sistema(self, _mock_input):
        # n =2 => matrix shape (2,3)
        # inputs: x1, x2, b1, x1, x2(invalid then valid), b2
        sistema = input_output.solicitar_sistema(2)
        esperado = np.array([[1.0,2.5,3.0], [4.0,5.0,6.0]], dtype=float)
        np.testing.assert_allclose(sistema, esperado)

    def test_imprimir_sistema(self):
        sistema = np.array([[1.0,2.0,3.0], [4.0,5.0,6.0]])
        out = io.StringIO()
        with redirect_stdout(out):
            input_output.imprimir_sistema(sistema)
        texto = out.getvalue()
        self.assertIn("Matriz Aumentada [A|b]", texto)
        self.assertIn("|", texto)
        self.assertIn("1.00", texto)

    def test_imprimir_resultado_si(self):
        out = io.StringIO()
        with redirect_stdout(out):
            input_output.imprimir_resultado("SI")
        texto = out.getvalue()
        self.assertIn("Sistema Impossível", texto)

    def test_imprimir_resultado_spd(self):
        out = io.StringIO()
        with redirect_stdout(out):
            input_output.imprimir_resultado(np.array([1.25, -2.0]))
        texto = out.getvalue()
        self.assertIn("[SPD]", texto)
        self.assertIn("x1", texto)
        self.assertIn("x2", texto)


if __name__ == "__main__":
    unittest.main()