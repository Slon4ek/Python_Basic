def sum_num(num):
    sum_number = 0
    while num != 0:
        sum_number += num % 10
        num //= 10
    return sum_number


def quantity_num(num):
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count


user_num = int(input('Введите целое, положительное число: '))
print(f'Сумма цифр введенного числа: {sum_num(user_num)}')
print(f'Количество цифр в числе: {quantity_num(user_num)}')
print(f'Разность суммы и количества цифр: {sum_num(user_num) - quantity_num(user_num)}')
