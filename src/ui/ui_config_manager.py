# -*- coding: utf-8 -*-

from kivy import Config

WINDOW_SIZE_X = 1280
WINDOW_SIZE_Y = 780


class UiConfigManager(object):
    def __init__(self, config: Config) -> None:
        self._config = config

    def setup(self) -> None:
        self._config.set('graphics', 'minimum_width', str(WINDOW_SIZE_X))
        self._config.set('graphics', 'minimum_height', str(WINDOW_SIZE_Y))

        self._config.set('graphics', 'width', str(WINDOW_SIZE_X))
        self._config.set('graphics', 'height', str(WINDOW_SIZE_Y))

        self._config.set('kivy', 'log_enable', "1")
        self._config.set('kivy', 'log_level', "warning")

        self._config.set('kivy', 'window_icon', 'ui/static/application.ico')

        self._config.set('kivy', 'default_font', [
            'AveriaSansLibre',
            'ui/static/fonts/AveriaSansLibre-Regular.ttf',
            'ui/static/fonts/AveriaSansLibre-Italic.ttf',
            'ui/static/fonts/AveriaSansLibre-Bold.ttf',
            'ui/static/fonts/AveriaSansLibre-BoldItalic.ttf',
        ])

        Config.write()
