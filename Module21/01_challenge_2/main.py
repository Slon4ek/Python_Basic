def all_num(num):
    if num == 1:
        print(num)
    else:
        all_num(num - 1)
        print(num)


user_num = int(input('Введите число: '))
all_num(user_num)
