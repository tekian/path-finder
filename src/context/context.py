# -*- coding: utf-8 -*-

from typing import Optional

from models import MapSpace
from models import PathSpace
from pathfinding import PathFinder
from ui.behaviors import ShowProps


class Context(object):
    def __init__(self) -> None:
        self._map_space: Optional[MapSpace] = None
        self._path_space: Optional[PathSpace] = None

        self._show_props: Optional[ShowProps] = None
        self._path_finder: Optional[PathFinder] = None

    @property
    def map_space(self) -> Optional[MapSpace]:
        return self._map_space

    @map_space.setter
    def map_space(self, value: MapSpace) -> None:
        self._map_space = value

    @property
    def path_space(self) -> Optional[PathSpace]:
        return self._path_space

    @path_space.setter
    def path_space(self, value: PathSpace) -> None:
        self._path_space = value

    @property
    def show_props(self) -> Optional[ShowProps]:
        return self._show_props

    @show_props.setter
    def show_props(self, value: ShowProps) -> None:
        self._show_props = value

    @property
    def path_finder(self) -> Optional[PathFinder]:
        return self._path_finder

    @path_finder.setter
    def path_finder(self, value: PathFinder) -> None:
        self._path_finder = value
