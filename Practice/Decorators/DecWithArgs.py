import time
from typing import Callable, Any
from time import sleep


def repeat(_func: Callable = None, *, n: int = 2) -> Callable:
    """
    Функция декоратор с аргументом n
    :param _func: декорируемая функция
    :param n: количество повторений запуска декорируемой функции
    :return:
    """

    def do_twice(func: Callable) -> Callable:
        """
        Декоратор который 2 раза вызывает декорируемую функцию
        :param func:
        :return:
        """

        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return

        return wrapper

    if _func is None:
        return do_twice
    else:
        return do_twice(_func)


# Задача 2. Замедление кода 2.
#
# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор,
# который перед выполнением декорируемой функции ждёт несколько секунд.
#
# Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента.
# По умолчанию декоратор ждёт одну секунду. Помимо этого сделайте так, чтобы декоратор можно было использовать
# как с аргументами, так и без них.

def slow_it_now(_func=None, *, n=1):
    def slowdown_ns(func):
        def wrapper(*args, **kwargs):
            for i in range(n, 0, -1):
                print(f'Код запустится через {i} сек')
                sleep(1)
            result = func(*args, **kwargs)
            return result

        return wrapper

    if _func is None:
        return slowdown_ns
    else:
        return slowdown_ns(_func)


@slow_it_now
def test() -> None:
    """
    Проверка декоратора и вывод простого сообщения

    :return:
    """
    print('<Тут что-то происходит...>')


test()
