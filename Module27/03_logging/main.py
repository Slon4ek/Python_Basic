import functools
import os
from typing import Callable


def logging(foo: Callable) -> Callable:
    """
    Декоратор логирования работы функций
    :param foo:
    :return:
    """

    @functools.wraps(foo)
    def wrapper(*args, **kwargs):
        import datetime
        now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print('Выполняется функция:\n\t{func_name}\nДокументация:\n\t{docstring}'.format(
            func_name=foo.__name__,
            docstring=foo.__doc__
        ))
        try:
            result = foo(*args, **kwargs)
            print('Функция отработала успешно!\n')
            if not result:
                return foo
            else:
                return result
        except Exception as exc:
            with open('errors.log', 'a', encoding='utf-8') as log_file:
                print('Ошибка выполнения функции! Описание ошибки записано в файл errors.log')
                log_file.write(f'{now}: Ошибка при выполнении функции '
                               f'{foo.__name__}.\n\tОписание ошибки: {str(type(exc))}\n')

    return wrapper


@logging
def square(n) -> int:
    """
    Функция генератор квадратов чисел от 1 до n
    """
    start_num = 1
    for num in range(n):
        yield start_num ** 2
        start_num += 1


@logging
def gen_files_path(directory: str, path: str = os.path.abspath(os.sep)) -> str:
    """
    Функция генерирует абсолютные пути до всех файлов находящихся в указанной директории.
    :param directory: целевая директория поиска.
    :param path: путь до начальной директории поиска(по умолчанию корень диска).
    :return: сгенерированные абсолютные пути до всех файлов в целевой директории
    """
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            if dir_name == directory:
                for file in files:
                    path_to_file = os.path.join('{}\\{}\\{}'.format(root, dir_name, file))
                    yield path_to_file


@logging
def error_def():
    x = 1 / 0
    return x


gen_files_path('Python_Basi')
square(10)
error_def()
