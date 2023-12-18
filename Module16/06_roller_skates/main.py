rolls_list = []
humans_list = []
roll_count = int(input('Количество роликов: '))

for i in range(1, roll_count + 1):
    print(f'Размер пары {i}: ', end='')
    size = int(input())
    rolls_list.append(size)

humans_count = int(input('Количество людей: '))
hum_in_rolls = 0

for i in range(1, humans_count + 1):
    print(f'Размер ноги человека {i}: ', end='')
    size = int(input())
    humans_list.append(size)
    if size in rolls_list:
        hum_in_rolls += 1
        rolls_list.remove(size)

print(f'Наибольшее количество людей, которые могут взять ролики: {hum_in_rolls}')
