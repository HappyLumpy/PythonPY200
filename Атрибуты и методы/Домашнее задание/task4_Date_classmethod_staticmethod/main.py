class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
 
        self.is_valid_date(self.day, self.month, self.year)
    @classmethod
    def is_leap_year(self, year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0: 
          return self.DAY_OF_MONTH[1]
        else: 
          return self.DAY_OF_MONTH[0]
 
    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        list_of_day = self.is_leap_year(self.year)
        return list_of_day[self.month-1]
 
    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int):
          raise TypeError()
        if not isinstance(month, int):
          raise TypeError()
        if not isinstance(year, int):
          raise TypeError()
 
if __name__ == "__main__":
    date = Date(2,2,2020)
    print(date.get_max_day(1,2021))
