def list_sort(user_list):
    for index_1 in range(len(user_list)):
        for index_2 in range(index_1 + 1, len(user_list)):
            if user_list[index_1] <= user_list[index_2]:
                user_list[index_1], user_list[index_2] = user_list[index_2], user_list[index_1]


numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
list_sort(numbers_list)

for i in range(len(numbers_list) - 1, -1, -1):
    num = numbers_list[i]
    if num % 2 != 0:
        numbers_list.remove(num)

print(numbers_list)
