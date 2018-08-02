# -*- coding: utf-8 -*-

from typing import Dict
from typing import Iterator

from models import PathNode


class PreviousDict(object):
    def __init__(self) -> None:
        self._store: Dict[PathNode, PathNode] = {}

    def __iter__(self) -> Iterator[PathNode]:
        return self._store.__iter__()

    def __setitem__(self, node: PathNode, previous: PathNode) -> None:
        self._store[node] = previous
        node.previous = previous
