from rose.common import obstacles, actions

driver_name = "Ori Driver"

barriers = (obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH)

def drive(world):
    x = world.car.x
    y = world.car.y

    side = 3
    if 0 <= x <= 2:
        side = 0

    obstacle1 = world.get((x, y - 1))
    if obstacle1 == obstacles.PENGUIN:
        return actions.PICKUP

    obstacle1 = world.get((x, y - 1))
    if obstacle1 == obstacles.WATER:
        return actions.BRAKE

    if obstacle1 == obstacles.CRACK:
        return actions.JUMP

    obstacle3 = world.get((x, y - 3))
    obstacle2 = world.get((x, y - 2))
    if obstacle2 == obstacle3 == obstacles.PENGUIN:
        return actions.NONE

    if obstacle1 in barriers:
        if x == 1 + side:
            left_obstacle1 = world.get((x - 1, y - 1))
            left_obstacle3 = world.get((x - 1, y - 3))
            right_obstacle1 = world.get((x + 1, y - 1))
            right_obstacle3 = world.get((x + 1, y - 3))
            if left_obstacle1 == obstacles.NONE and left_obstacle3 == obstacles.PENGUIN:
                return actions.LEFT
            if right_obstacle1 == obstacles.NONE and right_obstacle3 == obstacles.PENGUIN:
                return actions.RIGHT

        if x == 2 + side or x == 1 + side:
            obstacle1 = world.get((x - 1, y - 1))
            if obstacle1 == obstacles.NONE:
                return actions.LEFT

        if x == 0 + side or x == 1 + side:
            obstacle1 = world.get((x + 1, y - 1))
            if obstacle1 == obstacles.NONE:
                return actions.RIGHT

    obstacle2 = world.get((x, y - 2))
    if obstacle2 == obstacles.PENGUIN:
        return actions.NONE

    if x == 0 + side or x == 1 + side:
        obstacle2 = world.get((x + 1, y - 2))
        if obstacle2 == obstacles.PENGUIN:
            return actions.RIGHT

    if x == 2 + side or x == 1 + side:
        obstacle2 = world.get((x - 1, y - 2))
        if obstacle2 == obstacles.PENGUIN:
            return actions.LEFT

    obstacle2 = world.get((x, y - 2))
    if obstacle2 == obstacles.WATER or obstacle2 == obstacles.CRACK:
        return actions.NONE

    if x == 0 + side or x == 1 + side:
        obstacle2 = world.get((x + 1, y - 2))
        if obstacle2 == obstacles.WATER or obstacle2 == obstacles.CRACK:
            return actions.RIGHT

    if x == 2 + side or x == 1 + side:
        obstacle2 = world.get((x - 1, y - 2))
        if obstacle2 == obstacles.WATER or obstacle2 == obstacles.CRACK:
            return actions.LEFT

    if x == 0 + side and world.get((x + 1, y - 1)) == obstacles.NONE:
        return actions.RIGHT

    if x == 2 + side and world.get((x - 1, y - 1)) == obstacles.NONE:
        return actions.LEFT

    return actions.NONE

