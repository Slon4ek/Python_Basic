num_count = int(input('Кол-во чисел в списке: '))
numbers_list = []
new_numbers_list = []

for _ in range(num_count):
    print('Введите число:', end=' ')
    numbers_list.append(int(input()))

shift = int(input('Сдвиг: '))
index = - shift

for _ in range(num_count):
    new_numbers_list.append(numbers_list[index])
    index += 1

print(new_numbers_list)
