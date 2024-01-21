def read_chat():
    try:
        with open('chat.txt', 'r', encoding='utf-8') as chat:
            result = chat.read()
            print(result)
    except FileNotFoundError:
        print('Тут пока пусто, введите сообщение!')


def send_message(name, text):
    with open('chat.txt', 'a', encoding='utf-8') as chat:
        chat.write('{:^10}\n\t\t\t>>>{:<40}\n'.format(name, text))


user_name = input('Введите имя пользователя:')
while True:
    print('Выбор действия:\n\t1.Посмотреть текущий текст чата \n\t2.Отправить сообщение')
    try:
        answer = int(input())
        if answer == 1:
            read_chat()
        if answer == 2:
            user_input = input('Введите сообщение: ')
            send_message(user_name, user_input)
        if answer < 1 or answer > 2:
            raise ValueError
    except ValueError:
        print('Ошибка: Введите 1 или 2')
