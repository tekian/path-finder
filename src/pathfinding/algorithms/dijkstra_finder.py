# -*- coding: utf-8 -*-

from models import PathNode
from pathfinding.path_finder import PathFinder


class DijkstraFinder(PathFinder):
    def calculate_cost(self, pair_from: PathNode, pair_to: PathNode) -> float:
        traveling_cost = pair_from.get_cost_to_(pair_to)
        return float(pair_from.cost + traveling_cost)
