# -*- coding: utf-8 -*-

from typing import Iterator
from typing import List

from models import PathNode


class ExploredList(object):
    def __init__(self) -> None:
        self._store: List[PathNode] = []

    def __iter__(self) -> Iterator[PathNode]:
        return self._store.__iter__()

    def append(self, node: PathNode) -> None:
        self._store.append(node)
        node.is_explored = True
