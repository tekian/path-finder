# -*- coding: utf-8 -*-

from typing import Dict
from typing import List
from typing import Tuple

from models import MapNode
from models import MapSpace
from models import PathEdge
from models import PathNode
from models.factories import PathSpaceFactoryType


class PathSpaceFactory(PathSpaceFactoryType):
    def __init__(self, map_space: MapSpace) -> None:
        self._map_space: MapSpace = map_space
        self._path_nodes_by_map_nodes: Dict[MapNode, PathNode] = {}

    def generate_edges(self) -> List[PathEdge]:
        path_edges = []

        for map_edge in self._map_space.edges:
            _1 = self._path_nodes_by_map_nodes[map_edge.pair[0]]
            _2 = self._path_nodes_by_map_nodes[map_edge.pair[1]]
            path_edges.append(PathEdge(map_edge, (_1, _2)))

        return path_edges

    def generate_nodes(self) -> List[PathNode]:
        for map_node in self._map_space.nodes:
            self._path_nodes_by_map_nodes[map_node] = PathNode(map_node)

        return list(self._path_nodes_by_map_nodes.values())

    def generate_defaults(self) -> Tuple[PathNode, PathNode]:
        from_node = self._path_nodes_by_map_nodes[self._map_space.from_node]
        to_node = self._path_nodes_by_map_nodes[self._map_space.to_node]

        return from_node, to_node
