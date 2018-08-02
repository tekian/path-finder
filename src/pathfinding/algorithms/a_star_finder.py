# -*- coding: utf-8 -*-

from funcy import first

from models import PathNode
from models import PathSpace
from pathfinding.path_finder import PathFinder


class AStarFinder(PathFinder):
    def __init__(self, path_space: PathSpace) -> None:
        super().__init__(path_space)

        from_node = self._path_space.from_node
        peer_node = first(from_node.get_peers())

        connecting_edge = from_node.get_edge_to_(peer_node)
        delta = self.get_air_distance(from_node, peer_node)

        self.k = connecting_edge.cost * .5 / delta

    def calculate_cost(self, pair_from: PathNode, pair_to: PathNode) -> float:
        to_node = self._path_space.to_node

        air_distance_from = self.get_air_distance(pair_from, to_node)
        air_distance_to = self.get_air_distance(pair_to, to_node)

        air_distance_delta = self.k * (air_distance_to - air_distance_from)
        travel_cost = pair_from.get_cost_to_(pair_to)

        return float(pair_from.cost + travel_cost + air_distance_delta)
