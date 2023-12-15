vcard_count = int(input('Введите количество видеокарт: '))
vcard_list = []
new_vcard_list = []
max_ID = max(vcard_list)

for _ in range(vcard_count):
    print('Введите модель видеокарты:', end=' ')
    vcard_list.append(int(input()))

print(f'Количество видеокарт: {len(vcard_list)}')

for i, ID in enumerate(vcard_list):
    print(f'Видеокарта {i + 1}: {ID}')

for card in vcard_list:
    if card == max_ID:
        continue
    else:
        new_vcard_list.append(card)

print(f'Старый список видеокарт: {vcard_list}')
print(f'Новый список видеокарт: {new_vcard_list}')
