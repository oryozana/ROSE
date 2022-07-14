from rose.common import obstacles, actions
driver_name = 'Best'

def return_direction_when_barrier(x, y, world):
    if x == 0 or x == 3:
        return actions.RIGHT
    if x == 2 or x == 5:
        return actions.LEFT
    rightobstacle = world.get((x + 1, y - 2))
    leftobstacle = world.get((x - 1, y - 2))
    if rightobstacle == obstacles.PENGUIN:
        return actions.RIGHT
    if leftobstacle == obstacles.PENGUIN:
        return actions.LEFT
    if rightobstacle == obstacles.CRACK:
        return actions.RIGHT
    if leftobstacle == obstacles.CRACK:
        return actions.LEFT
    if rightobstacle == obstacles.WATER:
        return actions.RIGHT
    if leftobstacle == obstacles.WATER:
        return actions.LEFT
    return actions.LEFT


def find_place_none(x, y, world):
    if x == 0 or x == 3:
        rightobstacle = world.get((x + 1, y - 2))
        if not rightobstacle == obstacles.PENGUIN:
            if rightobstacle == obstacles.CRACK or rightobstacle == obstacles.WATER:
                return actions.RIGHT
            return actions.NONE
    else:
        if x == 2 or x == 5:
            leftobstacle = world.get((x - 1, y - 2))
            if not leftobstacle == obstacles.PENGUIN:
                if leftobstacle == obstacles.CRACK or leftobstacle == obstacles.WATER:
                    return actions.LEFT
                return actions.NONE
        else:
            rightobstacle = world.get((x + 1, y - 2))
            leftobstacle = world.get((x - 1, y - 2))
            if rightobstacle == obstacles.PENGUIN:
                return actions.RIGHT
            if leftobstacle == obstacles.PENGUIN:
                return actions.LEFT
            if rightobstacle == obstacles.CRACK:
                return actions.RIGHT
            if leftobstacle == obstacles.CRACK:
                return actions.LEFT
            if rightobstacle == obstacles.WATER:
                return actions.RIGHT
            if leftobstacle == obstacles.WATER:
                return actions.LEFT
            return actions.NONE


def drive(world):
    x = world.car.x
    y = world.car.y
    obstacle = world.get((x, y - 1))
    if obstacle == obstacles.PENGUIN:
        return actions.PICKUP
    if obstacle == obstacles.WATER:
        return actions.BRAKE
    if obstacle == obstacles.CRACK:
        return actions.JUMP
    if not obstacle == obstacles.TRASH:
        if obstacle == obstacles.BIKE or obstacle == obstacles.BARRIER:
            return return_direction_when_barrier(x, y, world)
        if obstacle == obstacles.NONE:
            return find_place_none(x, y, world)
    return actions.NONE