input_str_1 = 'abcde'
input_str_2 = 'cedab'
shift = 0

for i_1, sym_1 in enumerate(input_str_1):
    for i_2, sym_2 in enumerate(input_str_2):
        if sym_1 == sym_2:
            shift = i_2 + 1
            if input_str_1.startswith(''.join(input_str_2[i_2:])) and input_str_1.endswith(
                    ''.join(input_str_2[:i_2])):
                print(f'Первая строка получается из второй со сдвигом {shift}')
                break
            else:
                print('Первую строку нельзя получить из второй с помощью циклического сдвига')
                break
    break

