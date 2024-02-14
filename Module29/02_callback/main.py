from typing import Callable
import functools

app = {}


def callback(answer: str) -> Callable:
    def function(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            app[answer] = func

        return wrapped

    return function


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


example()
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
