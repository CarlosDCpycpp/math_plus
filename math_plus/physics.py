import typing as _t

from .const import G as _G


def speed(distance: int or float, time: int or float) -> int or float:
    """Calculates the speed.
    Takes distance and time as arguments."""
    return distance / time


def time(distance: int or float, speed: int or float) -> int or float:
    """Calculates the time.
    Takes distance and speed as arguments."""
    return distance / speed


def distance(speed: _t.Union[int, float], time: _t.Union[int, float]) -> _t.Union[int, float]:
    """Calculates the distance.
    Takes speed and time as arguments."""
    return speed * time


def force(mass: _t.Union[int, float], acceleration: _t.Union[int, float]) -> _t.Union[int, float]:
    """Calculates the force.
    Takes mass and acceleration as arguments."""
    return mass * acceleration


def weight(mass: _t.Union[int, float], gravity: _t.Union[int, float] = _G) -> _t.Union[int, float]:
    """Calculates the weight.
    Takes mass and gravity as arguments.
    (gravity is, by default, 9.8, however can be altered by being passed as an argument.)"""
    return mass * gravity


def space_travelled(starting_pos: _t.Union[int, float], ending_pos: _t.Union[int, float]) -> _t.Union[int, float]:
    """Calculates the space travelled.
    Takes the starting position and ending position as arguments."""
    return abs(starting_pos - ending_pos)
