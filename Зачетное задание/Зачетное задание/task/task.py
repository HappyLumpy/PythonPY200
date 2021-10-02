from collections.abc import MutableSequence
from node import Node, DoubleLinkedNode
from typing import Any, Iterable, Optional, Iterator


class LinkedList(MutableSequence):
    CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self._tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        node = self.step_by_step_on_nodes(index)
        node.value = value

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
            self.linked_nodes(prev_node, next_node)
            current_node.next = None
        self.len -= 1

    def __len__(self):
        return self.len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        insertnode = self.CLASS_NODE(value)
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

    def append(self, value: Any):
        append_node = self.CLASS_NODE(value)

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
        if node is None:
            self._tail = None
        else:
            if self.len == 1:
                self._tail = self.head = node
            else:
                prev = self.step_by_step_on_nodes(self.len - 2)
                self._tail = node
                self.linked_nodes(prev, self._tail)

    def nodes_iterator(self) -> Iterator[Node]:
        current_node = self.head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

    def __contains__(self, value):
        for node in self.nodes_iterator():
            if node.value == value:
                return True
        return False

    # def pop(self):
    #     prev_node = self.step_by_step_on_nodes(self.len - 2)
    #     self.len -= 1
    #     self.tail = None
    #     self.tail = prev_node
    #     prev_node.next = None


    def __reversed__(self):
        list_ = [i for i in self]
        revers_list = list_.reverse()
        return LinkedList(revers_list)


class DoubleLinkedList(LinkedList):
    CLASS_NODE = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        right_node.prev = left_node
        left_node.next = right_node


if __name__ == "__main__":
    list_ = []
    list_2 = [i for i in range(10)]
    new_1 = DoubleLinkedNode(1)
    new_2 = DoubleLinkedNode(2)
    new_3 = DoubleLinkedNode(3)
    new_4 = DoubleLinkedNode(4)
    ll_2 = LinkedList(list_2)

    dll = DoubleLinkedList(list_2)
    ll = LinkedList(list_2)
    print(dll)
    print(dll.reverse())

    print(repr(ll))
    print(repr(ll.tail))
