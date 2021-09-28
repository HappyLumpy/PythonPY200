from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def is_valid(cls, node: Any) -> None:
        if not isinstance(node, (type(None), cls)):
            raise TypeError

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self.__next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        return f"DoubleLinkedNode({self.value}, {None}, {None})" if self.next is None else f"DoubleLinkedNode({self.value}, Node({self.next}), Node({self.prev}))"

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        self.is_valid(prev_)
        self.__prev = prev_


if __name__ == "__main__":
    dn1 = DoubleLinkedNode(3)
    dn2 = DoubleLinkedNode(4)
    dn3 = DoubleLinkedNode(6, dn2, dn1)
    print(repr(dn3))
    print(dn3)
    print(dn3.prev)
    dn4 = repr(dn3)
    print(dn4)
