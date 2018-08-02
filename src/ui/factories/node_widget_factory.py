# -*- coding: utf-8 -*-

from typing import Any

from kivy.uix.widget import Widget

from models import PathNode
from ui.behaviors import ShowProps
from ui.factories import AbstractWidgetFactory


class NodeWidgetFactory(AbstractWidgetFactory):
    def create(self,
               node: PathNode,
               widget: Widget,
               show_props: ShowProps,
               **__: Any) -> Any:

        from ui.widgets import NodeWidget
        return NodeWidget(node, widget, show_props, **__)
