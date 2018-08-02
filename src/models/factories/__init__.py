# -*- coding: utf-8 -*-

from models import MapEdge
from models import MapNode
from models import MapSpace

from models import PathNode
from models import PathEdge
from models import PathSpace

from .abstract_space_factory import AbstractSpaceFactory

MapSpaceFactoryType = AbstractSpaceFactory[MapSpace, MapNode, MapEdge]
PathSpaceFactoryType = AbstractSpaceFactory[PathSpace, PathNode, PathEdge]

from .grid_map_space_factory import GridMapSpaceFactory
from .file_spring_map_space_factory import FileSpringMapSpaceFactory
from .path_space_factory import PathSpaceFactory
