import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


# def use(x, y, front, obstacle0, obstacle1, obstacle2, obstacle, use_action):


def drive(world):
    x = world.car.x
    y = world.car.y
    obstacle = world.get((x, y - 1))
    if obstacle == obstacles.obstacles.PENGUIN:
        return actions.PICKUP
    return actions.NONE
    