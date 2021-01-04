from src.GraphAlgo import GraphAlgo
import unittest
from unittest import TestCase

if __name__ == '__main__':
    algo = GraphAlgo()

    print(algo.load_from_json("../data/T0.json"))

    graph = algo.get_graph()

    print("***********get edge/vertex**************")
    vertexs = graph.get_all_v()
    for x in vertexs:
        print("key: ",x,"values: ",vertexs[x])
        for y in graph.all_out_edges_of_node(x):
            print("key: ", y, "values: ", graph.all_out_edges_of_node(x)[y])

    print("***********finish**************")