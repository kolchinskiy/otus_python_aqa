from figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        p = self.perimeter / 2
        area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        super().__init__(name='triangle', area=area)
        if a + b < c or a + c < b or b + c < a or a <= 0 or b <= 0 or c <= 0:
            raise ValueError('Impossible triangle')

    @property
    def perimeter(self):
        return self.a + self.b + self.c


triangle = Triangle(13, 14, 15)
triangle.add_area('square')