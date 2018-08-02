# -*- coding: utf-8 -*-

from typing import Any
from typing import Dict
from typing import Tuple

from kivy.properties import BooleanProperty
from kivy.properties import ColorProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from models import PathNode
from ui.behaviors.show_props import ShowProps
from ui.helpers import TraitletSplitter
from ui.widgets.color_sets import BLUE_COLOR
from ui.widgets.color_sets import DEFAULT_COLOR
from ui.widgets.color_sets import GREEN_COLOR
from ui.widgets.color_sets import HIGHLIGHT_COLOR
from ui.widgets.color_sets import RED_COLOR
from ui.widgets.color_sets import SOFT_BLUE_COLOR
from ui.widgets.color_sets import TRANSPARENT_COLOR


class NodeWidget(Widget):
    _name = StringProperty("")
    _name_disabled = BooleanProperty(True)

    _cost = StringProperty("")
    _cost_disabled = BooleanProperty(True)

    _color = ColorProperty(DEFAULT_COLOR)
    _hl_color = ColorProperty(TRANSPARENT_COLOR)

    _pos_x = NumericProperty()
    _pos_y = NumericProperty()

    _size = NumericProperty(20)

    # noinspection PyArgumentList
    def __init__(self, node: PathNode, widget: Widget,
                 show_props: ShowProps, *_: Any, **__: Any) -> None:

        self._node: PathNode = node

        self._widget: Widget = widget
        self._widget.bind(size=self._update_widget_position)

        self._update_widget_position()  # first time

        self._name = str(node.name)

        self._name_disabled = not show_props.show_node_labels
        self._cost_disabled = not show_props.show_node_costs

        show_props.bind(_show_node_labels=self.update_show_node_label)
        show_props.bind(_show_node_costs=self.update_show_node_cost)

        node.observe(self.on_cost, "cost")
        node.observe(self.on_explored, "is_explored")
        node.observe(self.on_is_from, "is_from")
        node.observe(self.on_is_to, "is_to")
        node.observe(self.on_progress, "is_progress")
        node.observe(self.on_frontier, "is_frontier")
        node.observe(self.on_is_final, "is_final")

        super().__init__(*_, **__)

    def _update_widget_position(self, _: Any=None, __: Any=None) -> None:
        padding_x = self._widget.width * .07
        padding_y = self._widget.height * .05

        relative_x = self._node.position[0] * .93
        relative_y = self._node.position[1] * .95

        self._pos_x = padding_x + self._widget.width * relative_x
        self._pos_y = padding_y + self._widget.height * relative_y

    def on_cost(self, change: Dict[str, Any]) -> None:
        _, _, new_cost = TraitletSplitter.split(change)
        self._cost = str(round(new_cost, 2))

    def on_explored(self, change: Dict[str, Any]) -> None:
        parent, _, is_explored = TraitletSplitter.split(change)

        if is_explored:
            self._color = RED_COLOR
            return

        if not parent.has_finder_flags_set():
            self._color = DEFAULT_COLOR
            return

    def on_frontier(self, change: Dict[str, Any]) -> None:
        parent, _, is_frontier = TraitletSplitter.split(change)

        if is_frontier:
            self._color = GREEN_COLOR
            return

        if not parent.has_finder_flags_set():
            self._color = DEFAULT_COLOR

    def on_is_from(self, change: Dict[str, Any]) -> None:
        parent, _, is_from = TraitletSplitter.split(change)

        if parent.has_finder_flags_set():
            return

        if is_from:
            self._color = BLUE_COLOR
            return

        if not parent.is_to:
            self._color = DEFAULT_COLOR

    def on_is_to(self, change: Dict[str, Any]) -> None:
        parent, _, is_to = TraitletSplitter.split(change)

        if parent.has_finder_flags_set():
            return

        if is_to:
            self._color = BLUE_COLOR
            return

        if not parent.is_from:
            self._color = DEFAULT_COLOR

    def on_progress(self, change: Dict[str, Any]) -> None:
        _, _, is_in_progress = TraitletSplitter.split(change)

        if is_in_progress:
            self._hl_color = HIGHLIGHT_COLOR
            return

        self._hl_color = TRANSPARENT_COLOR

    def on_is_final(self, change: Dict[str, Any]) -> None:
        _, _, is_final = TraitletSplitter.split(change)

        if is_final:
            self._color = BLUE_COLOR
            self._hl_color = SOFT_BLUE_COLOR
            return

        self._color = DEFAULT_COLOR
        self._hl_color = TRANSPARENT_COLOR

    def update_show_node_label(self, _: Any, x: str) -> None:
        self._name_disabled = not bool(x)

    def update_show_node_cost(self, _: Any, x: str) -> None:
        self._cost_disabled = not bool(x)
