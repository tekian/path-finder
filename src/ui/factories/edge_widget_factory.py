# -*- coding: utf-8 -*-

from typing import Any
from typing import Tuple

from kivy.uix.widget import Widget

from models import PathEdge
from ui.behaviors import ShowProps
from ui.factories import AbstractWidgetFactory
from ui.widgets import NodeWidget


class EdgeWidgetFactory(AbstractWidgetFactory):
    def create(self,
               edge: PathEdge,
               widget: Widget,
               pair: Tuple[NodeWidget, NodeWidget],
               show_props: ShowProps,
               **__: Any) -> Any:

        from ui.widgets import EdgeWidget
        return EdgeWidget(edge, widget, pair, show_props)
