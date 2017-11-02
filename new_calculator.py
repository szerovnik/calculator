from math import factorial


class Calculator:

    def __init__(self):
        pass

    def sum_ab(self, a, b):

        return a + b

    def subs_ab(self, a, b):

        return a - b

    def multiply_ab(self, a, b):

        return a * b

    def divide_ab(self, a, b):

        return a / b

    def power_2n(self, n):

        return 2 ** n

    def power_ax(self, a, x):

        return a ** x

    def factorial_n(self, n):

        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)