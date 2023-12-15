num_count = int(input('Кол-во чисел в списке: '))
numbers_list = []
new_numbers_list = []
start_new_list = []
end_new_list = []

for _ in range(num_count):
    print('Введите число:', end=' ')
    numbers_list.append(int(input()))

shift = int(input('Сдвиг: '))

for index, num in enumerate(numbers_list):
    if index >= shift - 1:
        start_new_list.append(num)
    else:
        end_new_list.append(num)

new_numbers_list = start_new_list + end_new_list

print(f'Изначальный список: {numbers_list}\n'
      f'Сдвинутый список: {new_numbers_list}')
