from python_aqa.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r: int):
        self.r = r
        if r <= 0:
            raise ValueError('Impossible circle')

    def perimeter(self):
        return round(2 * pi * self.r, 2)

    def area(self):
        return round(pi * self.r ** 2, 2)
