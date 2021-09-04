from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(...):  # TODO наследовать класс LinkedList
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        ...  # TODO расширяем конструктор, чтобы в связном списке был driver

    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        ...  # TODO считать данные из драйвера

    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        ...  # TODO записать данные с помощью драйвера


if __name__ == '__main__':
    ll = LinkedListWithDriver([1, 2, 3, 4, 5])
    # TODO инициализировать драйвер и записать данные

    # TODO заменить драйвер и считать данные
    print(ll)
