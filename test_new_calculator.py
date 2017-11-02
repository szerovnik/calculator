import unittest

from new_calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        pass

    def test_sum_ab(self):
        calc = Calculator()

        sum_ab = calc.sum_ab(10, 11)
        print(sum_ab)
        self.assertEqual(sum_ab, 21)

    def test_subs_ab(self):
        calc = Calculator()

        sum_ab = calc.subs_ab(21, 7)
        print(sum_ab)
        self.assertEqual(sum_ab, 14)

    def test_multiply_ab(self):
        calc = Calculator()

        multiply_ab = calc.multiply_ab(5, 8)
        print(multiply_ab)
        self.assertEqual(multiply_ab, 40)

    def test_divide_ab(self):
        calc = Calculator()

        divide_ab = calc.divide_ab(15, 3)
        print(divide_ab)
        self.assertEqual(divide_ab, 5)

    def test_power_2n(self):
        calc = Calculator()

        power_2n = calc.power_2n(3)
        print(power_2n)
        self.assertEqual(power_2n, 8)

    def test_power_ax(self):
        calc = Calculator()

        power_ax = calc.power_ax(4, 2)
        print(power_ax)
        self.assertEqual(power_ax, 16)

    def test_factorial_n(self):
        calc = Calculator()

        factorial_n = calc.factorial_n(10)
        print(factorial_n)
        self.assertEqual(factorial_n, 3628800)
