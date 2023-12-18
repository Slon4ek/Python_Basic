num_of_per = int(input('Кол-во человек: '))
persons_list = list(range(1, num_of_per + 1))
out_per_num = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {out_per_num}-й человек')
i_per = 0
out_per = 0

while len(persons_list) > 1:
    print(f'Текущий круг людей: {persons_list}')
    start_num = i_per % len(persons_list)
    print(f'Начало счёта с номера {persons_list[start_num]}')
    i_per = (i_per + out_per_num - 1) % len(persons_list)
    out_per = persons_list.pop(i_per)
    print(f'Выбывает человек под номером {out_per}')

print(f'\nОстался человек под номером: {persons_list[0]}')
