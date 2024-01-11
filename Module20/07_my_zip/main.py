def my_zip(l1, l2):
    if isinstance(l1, dict):
        my_gen = (
            (key, l2[i])
            for i in range(min(len(l1.keys()), len(l2)))
            for i_key, key in enumerate(l1.keys())
            if i_key == i
        )
    elif isinstance(l2, dict):
        my_gen = (
            (l1[i], key)
            for i in range(min(len(l1), len(l2.keys())))
            for i_key, key in enumerate(l2.keys())
            if i_key == i
        )
    else:
        my_gen = (
            (l1[i], l2[i])
            for i in range(min(len(l1), len(l2)))
        )
    return my_gen


test_dict = {
    1: 'a',
    2: 'b',
    3: 'c'
}
test_str = 'abcd'
test_list = [20, 30, 40, 50, 20]

print(my_zip(test_dict, test_list))
for elem in my_zip(test_list, test_dict):
    print(elem)
