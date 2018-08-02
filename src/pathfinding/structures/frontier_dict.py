# -*- coding: utf-8 -*-

from typing import Tuple

from heapdict import heapdict

from models import PathNode


class FrontierDict(object):
    def __init__(self) -> None:
        self._store: heapdict = heapdict()

    def __getitem__(self, node: PathNode) -> PathNode:
        return self._store[node]

    def __setitem__(self, node: PathNode, cost: float) -> None:
        self._store[node] = cost
        node.is_frontier = True
        node.cost = cost

    def is_empty(self) -> bool:
        return bool(self._store.__len__() == 0)

    def popitem(self) -> Tuple[PathNode, float]:
        node, cost = self._store.popitem()
        node.is_frontier = False

        return node, cost
