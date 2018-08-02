# -*- coding: utf-8 -*-

from typing import Any

from ui.factories import AbstractWidgetFactory


class PlayPanelFactory(AbstractWidgetFactory):
    def create(self, **__: Any) -> Any:
        from ui.layout import PlayPanel
        return PlayPanel(self._bus, self._context, **__)
