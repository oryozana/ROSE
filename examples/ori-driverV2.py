from rose.common import obstacles, actions

driver_name = "Ori DriverV2"

barriers = (obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH)
side_barriers = (obstacles.WATER, obstacles.CRACK)
clear = (obstacles.NONE, obstacles.PENGUIN)
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

    if x == 0 + side or x == 1 + side:
        right_obstacle1 = world.get((x + 1, y - 1))
        obstacle2 = world.get((x + 1, y - 2))
        if obstacle2 == obstacles.PENGUIN and right_obstacle1 in clear:
            return actions.RIGHT

    if x == 2 + side or x == 1 + side:
        left_obstacle1 = world.get((x - 1, y - 1))
        obstacle2 = world.get((x - 1, y - 2))
        if obstacle2 == obstacles.PENGUIN and left_obstacle1 in clear:
            return actions.LEFT

    obstacle2 = world.get((x, y - 2))
    if (obstacle2 == obstacles.WATER or obstacle2 == obstacles.CRACK) and obstacle1 not in barriers:
        return actions.NONE

    if obstacle1 in barriers:
        if x == 1 + side:
            left_obstacle1 = world.get((x - 1, y - 1))
            left_obstacle2 = world.get((x - 1, y - 2))
            left_obstacle3 = world.get((x - 1, y - 3))
            middle_obstacle3 = world.get((x, y - 3))
            right_obstacle1 = world.get((x + 1, y - 1))
            right_obstacle2 = world.get((x + 1, y - 2))
            right_obstacle3 = world.get((x + 1, y - 3))

            left_sum = obstacles_dict[left_obstacle2] + obstacles_dict[left_obstacle3]
            right_sum = obstacles_dict[right_obstacle2] + obstacles_dict[right_obstacle3]
            special_path1 = obstacles_dict[left_obstacle2] + obstacles_dict[middle_obstacle3]
            special_path2 = obstacles_dict[right_obstacle2] + obstacles_dict[middle_obstacle3]

            if left_obstacle1 in clear and left_sum >= special_path1:
                return actions.LEFT
            if left_obstacle1 in clear and special_path1 >= right_sum:
                return actions.LEFT
            if right_obstacle1 in clear and right_sum >= left_sum:
                return actions.RIGHT
            if right_obstacle1 in clear and special_path2 >= 0:
                return actions.RIGHT

        if x == 2 + side:
            obstacle1 = world.get((x - 1, y - 1))
            if obstacle1 in clear:
                return actions.LEFT

        if x == 0 + side:
            obstacle1 = world.get((x + 1, y - 1))
            if obstacle1 in clear:
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
    if obstacle2 == obstacles.PENGUIN:
        return actions.NONE

    obstacle2 = world.get((x, y - 2))
    if obstacle2 in side_barriers:
        return actions.NONE

    if x == 0 + side or x == 1 + side:
        obstacle2 = world.get((x + 1, y - 2))
        if obstacle2 in side_barriers:
            return actions.RIGHT

    if x == 2 + side or x == 1 + side:
        obstacle2 = world.get((x - 1, y - 2))
        if obstacle2 in side_barriers:
            return actions.LEFT

    if x == 0 + side and world.get((x + 1, y - 1)) == obstacles.NONE:
        return actions.RIGHT

    if x == 2 + side and world.get((x - 1, y - 1)) == obstacles.NONE:
        return actions.LEFT

    return actions.NONE
