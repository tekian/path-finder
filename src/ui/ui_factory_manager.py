# -*- coding: utf-8 -*-

from typing import Any

from cyrusbus import Bus
from kivy.factory import Factory

from ui.factories import ControlsLayoutFactory
from ui.factories import DisplayBehaviorFactory
from ui.factories import EdgeWidgetFactory
from ui.factories import MapPanelFactory
from ui.factories import NodeWidgetFactory
from ui.factories import PlayPanelFactory
from ui.factories import PlotLayoutFactory
from ui.factories import SearchPanelFactory


class UiFactoryManager(object):
    def __init__(self, factory: Factory, bus: Bus, context: Any) -> None:
        self._factory = factory
        self._bus = bus
        self._context = context

    def setup(self) -> None:
        _1 = PlayPanelFactory(self._bus, self._context)
        self._factory.register('PlayPanel', _1.create)

        _2 = SearchPanelFactory(self._bus, self._context)
        self._factory.register('SearchPanel', _2.create)

        _3 = DisplayBehaviorFactory(self._bus, self._context)
        self._factory.register('VisibilityBehavior', _3.create)

        _4 = NodeWidgetFactory(self._bus, self._context)
        self._factory.register('NodeWidget', _4.create)

        _5 = EdgeWidgetFactory(self._bus, self._context)
        self._factory.register('EdgeWidget', _5.create)

        _6 = PlotLayoutFactory(self._bus, self._context)
        self._factory.register('PlotLayout', _6.create)

        _7 = ControlsLayoutFactory(self._bus, self._context)
        self._factory.register('ControlsLayout', _7.create)

        _8 = MapPanelFactory(self._bus, self._context)
        self._factory.register('MapPanel', _8.create)
