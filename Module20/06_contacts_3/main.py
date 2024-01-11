def add_contact(dictionary):
    name, surname = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
    if (name, surname) in dictionary.keys():
        print(f'Такой человек уже есть в контактах.\n'
              f'Текущий словарь контактов: {dictionary}')
    else:
        phone_num = input('Введите номер телефона: ')
        dictionary[(name, surname)] = phone_num
        print(f'Текущий словарь контактов: {dictionary}')


def search_contact(dictionary):
    surname = input('Введите фамилию для поиска: ').title()
    for person in dictionary:
        if surname in person:
            print(f'{person[0]} {person[1]}: {dictionary[person]}')
        else:
            print(f'Человека с фамилией {surname} нет в списке контактов.')


phone_dict = {}
while True:
    print('Введите номер действия\n'
          '\t1. Добавить контакт\n'
          '\t2. Найти человека')
    answer = input()
    if answer == '1':
        add_contact(phone_dict)
    elif answer == '2':
        search_contact(phone_dict)
    else:
        break
