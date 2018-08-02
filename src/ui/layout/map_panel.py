# -*- coding: utf-8 -*-

import json
from typing import Any
from typing import Dict

from cyrusbus import Bus
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

from context import Context
from models import MapSpace
from models import PathSpace
from models.factories import FileSpringMapSpaceFactory
from models.factories import GridMapSpaceFactory
from models.factories import PathSpaceFactory
from ui.behaviors.display_behavior import DisplayBehavior
from ui.behaviors.show_props import ShowProps
from ui.layout.layout_events import MAP_LOAD_EVENT
from ui.layout.layout_events import MAP_RESET_EVENT
from ui.layout.layout_events import SEARCH_RESET_EVENT


class MapPanel(GridLayout, DisplayBehavior, EventDispatcher):
    _grid_x_size = StringProperty()
    _grid_y_size = StringProperty()

    _grid_edges_keep = StringProperty()

    _json_distortion_level = StringProperty()
    _json_map_path = StringProperty()

    _show_node_labels = BooleanProperty()
    _show_node_costs = BooleanProperty()
    _show_edge_costs = BooleanProperty()

    # noinspection PyArgumentList
    def __init__(self, bus: Bus, context: Context, *_: Any, **__: Any) -> None:
        super().__init__(*_, **__)

        self._bus = bus
        self._context = context

        self._grid_x_size = "12"
        self._grid_y_size = "12"
        self._grid_edges_keep = "100"

        self._json_distortion_level = "46"
        self._json_map_path = "romania.json"

        self._context.show_props = ShowProps()

        self._show_node_labels = self._context.show_props.show_node_labels
        self._show_node_costs = self._context.show_props.show_node_costs
        self._show_edge_costs = self._context.show_props.show_edge_costs

        self.bind(_show_node_labels=self.update_show_node_labels)
        self.bind(_show_node_costs=self.update_show_node_costs)
        self.bind(_show_edge_costs=self.update_show_edge_costs)

        bus.subscribe(SEARCH_RESET_EVENT, self.reload_path_nodes_properties)

        self.display_enabled()

    def _create_map_system(self, map_name: str) -> MapSpace:
        if map_name == "Grid Map":
            position = (int(self._grid_x_size), int(self._grid_y_size))
            edges_keep = int(self._grid_edges_keep)

            _1 = GridMapSpaceFactory(position, edges_keep)
            return _1.create(MapSpace)

        if map_name == "File Spring Map":
            json_content = json.loads(open(self._json_map_path).read())
            distortion_level = int(self._json_distortion_level)

            _2 = FileSpringMapSpaceFactory(json_content, distortion_level)
            return _2.create(MapSpace)

        raise NotImplementedError(map_name)

    def _create_path_system(self) -> PathSpace:
        if not self._context.map_space:
            raise RuntimeError("map_space")

        path_system_creator = PathSpaceFactory(self._context.map_space)
        return path_system_creator.create(PathSpace)

    def update_show_node_labels(self, _: Any, value: str) -> None:
        if not self._context.show_props:
            raise RuntimeError("show_props")

        self._context.show_props.show_node_labels = bool(value)

    def update_show_node_costs(self, _: Any, value: str) -> None:
        if not self._context.show_props:
            raise RuntimeError("show_props")

        self._context.show_props.show_node_costs = bool(value)

    def update_show_edge_costs(self, _: Any, value: str) -> None:
        if not self._context.show_props:
            raise RuntimeError("show_props")

        self._context.show_props.show_edge_costs = bool(value)

    def load_map(self, *_: Any, **kwargs: Any) -> None:
        self.display_disabled()
        self._context.map_space = self._create_map_system(kwargs["map_name"])
        self._context.path_space = self._create_path_system()
        self._bus.publish(MAP_LOAD_EVENT)

    def reload_path_nodes_properties(self, *_: Any, **__: Any) -> None:
        for node in self._context.path_space.nodes:  # type: ignore
            node.reset_properties()

        for edge in self._context.path_space.edges:  # type: ignore
            edge.reset_properties()

    def reset_map(self, *_: Any, **__: Any) -> None:
        self.display_enabled()

        self._context.map_space = None
        self._context.path_space = None

        self._bus.publish(MAP_RESET_EVENT)
