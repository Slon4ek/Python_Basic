class DateException(Exception):
    def __str__(self):
        return 'Неверная дата!'


class Date:
    __large_months = [1, 3, 5, 6, 8, 10, 12]
    __small_months = [4, 7, 9, 11]
    __feb = 2

    def __init__(self, day: int, month: int, year: int) -> None:
        self._day = day
        self._month = month
        self._year = year

    def __str__(self) -> str:
        return 'День: {} Месяц: {} Год: {}'.format(
            self._day,
            self._month,
            self._year
        )

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, val: int):
        self._day = val

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, val: int):
        self._month = val

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, val: int):
        self._year = val

    @classmethod
    def from_string(cls, date: str) -> 'Date':
        if cls.is_date_valid(date):
            day, month, year = date.split('-')
            return Date(day, month, year)
        else:
            raise DateException

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = date.split('-')
        day, month, year = int(day), int(month), int(year)
        if month not in range(1, 13):
            return False
        elif day < 1:
            return False
        elif month in cls.__large_months and day > 31:
            return False
        elif month in cls.__small_months and day > 30:
            return False
        elif month == cls.__feb and day > 28:
            return False
        return True


my_date = Date.from_string('10-12-2077')
print(my_date)
print(Date.is_date_valid('10-13-2077'))
print(Date.is_date_valid('40-12-2077'))
