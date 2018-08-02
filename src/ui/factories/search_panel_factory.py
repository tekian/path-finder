# -*- coding: utf-8 -*-

from typing import Any

from ui.factories import AbstractWidgetFactory


class SearchPanelFactory(AbstractWidgetFactory):
    def create(self, **__: Any) -> Any:
        from ui.layout import SearchPanel
        return SearchPanel(self._bus, self._context, **__)
