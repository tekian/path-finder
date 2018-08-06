# -*- coding: utf-8 -*-

from random import choice
from random import randint
from typing import Dict
from typing import List
from typing import Tuple

from models import MapEdge
from models import MapNode
from models.factories import MapSpaceFactoryType


class GridMapSpaceFactory(MapSpaceFactoryType):
    def __init__(self, grid_size: Tuple[int, int], keep_edges: int) -> None:
        self._grid_size = grid_size
        self._keep_edges = keep_edges

        self._size_x, self._size_y = self._grid_size

        self._map_nodes: Dict[Tuple[int, int], MapNode] = {}

    def generate_nodes(self) -> List[MapNode]:
        for grid_x in list(range(self._size_x)):
            pos_x = float(grid_x) / self._size_x
            for grid_y in list(range(self._size_y)):
                pos_y = float(grid_y) / self._size_y
                node = MapNode(str((grid_x, grid_y)), (pos_x, pos_y))
                self._map_nodes[(grid_x, grid_y)] = node

        return list(self._map_nodes.values())

    def generate_edges(self) -> List[MapEdge]:
        edges = []

        _1: MapNode
        for position, _1 in self._map_nodes.items():
            pos_x, pos_y = position[0], position[1]

            pair_with: List[MapNode] = []
            if pos_x + 1 < self._size_x:
                peer_pos = (pos_x + 1, pos_y)

                if not randint(0, 100) > self._keep_edges:
                    pair_with.append(self._map_nodes[peer_pos])

            if pos_y + 1 < self._size_y:
                peer_pos = (pos_x, pos_y + 1)

                if not randint(0, 100) > self._keep_edges:
                    pair_with.append(self._map_nodes[peer_pos])

            _2: MapNode
            for _2 in pair_with:
                edges.append(MapEdge((_1, _2), 1))

        return edges

    def generate_defaults(self) -> Tuple[MapNode, MapNode]:
        from_node: MapNode = choice(list(self._map_nodes.values()))
        to_node: MapNode = choice(list(self._map_nodes.values()))

        if from_node.name == to_node.name:
            return self.generate_defaults()

        return from_node, to_node
