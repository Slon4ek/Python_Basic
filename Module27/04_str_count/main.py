from typing import Callable


class Counter:
    """
    Класс декоратор подсчитывающий количество вызовов функции
    """
    def __init__(self, func: Callable) -> None:
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs) -> None:
        self.calls += 1
        self.func(*args, **kwargs)


@Counter
def my_func():
    print('Привет')


my_func()
my_func()
my_func()
my_func()

print(f'Функция my_func была вызвана {my_func.calls} раз')
