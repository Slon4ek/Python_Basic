def min_divider(num):
    for i in range(2, num + 1):
        if num % i == 0:
            return i


user_num = int(input('Введите число: '))
print(f'Наименьший делитель, отличный от единицы: {min_divider(user_num)}')
