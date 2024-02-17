import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapper():
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    cls.instance = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
