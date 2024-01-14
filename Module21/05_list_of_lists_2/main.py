nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def unfold_lists(lst):
    new_list = []
    if isinstance(lst, (int, float, str)):
        new_list.append(lst)
    else:
        for elem in lst:
            new_list.extend(unfold_lists(elem))
    return new_list


print(unfold_lists(nice_list))
