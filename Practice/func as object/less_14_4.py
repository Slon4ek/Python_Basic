import functools
from typing import Callable, Dict


def get_some_salad(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrap_that_salad(*args, **kwargs):
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")

    return wrap_that_salad


def get_some_buns(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrap_that_buns(*args, **kwargs):
        print("</----------\\>")
        func(*args, **kwargs)
        print("<\\______/>")

    return wrap_that_buns


@get_some_buns
@get_some_salad
def filling_burger(filler):
    print(filler)


plugins: Dict[str, Callable] = {}


def go_to_plugins(func: Callable) -> Callable:
    plugins[func.__name__] = func
    return func


@go_to_plugins
def hello(name: str):
    print('Hello {name}!'.format(name=name))


print(plugins)
