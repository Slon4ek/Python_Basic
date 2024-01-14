def create_total_dict(dictionary, d_key):
    total_quantity = 0
    total_price = 0
    for item in dictionary[d_key]:
        total_quantity += item['quantity']
        total_price += item['quantity'] * item['price']
    return total_quantity, total_price


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key, val in goods.items():
    quantity, price = create_total_dict(store, val)
    print(f'{key} - {quantity} штук, стоимость {price} рублей')


for i_name in goods.keys():
    total_quantity = 0
    total_cost = 0
    for j_good in store[goods[i_name]]:
        total_quantity += j_good['quantity']
        total_cost += j_good['price'] * j_good['quantity']
    print('{} - {} шт, стоимость {} руб'.format(
        i_name, total_quantity, total_cost))
