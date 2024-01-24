import random


class Human:
    def __init__(self, name, house):
        self.name = name
        self.degree_of_satiety = 50
        self.house = house

    def is_alive(self):
        if self.degree_of_satiety > 0:
            return True
        else:
            return False

    def eat(self):
        if self.house.food > 10:
            self.degree_of_satiety += 10
            self.house.change_food(-10)
            print('{} пошел есть'.format(self.name))
        else:
            self.go_store()

    def working(self):
        self.degree_of_satiety -= 10
        self.house.change_money(10)
        print('{} пошел работать'.format(self.name))

    def gaming(self):
        self.degree_of_satiety -= 10
        print('{} пошел играть'.format(self.name))

    def go_store(self):
        self.house.change_money(-10)
        self.house.change_food(10)
        print('{} пошел в магазин'.format(self.name))

    def live_day(self):
        num = random.randint(1, 7)
        if self.degree_of_satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_store()
        elif self.house.money < 50:
            self.working()
        elif num == 1:
            self.working()
        elif num == 2:
            self.eat()
        else:
            self.gaming()


class House:
    def __init__(self):
        self.food = 50
        self.money = 0

    def change_food(self, amount):
        self.food += amount

    def change_money(self, amount):
        self.money += amount
