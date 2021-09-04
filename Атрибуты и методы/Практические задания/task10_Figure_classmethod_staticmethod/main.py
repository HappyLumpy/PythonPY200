class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """

    def area(self, *args):
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            self.area_height(*args)
        if len(args) == 3:
            self.area_by_angle(*args)

    def area_by_angle(self, a, b, angle):
        """ Формула площади по двум сторонам и углу между ними. """
        ...

    def area_height(self, a, h):
        """ Формула площади по основанию и высоте. """
        ...
