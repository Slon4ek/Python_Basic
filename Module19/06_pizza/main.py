def processing_orders(num):
    num_word = {
        1: 'Первый',
        2: 'Второй',
        3: 'Третий',
        4: 'Четвертый',
        5: 'Пятый',
        6: 'Шестой',
        7: 'Седьмой',
        8: 'Восьмой',
        9: 'Девятый'
    }
    orders = dict()
    for order in range(1, num + 1):
        customer, pizza, quantity = input(f'{num_word[order]} заказ: ').split()
        quantity = int(quantity)
        if customer in orders:
            if pizza in orders[customer]:
                orders[customer][pizza] += quantity
            else:
                orders[customer][pizza] = quantity
        else:
            orders[customer] = {pizza: quantity}
    return orders


def print_orders(order):
    for customer in sorted(order):
        print(f'{customer}: ')
        for pizza in order[customer]:
            print(f'     {pizza}: {order[customer][pizza]}')


order_count = int(input('Введите количество заказов: '))
current_orders = processing_orders(order_count)
print_orders(current_orders)
