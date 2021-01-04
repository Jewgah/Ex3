import unittest
from unittest import TestCase
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def test_load_from_json(self):
        self.graph = None
        self.algo = GraphAlgo()

        self.algo.load_from_json("../data/T0.json")
        self.graph = self.algo.get_graph()

        # TODO: verify if graph == T0


if __name__ == '__main__':
    unittest.main()
