import unittest
from src.currency_converter import calculate_conversion_rate, convert_currency


class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "JPY": 110.0
        }

    def test_calculate_conversion_rate(self):
        self.assertAlmostEqual(
            calculate_conversion_rate(self.rates, "USD", "EUR"), 0.85)
        self.assertAlmostEqual(
            calculate_conversion_rate(self.rates, "EUR", "USD"), 1.0 / 0.85)

    def test_convert_currency(self):
        self.assertAlmostEqual(
            convert_currency(self.rates, "USD", "EUR", 100), 85.0)
        self.assertAlmostEqual(
            convert_currency(self.rates, "EUR", "USD", 85), 100.0)


if __name__ == "__main__":
    unittest.main()
