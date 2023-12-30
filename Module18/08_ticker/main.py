input_str_1 = 'abcde'
input_str_2 = 'cedab'
start_sym = input_str_2.find(input_str_1[0])

if input_str_1.startswith(''.join(input_str_2[start_sym:])) and input_str_1.endswith(''.join(input_str_2[:start_sym])):
    print(f'Первая строка получается из второй со сдвигом {start_sym + 1}')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')
