# -*- coding: utf-8 -*-

from abc import ABC
from abc import abstractmethod
from typing import Any

from cyrusbus import Bus


class AbstractWidgetFactory(ABC):
    def __init__(self, bus: Bus, context: Any) -> None:
        self._bus = bus
        self._context = context
