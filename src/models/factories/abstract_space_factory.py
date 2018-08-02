# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from typing import Callable
from typing import Generic
from typing import List
from typing import Tuple
from typing import TypeVar

from models import AbstractSpace
from models import MapEdge
from models import MapNode

TSpace = TypeVar("TSpace", bound=AbstractSpace)
TNode = TypeVar("TNode", bound=MapNode)
TEdge = TypeVar("TEdge", bound=MapEdge)


class AbstractSpaceFactory(ABC, Generic[TSpace, TNode, TEdge]):
    @abstractmethod
    def generate_nodes(self) -> List[TNode]:
        raise NotImplementedError("generate_nodes")

    @abstractmethod
    def generate_edges(self) -> List[TEdge]:
        raise NotImplementedError("generate_edges")

    @abstractmethod
    def generate_defaults(self) -> Tuple[TNode, TNode]:
        raise NotImplementedError("generate_defaults")

    def create(self, type_: Callable[..., TSpace]) -> TSpace:
        nodes: List[TNode] = self.generate_nodes()
        edges: List[TEdge] = self.generate_edges()

        defaults = self.generate_defaults()
        from_node, to_node = defaults

        for edge in edges:
            node, peer = edge.pair
            node.edges.append(edge)  # add edge to node
            peer.edges.append(edge)  # add edge to peer

        return type_(nodes, edges, from_node, to_node)
