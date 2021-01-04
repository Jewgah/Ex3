from typing import List
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface
import json

# TODO: IMPLEMENT
class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
        self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:

        try:
            filep = open(file_name)
            graphfromjson=json.load(filep)
            edges=graphfromjson.get('Edges')
            vertexs=graphfromjson.get('Nodes')
            self.graph = DiGraph()
            for x in vertexs:
                pos=x.get('pos')
                if pos is None:
                    self.graph.add_node(x.get('id'))
                else:
                    posi = tuple(map(float, x.get('pos').split(",")))
                    self.graph.add_node(x.get('id'),posi)
            for x in edges:
                self.graph.add_edge(x.get('src'),x.get('dest'),x.get('w'))

        except FileExistsError:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass


