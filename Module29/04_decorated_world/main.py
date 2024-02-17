import functools
from typing import Callable


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    def decorator(*args, **kwargs):
        @functools.wraps(func)
        def wrapper(func: Callable) -> Callable:
            print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
            return func

        return wrapper

    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable):
    @functools.wraps(func)
    def wrapper(func: Callable) -> Callable:
        return func()

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
