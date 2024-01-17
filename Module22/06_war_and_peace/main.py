import zipfile


def alphabet_generator(start_sym, a_sym_quantity):
    # Функция генерирует строку с алфавитом
    alpha_str = ''.join(chr(i) + chr(i).upper()
                        for i in range(start_sym, start_sym + a_sym_quantity))
    return alpha_str


def text_analyzer(file_name):
    # Функция анализирует текст из файла и возвращает список букв и сколько раз они встречаются в тексте
    file = open(file_name, 'r', encoding='utf-8')
    text = file.read()
    ru_alphabet = alphabet_generator(1072, 32) + 'ёЁ'
    en_alphabet = alphabet_generator(97, 26)
    ru_sym_dict = {(sym, 'ru'): text.count(sym) for sym in ru_alphabet if sym in text}
    en_sym_dict = {(sym, 'en'): text.count(sym) for sym in en_alphabet if sym in text}
    all_sym_dict = {**ru_sym_dict, **en_sym_dict}
    sort_sym = sorted(all_sym_dict.items(), key=lambda x: x[1], reverse=True)
    file.close()
    return sort_sym


my_zip = zipfile.ZipFile('voyna-i-mir.zip', 'r')
my_zip.extract('voyna-i-mir.txt')
my_zip.close()

analyze = text_analyzer('voyna-i-mir.txt')
file_for_write = open('text_analyze.txt', 'w', encoding='utf-8')

for elem in analyze:
    string = ''.join('{} : {}'.format(elem[0], elem[1]))
    file_for_write.write(string + '\n')

file_for_write.close()
