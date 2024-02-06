import time
from typing import Callable
import functools


def slowdown(func: Callable) -> Callable:
    """
    Декоратор запускает функцию не сразу, а подождав 5 секунд
    :param func: Any
    :return: wrapped function
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Функция запустится через 5 сек')
        for i in range(4, 0, -1):
            time.sleep(1)
            print('Функция запустится через {} сек'.format(i))
        else:
            time.sleep(1)
        result = func(*args, **kwargs)
        return result

    return wrapper


@slowdown
def sum_squares(n: int) -> int:
    """
    Функция возвращает сумму квадратов чисел от 0 до n
    """
    return sum(i ** 2 for i in range(n))


print('Результат работы функции:', sum_squares(100))
