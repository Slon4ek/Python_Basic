import math


class MyMath:
    """
    Математический модуль
    """

    @classmethod
    def circle_len(cls, radius: int) -> float:
        """
        Метод вычисляет длину окружности и возвращает результат
        :param radius: радиус окружности
        :rtype: int
        """
        result = 2 * math.pi * radius
        return result

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        """
        Метод вычисляет площадь круга и возвращает результат
        :param radius: радиус окружности
        :rtype: int
        """
        result = math.pi * radius ** 2
        return result

    @classmethod
    def cube_vol(cls, edge: int) -> int:
        """
        Метод вычисляет объем куба и возвращает результат
        :param edge: длина ребра куба
        :rtype: int
        """
        result = edge ** 3
        return result

    @classmethod
    def sphere_sq(cls, radius: int) -> float:
        """
        Метод вычисляет площадь сферы и возвращает результат
        :param radius: радиус сферы
        :rtype: int
        """
        result = 4 * math.pi * radius ** 2
        return result


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
