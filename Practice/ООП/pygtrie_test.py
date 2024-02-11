from pygtrie import Trie

# Создание экземпляра дерева префиксов
trie = Trie()

# Вставка элементов в дерево
trie["apple"] = 1
trie["banana"] = 2
trie["orange"] = 3

# Проверка наличия элементов
print("apple" in trie)  # Вывод: True
print("pear" in trie)  # Вывод: False

# Получение значения элемента
print(trie["banana"])  # Вывод: 2

# Удаление элемента
del trie["banana"]
print("banana" in trie)  # Вывод: False

# Поиск всех элементов с заданным префиксом
prefix_items = trie.items("a")
print(list(prefix_items))  # Вывод: [(('a', 'p', 'p', 'l', 'e'), 1)]

# Автодополнение
prefix = "app"
matching_suggestions = list(trie.iterkeys(prefix))
print(matching_suggestions)  # Вывод: [('a', 'p', 'p', 'l', 'e')]
