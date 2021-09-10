class Date:
    def __init__(self, day: [int], month: [int], year: [int]):
        self.day = None
        self.correct_day(day)
        self.month = None
        self.correct_month(month)
        self.year = None
        self.correct_year(year)

    def correct_day(self, day):
        if not isinstance(day, int):
            raise TypeError()
        self.day = day

    def correct_month(self, month):
        if not isinstance(month, int):
            raise TypeError()
        self.month = month

    def correct_year(self, year):
        if not isinstance(year, int):
            raise TypeError()
        self.year = year

    def __str__(self):
        if self.day and self.month < 10:
            return f"0{self.day}/0{self.month}/{self.year}"
        elif self.day < 10:
            return f"0{self.day}/{self.month}/{self.year}"
        elif self.month < 10:
            return f"{self.day}/0{self.month}/{self.year}"
        else:
            return f"{self.day}/{self.month}/{self.year}"

    def __repr__(self):
        return f"Node({self.day}, {self.month}, {self.year})"


if __name__ == "__main__":
    date = Date(12, 5, 1993)
    print(date)
