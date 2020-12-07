import unittest

from py_mu_graphs.graphs.node import Node


class TestNodeMethods(unittest.TestCase):
    node1 = Node()
    node2 = Node()
    node3 = Node()

    def test_node_creation(self):
        assert TestNodeMethods.node1.id == 0
        assert TestNodeMethods.node2.id == 1
        assert TestNodeMethods.node3.id == 2

    def test_add_adj(self):
        TestNodeMethods.node1.add_adj(TestNodeMethods.node2, is_oriented=False)
        assert TestNodeMethods.node1.adj == {TestNodeMethods.node2.id}
        assert TestNodeMethods.node2.adj == {TestNodeMethods.node1.id}

        TestNodeMethods.node1.add_adj(TestNodeMethods.node2, is_oriented=False)
        assert TestNodeMethods.node1.adj == {TestNodeMethods.node2.id}
        assert TestNodeMethods.node2.adj == {TestNodeMethods.node1.id}

        TestNodeMethods.node1.add_adj(TestNodeMethods.node3, is_oriented=True)
        assert TestNodeMethods.node1.adj == {
            TestNodeMethods.node2.id,
            TestNodeMethods.node3.id,
        }
        assert TestNodeMethods.node3.adj == set()

        TestNodeMethods.node1.add_adj(TestNodeMethods.node3, is_oriented=False)
        assert TestNodeMethods.node1.adj == {
            TestNodeMethods.node2.id,
            TestNodeMethods.node3.id,
        }
        assert TestNodeMethods.node3.adj == {TestNodeMethods.node1.id}
        TestNodeMethods.node1.remove_adj(TestNodeMethods.node2)
        assert TestNodeMethods.node2.id not in TestNodeMethods.node1.adj
