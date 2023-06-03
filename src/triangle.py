from python_aqa.figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        if a + b < c or a + c < b or b + c < a or a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Impossible triangle')

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)
