# -*- coding: utf-8 -*-

from .map_edge import MapEdge
from .map_node import MapNode

from .path_edge import PathEdge
from .path_node import PathNode

from .abstract_space import AbstractSpace

MapSpace = AbstractSpace[MapNode, MapEdge]
PathSpace = AbstractSpace[PathNode, PathEdge]
