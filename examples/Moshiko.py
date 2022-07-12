import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


# def use(x, y, front, obstacle0, obstacle1, obstacle2, obstacle, use_action):


def drive(world):
    x = world.car.x
    y = world.car.y
    obstacle0 = world.get((0, y - 2))
    obstacle1 = world.get((1, y - 2))
    obstacle2 = world.get((2, y - 2))
    front = world.get((x, y - 1))
    if front == obstacles.PENGUIN or obstacles.WATER or obstacles.CRACK:
        if front == obstacles.PENGUIN:
            return actions.PICKUP
        if front == obstacles.WATER:
            return actions.BRAKE
        if front == obstacles.CRACK:
            return actions.JUMP
    if obstacle0 == obstacles.PENGUIN or obstacles.WATER or obstacles.CRACK:
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

    if world.get((x, y - 1)) == obstacles.WATER:
        return actions.BRAKE
    if obstacle0 == obstacles.WATER:
        if x == 0:
            return actions.NONE
        if x == 1:
            return actions.LEFT
    if obstacle1 == obstacles.WATER:
        if x == 0:
            return actions.RIGHT
        if x == 1:
            return actions.NONE
        if x == 2:
            return actions.LEFT
    if obstacle2 == obstacles.WATER:
        if x == 1:
            return actions.RIGHT
        if x == 2:
            return actions.NONE

    if world.get((x, y - 1)) == obstacles.CRACK:
        return actions.JUMP
    if obstacle0 == obstacles.CRACK:
        if x == 0:
            return actions.NONE
        if x == 1:
            return actions.LEFT
    if obstacle1 == obstacles.CRACK:
        if x == 0:
            return actions.RIGHT
        if x == 1:
            return actions.NONE
        if x == 2:
            return actions.LEFT
    if obstacle2 == obstacles.CRACK:
        if x == 1:
            return actions.RIGHT
        if x == 2:
            return actions.NONE
    if world.get((x, y - 1)) == obstacles.TRASH or obstacles.BARRIER or obstacles.BIKE:
        if x == 0:
            return actions.RIGHT
        if x == 1:
            return actions.LEFT
        if x == 2:
            return actions.LEFT

    if x == 0:
        return actions.RIGHT
    if x == 2:
        return actions.LEFT
    return actions.NONE