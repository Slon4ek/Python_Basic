grades = [
    {'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24},
    {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
    {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
    {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
    {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
    {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
    {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
    {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
    {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
]

# Решение через key
print(max(grades, key=lambda x: x["score"]))
print(min(grades, key=lambda x: x["score"]))
# Вывод исключительно очков:
print(max(grades, key=lambda x: x["score"])['score'])
print(min(grades, key=lambda x: x["score"])['score'])

# Решение через map, который будет изучен в следующем модуле
print(list(map(lambda x: x['score'], grades)))  # для наглядности
print(max(map(lambda x: x['score'], grades)))
print(min(map(lambda x: x['score'], grades)))


# Задача 2. Сортировка
#
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке:
# его имя, возраст и остальные данные.
# Вас попросили реализовать для этой базы сортировку по возрасту (по убыванию и по возрастанию).
#
# Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами.
# Затем создайте список из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @name.setter
    def name(self, word):
        self._name = word

    def __repr__(self):
        return f"({self.name}, {self.age})"


first = Person("Max", 29)
second = Person("Christine", 21)
third = Person("Anthony", 35)
humans = [first, second, third]
print(humans)
humans.sort(key=lambda x: x.age)
print(humans)
humans.sort(key=lambda x: -x.age)
print(humans)