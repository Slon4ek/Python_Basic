from typing import Callable, Any
import functools


def how_are_you(foo: Callable) -> Callable:
    """
    Декоратор от скуки :)
    :param foo: Any
    :return: wrapped function
    """

    @functools.wraps(foo)
    def wrapped_func(*args, **kwargs):
        print('Привет! Как дела?')
        input('')
        print('А у меня не очень! Скучно!!! Ладно, продолжаем работу :)')
        result = foo(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def sum_squares(n: int) -> int:
    return sum(i ** 2 for i in range(n))


print(sum_squares(100))
