num_list = [10, 3, -5, 0, 45, 23, 8, 0, 10]


def list_sort(user_list):
    for index_1 in range(len(user_list)):
        for index_2 in range(index_1 + 1, len(user_list)):
            if user_list[index_1] >= user_list[index_2]:
                user_list[index_1], user_list[index_2] = user_list[index_2], user_list[index_1]


list_sort(num_list)

print(num_list)
