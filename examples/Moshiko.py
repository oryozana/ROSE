import random
from xmlrpc.client import TRANSPORT_ERROR
from rose.common import obstacles, actions  # NOQA

driver_name = "Moshiko Boozaglo"


# def use(x, y, front, obstacle0, obstacle1, obstacle2, obstacle, use_action):


USABLES = [obstacles.PENGUIN, obstacles.WATER, obstacles.CRACK]
UNUSABLES = [obstacles.BARRIER, obstacles.TRASH, obstacles.BIKE]
ACTIONS = [actions.PICKUP, actions.BRAKE, actions.JUMP]
def drive(world):
    
    x = world.car.x
    y = world.car.y
    obst = world.get((x, y - 1))

    if obst in USABLES:
        return ACTIONS[USABLES.index(obst)]
    if obst in UNUSABLES:
        return actions.LEFT
    return actions.RIGHT
    