import unittest

from task import Node, linked_nodes


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_linked_nodes(self):
        left_node = Node("left")
        right_node = Node("right")

        linked_nodes(left_node, right_node)

        msg = "Узлы не были успешно связаны. Проверьте функцию linked_nodes. "
        self.assertEqual(repr(left_node.next), repr(right_node), msg)
