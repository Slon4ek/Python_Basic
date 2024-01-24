from Classes import House
from Classes import Human
house = House()
hum_1 = Human('Bob', house)
hum_2 = Human('John', house)
dey_count = 0

for i in range(365):
    if not hum_1.is_alive():
        print(hum_1.name, 'умер :(')
        print(f'Прошло {dey_count} дней')
        break
    elif not hum_2.is_alive():
        print(hum_2.name, 'умер :(')
        print(f'Прошло {dey_count} дней')
        break
    else:
        print('Имя: {}, сытость: {}'.format(hum_1.name, hum_1.degree_of_satiety))
        print('Имя: {}, сытость: {}'.format(hum_2.name, hum_2.degree_of_satiety))
        print('Еды в доме: {}, денег в сейфе: {}'.format(house.food, house.money))
        hum_1.live_day()
        hum_2.live_day()
        dey_count += 1
else:
    print(f'Прошло {dey_count} дней')
