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
    layer1 = world.get((x, y - 1))
    layer2 = [world.get((0, y - 2)), world.get((1, y - 2)), world.get((2, y - 2))]
    if layer1 in USABLES:
        return ACTIONS[USABLES.index(layer1)]
    if layer1 in UNUSABLES:
        return actions.LEFT
    
    for o in layer2:
        if o in USABLES:
            if x - USABLES.index(o) == 1:
                return actions.RIGHT
            if x - USABLES.index(o) == -1:
                return actions.LEFT
            return actions.NONE
                