sym_sum = 0
line_count = 0

try:
    with open('people.txt', 'r', encoding='utf-8') as user_names, open('errors.log', 'a', encoding='utf-8') as errors:
        for i_line in user_names:
            try:
                line = i_line.rstrip()
                line_count += 1
                if len(line) < 3:
                    raise ValueError
                sym_sum += len(line)
            except ValueError:
                errors.write('Ошибка: менее трёх символов в строке {}\n'.format(line_count))
                print('Ошибка: менее трёх символов в строке {}'.format(line_count))
        print('Общее количество символов: {}'.format(sym_sum))
except FileNotFoundError as exc:
    print(exc, 'Файл не найден!')
