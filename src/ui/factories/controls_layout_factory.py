# -*- coding: utf-8 -*-

from typing import Any

from ui.factories import AbstractWidgetFactory


class ControlsLayoutFactory(AbstractWidgetFactory):
    def create(self, **__: Any) -> Any:
        from ui.layout import ControlsLayout
        return ControlsLayout(**__)
