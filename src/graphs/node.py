class Node(object):
    """
    A python implementation of a graph node.
    """

    node_id = 0

    def __init__(self):
        super(Node, self).__init__()
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

    def add_adj(self, node, is_oriented=False):
        """
        Add a node to the adjacent nodes set
        :param is_oriented: the type of the graph. If it's not oriented : self will be added as an adj node to the given node.
        :param node: of type Node
        """
        if not isinstance(node, Node):
            raise TypeError("node must be an instance of Node")
        self.__adj.add(node.id)
        if not is_oriented:
            node.add_adj(self, is_oriented=True)

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
