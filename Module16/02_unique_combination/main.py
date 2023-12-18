def merge_sorted_lists(first_list, second_list):
    first_list.extend(second_list)
    for i_fl in first_list:
        if first_list.count(i_fl) > 1:
            first_list.remove(i_fl)
    return sorted(first_list)


# Пример использования:
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
