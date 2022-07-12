import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


def use(x, y, front, obstacle0, obstacle1, obstacle2, obstacle, use_action):

    if front == obstacle:
        return use_action
    if obstacle0 == obstacle:
        if x == 0:
            return actions.NONE
        if x == 1:
            return actions.LEFT
    if obstacle1 == obstacle:
        if x == 0:
            return actions.RIGHT
        if x == 1:
            return actions.NONE
        if x == 2:
            return actions.LEFT
    if obstacle2 == obstacle:
        if x == 1:
            return actions.RIGHT
        if x == 2:
            return actions.NONE


def drive(world):
    x = world.car.x
    y = world.car.y
    obstacle0 = world.get(0, y - 2)
    obstacle1 = world.get(1, y - 2)
    obstacle2 = world.get(2, y - 2)
    use(x, y, world.get((x, y - 1)), obstacle0, obstacle1, obstacle2, obstacles.PENGUIN, actions.PICKUP)
    # use(obstacles.WATER, actions.BRAKE)
    # use(obstacles.CRACK, actions.JUMP)
    return actions.NONE
