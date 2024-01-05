array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1: ')

print('Решение без множеств: ', end='')
for elem in array_3:
    if elem in array_1 and elem in array_2:
        print(elem, end=' ')

print(f'\nРешение с множествами: {set(array_1) & set(array_2) & set(array_3)}')

print('Решение без множеств: ', end='')
for elem in array_1:
    if elem not in array_2 and elem not in array_3:
        print(elem, end=' ')

print(f'\nРешение с множествами: {set(array_1) - (set(array_2) | set(array_3))}')