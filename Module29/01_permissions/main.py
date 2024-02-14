from typing import Callable
import functools


def check_permission(user: str) -> Callable:
    def use_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if user.title() in user_permission:
                print(f'Access granted: coll function {func.__name__}')
                return func()
            else:
                print(f'PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')

        return wrapper

    return use_func


user_permission = ['Admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
