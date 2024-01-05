def check_word(word, dictionary):
    # Функция проверяет наличие слова в словаре
    if word in dictionary.values() or word in dictionary.keys():
        return True
    else:
        return False


def synonym(word, dictionary):
    # Функция выводит на экран синоним к слову word
    for key, val in dictionary.items():
        if word == key:
            print(f'Синоним: {val.title()}')
        else:
            print(f'Синоним: {key.title()}')


synonym_dict = dict()
word_count = int(input('Введите количество пар слов: '))

for i in range(1, word_count + 1):  # Создаем словарь из пар слов синонимов
    word_list = input(f'{i} пара слов: ').lower().split(' - ')
    synonym_dict[word_list[0]] = word_list[1]

while True:
    user_input = input('Введите слово: ')
    if check_word(user_input, synonym_dict):
        break
    else:
        print('Такого слова в словаре нет.')

synonym(user_input, synonym_dict)
