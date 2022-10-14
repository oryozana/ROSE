"""
NonRandom driver
"""

from examples.Tree import *
from rose.common import obstacles, actions  # NOQA

driver_name = "LI OR I"

clear = (obstacles.NONE, obstacles.PENGUIN)
notclear = (obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH)
obstacles_dict = {obstacles.NONE: 0,
                  obstacles.TRASH: -10,
                  obstacles.BIKE: -10,
                  obstacles.BARRIER: -10,
                  obstacles.CRACK: 5,
                  obstacles.WATER: 4,
                  obstacles.PENGUIN: 10}


class OBS:
    def __init__(self, x, y, world):
        self.x = x
        self.o = world.get((x, y))

        self.p = obstacles_dict[self.o]
        try:
            self.nextObs = obstacles_dict[world.get((x, y - 1))]
        except:
            self.nextObs = 0

    def set_points(self):
        points = self.p
        self.p = 0
        if self.o not in clear:
            self.p = -10
        if self.o in notclear and self.nextObs > 0:
            self.p = 0


def createTree(t, x, y, r, world, counter):
    if t is not None and counter < 6:
        if x == r + 2:
            rightroot = None
        else:
            rightroot = Tree(OBS(x + 1, y - 1, world))
            rightroot.value.set_points()
        if x == r:
            leftroot = None
        else:
            leftroot = Tree(OBS(x - 1, y - 1, world))
            leftroot.value.set_points()
        middleroot = Tree(OBS(x, y - 1, world))
        if counter == 0:
            value = OBS(x, y, world)
            t = Tree(value, leftroot, middleroot, rightroot)
        else:
            t.setAll(leftroot, middleroot, rightroot)
        createTree(t.left, x - 1, y - 1, r, world, counter + 1)
        createTree(t.middle, x, y - 1, r, world, counter + 1)
        createTree(t.right, x + 1, y - 1, r, world, counter + 1)
    return t


def max_path(t):
    if t is None:
        return 0
    if t.isleaf():
        return t.value.p
    return t.value.p + max(max_path(t.left), max_path(t.middle), max_path(t.right))


def best_path(t):
    left = max_path(t.left)
    middle = max_path(t.middle)
    right = max_path(t.right)
    if right <= middle >= left:
        return None  # to decide which action
    if middle < left > right:
        return actions.LEFT
    if middle < right > left:
        return actions.RIGHT


def leftOrRight(x, r):
    if x == r + 2:
        return actions.LEFT
    if x == r:
        return actions.RIGHT
    else:
        return actions.LEFT


def drive(world):
    x = world.car.x
    y = world.car.y
    r = 0
    if 3 <= x:
        r = 3
    t = Tree(0)
    t = createTree(t, x, y, r, world, 0)
    print("max:", max_path(t))
    if best_path(t) is not None:
        return best_path(t)
    obstacle = world.get((x, y - 1))
    if obstacle == obstacles.PENGUIN:
        return actions.PICKUP
    if obstacle == obstacles.WATER:
        return actions.BRAKE
    if obstacle == obstacles.CRACK:
        return actions.JUMP
    if obstacle != obstacles.NONE:
        return leftOrRight(x, r)
    return actions.NONE
