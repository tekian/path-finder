# -*- coding: utf-8 -*-

from typing import Any
from typing import List
from typing import Tuple


class MapNode(object):
    def __init__(self, name: str, position: Tuple[float, float]) -> None:
        self._name = name
        self._position = position

        self._edges: List[Any] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def position(self) -> Tuple[float, float]:
        return self._position

    @property
    def edges(self) -> List[Any]:
        return self._edges

    def get_peers(self) -> List[Any]:
        return [edge.opposite_to(self) for edge in self._edges]

    def get_edge_to_(self, peer: Any) -> Any:
        for edge in self._edges:
            if edge.is_connecting(self, peer):
                return edge

        raise RuntimeError("get_edge_to_")

    def get_cost_to_(self, peer: Any) -> float:
        edge = self.get_edge_to_(peer)
        return float(edge.cost)
