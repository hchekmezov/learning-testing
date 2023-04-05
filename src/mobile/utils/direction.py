from enum import Enum


class Direction(Enum):
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    UP = 'UP'
    DOWN = 'DOWN'
    VERTICAL = 'VERTICAL'
    HORIZONTAL = 'HORIZONTAL'
    VERTICAL_DOWN_FIRST = 'VERTICAL_DOWN_FIRST'
    HORIZONTAL_RIGHT_FIRST = 'HORIZONTAL_RIGHT_FIRST'
