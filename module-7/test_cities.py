"""Tests for city_functions.py."""

import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Does 'santiago, chile' return 'Santiago, Chile'?"""
        formatted_city = city_country("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
