import os
from contextlib import contextmanager
from collections.abc import Iterator
import time


@contextmanager
def in_dir(path: str) -> Iterator:
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        os.chdir(cur_path)


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except FileNotFoundError as exc:
        print('{} --> {}'.format(type(exc), exc))
    finally:
        print('Код выполнился за {} сек.'.format(round((time.time() - start), 4)))


with timer() as t1:
    print('Первый код')
    val_1 = 100 * 100 ** 1000000

with timer() as t2:
    print('Второй код')
    val_2 = 100 * 100 ** 1000000

with timer() as t3:
    print('Третий код')
    val_3 = 100 * 100 ** 1000000

    with in_dir('E:\\'):
        for directory in os.listdir():
            print(directory)
