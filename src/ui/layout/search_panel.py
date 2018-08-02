# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from cyrusbus import Bus
from funcy import first
from funcy import select_values
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

from context import Context
from models import PathNode
from pathfinding import PathFinder
from pathfinding.algorithms import AStarFinder
from pathfinding.algorithms import BfsFinder
from pathfinding.algorithms import DijkstraFinder
from pathfinding.algorithms import GreedyFinder
from ui.behaviors.display_behavior import DisplayBehavior
from ui.layout.layout_events import MAP_NODES_LOADED_EVENT
from ui.layout.layout_events import MAP_READY_EVENT
from ui.layout.layout_events import MAP_RESET_EVENT
from ui.layout.layout_events import SEARCH_LOADED_EVENT
from ui.layout.layout_events import SEARCH_RESET_EVENT


class SearchPanel(GridLayout, DisplayBehavior, EventDispatcher):

    _from_node = StringProperty()
    _from_node_list = ListProperty()

    _to_node = StringProperty()
    _to_node_list = ListProperty()

    _algorithm_toggle = BooleanProperty(True)
    _is_ready = BooleanProperty(False)

    def __init__(self, bus: Bus, context: Context, *_: Any, **__: Any) -> None:
        super().__init__(*_, **__)

        self.nodes: Dict[str, PathNode] = {}
        self.bus: Bus = bus
        self.context: Context = context

        self._initial_from: Optional[str] = None
        self._initial_to: Optional[str] = None

        bus.subscribe(MAP_NODES_LOADED_EVENT, self.preload_search_settings)
        bus.subscribe(MAP_READY_EVENT, self.display_enabled)
        bus.subscribe(MAP_RESET_EVENT, self.restart_search_settings)

    @staticmethod
    def set_new_unset_old(attr: str,
                          old_node: PathNode,
                          new_node: PathNode) -> None:

        if old_node is not None:
            setattr(old_node, attr, False)

        setattr(new_node, attr, True)

    def path_finder_factory(self, name: str) -> PathFinder:
        if not self.context.path_space:
            raise RuntimeError("path_space")

        if name == "a_star":
            return AStarFinder(self.context.path_space)

        if name == "greedy":
            return GreedyFinder(self.context.path_space)

        if name == "bfs":
            return BfsFinder(self.context.path_space)

        if name == "dijkstra":
            return DijkstraFinder(self.context.path_space)

        raise KeyError("Unsupported maps!")

    def set_from_node_list(self, nodes: List[PathNode]) -> None:
        self._from_node_list = nodes

    def set_to_node_list(self, nodes: List[PathNode]) -> None:
        self._to_node_list = nodes

    def reselect_from_node(self, *args: Any, **__: Any) -> None:
        if self.context.path_space is None or len(args) == 0:
            return  # Map cleaned or not yet exist

        new_node: PathNode = self.nodes[args[0]]
        old_node: PathNode = self.context.path_space.from_node

        self.set_new_unset_old("is_from", old_node, new_node)
        self.context.path_space.from_node = new_node

    def reselect_to_node(self, *args: Any, **__: Any) -> None:
        if self.context.path_space is None or len(args) == 0:
            return  # Map cleaned or not yet exist

        new_node: PathNode = self.nodes[args[0]]
        old_node: PathNode = self.context.path_space.to_node

        self.set_new_unset_old("is_to", old_node, new_node)
        self.context.path_space.to_node = new_node

    def preload_search_settings(self, *_: Any, **__: Any) -> None:
        if not self.context.map_space:
            raise RuntimeError("map_space")

        if not self.context.path_space:
            raise RuntimeError("path_space")

        for node in self.context.path_space.nodes:
            self.nodes[node.name] = node

        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.set_from_node_list,
                            self.nodes.keys()).result()

            executor.submit(self.set_to_node_list,
                            self.nodes.keys()).result()

        self._initial_from = str(self.context.map_space.from_node.name)
        self._initial_to = str(self.context.map_space.to_node.name)

        self._from_node = self._initial_from
        self._to_node = self._initial_to

    def load_search_settings(self, *_: Any, **kwargs: Any) -> None:
        self.display_disabled()

        active_func = lambda v: v == "down"
        name = first(select_values(active_func, kwargs))

        self.context.path_finder = self.path_finder_factory(name)
        self.bus.publish(SEARCH_LOADED_EVENT)

    def reset_search_settings(self, *_: Any, **__: Any) -> None:
        self.display_enabled()

        self._algorithm_toggle = not self._algorithm_toggle
        self._is_ready = False

        self.bus.publish(SEARCH_RESET_EVENT)

    def restart_search_settings(self, *_: Any, **__: Any) -> None:
        self.display_uninitialized()

        self._initial_from = None
        self._initial_to = None

        self._from_node = ""
        self._from_node_list = []

        self._to_node = ""
        self._to_node_list = []

        self._algorithm_toggle = not self._algorithm_toggle
        self._is_ready = False
