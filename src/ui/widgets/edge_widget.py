# -*- coding: utf-8 -*-

from typing import Any
from typing import Dict
from typing import Tuple

from kivy.properties import BooleanProperty
from kivy.properties import ColorProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

from models import PathEdge
from ui.behaviors.show_props import ShowProps
from ui.helpers import DrawingMath
from ui.helpers import TraitletSplitter
from ui.widgets.color_sets import BLUE_COLOR
from ui.widgets.color_sets import DEFAULT_COLOR
from ui.widgets.node_widget import NodeWidget


class EdgeWidget(Widget):

    _cost = StringProperty("")
    _cost_disabled = BooleanProperty(True)

    _color = ColorProperty(DEFAULT_COLOR)

    _x1 = NumericProperty()
    _y1 = NumericProperty()
    _x2 = NumericProperty()
    _y2 = NumericProperty()

    _points = ListProperty()
    _width = NumericProperty(1)

    # noinspection PyArgumentList
    def __init__(self, edge: PathEdge, widget: Widget,
                 node_pair: Tuple[NodeWidget, NodeWidget],
                 show_props: ShowProps, **__: Any) -> None:

        self._edge = edge
        self._widget = widget
        self._node_pair = node_pair

        self._cost = str(edge.cost)

        self._node_pair[0].bind(size=self.update_widget_position)
        self._node_pair[1].bind(size=self.update_widget_position)

        self._cost_disabled = not show_props.show_edge_costs

        show_props.bind(_show_edge_costs=self.update_show_edge_cost)

        edge.observe(self.on_is_final, "is_final")

        Widget.__init__(self, **__)

    def update_widget_position(self, _: Any=None, __: Any=None) -> None:
        node_1, node_2 = self._node_pair

        self._x1 = node_1._pos_x + node_1._size / 2
        self._y1 = node_1._pos_y + node_1._size / 2

        self._x2 = node_2._pos_x + node_2._size / 2
        self._y2 = node_2._pos_y + node_2._size / 2

        xn, yn = DrawingMath.cross_coordinates(  # ..
            self._x1, self._y1, self._x2, self._y2)

        xm, ym = DrawingMath.cross_coordinates(  # ..
            self._x2, self._y2, self._x1, self._y1)

        self._points = [xn, yn, xm, ym]

    def on_is_final(self, change: Dict[str, Any]) -> None:
        _, _, is_final = TraitletSplitter.split(change)
        self._color = BLUE_COLOR if is_final else DEFAULT_COLOR

    def update_show_edge_cost(self, _: Any, x: str) -> None:
        self._cost_disabled = not bool(x)
