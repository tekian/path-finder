# -*- coding: utf-8 -*-

from typing import Any

from cyrusbus import Bus
from kivy.event import EventDispatcher
from kivy.factory import Factory
from kivy.uix.scatterlayout import ScatterLayout

from context import Context
from ui.behaviors.show_props import ShowProps
from ui.layout.layout_events import MAP_LOAD_EVENT
from ui.layout.layout_events import MAP_NODES_LOADED_EVENT
from ui.layout.layout_events import MAP_READY_EVENT
from ui.layout.layout_events import MAP_RESET_EVENT


class PlotLayout(ScatterLayout, EventDispatcher):
    def __init__(self, bus: Bus, context: Context, *_: Any, **__: Any) -> None:
        super().__init__(*_, **__)

        bus.subscribe(MAP_LOAD_EVENT, self.draw_initial_map)
        bus.subscribe(MAP_RESET_EVENT, self.clear_all_widgets)

        self.bus: Bus = bus
        self.context: Context = context

    def draw_initial_map(self, *_: Any, **__: Any) -> None:
        if not self.context.show_props:
            raise RuntimeError("show_props")

        if not self.context.path_space:
            raise RuntimeError("path_space")

        show_props: ShowProps = self.context.show_props
        node_plots = {}

        for node in self.context.path_space.nodes:
            node_plot = Factory.NodeWidget(node, self, show_props)
            node_plots[node.name] = node_plot
            self.add_widget(node_plot)

        self.bus.publish(MAP_NODES_LOADED_EVENT)

        for edge in self.context.path_space.edges:
            _1_node, _2_node = edge.pair
            _1 = node_plots[_1_node.name]
            _2 = node_plots[_2_node.name]

            w = Factory.EdgeWidget(edge, self, (_1, _2), show_props)
            self.add_widget(w)

        self.bus.publish(MAP_READY_EVENT)

    def clear_all_widgets(self, *_: Any, **__: Any) -> None:
        self.clear_widgets()
