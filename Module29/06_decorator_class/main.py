from typing import Callable
import time


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        func_result = self.func(*args, **kwargs)
        end = time.time()
        print('Вызов функции {name}\n'
              'Аргументы: {args}, {kwargs}\n'
              'Результат: {res}\n'
              'Время выполнения: {time} секунд'.format(
                name=self.func.__name__,
                args=args,
                kwargs=kwargs,
                res=func_result,
                time=end - start
                ))
        return func_result


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
