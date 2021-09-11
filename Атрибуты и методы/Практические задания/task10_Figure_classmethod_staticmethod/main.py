class TriangleCalculator:
    """ Класс-калькулятор площадей треугольников. """

    @classmethod
    def area(cls, *args):
        """
        Метод, который считает площадь по разным формулам,
         в зависимости от количества переданных аргументов.
        """
        if len(args) == 2:
            cls.area_height(*args)
        if len(args) == 3:
            cls.area_by_angle(*args)

    @staticmethod
    def area_by_angle(a, b, angle):
        """ Формула площади по двум сторонам и углу между ними. """
        ...

    @staticmethod
    def area_height(a, h):
        """ Формула площади по основанию и высоте. """
        ...

