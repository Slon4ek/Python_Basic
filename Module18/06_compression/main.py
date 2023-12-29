user_input = input('Введите строку: ')
count = 1
output_str = []
for i in range(len(user_input)):
    if user_input[i] == user_input[i + 1: i + 2]:
        count += 1
        continue
    output_str.append(user_input[i] + str(count))
    count = 1

print(''.join(output_str))
