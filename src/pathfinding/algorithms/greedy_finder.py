# -*- coding: utf-8 -*-

from models import PathNode
from models import PathSpace
from pathfinding.path_finder import PathFinder


class GreedyFinder(PathFinder):
    AIR_DISTANCE_MULTIPLIER = 0.1

    def __init__(self, path_space: PathSpace) -> None:
        super().__init__(path_space)
        self.k = float(GreedyFinder.AIR_DISTANCE_MULTIPLIER)

    def calculate_cost(self, pair_from: PathNode, pair_to: PathNode) -> float:
        to_node = self._path_space.to_node
        air_distance_to = self.get_air_distance(pair_to, to_node)

        return float(self.k * air_distance_to)
