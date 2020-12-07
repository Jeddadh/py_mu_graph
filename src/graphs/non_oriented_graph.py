from src.graphs.node import Node


class NonOrientedGraph(object):
    """
    A python implementation of a graph.
    """

    def __init__(self):
        super(NonOrientedGraph, self).__init__()
        self.__nodes_id = set()
        self.__is_oriented = False

    def add_node(self, node: Node):
        self.__nodes_id.append(node.id)

    def is_connected(self):
        pass

    @property
    def is_oriented(self) -> bool:
        return self.__oriented
