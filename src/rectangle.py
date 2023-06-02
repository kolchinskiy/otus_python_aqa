from figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        area = self.a * self.b
        super().__init__(name='rectangle', area=area)
        if a <= 0 or b <= 0:
            raise ValueError('Impossible rectangle')

    @property
    def perimeter(self):
        return self.a * 2 + self.b * 2


rectangle = Rectangle(10, 20)
rectangle.add_area('square')