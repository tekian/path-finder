# -*- coding: utf-8 -*-

from os import environ

from cyrusbus import Bus
from kivy.app import App
from kivy.app import Builder
from kivy.config import Config
from kivy.factory import Factory

from context import Context
from ui import UiConfigManager
from ui import UiFactoryManager
from ui import UiPathFinder

environ['KIVY_GL_BACKEND'] = "glew"

ui_config_manager = UiConfigManager(Config)
ui_config_manager.setup()

ui_factory_manager = UiFactoryManager(Factory, Bus(), Context())
ui_factory_manager.setup()


class ApplicationUi(App):
    def build(self) -> App:
        self.title = "PathFinder"

        Builder.load_file('ui/ui_path_finder.kv')

        app = UiPathFinder()
        return app


ApplicationUi.run(ApplicationUi())
