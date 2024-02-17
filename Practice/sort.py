def bubble_sort(lst):
    """
    Сортировка пузырьком - простой алгоритм сортировки, который проходит по списку несколько раз, сравнивая пары
    соседних элементов и меняя их местами, если они находятся в неправильном порядке. Этот процесс повторяется до тех
    пор, пока весь список не будет отсортирован.
    """
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            # Сравниваем пару соседних элементов
            if lst[j] > lst[j + 1]:
                # Если элементы находятся в неправильном порядке, меняем их местами
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# Пример использования


numbers = [5, 3, 8, 2, 1]

bubble_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]


def insertion_sort(lst):
    """
    Сортировка вставками (insertion sort) — это простой алгоритм сортировки, который постепенно строит
    отсортированную последовательность, один элемент за другим, вставляя каждый новый элемент в правильное место.
    """
    n = len(lst)
    for i in range(1, n):
        key = lst[i]  # Берём текущий элемент, который нужно вставить в отсортированную часть списка
        j = i - 1
        # Перемещаем элементы, которые больше key, на одну позицию вперёд
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
            lst[j + 1] = key  # Вставляем key в правильное место


# Пример использования
numbers = [5, 3, 8, 2, 1]
insertion_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]


def shell_sort(lst):
    """Сортировка Шелла(улучшенная версия сортировки вставками)"""
    n = len(lst)
    gap = n // 2  # Инициализация начального значения интервала
    while gap > 0:
        # Применяем сортировку вставками с заданным интервалом
        for i in range(gap, n):
            temp = lst[i]
            j = i
            # Сдвигаем элементы, чтобы найти правильную позицию для вставки элемента
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2  # Уменьшаем интервал
    return lst


# Пример использования
numbers = [8, 3, 1, 5, 2]
sorted_numbers = shell_sort(numbers)
print(sorted_numbers)  # Вывод: [1, 2, 3, 5, 8]


def selection_sort(lst):
    """
    Сортировка выбором (selection sort) — это простой алгоритм сортировки, который на каждом шаге находит
    минимальный или максимальный элемент из неотсортированной части списка и помещает его в начало или конец
    отсортированной части.
    """
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        # Находим индекс минимального элемента в неотсортированной части списка
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        # Меняем местами минимальный элемент с первым элементом неотсортированной части
        lst[i], lst[min_index] = lst[min_index], lst[i]


# Пример использования
numbers = [5, 3, 8, 2, 1]
selection_sort(numbers)
print(numbers)  # Вывод: [1, 2, 3, 5, 8]


# Сортировка слиянием (merge sort) — это алгоритм сортировки, который использует стратегию «разделяй и властвуй».
# Он разбивает список на две половины, рекурсивно сортирует каждую, а затем объединяет их в отсортированный список.
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    # Разделяем список на две половины
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Объединяем отсортированные половины в один список
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        # Сравниваем элементы из обоих списков и добавляем меньший в объединённый список
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Добавляем оставшиеся элементы из левого списка
    merged.extend(left[left_index:])
    # Добавляем оставшиеся элементы из правого списка
    merged.extend(right[right_index:])
    return merged


# Пример использования
numbers = [8, 3, 1, 5, 2]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)  # Вывод: [1, 2, 3, 5, 8]


# Карманная сортировка (bucket sort) — это алгоритм сортировки, который разбивает список на равные интервалы,
# называемые карманами, а затем сортирует элементы в каждом кармане отдельно. Затем элементы из всех карманов
# объединяются, чтобы получить окончательно отсортированный список.
def bucket_sort(lst):
    # Определяем количество карманов
    num_buckets = len(lst)
    # Создаём пустые карманы
    buckets = [[] for _ in range(num_buckets)]
    # Распределяем элементы по карманам
    for num in lst:
        index = int(num * num_buckets)  # Вычисляем индекс кармана для текущего элемента
        buckets[index].append(num)
    # Сортируем каждый карман отдельно
    for bucket in buckets:
        bucket.sort()
    # Объединяем элементы из всех карманов
    sorted_lst = []
    for bucket in buckets:
        sorted_lst += bucket
    return sorted_lst


# Пример использования
numbers = [0.42, 0.25, 0.75, 0.12, 0.9]
sorted_numbers = bucket_sort(numbers)
print(sorted_numbers)  # Вывод: [0.12, 0.25, 0.42, 0.75, 0.9]
