def count_sym(txt):
    txt_dict = {
        sym: txt.count(sym)
        for sym in txt
    }
    return txt_dict


def invert(dictionary):
    invert_dict = {
        d_key: [sym for sym in dictionary.keys() if dictionary[sym] == d_key]
        for d_key in dictionary.values()
    }
    return invert_dict


user_input = input('Введите текст: ')
user_input_dict = count_sym(user_input)
user_invert_dict = invert(user_input_dict)

print('Оригинальный словарь частот:')

for key, val in user_input_dict.items():
    print(f'{key}: {val}')

print('Инвертированный словарь частот:')

for key, val in user_invert_dict.items():
    print(f'{key}: {val}')
