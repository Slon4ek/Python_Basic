num_quantity = int(input('Введите количество чисел: '))
numbers = []

for i in range(num_quantity):
    print(f'Число {i + 1}: ', end='')
    user_num = int(input())
    numbers.append(user_num)

add_nums = []
for i_num in range(0, len(numbers)):
    if numbers[i_num:] == numbers[:i_num - 1: -1]:
        add_nums = numbers[:i_num]
        add_nums.reverse()
        break
    tmp_num_list = []
print(f'Последовательность чисел: {numbers}\n'
      f'Нужно приписать чисел: {len(add_nums)}\n'
      f'Сами числа: {add_nums}')
