"""Sample test"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Calculations tests"""

    def test_add(self):
        """Testing adding two numbers"""

        res = calc.add(1, 9)

        self.assertEqual(res, 10)

    def test_sub(self):
        """Testing subtracting two numbers"""

        res = calc.sub(1, 9)

        self.assertEqual(res, 8)
