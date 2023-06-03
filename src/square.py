from python_aqa.figure import Figure


class Square(Figure):
    def __init__(self, a: int):
        self.a = a
        if a <= 0:
            raise ValueError('Impossible square')

    def perimeter(self):
        return self.a * 4

    def area(self):
        return self.a ** 2
