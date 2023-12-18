a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
t = a.count(5)
print(f'Количество цифр 5 при первом объединении: {t}')

for _ in range(t):
    a.remove(5)

a.extend(c)
t = a.count(3)
print(f'Количество цифр 3 при втором объединении: {t}')
print(f'Итоговый список: {a}')
