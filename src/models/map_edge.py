# -*- coding: utf-8 -*-

from typing import Any
from typing import Tuple


class MapEdge(object):
    def __init__(self, pair: Tuple[Any, Any], cost: float) -> None:
        super().__init__()

        self._node_one, self._node_two = pair
        self._cost = cost

    @property
    def pair(self) -> Tuple[Any, Any]:
        return self._node_one, self._node_two

    @property
    def cost(self) -> float:
        return self._cost

    def opposite_to(self, node: Any) -> Any:
        if node is self._node_one:
            return self._node_two

        if node is self._node_two:
            return self._node_one

        raise RuntimeError("opposite_to")

    def is_connecting(self, pair_from: Any, pair_to: Any) -> bool:
        if self._node_one is pair_from and self._node_two is pair_to:
            return True

        if self._node_two is pair_from and self._node_one is pair_to:
            return True

        return False
