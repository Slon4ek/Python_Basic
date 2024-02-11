import datetime
import functools
import random
import time
from typing import Callable


def timer(foo: Callable) -> Callable:
    """
    Декоратор, замеряющий время выполнения декорируемой функции
    :param foo: декорируемая функция
    :return: wrapped_foo
    :rtype: Callable
    """

    @functools.wraps(foo)
    def wrapped_foo(*args, **kwargs):
        start_timer = time.time()
        foo(*args, **kwargs)
        end_timer = time.time()
        res = round(end_timer - start_timer, 4)
        return res

    return wrapped_foo


@timer
def text_generator():
    """Функция генерирует N сообщений и записывает их в файл work_logs.txt"""
    N = 1000

    error_names = ['ValueError', 'ArithmeticError', 'AssertionError', 'ImportError', 'NameError', 'OSError']

    with open('work_logs.txt', 'w', encoding='utf8') as file:
        for _ in range(N):
            if random.randint(1, 10) == 5:
                text = 'ERROR: ' + random.choice(error_names) + ' ' + str(datetime.datetime.today())
            else:
                text = 'COMPLETE: Данные успешно переданы.'
            file.write(text + '\n')


result = text_generator()
print('Function name:', text_generator.__name__)
print('Docstring:', text_generator.__doc__)
print('Выполнение функции заняло {} сек'.format(result))
