class Toyota:
    def __init__(self, color, price, max_speed, curr_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.curr_speed = curr_speed

    def car_info(self):
        print(
            'Цвет автомобиля: {}\nСтоимость: {:,}\nМакс. скорость: {}'.format(
                self.color, self.price, self.max_speed
            )
        )

    def change_curr_speed(self, speed):
        self.curr_speed = speed


class Family:
    sur_name = 'Ивановы'
    family_budget = 100000
    have_a_house = False

    def family_info(self):
        print('Фамилия семьи: {}\nБюджет семьи: {}руб.\nНаличие дома: {}'.format(
            self.sur_name, self.family_budget, self.have_a_house
        ))

    def earn_money(self, money):
        self.family_budget += money
        print('Семейный бюджет пополнился, теперь в нем {}руб.'.format(
            self.family_budget
        ))

    def bay_house(self, house_price, discount=0):
        house_price -= house_price * discount // 100
        if self.family_budget >= house_price:
            self.family_budget -= house_price
            self.have_a_house = True
            print('Дом успешно приобретен! Остаток денег: {}руб.'.format(self.family_budget))
        else:
            print('Денег на покупку дома не хватает, надо поработать :)\n'
                  'Стоимость додма со скидкой: {}\n'
                  'Бюджет семьи: {}руб.'.format(house_price, self.family_budget))


car = Toyota('Белый', 10**6, 200)
car.car_info()