import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


def use(world, obstacle, use_action, x, y):
    obstacle0 = world.get((0, y - 2))
    obstacle1 = world.get((1, y - 2))
    obstacle2 = world.get((2, y - 2))
    if world.get((x, y - 1)) == obstacle:
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
    self.use(world, obstacles.PENGUIN, actions.PICKUP, world.car.x, world.car.y)
    # use(obstacles.WATER, actions.BRAKE)
    # use(obstacles.CRACK, actions.JUMP)
    return actions.NONE
