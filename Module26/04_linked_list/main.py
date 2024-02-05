from typing import Any, Optional


class Node:
    def __init__(self, value: Optional[Any] = None, next_node: Optional['Node'] = None) -> None:
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        return '{value}'.format(
            value=self.value
        )


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.__length = 0
        self.__cur_node = None

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next_node is not None:
                current = current.next_node
                values.append(str(current.value))
            return '[{val}]'.format(val=', '.join(values))
        return 'LinkedList []'

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cur_node is None:
            self.__cur_node = self.head
            return self.__cur_node
        if self.__cur_node.next_node is None:
            raise StopIteration
        self.__cur_node = self.__cur_node.next_node
        return self.__cur_node

    def append(self, elem: Any) -> None:
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = new_node
        self.__length += 1

    def remove(self, index: int) -> None:
        cur_node = self.head
        cur_index = 0
        prev = None
        if self.__length == 0 or self.__length <= index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next_node
                self.__length -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next_node
            cur_index += 1

        prev.next_node = cur_node.next_node
        self.__length -= 1

    def get(self, index: int) -> Node:
        cur_node = self.head
        cur_index = 0
        prev = None
        if self.__length == 0 or self.__length < index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                return cur_node

        while cur_node is not None:
            if cur_index == index:
                break
            cur_node = cur_node.next_node
            cur_index += 1
        return cur_node


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list.remove(1)
print(my_list)
print(my_list.get(1))
for i in my_list:
    print(i)
