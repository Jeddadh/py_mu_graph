class Graph(object):
    def __init__(
        self,
    ):
        super(Graph, self).__init__()
        self.__nodes = {}  # dictionary containing all nodes in the graph.
        self.__node_id = 0  # a variable that we increment each time we add a node.
        self.__root_node_id = None
        self.__root_node = None

    class Node(object):
        """
        A python implementation of a graph node.
        """

        def __init__(self, value, graph):
            self.graph = graph
            self.__id = graph.node_id
            self.value = value
            graph.node_id += 1
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
            :param is_oriented: the type of the graph. If it's not oriented : self will be added as an adj node to the given
             node.
            :param node: of type Node
            """
            self.__adj.add(node.id)
            if not is_oriented:
                node.add_adj(self, is_oriented=True)

        def remove_adj(self, node):
            """
            remove a node from adjacent nodes set. Raises a KeyError if the node does not exist.
            :param node: of type Node
            :return:
            """
            try:
                self.__adj.remove(node.id)
            except KeyError:
                raise KeyError("node must be an adjacent node")

        def breadth_first(self, function: callable):
            if self.__adj.isempty():
                function(self)
                return
            else:
                for child_id in self.__adj:
                    child_node = self.graph.get_node_by_id(child_id)
                    child_node.breadth_first(function)

    @property
    def root_node(self):
        return self.__root_node

    @property
    def root_node_id(self):
        return self.root_node_id

    @root_node_id.setter
    def root_node_id(self, new_root_node_id):
        if new_root_node_id not in self.__nodes:
            raise ValueError("root_node must be an id of an existing node")
        self.__root_node_id = new_root_node_id
        self.__root_node = self.__nodes[new_root_node_id]

    def get_node_by_id(self, node_id):
        try:
            return self.__nodes[node_id]
        except KeyError:
            raise KeyError("Given node id does not exist")

    def add_root(self, node_value):
        if self.root_node is None:
            raise ValueError(
                "A graph root already exists. You can use set_root method."
            )
        root_node = Graph.Node(node_value, self)
        self.__root_node = root_node

    def set_root(self, node_id):
        # TODO
        pass

    def add_node(self, node_value, node_parent_id, edge_value):
        # TODO
        node_parent = self.__nodes[node_parent_id]
        node = Graph.Node(node_value, self)
        node_parent.add_adj(node)

    def breadth_first(self, function: callable):
        self.root_node.breadth_first(function)
