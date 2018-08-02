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

        self._nodes_by_position: Dict[Tuple[int, int], MapNode] = {}

    def generate_nodes(self) -> List[MapNode]:
        size_x, size_y = self._grid_size

        for grid_x in list(range(size_x)):
            pos_x = float(grid_x) / size_x
            for grid_y in list(range(size_y)):
                pos_y = float(grid_y) / size_y
                node = MapNode(str((grid_x, grid_y)), (pos_x, pos_y))
                self._nodes_by_position[(grid_x, grid_y)] = node

        return list(self._nodes_by_position.values())

    def generate_edges(self) -> List[MapEdge]:
        edges = []
        size_x, size_y = self._grid_size

        node_1: MapNode
        for position, node_1 in self._nodes_by_position.items():
            pos_x, pos_y = position[0], position[1]

            pair_with: List[MapNode] = []
            if pos_x + 1 < size_x:
                peer_pos = (pos_x + 1, pos_y)

                if not randint(0, 100) > self._keep_edges:
                    pair_with.append(self._nodes_by_position[peer_pos])

            if pos_y + 1 < size_y:
                peer_pos = (pos_x, pos_y + 1)

                if not randint(0, 100) > self._keep_edges:
                    pair_with.append(self._nodes_by_position[peer_pos])

            node_2: MapNode
            for node_2 in pair_with:
                edges.append(MapEdge((node_1, node_2), 1))

        return edges

    def generate_defaults(self) -> Tuple[MapNode, MapNode]:
        from_node: MapNode = choice(list(self._nodes_by_position.values()))
        to_node: MapNode = choice(list(self._nodes_by_position.values()))

        if from_node.name == to_node.name:
            return self.generate_defaults()

        return from_node, to_node
