from rose.common import obstacles, actions

driver_name = "Ori Driver"


def drive(world):
    x = world.car.x
    y = world.car.y

    side = 3
    if 0 <= x <= 2:
        side = 0

    obstacle = world.get((x, y))
    if obstacle == obstacles.PENGUIN:
        return actions.PICKUP

    obstacle = world.get((x, y - 1))
    if obstacle == obstacles.PENGUIN:
        return actions.NONE

    if x == 0 + side or x == 1 + side:
        obstacle = world.get((x + 1, y - 1))
        if obstacle == obstacles.PENGUIN:
            return actions.RIGHT

    if x == 2 + side or x == 1 + side:
        obstacle = world.get((x - 1, y - 1))
        if obstacle == obstacles.PENGUIN:
            return actions.LEFT

    obstacle = world.get((x, y - 1))
    if obstacle == obstacles.WATER:
        return actions.BRAKE

    if obstacle == obstacles.CRACK:
        return actions.JUMP

    if obstacle == obstacles.TRASH or obstacle == obstacles.BIKE or obstacle == obstacles.BARRIER:
        if x == 2 + side or x == 1 + side:
            obstacle = world.get((x - 1, y - 1))
            if obstacle == obstacles.NONE:
                return actions.LEFT

        if x == 0 + side or x == 1 + side:
            obstacle = world.get((x + 1, y - 1))
            if obstacle == obstacles.NONE:
                return actions.RIGHT

    if x == 0 + side and world.get((x + 1, y - 1)) == obstacles.NONE:
        return actions.RIGHT

    if x == 2 + side and world.get((x - 1, y - 1)) == obstacles.NONE:
        return actions.LEFT

    return actions.NONE

