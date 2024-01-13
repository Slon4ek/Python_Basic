site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def dict_depth(dictionary, depth=0):
    """Функция определяет глубину вложенности словаря"""
    if not isinstance(dictionary, dict) or not dictionary:
        return depth
    return max(dict_depth(val, depth+1) for key, val in dictionary.items())


def search_elem(tag, structure, depth_lvl=None):
    """Функция ищет ключ до глубины depth_lvl, если глубина не указана, то ищет
    по всему словарю"""
    result = None
    depth_lvl = depth_lvl or dict_depth(structure)
    if tag in structure:
        return structure[tag]
    for key, val in structure.items():
        if isinstance(val, dict) and depth_lvl > 1:
            result = search_elem(tag, val, depth_lvl - 1)
            if result:
                return result
    return result


user_input = input('Искомый ключ: ')
answer = input('Хотите ввести максимальную глубину? Y/N: ')
if answer.lower() == 'n':
    res = search_elem(user_input, site)
    print(f'Значение ключа: {res}')
if answer.lower() == 'y':
    udl = int(input('Введите максимальную глубину: '))
    print(search_elem(user_input, site, udl))

