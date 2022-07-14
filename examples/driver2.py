from rose.common import obstacles, actions  # NOQA
from examples.tree import Tree


driver_name = "מושיקו בוזגלו2"
POINTS = [obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER]  # All of the point obstacles
PENALTY = [obstacles.TRASH, obstacles.BARRIER, obstacles.BIKE]  # All of the penalty obstacles
POINTS_DICT = {obstacles.WATER: 4,
               obstacles.CRACK: 5,
               obstacles.PENGUIN: 10,
               obstacles.NONE: 0,
               obstacles.TRASH: -10,
               obstacles.BIKE: -10,
               obstacles.BARRIER: -10}


def make_tree(world, root, distance):
    x = world.car.x
    y = world.car.y

    if root is None:
        return
    if not root.has_left():
        root.middle = Tree(POINTS_DICT[world.get((x, y + distance))])
        root.right = Tree(POINTS_DICT[world.get((x + 1, y + distance))])
    if not root.has_right():
        root.middle = Tree(POINTS_DICT[world.get((x, y + distance))])
        root.left = Tree(POINTS_DICT[world.get((x - 1, y + distance))])
    make_tree(world, root.left, distance)
    make_tree(world, root.middle, distance)


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
    if x == min_x:
        root = Tree(0, None, first_middle, first_right)
    elif x == max_x:
        root = Tree(0, first_left, first_middle, None)
    else:
        root = Tree(0, first_left, first_middle, first_right)
    make_tree(world, root, 1)
    print_tree(root)
    return actions.NONE