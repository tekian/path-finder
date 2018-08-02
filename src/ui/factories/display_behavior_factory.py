# -*- coding: utf-8 -*-

from typing import Any

from ui.factories import AbstractWidgetFactory


class DisplayBehaviorFactory(AbstractWidgetFactory):
    def create(self, **__: Any) -> Any:
        from ui.behaviors import DisplayBehavior
        return DisplayBehavior()
