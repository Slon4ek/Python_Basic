from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape, ABC):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = math.pi * self.radius ** 2
        return round(result, 2)


class Rectangle(Shape, ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        return round(result, 2)


class Triangle(Shape, ABC):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        result = (self.base * self.height) / 2
        return round(result, 2)


# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
