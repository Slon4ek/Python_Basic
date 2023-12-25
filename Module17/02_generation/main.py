user_num = int(input('Введите длину списка: '))
sequence = [1 if num % 2 == 0 else num % 5 for num in range(user_num)]

print(sequence)
