# -*- coding: utf-8 -*-

from typing import Any

from ui.factories import AbstractWidgetFactory


class PlotLayoutFactory(AbstractWidgetFactory):
    def create(self, **__: Any) -> Any:
        from ui.layout import PlotLayout
        return PlotLayout(self._bus, self._context, **__)
