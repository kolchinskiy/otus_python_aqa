class Figure:

    def add_area(self, figure):
        area_1 = self.area()
        area_2 = figure.area()
        summa = area_1 + area_2
        return summa