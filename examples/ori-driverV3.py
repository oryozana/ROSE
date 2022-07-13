from rose.common import obstacles, actions
from examples import movement_options

driver_name = "Ori DriverV3"

barriers = (obstacles.BARRIER, obstacles.BIKE, obstacles.TRASH, obstacles.CRACK, obstacles.WATER)
obstacles_dict = {obstacles.NONE: 0,
                  obstacles.TRASH: -10,
                  obstacles.BIKE: -10,
                  obstacles.BARRIER: -10,
                  obstacles.CRACK: 5,
                  obstacles.WATER: 4,
                  obstacles.PENGUIN: 10}


def sum_path(path, values, x):  # sum up the whole path value
    sum = 0
    x %= 3  # side
    for row in range(len(path)):
        for col in range(len(path[row])):
            if path[row][col]:
                if col > 0:
                    if values[row][col - 1] != -10 and values[row][col - 1] != 5 and values[row][col - 1] != 4:
                        sum += values[row][col]
                else:
                    if values[row][col] == -10 or (values[row][col] == 4 or values[row][col] == 5) and row != x:
                        sum += -10
                    elif (values[row][col] == 4 or values[row][col] == 5) and row == x:
                        sum += values[row][col]
    return sum


def update_values(world, values, side, y):  # update "values" to match the map at the car current position
    for row in range(len(values)):
        for col in range(len(values[row])):
            obstacle = world.get((side + row, y - col - 1))
            values[row][col] = obstacles_dict[obstacle]
    return values


def find_path(values, path, side, x):  # search for the best path to go based on points
    max_points = 0
    for possability in movement_options.middle_moves:
        current = sum_path(possability, values, x)
        if current > max_points:
            max_points = current
            path = possability

    if x == 0 + side or x == 1 + side:
        for possability in movement_options.left_moves:
            current = sum_path(possability, values, x)
            if current > max_points:
                max_points = current
                path = possability

    if x == 2 + side or x == 1 + side:
        for possability in movement_options.right_moves:
            current = sum_path(possability, values, x)
            if current > max_points:
                max_points = current
                path = possability
    return path


def drive(world):
    x = world.car.x
    y = world.car.y

    side = 3  # match the "x" value to the side of the road
    if 0 <= x <= 2:
        side = 0

    global path
    path = None
    global values
    values = None

    obstacle1 = world.get((x, y - 1))
    if obstacle1 == obstacles.PENGUIN:  # pick up penguins
        return actions.PICKUP

    if obstacle1 == obstacles.WATER:  # brakes at water
        return actions.BRAKE

    if obstacle1 == obstacles.CRACK:  # jump over cracks
        return actions.JUMP

    # starting values:
    values = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

    path = [[True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True]]

    values = update_values(world, values, side, y)
    path = find_path(values, path, side, x)

    if obstacle1 in barriers:  # avoid barriers
        if x == 1 + side:
            right_obstacle1 = world.get((x + 1, y - 1))
            left_obstacle1 = world.get((x - 1, y - 1))
            if (left_obstacle1 == obstacles.NONE or left_obstacle1 == obstacles.PENGUIN) and path[0][1]:
                return actions.LEFT
            if (right_obstacle1 == obstacles.NONE or right_obstacle1 == obstacles.PENGUIN) and path[2][1]:
                return actions.RIGHT
        if x == 2 + side or x == 1 + side:
            obstacle1 = world.get((x - 1, y - 1))
            if obstacle1 == obstacles.NONE or obstacle1 == obstacles.PENGUIN:
                return actions.LEFT
        if x == 0 + side or x == 1 + side:
            obstacle1 = world.get((x + 1, y - 1))
            if obstacle1 == obstacles.NONE or obstacle1 == obstacles.PENGUIN:
                return actions.RIGHT

    # chose destination based on the path:
    if ((x == 0 + side and path[0][1]) or (x == 1 + side and path[1][1]) or (x == 2 + side and path[2][1])) and world.get((x, y - 1)) not in barriers:
        return actions.NONE
    if ((x == 0 + side and path[1][1]) or (x == 1 + side and path[2][1])) and world.get((x + 1, y - 1)) not in barriers:
        return actions.RIGHT
    if ((x == 1 + side and path[0][1]) or (x == 2 + side and path[1][1])) and world.get((x - 1, y - 1)) not in barriers:
        return actions.LEFT
    return actions.NONE
