def a_movie(movie, films_list):
    if movie not in films_list:
        return False
    return True


def add_movie(film, movies):
    if film not in movies:
        print('\nФильм успешно добавлен в вашу коллекцию!\n')
        movies.append(film)
    else:
        print('\nФильм уже находится у вас в коллекции!\n')


def del_movie(film, movies):
    if a_movie(film, movies):
        print('\nФильм успешно удален из вашей коллекции!\n')
        movies.remove(film)
    else:
        print('\nТакого фильма нет в вашей коллекции!\n')


films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

my_films_list = []

while True:
    print(f'Ваш список фильмов - {my_films_list}')
    new_movie = input('Название фильма: ')
    if a_movie(new_movie, films):
        print('Команды: добавить, удалить, вставить')
        command = input('Введите команду: ')
        if command == 'добавить':
            add_movie(new_movie, my_films_list)
        if command == 'удалить':
            del_movie(new_movie, my_films_list)
        if command == 'вставить':
            continue
    else:
        print('Такого фильма нет на сайте :(\n')
