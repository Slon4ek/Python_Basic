import time
import functools
from datetime import datetime
from typing import Callable


def logging(_func: Callable = None, *, date_format: str, name_prefix: str = '') -> Callable:
    def logger(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            date_str = date_format
            for sym in date_str:
                if sym.isalpha():
                    date_str = date_str.replace(sym, '%' + sym)

            print(f"Запускается '{name_prefix}.{func.__name__}'. "
                  f"Дата и время запуска: {datetime.now().strftime(date_str)}")
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Завершение '{name_prefix}.{func.__name__}', "
                  f"время работы = {round(end - start, 3)} сек.")
            return result

        return wrapper

    if _func is None:
        return logger
    else:
        return logger(_func)


def log_methods(date_format: str) -> Callable:
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                curr_method = getattr(cls, method)
                if hasattr(curr_method, '__call__'):
                    decorated_method = logging(curr_method,
                                               date_format=date_format,
                                               name_prefix=cls.__name__)
                    setattr(cls, method, decorated_method)
        return cls

    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

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
