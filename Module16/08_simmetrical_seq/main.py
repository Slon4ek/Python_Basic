def is_palindrome(nums_list):
    temp_list = []
    for i_num in range(len(nums_list) - 1, -1, -1):
        temp_list.append(nums_list[i_num])
    if nums_list == temp_list:
        return True
    else:
        return False


num_quantity = int(input('Введите количество чисел: '))
numbers = []
for i in range(num_quantity):
    print(f'Число {i + 1}: ', end='')
    user_num = int(input())
    numbers.append(user_num)

if is_palindrome(numbers):
    print(f'Последовательность чисел {numbers} является сммтричной, ничего добавлять не нужно.')
else:
    tmp_num_list = []
    add_nums = []
    for i_num in range(0, len(numbers)):
        for j_num in range(i_num, len(numbers)):
            tmp_num_list.append(numbers[j_num])
        if is_palindrome(tmp_num_list):
            for add_num in range(0, i_num):
                add_nums.append(numbers[add_num])
            add_nums.reverse()
            break
        tmp_num_list = []
    print(f'Последовательность чисел: {numbers}\n'
          f'Нужно приписать чисел: {len(add_nums)}\n'
          f'Сами числа: {add_nums}')
