#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional
from typing import Tuple


class DrawingMath(object):
    @staticmethod
    def calculate_slope(x_1: float, y_1: float,
                        x_2: float, y_2: float) -> Optional[float]:

        if (x_2 - x_1) == 0:
            return None

        return (y_2 - y_1) / (x_2 - x_1)

    @staticmethod
    def evaluate_square_side(x_1: float, y_1: float,
                             x_2: float, y_2: float) -> str:

        slope = DrawingMath.calculate_slope(x_1, y_1, x_2, y_2)

        if slope is not None:
            if ((0 <= slope < 1) or (-1 < slope <= 0)) and x_2 >= x_1:
                return 'E'

            if ((0 <= slope < 1) or (-1 < slope <= 0)) and x_2 < x_1:
                return 'W'

        if (slope is None or (slope > 1 or slope < -1)) and y_2 >= y_1:
            return 'N'

        if (slope is None or (slope > 1 or slope < -1)) and y_2 < y_1:
            return 'S'

        raise RuntimeError("Error in calculations")

    @staticmethod
    def cross_coordinates(x_1: float, y_1: float,
                          x_2: float, y_2: float,
                          width: int=20) -> Tuple[float, float]:

        slope = DrawingMath.calculate_slope(x_1, y_1, x_2, y_2)
        side = DrawingMath.evaluate_square_side(x_1, y_1, x_2, y_2)

        if slope is None:
            if side == 'N':
                return x_1, y_1 + width

            if side == 'S':
                return x_1, y_1 - width

            raise Exception("m == None and side != {'N', 'S'}")

        delta = y_1 - slope * x_1

        if side == 'N':
            return (y_1 + width - delta) / slope, y_1 + width

        if side == 'S':
            return (y_1 - width - delta) / slope, y_1 - width

        if side == 'E':
            return x_1 + width, slope * (x_1 + width) + delta

        if side == 'W':
            return x_1 - width, slope * (x_1 - width) + delta

        raise Exception("Side does not match {'N', 'S', 'E', 'W'}")
