# -*- coding: utf-8 -*-

from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty


class ShowProps(EventDispatcher):
    _show_node_labels = BooleanProperty(True)
    _show_node_costs = BooleanProperty(True)
    _show_edge_costs = BooleanProperty(True)

    @property
    def show_node_labels(self) -> bool:
        return self._show_node_labels

    @show_node_labels.setter
    def show_node_labels(self, value: bool) -> None:
        self._show_node_labels = value

    @property
    def show_node_costs(self) -> bool:
        return self._show_node_costs

    @show_node_costs.setter
    def show_node_costs(self, value: bool) -> None:
        self._show_node_costs = value

    @property
    def show_edge_costs(self) -> bool:
        return self._show_edge_costs

    @show_edge_costs.setter
    def show_edge_costs(self, value: bool) -> None:
        self._show_edge_costs = value
