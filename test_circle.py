import math
import unittest

import circle


class CircleTestCase(unittest.TestCase):
    def test_area_integer(self):
        self.assertAlmostEqual(circle.area(3), 9 * math.pi)

    def test_area_fraction(self):
        self.assertAlmostEqual(circle.area(1.5), 2.25 * math.pi)

    def test_area_zero(self):
        self.assertAlmostEqual(circle.area(0), 0)

    def test_perimeter_integer(self):
        self.assertAlmostEqual(circle.perimeter(3), 6 * math.pi)

    def test_perimeter_fraction(self):
        self.assertAlmostEqual(circle.perimeter(1.5), 3 * math.pi)

    def test_perimeter_zero(self):
        self.assertAlmostEqual(circle.perimeter(0), 0)
