# -*- coding: utf-8 -*-

from typing import Any

from ui.factories import AbstractWidgetFactory


class MapPanelFactory(AbstractWidgetFactory):
    def create(self, **__: Any) -> Any:
        from ui.layout import MapPanel
        return MapPanel(self._bus, self._context, **__)
