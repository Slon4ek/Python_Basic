films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []
films_count = int(input('Сколько фильмов хотите добавить? '))

for _ in range(films_count):
    print('Введите название фильма:', end=' ')
    film = input()
    while film not in films:
        print(f'Ошибка: фильма {film} у нас нет :(')
        film = input('Введите название фильма: ')
    favorite_films.append(film)

print(f'Ваш список любимых фильмов:', end=' ')
for i in favorite_films:
    print(f'{i},', end=' ')
