container_count = int(input('Введите количество контейнеров: '))
container_list = []

for i in range(container_count):
    print('Введите вес контейнера:', end=' ')
    container = int(input())
    while container > 200:
        print('Вес контейнера не должен превышать 200кг')
        container = int(input('Введите вес контейнера: '))
    container_list.append(container)
else:
    list.sort(container_list, reverse=True)

print(container_list)
new_container = int(input('Введите вес нового контейнера: '))
new_container_point = 1

for i in range(len(container_list)):
    if new_container <= container_list[i]:
        new_container_point += 1

print(f'Номер, который получит новый контейнер: {new_container_point}')