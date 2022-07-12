from rose.common import obstacles, actions

driver_name = "Ori Driver"

barriers = (obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH)
obstacles_dict = {obstacles.NONE: 0,
                  obstacles.TRASH: -10,
                  obstacles.BIKE: -10,
                  obstacles.BARRIER: -10,
                  obstacles.CRACK: 5,
                  obstacles.WATER: 4,
                  obstacles.PENGUIN: 10}


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
            left_obstacle2 = world.get((x - 1, y - 2))
            left_obstacle3 = world.get((x - 1, y - 3))
            right_obstacle1 = world.get((x + 1, y - 1))
            right_obstacle2 = world.get((x + 1, y - 2))
            right_obstacle3 = world.get((x + 1, y - 3))

            left_sum = obstacles_dict[left_obstacle2] + obstacles_dict[left_obstacle3]
            right_sum = obstacles_dict[right_obstacle2] + obstacles_dict[right_obstacle3]

            if left_obstacle1 == obstacles.NONE and left_sum >= right_sum:
                return actions.LEFT
            if right_obstacle1 == obstacles.NONE and right_sum > left_sum:
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

