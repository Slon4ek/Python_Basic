num_quantity = int(input('Введите количество чисел: '))
numbers = [int(input('Введите число: ')) for _ in range(num_quantity)]
add_nums = []

if numbers == numbers[::-1]:
    print(f'Последовательность {numbers} симметрична, ничего добавлять не нужно.')
else:
    for i_num in range(0, len(numbers)):
        if numbers[i_num:] == numbers[:i_num - 1: -1]:
            add_nums = numbers[:i_num]
            add_nums.reverse()
            break

    print(f'Последовательность чисел: {numbers}\n'
          f'Нужно приписать чисел: {len(add_nums)}\n'
          f'Сами числа: {add_nums}')
