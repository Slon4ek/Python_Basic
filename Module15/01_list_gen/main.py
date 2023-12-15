user_num = int(input('Введите число: '))
num_list = []

for i in range(1, user_num + 1, 2):
    num_list.append(i)

print(f'Список из нечётных чисел от одного до {user_num}: {num_list}')
