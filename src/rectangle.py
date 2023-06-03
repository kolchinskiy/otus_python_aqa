from python_aqa.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        if a <= 0 or b <= 0:
            raise ValueError('Impossible rectangle')

    def perimeter(self):
        return self.a * 2 + self.b * 2

    def area(self):
        return self.a * self.b
