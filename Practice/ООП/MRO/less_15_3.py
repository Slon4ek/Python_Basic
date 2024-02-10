from abc import ABC, abstractmethod


class MusicMixin:

    def play_music(self):
        print("""
        I see trees of green
        Red roses too
        I see them bloom
        For me and for you
        And I think to myself
        What a wonderful world
        """)


class Transport(ABC):

    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass

    def signal(self):
        print("Сигнал")


class Car(Transport):

    def ride_on_earth(self):
        print("Едем по земле")


class Boat(Transport):

    def ride_on_water(self):
        print("Ходим по воде")


class Amphibian(Car, Boat, MusicMixin):
    pass


amph_transport = Amphibian('blue', 123)
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()
print(amph_transport.color)
amph_transport.color = 'white'
print(amph_transport.color)