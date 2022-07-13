from rose.common import obstacles, actions  # NOQA

driver_name = "מושיקו בוזגלו"
POINTS = [obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER]  # All of the point obstacles
PENALTY = [obstacles.TRASH, obstacles.BARRIER, obstacles.BIKE]  # All of the penalty obstacles
SPECIAL_PENALTY = [obstacles.WATER, obstacles.CRACK]
POINTS_DICT = {obstacles.WATER: 4,
               obstacles.CRACK: 5,
               obstacles.PENGUIN: 10}


def get_points(obs):  # Checking which point obstacle is ahead and doing it's respective action
    if obs == obstacles.PENGUIN:
        return actions.PICKUP
    if obs == obstacles.WATER:
        return actions.BRAKE
    if obs == obstacles.CRACK:
        return actions.JUMP


def avoid_obstacles(world, max_x):  # If there is a penalty obstacle ahead and the car can move left - move left, otherwise, move right
    x = world.car.x
    y = world.car.y
    if world.get((x, y - 1)) in PENALTY:
        if x == max_x:
            return actions.LEFT
        if x == max_x - 2:  # Max_x - 2 is min_x
            return actions.RIGHT
        if world.get((x - 1, y - 2)) in POINTS:  # Checks if there are point obstacles next to the penalty one
            if world.get((x + 1, y - 2)) in POINTS:  # Checks if there are point obstacles on both sides
                if POINTS_DICT[world.get((x - 1, y - 2))] < POINTS_DICT[world.get((x + 1, y - 2))]:  # Checks which side has more points
                    return actions.RIGHT
            return actions.LEFT
        if world.get((x - 1, y - 3)) in POINTS:  # Checks if there are point obstacles next to the penalty one
            if world.get((x + 1, y - 3)) in POINTS:  # Checks if there are point obstacles on both sides
                if POINTS_DICT[world.get((x - 1, y - 3))] < POINTS_DICT[world.get((x + 1, y - 3))]:  # Checks which side has more points
                    return actions.RIGHT
            return actions.LEFT
        return actions.RIGHT
    if x == max_x:
        if world.get((x - 1, y - 1)) not in PENALTY and world.get((x - 1, y - 1)) not in SPECIAL_PENALTY:
            return actions.LEFT
    if x == max_x - 2:
        if world.get((x + 1, y - 1)) not in PENALTY and world.get((x + 1, y - 1)) not in SPECIAL_PENALTY:
            return actions.RIGHT
    return actions.NONE


def drive(world):
    x = world.car.x
    MAX_X = 2
    MIN_X = 0
    if 3 <= x <= 5:
        MAX_X = 5
        MIN_X = 3
    y = world.car.y
    obs = world.get((x, y - 1))

    # Checking if there are points in front of the car and collecting them
    if obs in POINTS:
        return get_points(obs)

    # Checking if there are points two spaces ahead of the car and planning what to do
    if world.get((x, y - 2)) in POINTS:  # in front of the car
        if obs not in PENALTY:
            return actions.NONE
    if x == MIN_X:  # Car in left lane
        if world.get((x + 1, y - 2)) in POINTS:
            if world.get((x + 1, y - 1)) not in PENALTY and world.get((x + 1, y - 1)) not in SPECIAL_PENALTY:
                return actions.RIGHT
    if x == MAX_X:  # Car in right lane
        if world.get((x - 1, y - 2)) in POINTS:
            if world.get((x - 1, y - 1)) not in PENALTY and world.get((x - 1, y - 1)) not in SPECIAL_PENALTY:
                return actions.LEFT
    if MIN_X < x < MAX_X:  # Car in middle lane
        if world.get((x - 1, y - 2)) in POINTS and world.get((x + 1, y - 2)) in POINTS:  # If there are two point obstacles in different lanes - go for the most points
            if POINTS_DICT[world.get((x - 1, y - 2))] > POINTS_DICT[world.get((x + 1, y - 2))]:
                if world.get((x - 1, y - 1)) not in PENALTY and world.get((x - 1, y - 1)) not in SPECIAL_PENALTY:
                    return actions.LEFT
            return actions.RIGHT
        if world.get((x - 1, y - 2)) in POINTS:
            if world.get((x - 1, y - 1)) not in PENALTY and world.get((x - 1, y - 1)) not in SPECIAL_PENALTY:
                return actions.LEFT
        if world.get((x + 1, y - 2)) in POINTS:
            if world.get((x + 1, y - 1)) not in PENALTY and world.get((x + 1, y - 1)) not in SPECIAL_PENALTY:
                return actions.RIGHT

    if x == MIN_X:
        if world.get((x + 2, y - 3)) in POINTS and world.get((x + 2, y - 3)) not in SPECIAL_PENALTY:
            if world.get((x + 1, y - 2)) not in PENALTY and world.get((x + 1, y - 2)) not in SPECIAL_PENALTY:
                return actions.RIGHT
    if x == MAX_X:
        if world.get((x - 2, y - 3)) in POINTS and world.get((x - 2, y - 3)) not in SPECIAL_PENALTY:
            if world.get((x - 1, y - 2)) not in PENALTY and world.get((x - 1, y - 2)) not in SPECIAL_PENALTY:
                return actions.LEFT

    # If there are no obstacles/points to be collected, do nothing
    if x == MIN_X:
        if world.get((x, y - 1)) == obstacles.NONE and world.get((x + 1, y - 1)) == obstacles.NONE:
            return actions.NONE
    if MIN_X < x < MAX_X:
        if world.get((x - 1, y - 1)) == obstacles.NONE and world.get((x, y - 1)) == obstacles.NONE and world.get((x + 1, y - 1)) == obstacles.NONE:
            return actions.NONE
    if x == MAX_X:
        if world.get((x - 1, y - 1)) == obstacles.NONE and world.get((x, y - 1)) == obstacles.NONE:
            return actions.NONE

    # Avoid any obstacles ahead
    return avoid_obstacles(world, MAX_X)
