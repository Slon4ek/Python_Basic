from typing import Callable, Dict, Any


class Caching:
    """
    Класс-декоратор для кеширования результатов выполнения функции.
    При первом запуске функции добавляет результат ее работы в словарь
    где ключем является аргумент функции, а значение - результат выполнения.
    При повторном вызове функции проверяется словарь и если аргумент уже присутствует
    в словаре - берет его значение.
    """

    def __init__(self, func: Callable) -> None:
        self.cache_dict: Dict = dict()
        self.func = func

    def __call__(self, *args) -> Any:
        for i in args:
            if i in self.cache_dict.keys():
                return self.cache_dict[i]
            else:
                self.cache_dict[i] = self.func(i)
                return self.cache_dict[i]


@Caching
def fibonacci(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
