# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from math import hypot
from typing import Any
from typing import List

from models import PathNode
from models import PathSpace
from pathfinding.structures import ExploredList
from pathfinding.structures import FrontierDict
from pathfinding.structures import PreviousDict
from pathfinding.structures import ProgressList


class PathFinder(ABC):
    def __init__(self, path_space: PathSpace) -> None:
        self._path_space: PathSpace = path_space

        self._frontier = FrontierDict()
        self._explored = ExploredList()
        self._progress = ProgressList()
        self._previous = PreviousDict()

        self._is_finished = False

    def _get_non_explored_peers(self, node: PathNode) -> List[PathNode]:
        return [p for p in node.get_peers() if p not in self._explored]

    def step(self, *_: Any, **__: Any) -> bool:
        if self._is_finished:
            return False

        if not self._progress.is_empty():
            self.handle_in_progress_node()
            return True

        if self._frontier.is_empty():
            self.handle_initial_state()
            return True

        node, ___ = self._frontier.popitem()
        self._explored.append(node)

        if node == self._path_space.to_node:
            self._is_finished = True
            self.highlight(node)
            return False

        for previous in self._get_non_explored_peers(node):
            self._progress.append(node, previous)

        return True

    def highlight(self, node: PathNode) -> None:
        node.is_final = True

        if node != self._path_space.from_node:
            previous_edge = node.get_edge_to_previous()
            previous_edge.is_final = True

            self.highlight(node.previous)

    def handle_in_progress_node(self) -> None:
        node, previous = self._progress.pop()

        new_cost = self.calculate_cost(node, previous)
        new_cost_is_better = previous.cost > new_cost

        previous_not_set = previous not in self._previous

        if previous_not_set or new_cost_is_better:
            self._frontier[previous] = new_cost
            self._previous[previous] = node

    def handle_initial_state(self) -> None:
        self._frontier[self._path_space.from_node] = 0

    @staticmethod
    def get_air_distance(node_1: PathNode, node_2: PathNode) -> float:
        x_1, y_1 = node_1.position
        x_2, y_2 = node_2.position

        return round(hypot(x_2 - x_1, y_2 - y_1), 2)

    @abstractmethod
    def calculate_cost(self, pair_from: PathNode, pair_to: PathNode) -> float:
        raise NotImplementedError("calculate_cost")
