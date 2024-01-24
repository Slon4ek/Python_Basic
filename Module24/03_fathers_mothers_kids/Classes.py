class Kid:
    calm_states = {0: 'Спокойствие', 1: 'Беспокойство'}
    hunger_states = {0: 'Сытость', 1: 'Голод'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm_state = 1
        self.hunger_state = 1

    def __str__(self):
        return '{} - {} лет'.format(self.name, self.age)

    def __repr__(self):
        return '{} : {}'.format(self.name, self.age)

    def eat(self):
        if not self.is_full():
            self.hunger_state -= 1
        self.print_state()

    def calm_down(self):
        if not self.is_calm():
            self.calm_state -= 1
        self.print_state()

    def is_full(self):
        if self.hunger_state == 0:
            return True
        else:
            return False

    def is_calm(self):
        if self.calm_state == 0:
            return True
        else:
            return False

    def print_state(self):
        print('{}: {} и {}'.format(
            self.name,
            self.hunger_states[self.hunger_state],
            self.calm_states[self.calm_state]
        ))


class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kids_list = []

    def add_kid(self, kid_name, kid_age):
        if self.age - kid_age >= 16:
            self.kids_list.append(Kid(kid_name, kid_age))
        else:
            print('Возраст ребенка должен быть меньше возраста родителя хотя бы на 16 лет')

    def print_info(self):
        if len(self.kids_list) == 1:
            print('Меня зовут {}, мне {} лет, у меня {} ребенок.'.format(
                self.name, self.age, len(self.kids_list)))
        else:
            print('Меня зовут {}, мне {} лет, у меня {} детей.'.format(
                self.name, self.age, len(self.kids_list)))
        if self.kids_list:
            for kid in self.kids_list:
                print('\t', kid)

    def feed(self, name):
        for kid in self.kids_list:
            if str(kid.name).lower() == str(name).lower():
                kid.eat()

    def calm(self, name):
        for kid in self.kids_list:
            if str(kid.name).lower() == str(name).lower():
                kid.calm_down()
