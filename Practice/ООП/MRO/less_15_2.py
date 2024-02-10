class Robot:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        res = super().__str__()
        return res + ' {} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Я - Робот!')


class CanFly:

    def __init__(self, *args, **kwargs):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        super().operate()
        print('летим')

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class ScoutDrone(CanFly, Robot):

    def __init__(self, model):
        super().__init__(model=model)

    def operate(self):
        super().operate()
        print('Робот ведет разведку с воздуха')


class WarDrone(CanFly, Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print(f'Робот защищает объект при помощи {self.gun}')


print()
ScoutDrone('a1').operate()
print()
WarDrone('r2-d2', 'intellect').operate()
ScoutDrone('a1').__str__()
my_drone = ScoutDrone('a1')
print(my_drone)
