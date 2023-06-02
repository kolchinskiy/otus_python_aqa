class Figure:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def add_area(self, figure: str):
        area_1 = self.area
        if figure == 'triangle':
            from src.triangle import Triangle
            triangle = Triangle(13, 14, 15)
            area_2 = triangle.area
        elif figure == 'square':
            from src.square import Square
            square = Square(10)
            area_2 = square.area
        elif figure == 'rectangle':
            from src.rectangle import Rectangle
            rectangle = Rectangle(10, 20)
            area_2 = rectangle.area
        elif figure == 'circle':
            from src.circle import Circle
            circle = Circle(10)
            area_2 = circle.area
        else:
            raise ValueError('Not a figure')
        summa = area_1 + area_2
        return summa

