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
            break
        if word == val:
            print(f'Синоним: {key.title()}')
            break


def create_synonym_dict(count):
    dictionary = dict()
    for num in range(1, count + 1):
        key, val = input(f'{num} пара слов: ').lower().split(' - ')
        dictionary[key] = val
    return dictionary


word_count = int(input('Введите количество пар слов: '))
synonym_dict = create_synonym_dict(word_count)

while True:
    user_input = input('Введите слово: ')
    if check_word(user_input, synonym_dict):
        break
    else:
        print('Такого слова в словаре нет.')

synonym(user_input, synonym_dict)
