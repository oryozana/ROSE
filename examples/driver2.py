from rose.common import obstacles, actions  # NOQA
from examples.tree import Tree


driver_name = "מושיקו בוזגלו2"
POINTS = [obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER]  # All of the point obstacles
PENALTY = [obstacles.TRASH, obstacles.BARRIER, obstacles.BIKE]  # All of the penalty obstacles
POINTS_DICT = {obstacles.WATER: 4,
               obstacles.CRACK: 5,
               obstacles.PENGUIN: 10}


def make_tree(world, root):
    x = world.car.x
    y = world.car.y

    if root is None:
        return
    if not root.has_left():
        root.middle = Tree(POINTS_DICT[world.get((x + 1, y + 1))])
        root.right = Tree(POINTS_DICT[world.get((x + 2, y + 1))])
    if not root.has_right():
        root.middle = Tree(POINTS_DICT[world.get((x - 1, y + 1))])
        root.left = Tree(POINTS_DICT[world.get((x - 2, y + 1))])
    make_tree(world, root.left)
    make_tree(world, root.middle)
    make_tree(world, root.right)


def drive(world):
    x = world.car.x
    max_x = 2
    min_x = 0
    if 3 <= x <= 5:
        max_x = 5
        min_x = 3
    y = world.car.y
    first_left = Tree(0)
    first_middle = Tree(0)
    first_right = Tree(0)
    if x == max_x - 2:
        root = Tree(0, None, first_middle, first_right)
    elif x == max_x:
        root = Tree(0, first_left, first_middle, None)
    else:
        root = Tree(0, first_left, first_middle, first_right)
    make_tree(world, root)
