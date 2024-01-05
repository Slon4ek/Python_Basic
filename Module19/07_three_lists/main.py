def no_set(a, b, c, task_num):
    if task_num == 1:
        print('Задача 1: ')
        max_array = max(a, b, c)
        print('Решение без множеств: ', end='')
        for elem in max_array:
            if elem in a and elem in b and elem in c:
                print(elem, end=' ')
    elif task_num == 2:
        print('Задача 2: ')
        print('Решение без множеств: ', end='')
        for elem in a:
            if elem not in b and elem not in c:
                print(elem, end=' ')


def with_set(a, b, c, task_num):
    if task_num == 1:
        sim_nums = set(a) & set(b) & set(c)
        print(f'\nРешение с множествами: {sim_nums}')
    elif task_num == 2:
        diff_nums = set(a) - (set(b) | set(c))
        print(f'\nРешение с множествами: {diff_nums}')


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

no_set(array_1, array_2, array_3, 1)
with_set(array_1, array_2, array_3, 1)
no_set(array_1, array_2, array_3, 2)
with_set(array_1, array_2, array_3, 2)
