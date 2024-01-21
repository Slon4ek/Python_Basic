import math


def get_sage_sqrt(num):
    try:
        return math.sqrt(num)
    except ValueError as exc:
        return f'{exc}: число не может быть отрицательным!'
    except TypeError as exc:
        return f'{exc}: должно быть число, не строка!'


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
