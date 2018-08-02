# -*- coding: utf-8 -*-

from models import PathNode
from pathfinding.path_finder import PathFinder


class BfsFinder(PathFinder):
    def calculate_cost(self, pair_from: PathNode, pair_to: PathNode) -> float:
        return float(pair_from.cost + 1)
