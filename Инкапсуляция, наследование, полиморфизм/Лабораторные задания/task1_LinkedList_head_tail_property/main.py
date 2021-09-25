from typing import Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node: Optional["Node"]):
        Node.is_valid(node)
        if node is None:
            self._head = None
            self.len = 0
        else:
            if self.head is None:
                self._head = node
                self.len += 1
            else:
                node.next = self.head.next
                self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node: Optional["Node"]):
        Node.is_valid(node)
        if node is None:
            self._tail = None
            self.len -= 1
        else:
            self._tail = node
            prev = self.step_by_step_on_nodes(self.len - 2)
            prev.next = self._tail




if __name__ == "__main__":
    list_ = [1, 2, 3]
    node = Node(4)
    ll = LinkedList(list_)
    print(repr(ll))
    # ll.head = node
    # print(ll.head)
    # ll.tail = node
    # print(ll.tail)
    #
    # print(repr(ll))
