# -*- coding: utf-8 -*-

from typing import Any
from typing import Tuple

from traitlets import Bool
from traitlets import HasTraits

from models import MapEdge


class PathEdge(MapEdge, HasTraits):
    is_final = Bool(False)

    def __init__(self, map_edge: MapEdge, pair: Tuple[Any, Any]) -> None:
        super().__init__(pair, map_edge.cost)

    def reset_properties(self) -> None:
        self.is_final = False
