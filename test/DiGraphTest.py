from src.DiGraph import DiGraph
import unittest
from unittest import TestCase
from src.NodeData import Node_data

# if __name__ == '__main__':
#     p=(5,4)
#     # node=Node_data(0,p)
#     # node.weight=500
#     # print(node.getKey())
#     # print(node)
#     # edge=Edge_data(0,1,500)
#     # print(edge)
#     graph=DiGraph()
#     print("***********add node**************")
#     print("add node:",graph.add_node(0,p))
#     print("add node:",graph.add_node(0,p))
#     print("add node:", graph.add_node(1, p))
#     print("mc:", graph.get_mc())
#     print("vsize:",graph.v_size())
#     print("esize:",graph.e_size())
#     print("***********finish**************")
#     print("                                ")
#     print("***********add edge**************")
#     print("add edge:",graph.add_edge(0,2,500))
#     print("add edge:",graph.add_edge(0,1,500))
#     print("add edge:", graph.add_edge(0, 1, 300))
#     print("add edge:", graph.add_edge(1, 0, 300))
#     print("mc:", graph.get_mc())
#     print("vsize:",graph.v_size())
#     print("esize:",graph.e_size())
#     print("***********finish**************")
#
#     print("                                ")
#     print("***********get edge/vertex**************")
#     vertexs = graph.get_all_v()
#     for x in vertexs:
#         print("key: ",x,"values: ",vertexs[x])
#
#     insid=graph.all_in_edges_of_node(0)
#     out=graph.all_out_edges_of_node(0)
#     for x in insid:
#         print("key: ",x,"values: ",insid[x])
#     for x in out:
#         print("key: ",x,"values: ",out[x])
#     print("***********finish**************")
#     print("                                ")
#     print("***********add edge**************")
#     print("remove edge:",graph.remove_edge(0,2))
#     print("remove edge:",graph.remove_edge(0,1))
#     print("remove edge:", graph.remove_edge(0, 1))
#     print("mc:", graph.get_mc())
#     print("vsize:",graph.v_size())
#     print("esize:",graph.e_size())
#     print("***********finish**************")
#
#     print("                                ")
#     print("***********add edge**************")
#     print("add edge:", graph.add_edge(0, 1, 500)) # 6
#     print("remove node:",graph.remove_node(2))
#     print("remove node:",graph.remove_node(1))
#     print("remove node:", graph.remove_node(1))
#     print("mc:", graph.get_mc()) # 9
#     print("vsize:",graph.v_size()) #1
#     print("esize:",graph.e_size()) #0
#     print("***********finish**************")
#
#     print("                                ")
#     print("***********get edge/vertex**************")
#     vertexs = graph.get_all_v()
#     for x in vertexs:
#         print("key: ",x,"values: ",vertexs[x])
#
#     insid=graph.all_in_edges_of_node(0)
#     out=graph.all_out_edges_of_node(0)
#     for x in insid:
#         print("key: ",x,"values: ",insid[x])
#     for x in out:
#         print("key: ",x,"values: ",out[x])
#     print("***********finish**************")

class Test(TestCase):

        def setUp(self) -> None:
            self.g = DiGraph()
            for i in range(6):
                self.g.add_node(i)
            self.g.add_edge(1, 2, 1)
            self.g.add_edge(1, 3, 1)
            self.g.add_edge(1, 4, 1)
            self.g.add_edge(2, 1, 1)
            self.g.add_edge(2, 5, 1)
            self.g.add_edge(3, 1, 1)
            self.g.add_edge(4, 5, 1)
            self.g.add_edge(4, 2, 1)

        def test_add_node(self):
            self.assertEqual(6, self.g.v_size())

            self.assertTrue(self.g.add_node(-2))
            self.assertEqual(7, self.g.v_size())
            self.assertEqual(15, self.g.get_mc())

            self.assertFalse(self.g.add_node(1))
            self.assertEqual(7, self.g.v_size())
            self.assertEqual(15, self.g.get_mc())

        def test_remove_node(self):
            self.assertEqual(6, self.g.v_size())

            self.assertTrue(self.g.remove_node(1))
            self.assertEqual(5, self.g.v_size())
            self.assertEqual(15, self.g.get_mc())

            self.assertFalse(self.g.remove_node(-3))
            self.assertEqual(5, self.g.v_size())
            self.assertEqual(15, self.g.get_mc())

        def test_add_edge(self):
            self.assertEqual(8, self.g.e_size())

            self.assertTrue(self.g.add_edge(3, 2, 1))
            self.assertEqual(9, self.g.e_size())
            self.assertEqual(15, self.g.get_mc())

            self.assertFalse(self.g.add_edge(2, 5, 1))
            self.assertFalse(self.g.add_edge(2, 100, 1))
            self.assertFalse(self.g.add_edge(100, 5, 1))
            self.assertFalse(self.g.add_edge(100, 200, 1))
            self.assertEqual(9, self.g.e_size())
            self.assertEqual(15, self.g.get_mc())

        def test_remove_edge(self):
            self.assertEqual(8, self.g.e_size())

            self.assertTrue(self.g.remove_edge(2, 5))
            self.assertEqual(7, self.g.e_size())
            self.assertEqual(15, self.g.get_mc())

            self.assertFalse(self.g.remove_edge(3, 2))
            self.assertEqual(7, self.g.e_size())
            self.assertEqual(15, self.g.get_mc())

        def test_get_all_v(self):
            d = {0: Node_data(0), 1: Node_data(1), 2: Node_data(2), 3: Node_data(3), 4: Node_data(4), 5: Node_data(5)}
            self.assertEqual(d.__repr__(), self.g.get_all_v().__repr__())

        def test_all_in_edges_of_node(self):
            self.assertIsNotNone(self.g.all_in_edges_of_node(1))
            self.assertIsNotNone(self.g.all_in_edges_of_node(2))
            self.assertIsNotNone(self.g.all_in_edges_of_node(3))
            self.assertIsNotNone(self.g.all_in_edges_of_node(4))

            self.assertIsNone(self.g.all_in_edges_of_node(6))
            self.assertIsNone(self.g.all_in_edges_of_node(7))
            self.assertIsNone(self.g.all_in_edges_of_node(-1))

        def test_all_out_edges_of_node(self):
            self.assertIsNotNone(self.g.all_out_edges_of_node(1))
            self.assertIsNotNone(self.g.all_out_edges_of_node(2))
            self.assertIsNotNone(self.g.all_out_edges_of_node(3))
            self.assertIsNotNone(self.g.all_out_edges_of_node(4))

            self.assertIsNone(self.g.all_out_edges_of_node(6))
            self.assertIsNone(self.g.all_out_edges_of_node(7))
            self.assertIsNone(self.g.all_out_edges_of_node(-1))

        def test_v_size(self):
            self.assertEqual(6, self.g.v_size())
            # adding a new node:
            self.assertTrue(self.g.add_node(7))
            self.assertEqual(7, self.g.v_size())
            # adding already inside nodes:
            for i in range(6):
                self.assertFalse(self.g.add_node(i))
            self.assertEqual(7, self.g.v_size())
            # adding 3 new nodes (#6, #8, #9):
            for i in range(6, 10):
                self.g.add_node(i)
            self.assertEqual(10, self.g.v_size())

        def test_e_size(self):
            self.assertEqual(8, self.g.e_size())
            # adding old edge - shouldn't update it
            self.assertFalse(self.g.add_edge(1, 2, 3.5))
            self.assertEqual(8, self.g.e_size())

        def test_get_mc(self):
            self.assertEqual(14, self.g.get_mc())

        if __name__ == '__main__':
            unittest.main()