from figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        self.a = a
        area = self.a ** 2
        super().__init__(name='square', area=area)
        if a <= 0:
            raise ValueError('Impossible square')

    @property
    def perimeter(self):
        return self.a * 4


square = Square(10)
square.add_area('circle')
