"""
NonRandom driver
"""

import random
from typing import Union
from TernaryTree import *
from TempObstacle import *
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


def build_tree(tree: Union["TernaryTree", None], x: int, y: int, road: int, world, current_tree_level: int):
    if tree is not None and current_tree_level < 6:
        if x == road + 2:
            right_root = None
        else:
            right_root = TernaryTree(TempObstacle(x + 1, y - 1, world))
            right_root.value.set_points()
            right_root.value.finish_line(current_tree_level)

        if x == road + 0:
            left_root = None
        else:
            left_root = TernaryTree(TempObstacle(x - 1, y - 1, world))
            left_root.value.set_points()
            left_root.value.finish_line(current_tree_level)

        middle_root = TernaryTree(TempObstacle(x, y - 1, world))
        middle_root.value.finish_line(current_tree_level)

        if current_tree_level == 0:
            value = TempObstacle(x, y, world)
            tree = TernaryTree(value, left_root, middle_root, right_root)
        else:
            tree.set_children(left_root, middle_root, right_root)

        build_tree(tree.left, x - 1, y - 1, road, world, current_tree_level + 1)
        build_tree(tree.middle, x, y - 1, road, world, current_tree_level + 1)
        build_tree(tree.right, x + 1, y - 1, road, world, current_tree_level + 1)
    return tree


def max_path(tree: Union["TernaryTree", None]):
    if tree is None:
        return -100
    if tree.is_leaf():
        return tree.value.points_value
    return tree.value.points_value + max(max_path(tree.left), max_path(tree.middle), max_path(tree.right))


def best_path(tree: Union["TernaryTree", None]):
    left = max_path(tree.left)
    middle = max_path(tree.middle)
    right = max_path(tree.right)
    if left < right > middle:
        return actions.RIGHT
    if middle < left > right:
        return actions.LEFT
    if right == left > middle:
        return random.choice([actions.LEFT, actions.RIGHT])
    return None   # to decide which action


def left_or_right(x: int, road: int):
    if x == road + 2:
        return actions.LEFT
    if x == road + 0:
        return actions.RIGHT
    return random.choice([actions.LEFT, actions.RIGHT])


def drive(world):
    if TernaryTree.steps == 0:
        TernaryTree.steps = 60
    TernaryTree.steps -= 1

    x = world.car.x
    y = world.car.y
    road = 0
    if 3 <= x:
        road = 3
    tree = TernaryTree(0)
    tree = build_tree(tree, x, y, road, world, 0)

    if best_path(tree) is not None:
        return best_path(tree)
    obstacle = world.get((x, y - 1))
    if obstacle == obstacles.PENGUIN:
        return actions.PICKUP
    if obstacle == obstacles.WATER:
        return actions.BRAKE
    if obstacle == obstacles.CRACK:
        return actions.JUMP
    if obstacle != obstacles.NONE:
        return left_or_right(x, road)
    return actions.NONE
