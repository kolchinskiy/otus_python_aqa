class Figure:

    def add_area(self, figure):
        if isinstance(figure, Figure):
            area_1 = self.area()
            area_2 = figure.area()
            summa = area_1 + area_2
            return summa
        raise ValueError(f'Object {figure} is not subclass of Figure class')
