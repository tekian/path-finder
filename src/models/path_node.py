# -*- coding: utf-8 -*-

from typing import Any
from typing import Optional

from traitlets import Bool
from traitlets import Float
from traitlets import HasTraits

from models import MapNode


class PathNode(MapNode, HasTraits):
    is_explored = Bool(False)
    is_frontier = Bool(False)
    is_progress = Bool(False)

    is_final = Bool(False)

    cost = Float(.0)

    is_from = Bool(False)
    is_to = Bool(False)

    def __init__(self, map_node: MapNode) -> None:
        super().__init__(map_node.name, map_node.position)

        self._previous: Optional[PathNode] = None

    def reset_properties(self) -> None:
        self.is_explored = False
        self.is_frontier = False
        self.is_progress = False
        self.is_final = False

        self.cost = .0

        was_is_from = self.is_from
        self.is_from = not self.is_from
        self.is_from = was_is_from

        was_is_to = self.is_to
        self.is_to = not self.is_to
        self.is_to = was_is_to

    def has_finder_flags_set(self) -> bool:
        return bool(self.is_explored) or bool(self.is_frontier)

    @property
    def previous(self) -> Any:
        return self._previous

    @previous.setter
    def previous(self, value: Any) -> None:
        self._previous = value

    def get_edge_to_previous(self) -> Any:
        for edge in self.edges:
            if edge.is_connecting(self, self.previous):
                return edge

        raise RuntimeError("get_edge_to_previous")
