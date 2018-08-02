# -*- coding: utf-8 -*-

from typing import Any
from typing import Optional

from cyrusbus import Bus
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout

from context import Context
from ui.behaviors.display_behavior import DisplayBehavior
from ui.layout.layout_events import MAP_RESET_EVENT
from ui.layout.layout_events import SEARCH_LOADED_EVENT
from ui.layout.layout_events import SEARCH_RESET_EVENT


class PlayPanel(GridLayout, DisplayBehavior, EventDispatcher):
    _is_continuous = BooleanProperty(False)
    _is_running = BooleanProperty(False)
    _playback_speed = NumericProperty(10)

    def __init__(self, bus: Bus, context: Context, *_: Any, **__: Any) -> None:
        super().__init__(*_, **__)

        bus.subscribe(SEARCH_LOADED_EVENT, self.toggle_visibility_enabled)
        bus.subscribe(SEARCH_RESET_EVENT, self.restart_play)
        bus.subscribe(MAP_RESET_EVENT, self.restart_play)

        self._bus: Bus = bus
        self._context: Context = context
        self._clock: Optional[Clock] = None

    def toggle_visibility_enabled(self, *_: Any, **__: Any) -> None:
        self.display_enabled()

    def make_a_step(self, *_: Any, **__: Any) -> None:
        if not self._context.path_finder:
            raise RuntimeError("path_finder")

        if not self._context.path_finder.step():
            self._is_running = False
            self.display_disabled()

    def toggle_play(self, *_: Any, **__: Any) -> None:
        self._is_running = not self._is_running
        self.play_step()

    def play_step(self, *_: Any, **__: Any) -> None:
        self.make_a_step()

        if self._is_running:
            interval = 1.0 / float(self._playback_speed)
            self._clock = Clock.schedule_once(self.play_step, interval)

    def restart_play(self, *_: Any, **__: Any) -> None:
        self.display_uninitialized()

        self._is_continuous = False
        self._is_running = False
        self._playback_speed = 10

        if self._clock:
            self._clock.cancel()
            self._clock = None
