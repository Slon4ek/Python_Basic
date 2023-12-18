guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
guests_count = len(guests)
user_input = ''

while user_input != 'пора спать':
    print(f'Сейчас на вечеринке {guests_count} человек: {guests}')
    user_input = input('Гость пришёл или ушёл? ')
    if user_input == 'пришел':
        guest_name = input('Имя гостя: ')
        if guests_count < 6:
            print(f'Привет {guest_name}')
            guests.append(guest_name)
            guests_count = len(guests)
        else:
            print(f'Прости, {guest_name}, но мест нет :(')
    if user_input == 'ушел':
        guest_name = input('Имя гостя: ')
        if guest_name not in guests:
            print(f'На вечеринке нет гостя с именем {guest_name}')
            guest_name = input('Имя гостя: ')
        print(f'Пока, {guest_name}')
        guests.remove(guest_name)
        guests_count = len(guests)

print('Вечеринка закончилась, все легли спать.')