# -*- coding: utf-8 -*-

from typing import Any

from kivy.properties import ColorProperty
from kivy.properties import NumericProperty
from kivy.properties import StringProperty


class Border(object):
    ENABLED = "ui/static/panel-border-enabled.png"
    DISABLED = "ui/static/panel-border-disabled.png"


class Display(object):
    UNINITIALIZED = 0
    DISABLED = 1
    ENABLED = 2


class DisplayBehavior(object):
    _background_color = ColorProperty([.10, .10, .10, 1])
    _display_state = NumericProperty(Display.UNINITIALIZED)
    _panel_border = StringProperty(Border.DISABLED)

    def display_uninitialized(self, *_: Any, **__: Any) -> None:
        self._background_color = [.10, .10, .10, 1]
        self._display_state = Display.UNINITIALIZED
        self._panel_border = Border.DISABLED

    def display_disabled(self, *_: Any, **__: Any) -> None:
        self._background_color = [.15, .15, .15, 1]
        self._display_state = Display.DISABLED
        self._panel_border = Border.DISABLED

    def display_enabled(self, *_: Any, **__: Any) -> None:
        self._background_color = [.20, .20, .20, 1]
        self._display_state = Display.ENABLED
        self._panel_border = Border.ENABLED
