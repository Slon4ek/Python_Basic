from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """Декоратор do_twice, который дважды вызывает декорируемую функцию"""

    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapped_func


