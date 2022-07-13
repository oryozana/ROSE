import random
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


# def use(x, y, front, obstacle0, obstacle1, obstacle2, obstacle, use_action):

USABLES = [obstacles.PENGUIN, obstacles.WATER, obstacles.CRACK]
ACTIONS = [actions.PICKUP, actions.BRAKE, actions.JUMP]
def drive(world):
    
    x = world.car.x
    y = world.car.y
    obst = world.get(x, y - 2)
    if obst in USABLES:
        return ACTIONS[USABLES.index(obst)]
    if obst not in USABLES:
        if x % 3 == 0:
            return actions.RIGHT
        if x % 3 == 1:
            return actions.LEFT
        return actions.LEFT
    
    