from rose.common import obstacles, actions

driver_name = "Random Driver"


def drive(world):
    x = world.car.x
    y = world.car.y

    obstacle = world.get((x, y - 1))
    if obstacle == "PENGUIN":
        return actions.NONE

    if x == 0 or x == 1:
        obstacle = world.get((x + 1, y - 1))
        if obstacle == "PENGUIN":
            return actions.RIGHT

    if x == 2 or x == 1:
        obstacle = world.get((x - 1, y - 1))
        if obstacle == "PENGUIN":
            return actions.LEFT

    obstacle = world.get((x, y - 1))
    if obstacle == "WATER":
        return actions.BRAKE

    if obstacle == "CRACK":
        return actions.JUMP

    if obstacle == "TRASH" or obstacle == "BIKE" or obstacle == "BARRIER":
        if x == 2 or x == 1:
            obstacle = world.get((x - 1, y - 1))
            if obstacle == "NONE":
                return actions.LEFT

        if x == 0 or x == 1:
            obstacle = world.get((x + 1, y - 1))
            if obstacle == "NONE":
                return actions.Right
    return actions.NONE