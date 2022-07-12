from rose.common import obstacles, actions  # NOQA

driver_name = "מושיקו בוזגלו"


def check_points_in_lane(obs):
    if obs == obstacles.BIKE or obs == obstacles.BARRIER or obs == obstacles.TRASH:
        return False
    return obs == obstacles.PENGUIN or obs == obstacles.WATER or obs == obstacles.CRACK


def get_points(obs):
    if obs == obstacles.PENGUIN:
        return actions.PICKUP
    if obs == obstacles.WATER:
        return actions.BRAKE
    if obs == obstacles.CRACK:
        return actions.JUMP


def avoid_obstacles(x, obs, max_x):
    if obs == obstacles.BIKE or obs == obstacles.BARRIER or obs == obstacles.TRASH:
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

    if x == MIN_X:
        if world.get((x, y - 1)) == obstacles.NONE and world.get((x + 1, y - 1)) == obstacles.NONE:
            return actions.NONE
    if MIN_X < x < MAX_X:
        if world.get((x - 1, y - 1)) == obstacles.NONE and world.get((x, y - 1)) == obstacles.NONE and world.get((x + 1, y - 1)) == obstacles.NONE:
            return actions.NONE
    if x == MAX_X:
        if world.get((x - 1, y - 1)) == obstacles.NONE and world.get((x, y - 1)) == obstacles.NONE:
            return actions.NONE

    if check_points_in_lane(obs):
        return get_points(obs)
    if x > MIN_X:
        obs = world.get((x - 1, y - 1))
        if check_points_in_lane(obs):
            return actions.LEFT
    if x < MAX_X:
        obs = world.get((x + 1, y - 1))
        if check_points_in_lane(obs):
            return actions.RIGHT
    return avoid_obstacles(x, world.get((x, y - 1)), MAX_X)
