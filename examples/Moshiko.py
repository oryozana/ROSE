import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


def drive(world):
    obstacle = world.get(x, y)
    if obstacle == obstacles.PENGUIN:
        actions.PICKUP
