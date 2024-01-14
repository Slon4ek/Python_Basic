def quick_sort(lst):
    if not lst:
        return []
    support_num = lst[-1]
    start_list = [num for num in lst if num < support_num]
    mid_list = [num for num in lst if num == support_num]
    end_list = [num for num in lst if num > support_num]
    result = quick_sort(start_list) + mid_list + quick_sort(end_list)
    return result


user_list = [5, 8, 9, 4, 2, 9, 1, 8]
print(quick_sort(user_list))
