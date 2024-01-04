violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
num_dict = {
    1: 'первой',
    2: 'второй',
    3: 'третьей',
    4: 'четвертой',
    5: 'пятой',
    6: 'шестой',
    7: 'седьмой',
    8: 'восьмой',
    9: 'девятой'
}
playing_time = 0
num_songs = int(input('Введите количество песен: '))

for num in range(1, num_songs + 1):
    user_song = input(f'Введите название {num_dict[num]} песни: ')
    while user_song not in violator_songs:
        print('Такой песни нет :(')
        user_song = input(f'Введите название {num_dict[num]} песни: ')
    playing_time += violator_songs.get(user_song)

print(f'Общее время звучания песен: {round(playing_time, 2)}мин')
