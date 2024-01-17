def count_sym_perc(file_name, alfa):
    # Функция считывает текст из файла, считает долю каждой буквы, встречающейся в тексте
    # и возвращает список в формате (буква : доля)
    file = open(file_name, 'r')
    file_text = ''.join(sym for sym in file.read().lower() if sym in alfa)
    count_sym_list = dict()
    for sym in alfa:
        sym_perc = round(file_text.count(sym) / len(file_text), 3)
        count_sym_list[sym] = sym_perc
    file.close()
    sort_sym_list = sorted(count_sym_list.items(), key=lambda x: x[1], reverse=True)
    return sort_sym_list


english_alphabet = ''.join(chr(i) for i in range(97, 123))
syms_count = count_sym_perc('zen.txt', english_alphabet)
write_file = open('analysis.txt', 'w')

for elem in syms_count:
    string = ''.join('{} : {}'.format(elem[0], elem[1]))
    write_file.write(string + '\n')

write_file.close()
