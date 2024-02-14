from typing import Callable
import functools
from datetime import datetime
import time


def log_methods(date: str) -> Callable:
    def logger(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            date_str = ''
            for sym in date:
                if sym.isalpha():
                    date_str += f'%{sym}'
                    continue
                if len(sym) > 1:
                    for i in sym:
                        if i.isalpha():
                            date_str += f'%{i}'
                        else:
                            date_str += i
                else:
                    date_str += f'{sym}'
            today = datetime.now().strftime(date_str)
            print(f'Запускается {func.__name__}. '
                  f'Дата и время запуска: {today}.')
            start = time.time()
            result = func(*args, **kwargs)
            print(f'Время работы функции: {time.time() - start}')
            return result

        return wrapper

    return logger


#@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


#@log_methods("b d Y - H:M:S")
class B(A):
    @log_methods("b d Y - H:M:S")
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    @log_methods("b d Y - H:M:S")
    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
