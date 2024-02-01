class Robot:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return 'Модель робота: {model}'.format(
            model=self.__model
        )

    def operate(self):
        pass

    def get_model(self):
        return self.__model


class CleanRobot(Robot):
    def __init__(self, model, ):
        super().__init__(model)
        self.__garbage_bag = 0

    def operate(self):
        for _ in range(6):
            print('Робот {model} пылесосит пол!\n\tТекущая запослненность мешка: {bag}'.format(
                model=self.get_model(),
                bag=self.__garbage_bag
            ))
            self.__garbage_bag += 1
        else:
            print('Мешок для мусора заполнен!')


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('Роботом: {model} ведется защита военного обьекта при помощи оружия: {gun}'.format(
            gun=self.gun,
            model=self.get_model()
        ))


class Submarine(WarRobot):
    def __init__(self, model, gun, depth):
        super().__init__(model, gun)
        self.depth = depth

    def operate(self):
        super().operate()
        print('Охрана ведется под водой, на глубине {} метров'.format(self.depth))


class MyException(Exception):
    pass


with open('numbers.txt', 'r') as file:
    for line in file:
        num_1, num_2 = line.rstrip().split()
        try:
            if int(num_1) < int(num_2):
                raise MyException
            result = int(num_1) / int(num_2)
            print('Результат деления {} на {} = {}'.format(
                num_1, num_2, result
            ))
        except MyException:
            print('нельзя делить меньшее на большее')
