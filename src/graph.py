class Node(object):
    """
    A python implementation of a graph node.
    """

    node_id = 0

    def __init__(self):
        self.__id = Node.node_id
        Node.node_id += 1
        self.__adj = set()

    @property
    def id(self) -> int:
        """The node's id"""
        return self.__id

    @property
    def adj(self) -> set:
        """
        The list of adjacent nodes
        :return: set : the list of adjacent nodes
        """
        return self.__adj

    def add_adj(self, node):
        """
        Add a node to the adjacent nodes set
        :param node: of type Node
        """
        if not isinstance(node, Node):
            raise TypeError("node must be an instance of Node")
        self.__adj.add(node.id)

    def remove_adj(self, node):
        """
        remove a node from adjacent nodes set. Raise a KeyError if the node does not exist.
        :param node: of type Node
        :return:
        """
        if not isinstance(node, Node):
            raise TypeError("node must be an instance of Node")
        try:
            self.__adj.remove(node.id)
        except KeyError:
            raise KeyError("node must be an adjacent node")


class Graph(object):
    """
    A python implementation of a graph.
    """

    def __init__(self, is_oriented=False):
        self.__nodes_id = set()
        self.__is_oriented = is_oriented

    def add_node(self, node: Node):
        self.__nodes_id.append(node.id)

    def is_connected(self):
        pass

    @property
    def is_oriented(self ) -> bool:
        return self.__oriented
