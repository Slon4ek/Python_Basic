input_str_1 = 'abcde'
input_str_2 = 'cdeab'
start_sym = input_str_1.find(input_str_2[0])

if input_str_2.startswith(''.join(input_str_1[start_sym:])) and input_str_2.endswith(''.join(input_str_1[:start_sym])):
    print(f'Первая строка получается из второй со сдвигом {start_sym}')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')
