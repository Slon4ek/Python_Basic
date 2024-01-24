import random


def check_winner(u_1, u_2):
    if u_1.status_alive:
        return u_1.name
    elif u_2.status_alive:
        return u_2.name


class Unit:
    def __init__(self, name='Воин', hp=100):
        self.name = name
        self.hp = hp
        self.status_alive = True

    def taking_dmg(self, dmg=20):
        self.hp -= dmg
        if self.hp <= 0:
            self.status_alive = False


unit_1 = Unit(name='Воин 1')
unit_2 = Unit(name='Воин 2')
while all([unit_1.status_alive, unit_2.status_alive]):
    random_num = random.randint(1, 2)
    if random_num == 1:
        unit_2.taking_dmg()
        print('Бьет - "{}": \n\t>>> У "{}" осталось {} здоровья'.format(
            unit_1.name, unit_2.name, unit_2.hp
        ))
    elif random_num == 2:
        unit_1.taking_dmg()
        print('Бьет - "{}": \n\t>>> У "{}" осталось {} здоровья'.format(
            unit_2.name, unit_1.name, unit_1.hp
        ))

winner = check_winner(unit_1, unit_2)
print('Победителем становится {}'.format(winner))
