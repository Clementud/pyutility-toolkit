import unittest

from main import (
    calculate_simple_interest,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    calculate_receipt_total,
    calculate_age,
)


class TestPyUtilityToolkit(unittest.TestCase):

    def test_simple_interest(self):
        interest, total = calculate_simple_interest(10000, 5, 2)

        self.assertEqual(interest, 1000)
        self.assertEqual(total, 11000)

    def test_simple_interest_rejects_negative_values(self):
        with self.assertRaises(ValueError):
            calculate_simple_interest(-100, 5, 2)

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(
            celsius_to_fahrenheit(25), 77
        )

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(
            fahrenheit_to_celsius(77), 25
        )

    def test_receipt_total(self):
        items = [
            ("Book", 1500, 2),
            ("Pen", 200, 3),
        ]

        self.assertAlmostEqual(
            calculate_receipt_total(items), 3600
        )

    def test_receipt_rejects_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_receipt_total([])

    def test_receipt_rejects_negative_price(self):
        items = [("Book", -100, 1)]

        with self.assertRaises(ValueError):
            calculate_receipt_total(items)

    def test_age_calculation(self):
        self.assertEqual(calculate_age(2000, 2026), 26)

    def test_age_rejects_future_birth_year(self):
        with self.assertRaises(ValueError):
            calculate_age(2027, 2026)


if __name__ == "__main__":
    unittest.main()