"""
NonRandom driver
"""

import random
from Tree import *
from rose.common import obstacles, actions  # NOQA

driver_name = "LI OR I"

side_obstacles = (obstacles.WATER, obstacles.CRACK)
obstacles_dict = {obstacles.NONE: 0,
                  obstacles.TRASH: -10,
                  obstacles.BIKE: -10,
                  obstacles.BARRIER: -10,
                  obstacles.CRACK: 5,
                  obstacles.WATER: 4,
                  obstacles.PENGUIN: 10}


class OBS:
    def _init_(self, x, y, world):
        self.x = x
        self.o = world.get((x, y))
        self.p = obstacles_dict[self.o]

    def set_points(self):
        self.p = 0
        if self.o in side_obstacles:
            self.p = -10

    def finish_line(self, counter):
        if Tree.steps - counter < 0:
            self.p = 0


def buildTree(t, x, y, r, world, counter):
    if t is not None and counter < 6:
        if x == r + 2:
            rightroot = None
        else:
            rightroot = Tree(OBS(x + 1, y - 1, world))
            rightroot.value.set_points()
            rightroot.value.finish_line(counter)
        if x == r:
            leftroot = None
        else:
            leftroot = Tree(OBS(x - 1, y - 1, world))
            leftroot.value.set_points()
            leftroot.value.finish_line(counter)
        middleroot = Tree(OBS(x, y - 1, world))
        middleroot.value.finish_line(counter)
        if counter == 0:
            value = OBS(x, y, world)
            t = Tree(value, leftroot, middleroot, rightroot)
        else:
            t.setAll(leftroot, middleroot, rightroot)
        buildTree(t.left, x - 1, y - 1, r, world, counter + 1)
        buildTree(t.middle, x, y - 1, r, world, counter + 1)
        buildTree(t.right, x + 1, y - 1, r, world, counter + 1)
    return t


def max_path(t):
    if t is None:
        return -100
    if t.isleaf():
        return t.value.p
    return t.value.p + max(max_path(t.left), max_path(t.middle), max_path(t.right))


def best_path(t):
    left = max_path(t.left)
    middle = max_path(t.middle)
    right = max_path(t.right)
    if left < right > middle:
        return actions.RIGHT
    if middle < left > right:
        return actions.LEFT
    if right == left > middle:
        return random.choice([actions.LEFT, actions.RIGHT])
    return None   # to decide which action


def leftOrRight(x, r):
    if x == r + 2:
        return actions.LEFT
    if x == r:
        return actions.RIGHT
    return random.choice([actions.LEFT, actions.RIGHT])


def drive(world):
    if Tree.steps == 0:
        Tree.steps = 60
    Tree.steps -= 1
    print(Tree.steps)
    x = world.car.x
    y = world.car.y
    r = 0
    if 3 <= x:
        r = 3
    t = Tree(0)
    t = buildTree(t, x, y, r, world, 0)
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