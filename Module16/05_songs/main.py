violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_count = int(input('Сколько песен выбрать? '))
total_time = 0

for i in range(1, songs_count + 1):
    print(f'Название {i}-й песни:', end=' ')
    user_input = input()
    for songs in violator_songs:
        if songs[0] == user_input:
            total_time += songs[1]

print(f'Общее время звучания песен — {round(total_time, 2)} минуты')
