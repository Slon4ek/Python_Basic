class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Storm:
    def __str__(self):
        return 'Вода + Воздух = Шторм'


class Vapor:
    def __str__(self):
        return 'Вода + Огонь = Пар'


class Dirt:
    def __str__(self):
        return 'Вода + Земля = Грязь'


class Lava:
    def __str__(self):
        return 'Огонь + Земля = Лава'


class Lightning:
    def __str__(self):
        return 'Огонь + Воздух = Молния'


class Dust:
    def __str__(self):
        return 'Воздух + Земля = Пыль'
