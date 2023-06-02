from figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, r: int):
        self.r = r
        area = pi * self.r ** 2
        super().__init__(name='circle', area=area)
        if r <= 0:
            raise ValueError('Impossible circle')

    @property
    def perimeter(self):
        return 2 * pi * self.r


circle = Circle(10)
circle.add_area('square')