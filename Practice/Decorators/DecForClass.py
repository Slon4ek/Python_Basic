from typing import Callable
import functools
from datetime import datetime


def logged(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        print("Запуск функции произошёл в:", datetime.now())
        print('Название функции: ', func.__name__)
        return func(*args, **kwargs)

    return wrapped


def decorator(cls):
    for i_method in dir(cls):
        if i_method.startswith('__'):
            continue
        curr_method = getattr(cls, i_method)
        if hasattr(curr_method, '__call__'):
            decorated_method = logged(curr_method)
            setattr(cls, i_method, decorated_method)
    return cls


@decorator
class A:

    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

    def test_sum_2(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


A().test_sum_1()
A().test_sum_2()
