import unittest
from currency_converter import calcular_tasa_conversion, convertir_moneda


class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.tasas = {
            "USD": 1.0,
            "EUR": 0.85,
            "JPY": 110.0
        }

    def test_calcular_tasa_conversion(self):
        self.assertAlmostEqual(
            calcular_tasa_conversion(self.tasas, "USD", "EUR"), 0.85)
        self.assertAlmostEqual(
            calcular_tasa_conversion(self.tasas, "EUR", "USD"), 1.0 / 0.85)

    def test_convertir_moneda(self):
        self.assertAlmostEqual(
            convertir_moneda(self.tasas, "USD", "EUR", 100), 85.0)
        self.assertAlmostEqual(
            convertir_moneda(self.tasas, "EUR", "USD", 85), 100.0)


if __name__ == "__main__":
    unittest.main()
