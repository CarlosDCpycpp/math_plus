from important_nums import G


def speed(distance: int or float, time: int or float) -> int or float:
    return distance / time


def time(distance: int or float, speed: int or float) -> int or float:
    return distance / speed


def distance(speed: int or float, time: int or float) -> int or float:
    return speed * time


def force(mass: int or float, acceleration: int or float) -> int or float:
    return mass * acceleration


def weight(mass: int or float, gravity: int or float = G) -> int or float:
    return mass * gravity
