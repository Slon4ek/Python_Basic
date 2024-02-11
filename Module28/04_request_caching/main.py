from collections import deque
from typing import Dict, Any


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._cache = dict()
        self.keys_list = deque()

    @property
    def cache(self) -> Dict.keys:
        """
        Метод возвращает ключ самого старого элемента
        """
        return self.keys_list.pop()

    @cache.setter
    def cache(self, value: (Any, Any)) -> None:
        """
        Метод добавляет новый элемент в кэш. Если количество элементов больше capacity,
        то удаляет самый старый элемент
        """
        if len(self._cache) >= self.capacity:
            del self._cache[self.cache]
        key, val = value
        self._cache[key] = val
        self.keys_list.appendleft(key)

    def get(self, key: Any):
        """
        Метод возвращает значение по ключу
        """
        if key in self._cache.keys():
            self.keys_list.appendleft(key)  # обновляем порядок использования элемента(ставим ключ в начало очереди)
            if self.keys_list[0] == self.keys_list[len(self.keys_list) - 1]:
                self.keys_list.pop()
            return self._cache[key]

    def print_cache(self) -> None:
        """
        Метод выводит на экран содержимое кэша
        :return:
        """
        for key, val in self._cache.items():
            print(f'{key}: {val}')


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2
print(cache.keys_list)
# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
