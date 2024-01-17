import zipfile


def write_analyze_in_file(a_list):
    file_for_write = open('text_analyze.txt', 'w', encoding='utf-8')
    file_for_write.write('+{:-^19}+\n'.format('+'))
    file_for_write.write('|{: ^9}|{: ^9}|\n'.format('Буква', 'Частота'))
    file_for_write.write('+{:-^19}+\n'.format('+'))
    for line in a_list:
        char, abbrev = line[0]
        file_for_write.write('|{: ^9}|{: ^9}|\n'.format(f'{char} [{abbrev}]', line[1]))
    file_for_write.write('+{:-^19}+'.format('+'))


def unzip(file_name):
    zip_file = zipfile.ZipFile(file_name, 'r')
    for i_file_name in zip_file.namelist():
        zip_file.extract(i_file_name)
    zip_file.close()


def alphabet_generator(start_sym, a_sym_quantity):
    # Функция генерирует строку с алфавитом
    alpha_str = ''.join(chr(i) + chr(i).upper()
                        for i in range(start_sym, start_sym + a_sym_quantity))
    return alpha_str


def text_analyzer(file_name):
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
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


analyze = text_analyzer('voyna-i-mir.zip')
write_analyze_in_file(analyze)
