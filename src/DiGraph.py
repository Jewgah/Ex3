from src.GraphInterface import GraphInteface


class DiGraph(GraphInteface):

    def __init__(self):  # initialize self
        self.V = dict()
        self.N_out = dict()
        self.N_in = dict()
        self.nodeSize = 0
        self.edgeSize = 0
        self.mc = 0

    # Returns the number of vertices in this graph
    def v_size(self) -> int:
        return self.nodeSize

    # Returns the number of edges in this graph
    def e_size(self) -> int:
        return self.edgeSize

    # Returns the current version of this graph (MC is incremented for every change)
    def get_mc(self) -> int:
        return self.mc

    # Adds an edge to the graph
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.V and id2 in self.V and id2 not in self.N_out[id1]:
            self.N_in[id2][id1] = weight
            self.N_out[id1][id2] = weight
            self.mc = self.mc+1
            self.edgeSize = self.edgeSize+1
            return True
        return False

    # Adds a node to the graph
    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.V:




    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass
