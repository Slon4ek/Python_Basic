vcard_list = [3070, 2060, 3090, 3070, 3090]
new_vcard_list = []
max_ID = max(vcard_list)

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
