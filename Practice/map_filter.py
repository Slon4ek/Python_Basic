from functools import reduce
numbers = input("Введите числа: ")
print(sorted(list(map(int, numbers.split()))))  # функция map обходит все элементы списка и применяет к каждому int()

text = input("Введите строку: ")

print(list(filter(lambda x: not (x.isupper() or x.isdigit()), text)))

# Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке:
#
#
#
sentences = ["Nory was a Catholic", "because her mother was a Catholic",
             "and Nory’s mother was a Catholic", "because her father was a Catholic",
             "and her father was a Catholic", "because his mother was a Catholic", "or had been"]


def check_was(a, b):
    if isinstance(a, str):  # обработаем первый элемент отдельно
        a = int(a.count('was'))
    result = a + int(b.count('was'))
    return result  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка


print(reduce(check_was, sentences))
