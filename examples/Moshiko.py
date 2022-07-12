import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


def drive(world):
    x = world.car.x
    y = world.car.y
    obstacle0 = world.get((0, y - 2))
    obstacle1 = world.get((1, y - 2))
    obstacle2 = world.get((2, y - 2))
    if world.get((x, y - 1)) == obstacles.PENGUIN:
        return actions.PICKUP
    if obstacle0 == obstacles.PENGUIN:
        if x == 0:
            return actions.NONE
        if x == 1:
            return actions.LEFT
    if obstacle1 == obstacles.PENGUIN:
        if x == 0:
            return actions.RIGHT
        if x == 1:
            return actions.NONE
        if x == 2:
            return actions.LEFT
    if obstacle2 == obstacles.PENGUIN:
        if x == 1:
            return actions.RIGHT
        if x == 2:
            return actions.NONE
