shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

total_goods = 0
total_cost = 0
user_input = input('Введите название детали: ')

for prod, cost in shop:
    if user_input == prod:
        total_goods += 1
        total_cost += cost

print(f'Кол-во деталей: {total_goods}\n'
      f'Общая стоимость: {total_cost}')
