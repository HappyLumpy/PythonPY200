class TriangleCalculator:

    @classmethod
    def area(cls, *args):
        if len(args) == 2:
            cls.area_height(*args)
        if len(args) == 3:
            cls.area_by_angle(*args)

    @staticmethod
    def area_by_angle(a, b, angle):
        ...

    @staticmethod
    def area_height(a, h):
        ...
