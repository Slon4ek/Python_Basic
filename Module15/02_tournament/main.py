name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day_list = []

for i, name in enumerate(name_list):
    if i % 2 == 0:
        first_day_list.append(name_list[i])

print(first_day_list)
