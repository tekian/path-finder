# -*- coding: utf-8 -*-

from abc import ABC
from typing import Generic
from typing import List
from typing import TypeVar

from models import MapEdge
from models import MapNode

TNode = TypeVar("TNode", bound=MapNode)
TEdge = TypeVar("TEdge", bound=MapEdge)


class AbstractSpace(ABC, Generic[TNode, TEdge]):
    def __init__(self, nodes: List[TNode], edges: List[TEdge],
                 from_node: TNode, to_node: TNode) -> None:

        self._nodes = nodes
        self._edges = edges

        self._from_node = from_node
        self._to_node = to_node

    @property
    def nodes(self) -> List[TNode]:
        return self._nodes

    @property
    def edges(self) -> List[TEdge]:
        return self._edges

    @property
    def from_node(self) -> TNode:
        return self._from_node

    @from_node.setter
    def from_node(self, value: TNode) -> None:
        self._from_node = value

    @property
    def to_node(self) -> TNode:
        return self._to_node

    @to_node.setter
    def to_node(self, value: TNode) -> None:
        self._to_node = value
