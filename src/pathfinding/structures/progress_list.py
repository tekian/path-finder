# -*- coding: utf-8 -*-

from typing import List
from typing import Tuple

from models import PathNode


class ProgressList(object):
    def __init__(self) -> None:
        self._store: List[Tuple[PathNode, PathNode]] = []

    def is_empty(self) -> bool:
        return bool(self._store.__len__() == 0)

    def append(self, node: PathNode, previous: PathNode) -> None:
        self._store.append((node, previous))
        previous.is_progress = True

    def pop(self) -> Tuple[PathNode, PathNode]:
        node, previous = self._store.pop()
        previous.is_progress = False
        return node, previous
