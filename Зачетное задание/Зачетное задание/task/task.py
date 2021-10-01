from collections.abc import MutableSequence
from node import Node, DoubleLinkedNode
from typing import Any, Iterable, Optional


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self._tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self._tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self._tail = append_node

        self.len += 1

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        left_node.next = right_node

    def step_by_step_on_nodes(self, index: int) -> Node:
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()
        current_node = self.step_by_step_on_nodes(index)
        if index == 0:
            self._head = self._head.next
            current_node.next = None
        elif index == self.len - 1:
            prev_node = self.step_by_step_on_nodes(index - 1)
            prev_node.next = None
            self._tail = prev_node
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = self.step_by_step_on_nodes(index + 1)
            prev_node.next = next_node
            current_node.next = None
        self.len -= 1

    def __len__(self):
        return self.len

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

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        insertnode = Node(value)
        if index == 0:
            self.linked_nodes(insertnode, self.head)
            self.head = insertnode
        elif index >= self.len - 1:
            tail = self.step_by_step_on_nodes(self.len - 1)
            self.linked_nodes(tail, insertnode)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            self.linked_nodes(insertnode, prev_node.next)
            prev_node.next = insertnode
        self.len += 1

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
            else:
                node.next = self.head.next
                self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node: Optional["Node"]):
        Node.is_valid(node)
        print('srabotal setter tail')
        if node is None:
            self._tail = None
        else:
            if self.len == 1:
                self._tail = self.head = node
            else:
                prev = self.step_by_step_on_nodes(self.len - 2)
                self._tail = node
                prev.next = self._tail


class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        super().__init__(data=data)

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        right_node.prev = left_node
        left_node.next = right_node

    def append(self, value: Any):
        append_node = DoubleLinkedNode(value)
        if self.head is None:
            self.head = self._tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self._tail = append_node
        self.len += 1

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:
            raise IndexError()
        current_node = self.step_by_step_on_nodes(index)
        if index == 0:
            self._head = self._head.next
            current_node.next = None
            self.head.prev = None
        elif index == self.len - 1:
            prev_node = self.step_by_step_on_nodes(index - 1)
            prev_node.next = None
            self._tail = prev_node
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = self.step_by_step_on_nodes(index + 1)
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node.next = None
        self.len -= 1

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        insertnode = DoubleLinkedNode(value)
        if index == 0:
            self.linked_nodes(insertnode, self.head)
            self.head = insertnode
        elif index >= self.len - 1:
            tail = self.step_by_step_on_nodes(self.len - 1)
            self.linked_nodes(tail, insertnode)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            self.linked_nodes(insertnode, prev_node.next)
            self.linked_nodes(prev_node, insertnode)
            prev_node.next = insertnode
        self.len += 1


if __name__ == "__main__":
    list_ = []
    new_1 = DoubleLinkedNode(1)
    new_2 = DoubleLinkedNode(2)
    new_3 = DoubleLinkedNode(3)
    new_4 = DoubleLinkedNode(4)
    ll = LinkedList(list_)

    dll = DoubleLinkedList(list_)
    dll.append(new_1)
    dll.append(new_2)
    dll.append(new_3)
    dll.append(new_4)
    ll.append(new_1)
    ll.append(new_2)
    ll.append(new_3)
    ll.append(new_4)
    dll.insert(2, DoubleLinkedNode(4))

    print(dll)
    print(repr(dll.tail))

