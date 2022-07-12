import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


def drive(world):
    x = world.car.x
    y = world.car.y
    obstacle = world.get(x, y)
    if obstacle == obstacles.PENGUIN:
        return actions.PICKUP
