from rose.common import obstacles, actions  # NOQA

driver_name = "מושיקו בוזגלו"
POINTS = [obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER]  # All of the point obstacles
PENALTY = [obstacles.TRASH, obstacles.BARRIER, obstacles.BIKE]  # All of the penalty obstacles


def check_points_in_lane(obs):  # Checking if there are any point obstacles ahead
    return obs in POINTS


def get_points(obs):  # Checking which point obstacle is ahead and doing it's respective action
    if obs == obstacles.PENGUIN:
        return actions.PICKUP
    if obs == obstacles.WATER:
        return actions.BRAKE
    if obs == obstacles.CRACK:
        return actions.JUMP


def avoid_obstacles(x, obs, max_x):  # If there is a penalty obstacle ahead and the car can move left - move left, otherwise, move right
    if obs in PENALTY:
        if x == max_x:
            return actions.LEFT
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
    if check_points_in_lane(obs):
        return get_points(obs)

    # Checking if there are points two spaces ahead of the car and planning what to do
    if world.get((x, y - 2)) in POINTS:
        if obs not in PENALTY:
            return actions.NONE
    if x > MIN_X:
        if world.get((x - 1, y - 2)) in POINTS:
            return actions.LEFT
    if x < MAX_X:
        if world.get((x + 1, y - 2)) in POINTS:
            return actions.RIGHT

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
    return avoid_obstacles(x, obs, MAX_X)
