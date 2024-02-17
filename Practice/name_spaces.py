global_count = {}
count = 0


def decorator_counter(func):
    local_count = {}

    def wrapped_func(*args, **kwargs):
        global global_count
        nonlocal local_count
        global count
        global_count[func.__name__] = global_count.get(func.__name__, 0) + 1
        local_count[func.__name__] = local_count.get(func.__name__, 0) + 1
        print(global_count, local_count)
        count += 1
        return func(*args, **kwargs)

    wrapped_func.check_count = local_count  # добавим на всякий случай ссылку на этот локальный словарь
    return wrapped_func


@decorator_counter
def hello():
    print('hello')


@decorator_counter
def hello_2():
    print('hello')


hello()
hello()
hello_2()
hello_2()
print(hello_2.check_count)

print('*' * 100)
print(dir(__builtins__))
print(count)
