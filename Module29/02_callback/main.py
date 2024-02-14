from typing import Callable
import functools


def callback(_func: Callable = None, *, answer: str = None) -> Callable:
    def function(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if answer:
                return func(*args, **kwargs)
            else:
                return None

        return wrapped

    if _func is None:
        return function
    else:
        return function(_func)


@callback(answer='//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


app = {'//': example}
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

