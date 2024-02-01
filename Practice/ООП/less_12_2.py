class Point:
    __count_point = 0

    def __init__(self, x=0, y=0):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)
        Point.__count_point += 1

    def get_count(self):
        return self.__count_point

    def set_x(self, x):
        self.__x = x
        return self.__x

    def set_y(self, y):
        self.__y = y
        return self.__y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def position(self):
        print('Координаты точки: х = {} y = {}'.format(self.get_x(), self.get_y()))
        print('Всего точек: {}'.format(self.get_count()))


class Human:

    def __init__(self, name, age):
        self.__name = self.set_name(name)
        self.__age = self.set_age(age)

    def __str__(self):
        return 'Имя: {}, возраст: {} лет'.format(self.__name, self.__age)

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
            return self.__name
        else:
            raise Exception('Имя должно состоять из букв!')

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
            return self.__age
        else:
            raise Exception('Должно быть число от 1 до 100')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


misha = Human('Миша', 20)
print(misha)
misha.set_age(25)
print(misha.get_name())
