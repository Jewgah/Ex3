import unittest
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


# TODO: save/load shortestpath components
class TestGraphAlgo(unittest.TestCase):

    def test_save_and_load(self):
        # add nodes
        self.graph = DiGraph()
        self.graph.add_node(1, (1.44, 2.43, 4.477))
        self.graph.add_node(2, (2.789, 4.3331, 6.41457))
        self.graph.add_node(3, (3.142, 4.1376, 2.1376))
        self.graph.add_node(4, (5.137, 6.2, 12.137))

        # add edges
        self.graph.add_edge(1, 2, 2)
        self.graph.add_edge(2, 3, 3)
        self.graph.add_edge(3, 4, 4)
        self.graph.add_edge(4, 1, 6)

        # init graph algo
        self.algo = GraphAlgo()
        self.algo.__init__(self.graph)

        # save as JSON file
        self.algo.save_to_json("../data/test.json")
        self.graph1 = self.algo.get_graph()

        # load JSON file
        self.algo.load_from_json("../data/test.json")
        self.graph2 = self.algo.get_graph()

        # check if Graph's.toString are equal
        self.assertEqual(self.graph1.__repr__(), self.graph2.__repr__())

    def test_save_and_load_no_pos(self):
        # add nodes
        self.graph = DiGraph()
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_node(4)

        # add edges
        self.graph.add_edge(1, 2, 2)
        self.graph.add_edge(2, 3, 3)
        self.graph.add_edge(3, 4, 4)
        self.graph.add_edge(4, 1, 6)

        # init graph algo
        self.algo = GraphAlgo()
        self.algo.__init__(self.graph)

        # save as JSON file
        self.algo.save_to_json("../data/test.json")
        self.graph1 = self.algo.get_graph()

        # load JSON file
        self.algo.load_from_json("../data/test.json")
        self.graph2 = self.algo.get_graph()

        # check if Graph's.toString are equal
        self.assertEqual(self.graph1.__repr__(), self.graph2.__repr__())

    def test_shortest_path(self):
        # add nodes
        self.graph = DiGraph()
        self.graph.add_node(1, (1.44, 2.43, 4.477))
        self.graph.add_node(2, (2.789, 4.3331, 6.41457))
        self.graph.add_node(3, (3.142, 4.1376, 2.1376))
        self.graph.add_node(4, (5.137, 6.2, 12.137))

        # add edges
        self.graph.add_edge(1, 2, 2)
        self.graph.add_edge(2, 3, 3)
        self.graph.add_edge(3, 4, 4)
        self.graph.add_edge(4, 1, 6)

        # init graph algo
        self.algo = GraphAlgo()
        self.algo.__init__(self.graph)

        # shortest path
        self.assertEqual("(9, [1, 2, 3, 4])", str(self.algo.shortest_path(1, 4)))

    def test_connected_components(self):
        p = (1.21, 2.12, 3.16)
        # add nodes
        self.graph = DiGraph()
        self.graph.add_node(1, p)
        self.graph.add_node(2, p)
        self.graph.add_node(3, p)
        self.graph.add_node(4, p)

        # add edges
        self.graph.add_edge(1, 2, 2)
        self.graph.add_edge(2, 3, 3)
        self.graph.add_edge(3, 4, 4)
        self.graph.add_edge(4, 2, 9)

        # init graph algo
        self.algo = GraphAlgo()
        self.algo.__init__(self.graph)

        # connected_components
        self.assertEqual("[[1], [2, 3, 4]]", str(self.algo.connected_components()))

        # connected_components(id)
        self.assertEqual("[[2, 3, 4]]", str(self.algo.connected_components(3)))


# TODO: test with boaz graphs

if __name__ == '__main__':
    unittest.main()
